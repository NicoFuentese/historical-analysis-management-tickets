# Analisis preliminares de los datos

## Columnas y nombres
Las columnas de los años no son iguales y estan algunos mal escritos. Se corrigieron y se normalizaron para todos los años.

## Analisis de nulos
En general los datos estan bien completos, los datos fundamentales estan casi completos y los faltantes son minimos.

## Reemplazo de categoria principal (area) y subcategorias (servicios)
Desde la columna "categoria" Se obtienen las areas y servicios indicadas por el ticket.

## Transformacion numerica de Prioridad
Actualmente columna "prioridad" es tipo str, se pasa a numerico para el mayor entendimiento de los modelos ML.

## Validacion de fuentes automaticas
La columna "estadisticas__hora_de_resolucion" calcula tiempos de resolucion automaticamente desde el Sistema pero comprobacion con la columna de "tiempo_vida_horas" calculado desde "fecha_de_apertura" y "fecha_de_cierre" indican tiempos diferentes e incoherentes. Por lo que se utilizara la columna creada y no la que viene incluida por sistema.

Ademas, en el año 2023 se encuentran 214 tickets con fecha de cierre anterior a la de apertura de la solicitud. Estos como representan un 0.59% de los datos de 2023 se eliminan, ademas que generan inconsistencia, ruido y es un volumen insignificante para modelos predictivos y Series de Tiempo.


| fecha_de_apertura | fecha_de_cierre | tiempo_vida_horas | resolucion_horas_decimal | estadisticas__hora_de_resolucion |
| :--- | :--- | :--- | :--- | :--- |
| 2024-12-17 17:45:00 | NaT | NaN | 0.00 | 0 segundos |
| 2024-12-10 09:04:00 | NaT | NaN | 0.00 | 0 segundos |
| 2024-12-23 17:32:00 | NaT | NaN | 0.00 | 0 segundos |
| 2024-05-24 14:49:00 | 2024-05-27 08:29:00 | 65.67 | 0.17 | 10 minutos |
| 2024-04-17 18:00:00 | 2024-05-02 22:20:00 | 364.33 | 311.28 | 12 días 23 horas 17 minutos |


