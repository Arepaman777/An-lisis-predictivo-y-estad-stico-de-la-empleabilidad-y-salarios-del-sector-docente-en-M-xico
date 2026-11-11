import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def load_docente_data(filepath: str) -> pd.DataFrame:
    return pd.read.csv("docentes_enoe_reporte_limpio.csv")