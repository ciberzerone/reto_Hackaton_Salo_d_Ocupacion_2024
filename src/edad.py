import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def edad(df):
    """Realiza el análisis exploratorio de los datos (EDAD)."""
    # Visualización de accidentes por distrito
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='Nom_districte', order=df['Nom_districte'].value_counts().index)
    plt.xticks(rotation=90)
    plt.title('Distribución de accidentes por distrito')
    plt.show()
    
    # Visualización de accidentes por día de la semana
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Descripcio_dia_setmana', order=df['Descripcio_dia_setmana'].value_counts().index)
    plt.title('Distribución de accidentes según el día de la semana')
    plt.show()

    # Distribución de accidentes por causa mediata
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Descripcio_causa_mediata', order=df['Descripcio_causa_mediata'].value_counts().index)
    plt.xticks(rotation=90)
    plt.title('Distribución de causas de accidentes')
    plt.show()

    # Distribución geográfica de accidentes
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Longitud_WGS84', y='Latitud_WGS84')
    plt.title('Distribución geográfica de accidentes')
    plt.show()

if __name__ == "__main__":
    # Cargar los datos limpios
    from data_preprocessing import load_data, clean_data
    file_path = '../data/raw/accidentes_transito.csv'
    df = load_data(file_path)
    df_clean = clean_data(df)
    
    # Realizar EDAD
    edad(df_clean)