```
% nulos en el DataFrame 2021:
TOTAL DATOS = 2
id                                        0.0
titulo                                    0.0
estado                                    0.0
ultima_modificacion                       0.0
fecha_de_apertura                         0.0
prioridad                                 0.0
solicitante__solicitante                  0.0
asignado_a__grupo_de_tecnicos             0.0
asignado_a__tecnico                       0.0
categoria                                 0.0
origen_de_la_solicitud                    0.0
ubicacion                               100.0
estadisticas__hora_de_resolucion          0.0
seguimientos__origen_de_la_solicitud    100.0
fecha_de_cierre                           0.0
fecha_de_solucion                       100.0
unnamed_16                              100.0
dtype: float64
Duplicados:
np.int64(0)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

% nulos en el DataFrame 2022:
TOTAL DATOS = 3827
id                                        0.0
titulo                                    0.0
estado                                    0.0
ultima_modificacion                       0.0
fecha_de_apertura                         0.0
prioridad                                 0.0
solicitante__solicitante                  1.0
asignado_a__grupo_de_tecnicos             7.0
asignado_a__tecnico                      33.0
categoria                                23.0
origen_de_la_solicitud                    0.0
ubicacion                               100.0
estadisticas__hora_de_resolucion          0.0
seguimientos__origen_de_la_solicitud     73.0
fecha_de_cierre                           0.0
fecha_de_solucion                       100.0
unnamed_16                              100.0
dtype: float64
Duplicados:
np.int64(0)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

% nulos en el DataFrame 2023:
TOTAL DATOS = 36259
id                                        0.0
titulo                                    0.0
estado                                    0.0
ultima_modificacion                       0.0
fecha_de_apertura                         0.0
prioridad                                 0.0
solicitante__solicitante                  1.0
asignado_a__grupo_de_tecnicos             6.0
asignado_a__tecnico                      17.0
categoria                                 6.0
origen_de_la_solicitud                    0.0
ubicacion                                94.0
estadisticas__hora_de_resolucion          0.0
seguimientos__origen_de_la_solicitud     72.0
fecha_de_cierre                           0.0
fecha_de_solucion                        67.0
unnamed_16                              100.0
dtype: float64
Duplicados:
np.int64(0)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

% nulos en el DataFrame 2024:
TOTAL DATOS = 35004
id                                        0.0
titulo                                    0.0
estado                                    0.0
ultima_modificacion                       0.0
fecha_de_apertura                         0.0
prioridad                                 0.0
solicitante__solicitante                  0.0
asignado_a__grupo_de_tecnicos             5.0
asignado_a__tecnico                       5.0
categoria                                10.0
origen_de_la_solicitud                    0.0
ubicacion                                89.0
estadisticas__hora_de_resolucion          0.0
seguimientos__origen_de_la_solicitud     72.0
fecha_de_cierre                           0.0
fecha_de_solucion                        62.0
unnamed_16                              100.0
dtype: float64
Duplicados:
np.int64(0)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

% nulos en el DataFrame 2025:
TOTAL DATOS = 36527
id                                        0.0
titulo                                    0.0
estado                                    0.0
ultima_modificacion                       0.0
fecha_de_apertura                         0.0
prioridad                                 0.0
solicitante__solicitante                  0.0
asignado_a__grupo_de_tecnicos             3.0
asignado_a__tecnico                       4.0
categoria                                 6.0
origen_de_la_solicitud                    0.0
ubicacion                                94.0
estadisticas__hora_de_resolucion          0.0
seguimientos__origen_de_la_solicitud     72.0
fecha_de_cierre                           0.0
fecha_de_solucion                        31.0
unnamed_16                              100.0
dtype: float64
Duplicados:
np.int64(0)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## Transformacion de tipos de columnas
Se transformo principalmente las columnas tipo fecha y de conteo de tiempo de resolucion a formato fecha y float (fraccion de horas) respectivamente.

## Texto en filas
Para algunas columnas mal escritos se normalizo para todas las columnas con buena escritura.

## Columnas eliminadas
Se elimino la columna 'unnamed_16'.

## Columnas agregadas
- Se agrego el calculo de SLA (hipotetico).
- Mes, dia, año y hora segun la fecha de apertura del ticket.
- Flag de apertura de ticket en horario laboral.
- Columna mes-año para analisis futuros de Series de Tiempo.

## Resultado finales de trabajo:

```
año 2021:
<class 'pandas.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 24 columns):
 #   Column                                Non-Null Count  Dtype         
---  ------                                --------------  -----         
 0   id                                    2 non-null      int64         
 1   titulo                                2 non-null      str           
 2   estado                                2 non-null      str           
 3   ultima_modificacion                   2 non-null      datetime64[us]
 4   fecha_de_apertura                     2 non-null      datetime64[us]
 5   prioridad                             2 non-null      str           
 6   solicitante__solicitante              2 non-null      str           
 7   asignado_a__grupo_de_tecnicos         2 non-null      str           
 8   asignado_a__tecnico                   2 non-null      str           
 9   categoria                             2 non-null      str           
 10  origen_de_la_solicitud                2 non-null      str           
 11  ubicacion                             0 non-null      str           
 12  estadisticas__hora_de_resolucion      2 non-null      str           
 13  seguimientos__origen_de_la_solicitud  0 non-null      str           
 14  fecha_de_cierre                       2 non-null      datetime64[us]
 15  fecha_de_solucion                     0 non-null      datetime64[s] 
 16  resolucion_horas_decimal              2 non-null      float64       
 17  cumple_SLA                            2 non-null      bool          
 18  fecha_de_apertura_dia                 2 non-null      int32         
 19  fecha_de_apertura_mes                 2 non-null      int32         
 20  fecha_de_apertura_año                 2 non-null      int32         
 21  fecha_de_apertura_hora                2 non-null      int32         
 22  creado_en_horario_laboral             2 non-null      bool          
 23  fecha_de_apertura_periodo_mes         2 non-null      period[M]     
