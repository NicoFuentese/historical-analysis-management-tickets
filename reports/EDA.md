# ANALISIS EXPLORATORIO DE DATOS

El objetivo es identificar observaciones, tendencias, estacionalidad, explosion de demandas, etc.

## Analisis estacionalidad y tendencias con HEATMAP

### Heatmap de Dia vs Hora de apertura de ticket
La gran mayoria de los ticket tiene apertura en horario laboral de lunes a viernes (8:00 - 18:00 hrs.). Dentro de esa tendencia los dias LUNES es donde presento una mayor solicitud de ticket, disminuyendo a medida que avanzamos al VIERNES.

![Heatmap de dia de la semana vs Horas del dia](img/hm_ds_h.png)

Las horas picos donde se solicitan mayores tickets son de las 9:00 a 10:00 horas. 

En las horas de almuerzo se aprecia una disminucion, sin embargo el dia Viernes donde se sale 15:00 horas se puede ver y apreciar que se pierde la apreciacion de la hora de almuerzo.

### Heatmap de Dias del mes vs Hora de apertura de ticket
Se puede ver las tendencias observadas previamente. Ademas que se aprecia una leve tendencia a mayor apertura de tickets en los primeros dias del mes. Aunque esta apreciacion es leve, generalmente el volumen de tickets aperturados depende en menor grado del dia del mes.

![Heat de dia del Mes vs Horas del dia](img/hm_dm_h.png)

Se aprecia el mayor pick de tickets emitidos los dias 2 de cada mes a las 12:00 horas.