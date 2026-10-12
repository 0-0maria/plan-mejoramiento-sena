import pandas as pd
from sklearn.linear_model import LinearRegression

datos = {
    'horas_estudio': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'calificacion': [20, 40, 45, 50, 65, 70, 80, 85, 95, 98]
}

df = pd.DataFrame(datos)

X = df[['horas_estudio']]
y = df['calificacion']

modelo = LinearRegression()
modelo.fit(X, y)

horas_prueba = [[5.5]]
prediccion = modelo.predict(horas_prueba)


print("=== MODELO DE REGRESIÓN LINEAL (INTELIGENCIA ARTIFICIAL) ===")
print(f"Pendiente del modelo: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"Predicción para 5.5 horas de estudio: {prediccion[0]:.2f}")