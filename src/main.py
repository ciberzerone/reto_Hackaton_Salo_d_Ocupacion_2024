from edad import edad
from data_preprocessing import load_data, clean_data
from modeling import train_logistic_regression, train_random_forest, plot_confusion_matrices
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def run_pipeline(file_path):
    # Cargar y limpiar los datos
    df = load_data(file_path)
    df_clean = clean_data(df)
    
    # Realizar EDAD
    edad(df_clean)
    
    # Codificación de variables categóricas
    df_encoded = pd.get_dummies(df_clean, drop_first=True)

    # Definir características (X) y objetivo (y)
    X = df_encoded.drop(columns=['Descripcio_causa_mediata_No respectar distàncies'])
    y = df_encoded['Descripcio_causa_mediata_No respectar distàncies']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Escalar los datos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Entrenar los modelos
    y_pred_logreg = train_logistic_regression(X_train_scaled, y_train, X_test_scaled, y_test)
    y_pred_rf = train_random_forest(X_train_scaled, y_train, X_test_scaled, y_test)

    # Mostrar matrices de confusión
    plot_confusion_matrices(y_test, y_pred_logreg, y_pred_rf)

if __name__ == "__main__":
    file_path = '../data/raw/accidentes_transito.csv'
    run_pipeline(file_path)