dtypes: bool(2), datetime64[s](1), datetime64[us](3), float64(1), int32(4), int64(1), period[M](1), str(11)
memory usage: 456.0 bytes
None
----------------------------------------
año 2022:
<class 'pandas.DataFrame'>
RangeIndex: 3827 entries, 0 to 3826
Data columns (total 24 columns):
 #   Column                                Non-Null Count  Dtype         
---  ------                                --------------  -----         
 0   id                                    3827 non-null   int64         
 1   titulo                                3827 non-null   str           
 2   estado                                3827 non-null   str           
 3   ultima_modificacion                   3827 non-null   datetime64[us]
 4   fecha_de_apertura                     3827 non-null   datetime64[us]
 5   prioridad                             3827 non-null   str           
 6   solicitante__solicitante              3772 non-null   str           
 7   asignado_a__grupo_de_tecnicos         3561 non-null   str           
 8   asignado_a__tecnico                   2580 non-null   str           
 9   categoria                             2956 non-null   str           
 10  origen_de_la_solicitud                3826 non-null   str           
 11  ubicacion                             10 non-null     str           
 12  estadisticas__hora_de_resolucion      3827 non-null   str           
 13  seguimientos__origen_de_la_solicitud  1040 non-null   str           
 14  fecha_de_cierre                       3827 non-null   datetime64[us]
 15  fecha_de_solucion                     2 non-null      datetime64[us]
 16  resolucion_horas_decimal              3827 non-null   float64       
 17  cumple_SLA                            3827 non-null   bool          
 18  fecha_de_apertura_dia                 3827 non-null   int32         
 19  fecha_de_apertura_mes                 3827 non-null   int32         
 20  fecha_de_apertura_año                 3827 non-null   int32         
 21  fecha_de_apertura_hora                3827 non-null   int32         
 22  creado_en_horario_laboral             3827 non-null   bool          
 23  fecha_de_apertura_periodo_mes         3827 non-null   period[M]     
dtypes: bool(2), datetime64[us](4), float64(1), int32(4), int64(1), period[M](1), str(11)
memory usage: 605.6 KB
None
----------------------------------------
año 2023:
<class 'pandas.DataFrame'>
RangeIndex: 36259 entries, 0 to 36258
Data columns (total 24 columns):
 #   Column                                Non-Null Count  Dtype         
---  ------                                --------------  -----         
 0   id                                    36259 non-null  int64         
 1   titulo                                36259 non-null  str           
 2   estado                                36259 non-null  str           
 3   ultima_modificacion                   36259 non-null  datetime64[us]
 4   fecha_de_apertura                     36259 non-null  datetime64[us]
 5   prioridad                             36259 non-null  str           
 6   solicitante__solicitante              35899 non-null  str           
 7   asignado_a__grupo_de_tecnicos         33944 non-null  str           
 8   asignado_a__tecnico                   30251 non-null  str           
 9   categoria                             34161 non-null  str           
 10  origen_de_la_solicitud                36259 non-null  str           
 11  ubicacion                             2199 non-null   str           
 12  estadisticas__hora_de_resolucion      36259 non-null  str           
 13  seguimientos__origen_de_la_solicitud  10185 non-null  str           
 14  fecha_de_cierre                       36259 non-null  datetime64[us]
 15  fecha_de_solucion                     11929 non-null  datetime64[us]
 16  resolucion_horas_decimal              36259 non-null  float64       
 17  cumple_SLA                            36259 non-null  bool          
 18  fecha_de_apertura_dia                 36259 non-null  int32         
 19  fecha_de_apertura_mes                 36259 non-null  int32         
 20  fecha_de_apertura_año                 36259 non-null  int32         
 21  fecha_de_apertura_hora                36259 non-null  int32         
 22  creado_en_horario_laboral             36259 non-null  bool          
 23  fecha_de_apertura_periodo_mes         36259 non-null  period[M]     
