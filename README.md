# análisis_nf

Este repositorio contiene el código y los datos utilizados para el análisis de niveles freáticos en distintas regiones de Australia, como parte de una investigación de tesis de maestría.

## Flujo del trabajo

## 1. Datos fuente (en Google drive: https://drive.google.com/drive/u/0/folders/1kkyR0gEmZlVYvAxt_IyXx7gXXHXx0_Ma)

Los datos originales utilizados en este análisis provienen del portal **[Australian Groundwater Explorer](http://www.bom.gov.au/water/groundwater/explorer/map.shtml)** del Bureau of Meteorology (BoM). Para cada estado se descargaron archivos ZIP que contienen:

- Medidas de niveles de agua: `level_<state>.csv`
- Medidas de salinidad: `salinity_<state>.csv`
- Información de hidroquímica: `hydrochem_bore_<state>.csv` y `hydrochem_results_<state>.csv`
- Archivos de la base de datos NGIS v1.7.1 (lithology, unidades hidrogeológicas, construcción, etc.)
- Notas del producto: `gw_state_README.txt`

Estos datos están estandarizados por BoM según las regulaciones nacionales de agua, y se han estructurado en carpetas por estado:

- `Australian Capital Territory (ACT)`
- `New South Wales (NSW)`
- `Northern Territory (NT)`
- `Queensland (QLD)`
- `South Australia (SA)`
- `Tasmania (TAS)`
- `Victoria (VIC)`
- `Western Australia (WA)`

La estructura y contenido específico puede variar según el formato de descarga (geodatabase, shapefiles o CSV).


### 2. Procesamiento por regiones geográficas (en Google drive: https://drive.google.com/drive/u/0/folders/1kkyR0gEmZlVYvAxt_IyXx7gXXHXx0_Ma)

El análisis inicial se organizó por regiones geográficas: ACT, NSW, NT, QLD, TAS, VIC y WA. Para cada región se trabajó con dos variables: SWL (Static Water Level) y DTW (Depth to Water). El flujo general del procesamiento se resume así:

- Se descargaron y procesaron archivos `.npz` para ambas variables.
- Se contabilizaron las estaciones disponibles por estado.
- Se generaron versiones ajustadas para análisis con modelos de regresión.

- **carga\_SWL / carga\_DTW**: Selección de estaciones con mínimo de datos y generación de gráficos por estado (se generan array en formatos .npz con el nombre de cada región).
- **rules\_SWL / rules\_DTW**: Se cargan los vectores de la anualización y se proponen dos condiciones más de limpieza (se generan array en formatos .npz con el nombre de cada región).
- **statistics\_SWL / statistics\_DTW**: Extracción de valores estadísticos (promedio, máximo, mínimo, mediana, varianza).
- **lat-lon\_SWL / lat-lon\_DTW**: Consolidación de información espacial con estadísticas en archivos unificados.
- **distribution\_SWL / distribution\_DTW**: Ubicación espacial y estadísticas por estado, visualizadas según lat-lon y color por categoría.
- **fit\_SWL / fit\_DTW**: Ajuste de tendencias por región con modelos lineales.
- **l1\_SWL / l1\_DTW**: Ajuste de tendencias por región con modelos robustos L1.
- **theilsen\_SWL / theilsen\_DTW**: Ajuste de tendencias por región con modelos robustos Theil-Sen.
- **hydrogeology\_DTW / hydrogeology\_SWL**: Asociación de los pozos con unidades hidrogeológicas y cálculo de pendientes por unidad (fit/L1/Theilsen)

### 3. Análisis general de las pendientes theil-sen

A partir de este punto, los scripts trabajan con un **bloque consolidado de datos para todo el país**, unificando los archivos procesados por región geográfica (pendientes Theilsen).




### 4. Datos derivados

- Archivos finales consolidados por región con estructura `lat-lon + stats`.
- Series temporales vectorizadas en diferentes resoluciones: anual, semestral, trimestral, mensual, semanal y diaria (desde 1970 hasta 2023).
- Imágenes de tendencias
- Mapas 

## Requisitos

- Python 3.10 o superior
- Bibliotecas:
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - geopandas
  - statsmodels

## Uso

1. Clonar el repositorio o descargar el ZIP.
2. Ejecutar los scripts en el orden indicado según el flujo de trabajo.
3. Ver resultados en las carpetas de salida (figuras, tablas, modelos).

## Autor

Afandinop – Tesis de Maestría en Geociencias (2024–2025)
