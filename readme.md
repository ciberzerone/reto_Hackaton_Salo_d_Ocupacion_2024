![cabecera](https://github.com/ciberzerone/reto_Hackaton_Salo_d_Ocupacion_2024/blob/main/img/cabecera.jpg)

![Salo Ocupacio](https://github.com/ciberzerone/reto_Hackaton_Salo_d_Ocupacion_2024/blob/main/img/logoOcupacion.jpg)



# Análisis de Accidentes de Tránsito en Barcelona

## 1. Introducción
Este proyecto tiene como objetivo analizar un conjunto de datos sobre accidentes de tránsito en la ciudad de Barcelona, gestionado por la Guardia Urbana. Utilizando técnicas de análisis exploratorio y modelado predictivo, busca entender patrones en las causas de los accidentes, la gravedad de los mismos y los factores que influyen en su ocurrencia.

## 2. Depuración de Datos
### Criterios de Limpieza
- **Columnas eliminadas:** Se eliminaron las columnas `Numero_expedient`, `Coordenades_UTM_X_ED50`, y `Coordenades_UTM_Y_ED50` debido a que no aportaban valor significativo al análisis.
- **Valores nulos:** Los valores faltantes se completaron usando la técnica `ffill` (forward fill).
- **Normalización:** Se estandarizaron las variables numéricas, como la `Hora_dia`, para asegurar una convergencia más rápida en los modelos predictivos.
- **Codificación de variables:** Las variables categóricas, como `Descripcio_dia_setmana`, se codificaron usando `get_dummies`.

## 3. Resultados
### Análisis Exploratorio de Datos (EDA)
Se realizaron varias visualizaciones para entender la distribución y los patrones en los accidentes:
- **Distribución de accidentes por distrito:** La mayoría de los accidentes ocurrieron en el distrito de "XXX".
- **Distribución de accidentes por día de la semana:** Los días con más accidentes fueron "Viernes" y "Sábado".
- **Causas más comunes de los accidentes:** "No respetar distancia" fue la causa principal en el 40% de los accidentes.

### Modelado Predictivo
- **Modelos implementados:** Se entrenaron modelos de Regresión Logística y Random Forest.
- **Mejores resultados:** El modelo de Random Forest tuvo mejores resultados con un F1-score de `XX`.

## 4. Conclusiones
El análisis sugiere que los días del fin de semana tienen una mayor incidencia de accidentes. Además, se identificó que la causa más común es la falta de respeto a la distancia entre vehículos. Este tipo de análisis puede ayudar a las autoridades a implementar campañas de concientización para reducir los accidentes en los días y lugares más críticos.


<hr>

## Author

### Nombre
**Yimmy Beltran**

## Información de Contacto

- **LinkedIn**: [https://www.linkedin.com/in/gianmarco-beltran-13959b232/](https://www.linkedin.com/in/gianmarco-beltran-13959b232/)
- **GitHub**: [https://github.com/ciberzerone](https://github.com/ciberzerone)
- **Correo Electrónico**: [gianmarcobeltran@gmail.com](mailto:gianmarcobeltran@gmail.com)