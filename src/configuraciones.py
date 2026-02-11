import re
from typing import Dict, Union
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import glob
import os


def cargar_dataframes(ruta: str, pattern: str = "*.csv", index_col: Union[int, str, None] = 0) -> Dict[Union[int, str], pd.DataFrame]:
    """Carga todos los archivos CSV de una carpeta y devuelve un diccionario.

    - ruta: ruta a la carpeta con archivos CSV
    - pattern: patrón glob para buscar archivos (por defecto '*.csv')
    - index_col: pasado a pd.read_csv (por defecto 0 para compatibilidad con los CSV del proyecto)

    Retorna un dict donde la clave es el año (int) si se detecta un año de 4 dígitos en el nombre del archivo,
    o el nombre de archivo sin extensión si no se detecta un año.

    Lanza FileNotFoundError si la carpeta no existe, ValueError si no hay archivos CSV, y RuntimeError si hay problemas leyendo un archivo.
    """
    ruta = os.path.abspath(ruta)
    if not os.path.exists(ruta) or not os.path.isdir(ruta):
        raise FileNotFoundError(f"La ruta {ruta} no existe o no es un directorio.")

    files = sorted(glob.glob(os.path.join(ruta, pattern)))
    if not files:
        raise ValueError(f"No se encontraron archivos con patrón '{pattern}' en {ruta}.")

    dict_df: Dict[Union[int, str], pd.DataFrame] = {}
    for file_path in files:
        file_name = os.path.basename(file_path)

        m = re.search(r"(19|20)\d{2}", file_name)
        if m:
            key = int(m.group(0))
        else:
            key = os.path.splitext(file_name)[0]

        try:
            df = pd.read_csv(file_path, index_col=index_col)
        except Exception as e:
            raise RuntimeError(f"Error leyendo '{file_name}': {e}") from e

        dict_df[key] = df

    return dict_df

def configuracion_visual():
    plt.style.use('ggplot')
    sns.set_context('notebook', font_scale=1.2)
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    print("Configurado visualmente")

def configuracion_format_df(df_all):
    #formato de fechas, al leer el csv se pierden
    cols_fecha = ['ultima_modificacion', 'fecha_de_apertura', 'fecha_de_cierre', 'fecha_de_solucion']
    for cols in cols_fecha:
        df_all[cols] = pd.to_datetime(df_all[cols], errors='coerce')

    #col con format Period [M]
    df_all['fecha_de_apertura_periodo_mes'] = df_all['fecha_de_apertura'].dt.to_period('M')

    #ordenar cronologicamente por apertura
    df_all = df_all.sort_values(by='fecha_de_apertura').reset_index(drop=True)

    #filtramos 2026 porque tiene pocos tickets
    df_all = df_all[df_all["fecha_de_apertura_año"].between(2022,2025)]
    print("Configuracion fechas lista")
    return df_all

#carga y preparacion de los dfs globales
def procesar_jerarquia(df):
    if 'categoria' not in df.columns: return df
    series_cat = df['categoria'].fillna('Sin Categoria').astype(str)
    df['area'] = series_cat.apply(lambda x: x.split('>')[0].strip() if '>' in x else x.strip())
    
    # Función interna para limpiar texto (mojibake)
    def reparar_texto(texto):
        if not isinstance(texto, str): return texto
        reemplazos = {
            'Ã³': 'ó', 'Ã¡': 'á', 'Ã©': 'é', 'Ã\xad': 'í', 'Ã': 'í', 'Ã±': 'ñ', 'Ãº': 'ú',
            'Ã\x81': 'Á', 'Ã\x89': 'É', 'Ã\x8d': 'Í', 'Ã\x93': 'Ó', 'Ã\x9a': 'Ú', 'Ã\x91': 'Ñ'
        }
        for mal, bien in reemplazos.items():
            if mal in texto: texto = texto.replace(mal, bien)
        return texto.strip()
    
    df['area'] = df['area'].apply(reparar_texto)
    return df

#limpiar texto
def limpiar_texto(texto):
    if not isinstance(texto, str): return ""
    texto = texto.lower()
    texto = re.sub(r'[^a-záéíóúñ ]', '', texto)
    return texto.strip()