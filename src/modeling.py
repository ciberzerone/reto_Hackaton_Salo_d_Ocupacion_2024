from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def train_logistic_regression(X_train, y_train, X_test, y_test):
    """Entrena un modelo de regresión logística."""
    log_reg = LogisticRegression(solver='saga', max_iter=200)
    log_reg.fit(X_train, y_train)
    y_pred = log_reg.predict(X_test)
    print("Resultados del modelo de Regresión Logística:")
    print(classification_report(y_test, y_pred))
    return y_pred

def train_random_forest(X_train, y_train, X_test, y_test):
    """Entrena un modelo Random Forest."""
    rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_clf.fit(X_train, y_train)
    y_pred = rf_clf.predict(X_test)
    print("Resultados del modelo Random Forest:")
    print(classification_report(y_test, y_pred))
    return y_pred

def plot_confusion_matrices(y_test, y_pred_logreg, y_pred_rf):
    """Dibuja las matrices de confusión para los modelos."""
    plt.figure(figsize=(14, 6))

    # Matriz de confusión para Regresión Logística
    plt.subplot(1, 2, 1)
    sns.heatmap(confusion_matrix(y_test, y_pred_logreg), annot=True, fmt='d', cmap='Blues')
    plt.title('Matriz de Confusión - Regresión Logística')

    # Matriz de confusión para Random Forest
    plt.subplot(1, 2, 2)
    sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt='d', cmap='Greens')
    plt.title('Matriz de Confusión - Random Forest')

    plt.tight_layout()
    plt.show()
