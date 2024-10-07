import pandas as pd

def load_data(file_path):
    """Carga los datos del archivo CSV."""
    df = pd.read_csv(file_path)
    print("Datos cargados con éxito.")
    return df

def clean_data(df):
    """Realiza la limpieza de los datos."""
    # Eliminamos columnas irrelevantes o con muchos valores nulos
    df = df.drop(columns=['Numero_expedient', 'Coordenades_UTM_X_ED50', 'Coordenades_UTM_Y_ED50'], errors='ignore')
    
    # Llenar valores nulos con forward fill (sin advertencia)
    df.ffill(inplace=True)
    
    print("Datos limpios y preprocesados.")
    return df

if __name__ == "__main__":
    # Cargar y limpiar los datos
    file_path = '../data/raw/accidentes_transito.csv'
    df = load_data(file_path)
    df_clean = clean_data(df)
    
    # Mostrar algunas filas de los datos limpios
    print(df_clean.head())
