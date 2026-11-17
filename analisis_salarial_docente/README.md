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

**`02.1_econometria_y_brecha_genero.ipynb`** 
- Evaluación de robustez y *benchmark* no lineal mediante *Random Forest Regressor* utilizando el dataset con varianza salarial no controlada.
- Extracción y análisis de importancia de variables (*feature importance*) para contrastar la estabilidad de los predictores clave frente al modelo econométrico lineal.

**`03_modelos_predictivos.ipynb`**
- Entrenamiento y evaluación de un *benchmark* de múltiples modelos de Machine Learning (Regresión Ridge, Árboles de Decisión, Random Forest y Gradient Boosting con pérdida de Huber).
- Análisis comparativo de métricas de desempeño ($R^2$ y MedAE).

**`04_clustering_perfiles.ipynb`**
- Segmentación no supervisada de perfiles docentes mediante algoritmos de agrupamiento (*K-Means* respaldado por el método del codo y coeficiente de silueta) y reducción dimensional (*PCA*).
- Identificación de clústeres por carga horaria e inserción laboral.

**`05_interpretabilidad_shap.ipynb`**
- Explicabilidad avanzada del modelo predictivo mediante valores SHAP (*SHapley Additive exPlanations*).
- Generación de gráficos de resumen (*beeswarm*), importancia absoluta promedio y descomposición individual de predicciones en pesos mexicanos (MXN).

### Material de apoyo y Reportes

**`Análisis Predictivo Docente (8).pdf`** - Presentación teórica y preliminar antes de obtener resultados concretos.

**`Proyecto final_BD_Advance6.pdf`** — Reporte técnico final y científico integrando toda la arquitectura analítica.


## Objetivos

Al revisar el proyecto se podrá:
- Aplicar un *pipeline* completo de ciencia de datos sobre microdatos demográficos y laborales reales.   
- Modelar retornos salariales utilizando tanto enfoques econométricos paramétricos (Mincer) como algoritmos de ensambles no lineales.   
- Identificar y aislar de manera sistemática valores atípicos mediante técnicas de aprendizaje no supervisado.
- Segmentar perfiles de la fuerza laboral docente con técnicas de agrupamiento.
- Explicar las predicciones algorítmicas utilizando explicabilidad basada en teoría de juegos (SHAP).


## Datasets

**Microdatos ENOE (INEGI)**
- Encuesta Nacional de Ocupación y Empleo (módulos sociodemográficos y de ocupación).
- Variables clave: ingreso ocupacional (ingocup), horas trabajadas (hrsocup), años de escolaridad y categorías ocupacionales (SINCO).
- Ubicación local: ../data/raw/ y ../data/processed/


## Orden recomendado de ejecución

1. `00_cruce_enoe.ipynb` — Unificación de las fuentes de datos crudos.
2. `01_limpieza_y_anomalias.ipynb` — Depuración de la muestra y eliminación de anomalías con *Isolation Forest*.
3. `02_econometria_y_brecha_genero.ipynb` — Análisis econométrico e inferencial clásico (Ecuación de Mincer).
4. `02.1_econometria_y_brecha_genero.ipynb`  — Evaluación de robustez y *benchmark* no lineal mediante *Random Forest* frente al modelo lineal.
5. `03_modelos_predictivos.ipynb` — Experimentación con Machine Learning y *benchmark* de modelos.
6. `04_clustering_perfiles.ipynb` — Segmentación de perfiles docentes (*K-Means* y *PCA*).
7. `05_interpretabilidad_shap.ipynb` — Explicabilidad y análisis de impacto con valores SHAP.


## Requisitos previos

- Entorno de desarrollo en Python (Jupyter Notebooks / VS Code).
- Librerías principales: pandas, numpy, statsmodels, scikit-learn, matplotlib, seaborn.


## Conceptos clave

- **Ecuación de Mincer** — Modelo econométrico clásico para estimar el impacto de la educación y experiencia en los ingresos.   
- **Isolation Forest** — Algoritmo de aislamiento para la detección multidimensional de anomalías.
- **Gradient Boosting & Random Forest** — Modelos predictivos avanzados para capturar relaciones no lineales y minimizar el error absoluto mediano.
- **K-Means y PCA** — Técnicas de clustering y reducción de dimensionalidad para tipificar perfiles docentes.
- **Valores SHAP** — Explicabilidad de modelos de caja negra para cuantificar el impacto marginal en pesos mexicanos de cada característica.
