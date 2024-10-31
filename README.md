📝 Descripción
Este Laboratorio  implementa un sistema de captura y análisis de señales electrocardiográficas (ECG) utilizando el microcontrolador ESP32 y el módulo AD8232. El sistema permite analizar la variabilidad de la frecuencia cardíaca (HRV) mediante el procesamiento de los intervalos R-R y su análisis a través de la transformada wavelet.

## Requisitos

Este laboratorio requiere las siguientes bibliotecas:

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `pywt` (para la Transformada Wavelet)

Puedes instalar las bibliotecas necesarias ejecutando:

pip install numpy pandas matplotlib scipy pywt

# Transformada Wavelet

## Introducción

La **Transformada Wavelet** es una técnica matemática utilizada para el análisis de señales y datos. A diferencia de la Transformada de Fourier, que proporciona información sobre la frecuencia, la Transformada Wavelet permite una representación tanto en el dominio del tiempo como en el de la frecuencia, lo que la hace especialmente útil para señales no estacionarias.

## Objetivos

- Comprender los fundamentos de la Transformada Wavelet.
- Implementar la Transformada Wavelet utilizando Python.
- Aplicar la Transformada Wavelet en ejemplos prácticos de análisis de señales.

## Estructura

**🔬 Fundamento Teórico**

1. Sistema nervioso autónomo (SNA)
El sistema nervioso autónomo (SNA) es una parte del sistema nervioso que regula involuntariamente las funciones fisiológicas del cuerpo como la frecuencia cardíaca, la presión arterial, la digestión y la respiración. 

**Sistema nervioso simpático:** Activa la respuesta de “lucha o huida”, aumenta la frecuencia cardíaca y la presión arterial y prepara el cuerpo para situaciones estresantes.

**Sistema nervioso parasimpático:** Promueve la respuesta de “descansar y digerir”, reduce la frecuencia cardíaca y promueve la relajación y la recuperación.
**2. Variabilidad de la Frecuencia Cardíaca (HRV)**

La Variabilidad de la Frecuencia Cardíaca (HRV) es una medida de la variación en el tiempo entre latidos sucesivos del corazón. Se considera un indicador importante de la salud del sistema cardiovascular y del estado del SNA. Una alta HRV generalmente se asocia con una buena salud y una mayor capacidad de adaptación al estrés, mientras que una baja HRV puede ser un signo de estrés crónico, fatiga o problemas de salud.

**Cálculo de la HRV:** Se calcula a partir de los intervalos R-R (el tiempo entre picos R en un electrocardiograma) utilizando diversos métodos, como:

**Dominio del Tiempo:** Análisis de estadísticas básicas, como la media y la desviación estándar de los intervalos R-R.
**Dominio de la Frecuencia:** Análisis espectral que divide la HRV en componentes de alta y baja frecuencia.

La variabilidad de la frecuencia cardíaca (HRV) es un indicador clave para evaluar la salud del sistema nervioso autónomo (SNA). El análisis incluye:
Parámetros en el Dominio del Tiempo

**RMSSD:** Variabilidad a corto plazo de intervalos R-R
**Media R-R:** Promedio del tiempo entre latidos
**SDNN:** Variabilidad global de intervalos R-R
**pNN30/pNN50:** Porcentaje de diferencias consecutivas >30ms o >50ms

**3. Transformada Wavelet**
La Transformada Wavelet es una técnica de análisis matemático que permite descomponer una señal en sus componentes de frecuencia y temporal. A diferencia de la Transformada de Fourier, que solo proporciona información de frecuencia, la Transformada Wavelet ofrece una representación de la señal que es simultáneamente en el dominio del tiempo y en el dominio de la frecuencia. Esto es especialmente útil para señales no estacionarias, como las señales ECG.

**Bandas de Frecuencia (Análisis Wavelet)**

Baja frecuencia (0.04 - 0.15 Hz): Actividad simpática
Alta frecuencia (0.15 - 0.4 Hz): Tono parasimpático

--> **Captura de la señal**
   **🛠️ Implementación**
ESP32
Módulo AD8232
Electrodos
**Configuración del Sistema**
Conexión del ESP32 con el módulo AD8232
Colocación de electrodos en el paciente
Configuración de la adquisición en tiempo real

El módulo AD8232 se conecta al ESP32, utilizando el pin D35(Utilizar el PIN que deses para la conexion serial) para recibir la señal de ECG. Se verifica que todas las conexiones de alimentación y tierra estén adecuadamente configuradas para garantizar una captura de señal sin interferencias.
Colocación de Electrodos: Los electrodos se colocan en el pecho del sujeto, siguiendo el esquema de derivaciones estándar, para obtener una señal ECG de calidad.

![] (https://github.com/Nupan07/Lab4ECG/blob/main/Colocacion%20electrodos.png)


Adquisición en Tiempo Real: El ESP32 captura la señal ECG y la transmite a una computadora o dispositivo donde se ejecuta un software de visualización y análisis en tiempo real, permitiendo una observación continua de la señal.


Preprocesamiento

Filtro pasa-bajos (fc = 30 Hz)
Filtro pasa-altos (fc = 0.5 Hz)
Detección de picos R mediante umbral dinámico


Análisis HRV

Cálculo de intervalos R-R
Obtención de métricas temporales
Análisis espectral mediante wavelet Morlet



📊 Resultados de Prueba
Métricas Temporales

Intervalos R-R totales: 349
Media R-R: 0.214 s
SDNN: 0.001 s
RMSSD: 0.001 s
pNN30: 0.09%

Análisis Espectral

Mayor actividad en banda de baja frecuencia
Menor potencia en banda de alta frecuencia
Predominio de actividad simpática

📋 Requisitos
Software

IDE de Arduino
Bibliotecas necesarias (lista pendiente)

Hardware

ESP32
Módulo AD8232
Electrodos compatibles
Cables de conexión
