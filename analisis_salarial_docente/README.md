# Análisis Estadístico y Predictivo de la Empleabilidad y Salarios del Sector Docente en México

Este repositorio contiene el desarrollo completo del proyecto de análisis econométrico y de aprendizaje automático enfocado en la evaluación de los salarios, la escolaridad y los factores de empleabilidad del sector docente en México, utilizando los microdatos de la ENOE (INEGI).

## Contenido

### Notebooks

**`00_cruce_enoe.ipynb`**
- Ingesta, cruce y unión de los microdatos trimestrales de la ENOE.
- Filtrado inicial de registros de docentes mediante catálogos y códigos ocupacionales específicos.

**`01_limpieza_y_anomalias.ipynb`**
- Limpieza de datos, manejo de valores nulos y filtrado de ingresos/horas válidos.
- Implementación del algoritmo Isolation Forest para la detección y depuración de anomalías y sesgos salariales extremos.

**`02_econometria_y_brecha_genero.ipynb`**
- Estimación de la Ecuación de Mincer mediante regresión lineal múltiple con errores robustos (statsmodels).
- Análisis econométrico de los retornos a la escolaridad, la experiencia laboral y evaluación de diferencias salariales.

**`03_modelos_predictivos.ipynb`**
- Implementación de modelos de machine learning no lineal con Random Forest Regressor (scikit-learn).
- Partición de datos, entrenamiento, evaluación de desempeño ($R^2$, MAE) y extracción de la importancia de variables.

### Material de apoyo

**`Análisis Predictivo Docente (8).pdf`**
- Presentación teórica y preliminar antes de obtener resultados concretos.


## Objetivos

Al revisar el proyecto se podrá:
- Aplicar un pipeline completo de ciencia de datos sobre microdatos demográficos y laborales reales.   
- Modelar retornos salariales utilizando tanto enfoques econométricos paramétricos (Mincer) como algoritmos de ensambles no lineales (Random Forest).   
- Identificar y aislar de manera sistemática valores atípicos mediante técnicas de aprendizaje no supervisado.
- Interpretar coeficientes y métricas de evaluación para la formulación de conclusiones basadas en evidencia.


## Datasets

**Microdatos ENOE (INEGI)**
- Encuesta Nacional de Ocupación y Empleo (módulos sociodemográficos y de ocupación).
- Variables clave: ingreso ocupacional (ingocup), horas trabajadas (hrsocup), años de escolaridad y categorías ocupacionales (SINCO).
- Ubicación local: ../data/raw/ y ../data/processed/


## Orden recomendado de ejecución

1. `00_cruce_enoe.ipynb` - Para unificar las fuentes de datos crudos.
2. `01_limpieza_y_anomalias.ipynb` - Para depurar la muestra y eliminar anomalías estadísticas.
3. `02_econometria_y_brecha_genero.ipynb` - Para el análisis econométrico e inferencial clásico.
4. `03_modelos_predictivos.ipynb` - Para la experimentación con Machine Learning y extracción de importancias.


## Requisitos previos

- Entorno de desarrollo en Python (Jupyter Notebooks / VS Code).
- Librerías principales: pandas, numpy, statsmodels, scikit-learn, matplotlib, seaborn.


## Conceptos clave

- **Ecuación de Mincer** - Modelo econométrico clásico para estimar el impacto de la educación y experiencia en los ingresos.   
- **Isolation Forest** - Algoritmo de aislamiento para la detección de anomalías y atípicos multidimensionales.
- **Random Forest Regressor** - Modelo de ensamble basado en árboles de decisión para capturar relaciones no lineales.
- **Importancia de Variables** - Métrica de los modelos de árboles para jerarquizar los factores determinantes del salario.  
