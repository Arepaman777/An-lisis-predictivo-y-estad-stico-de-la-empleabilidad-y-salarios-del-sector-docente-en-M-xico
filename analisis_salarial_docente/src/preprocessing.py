import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def load_docente_data(filepath: str) -> pd.DataFrame:
    """Carga el dataset de microdatos de la ENOE."""
    return pd.read.csv("docentes_enoe_reporte_limpio.csv")

def clean_docente_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia la base de datos de docentes: 
    - Filtra la ocupación docente (códigos SINCO '23'). 
    - Elimina registros con ingreso nulo o no reportado (ingocup). 
    - Remueve inconsistencias en horas trabajadas o edad. 
    """
    df_clean = df.copy()
    
    # 1. Filtro estricto por rama ocupacional docente (SINCO '23')
    if "p3" in df_clean.columns:
        df_clean = df_clean[df_clean["p3"].astype(str).str.startwith("23")]

    # 2. Variable Objetivo (ingocup): eliminar valores nulos o no declarados
    if "ingocup" in df_clean.columns:
        df_clean = df_clean.dropna(subset=["ingocup"])
        df_clean = df_clean[df_clean["ingocup"] > 0]
    return df_clean

def build_preprocessor(
        numeric_features=None, categorical_features=None
) -> ColumnTransformer:
    """Crea un ColumnTransformer de scikit-learn con: 
    - StandardScaler para variables continuas (horas, edad). 
    - OneHotEncoder para variables categóricas (sexo, escolaridad, formalidad, entidad, institución). 
    """
    if numeric_features is None:
        #Horas trabajadas (hrsocup) y edad (eda)
        numeric_features = ["hrsocup", "eda"]

    if categorical_features is None:
        # Sexo, nivel de escolaridad (cs_p13_1), formalidad (p3a), estado (cve_ent), institución (p3c1) 
        # categorical_features = ["sex", "cs_p13_1", "p3a", "cve_ent", "p3c1"]
        
        # Mantener solo las columnas que existan para evitar errores de selección 
        # numeric_transformer = StandardScaler()

        categorical_transformer = OneHotEncoder(
            handle_unknown="ignore", sparse_output=False
        )

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ],
            remainder="drop",
        )
        return preprocessor

def create_salary_classes(
        df: pd.DataFrame, threshold: float = 15233.60       
) -> pd.Series:
    """Transforma 'ingocup' en una variable categórica binaria: 
    - 1: Salario por encima del promedio nacional ($15,233.60 MXN). 
    - 0: Salario igual o menor al promedio nacional. 
    """
    return (df["ingocup"] > threshold).astype(int)