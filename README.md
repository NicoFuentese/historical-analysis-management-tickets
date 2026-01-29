# historical-analysis-management-tickets

## Crer ambiente virtual venv

Despues de activar e instalar dependencias en el ambiente virtual, seleccionar el kernel (elegir el .venv).

```powershell
# Crear ambiente virtual .venv

#ubuntu
python3 -m venv .venv

#windows
python -m venv .venv

# Activar Ambiente Virtual

#windows
.venv/Scripts/activate

#ubuntu
source .venv/bin/activate

#Desactivar ambiente virtual
deactivate

#Instalar requerimientos
pip install -r requirements.txt
```

# Columnas de los datos brutos:

1. id
2. titulo
3. estado
4. ultima_modificacion
5. fecha_de_apertura
6. prioridad
7. solicitante__solicitante
8. asignado_a__grupo_de_tecnicos
9. asignado_a__tecnico
10. categoria
11. origen_de_la_solicitud
12. ubicacion
13. estadisticas__hora_de_resolucion
14. seguimientos__origen_de_la_solicitud
15. fecha_de_cierre
16. fecha_de_solucion
17. unnamed_16