dtypes: bool(2), datetime64[us](4), float64(1), int32(4), int64(1), period[M](1), str(11)
memory usage: 5.6 MB
None
----------------------------------------
año 2024:
<class 'pandas.DataFrame'>
RangeIndex: 35004 entries, 0 to 35003
Data columns (total 24 columns):
 #   Column                                Non-Null Count  Dtype         
---  ------                                --------------  -----         
 0   id                                    35004 non-null  int64         
 1   titulo                                35004 non-null  str           
 2   estado                                35004 non-null  str           
 3   ultima_modificacion                   35004 non-null  datetime64[us]
 4   fecha_de_apertura                     35004 non-null  datetime64[us]
 5   prioridad                             35004 non-null  str           
 6   solicitante__solicitante              34858 non-null  str           
 7   asignado_a__grupo_de_tecnicos         33346 non-null  str           
 8   asignado_a__tecnico                   33356 non-null  str           
 9   categoria                             31389 non-null  str           
 10  origen_de_la_solicitud                35003 non-null  str           
 11  ubicacion                             3973 non-null   str           
 12  estadisticas__hora_de_resolucion      35004 non-null  str           
 13  seguimientos__origen_de_la_solicitud  9877 non-null   str           
 14  fecha_de_cierre                       34923 non-null  datetime64[us]
 15  fecha_de_solucion                     13400 non-null  datetime64[us]
 16  resolucion_horas_decimal              35004 non-null  float64       
 17  cumple_SLA                            35004 non-null  bool          
 18  fecha_de_apertura_dia                 35004 non-null  int32         
 19  fecha_de_apertura_mes                 35004 non-null  int32         
 20  fecha_de_apertura_año                 35004 non-null  int32         
 21  fecha_de_apertura_hora                35004 non-null  int32         
 22  creado_en_horario_laboral             35004 non-null  bool          
 23  fecha_de_apertura_periodo_mes         35004 non-null  period[M]     
dtypes: bool(2), datetime64[us](4), float64(1), int32(4), int64(1), period[M](1), str(11)
memory usage: 5.4 MB
None
----------------------------------------
año 2025:
<class 'pandas.DataFrame'>
RangeIndex: 36527 entries, 0 to 36526
Data columns (total 24 columns):
 #   Column                                Non-Null Count  Dtype         
---  ------                                --------------  -----         
 0   id                                    36527 non-null  int64         
 1   titulo                                36527 non-null  str           
 2   estado                                36527 non-null  str           
 3   ultima_modificacion                   36527 non-null  datetime64[us]
 4   fecha_de_apertura                     36527 non-null  datetime64[us]
 5   prioridad                             36527 non-null  str           
 6   solicitante__solicitante              36369 non-null  str           
 7   asignado_a__grupo_de_tecnicos         35292 non-null  str           
 8   asignado_a__tecnico                   35160 non-null  str           
 9   categoria                             34169 non-null  str           
 10  origen_de_la_solicitud                36526 non-null  str           
 11  ubicacion                             2337 non-null   str           
 12  estadisticas__hora_de_resolucion      36527 non-null  str           
 13  seguimientos__origen_de_la_solicitud  10109 non-null  str           
 14  fecha_de_cierre                       36527 non-null  datetime64[us]
 15  fecha_de_solucion                     25074 non-null  datetime64[us]
 16  resolucion_horas_decimal              36527 non-null  float64       
 17  cumple_SLA                            36527 non-null  bool          
 18  fecha_de_apertura_dia                 36527 non-null  int32         
 19  fecha_de_apertura_mes                 36527 non-null  int32         
 20  fecha_de_apertura_año                 36527 non-null  int32         
 21  fecha_de_apertura_hora                36527 non-null  int32         
 22  creado_en_horario_laboral             36527 non-null  bool          
 23  fecha_de_apertura_periodo_mes         36527 non-null  period[M]     
dtypes: bool(2), datetime64[us](4), float64(1), int32(4), int64(1), period[M](1), str(11)
memory usage: 5.6 MB
None
----------------------------------------
```