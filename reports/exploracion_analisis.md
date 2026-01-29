# Analisis preliminares de los datos

## Columnas y nombres
Las columnas de los años no son iguales y estan algunos mal escritos. Se corrigieron y se normalizaron para todos los años.

## Analisis de nulos
En general los datos estan bien completos, los datos fundamentales estan casi completos y los faltantes son minimos.

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