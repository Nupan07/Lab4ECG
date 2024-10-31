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

La wavelet Morlet combina una onda sinusoidal y una envoltura gaussiana. Esto significa que tiene la forma de una onda que se modula (cambia) de manera suave, lo que nos permite observar diferentes detalles de la señal que estamos analizando. Esta combinación nos ayuda a identificar patrones en la señal que podrían no ser visibles de otra manera.

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

![](https://github.com/Nupan07/Lab4ECG/blob/main/Colocacion%20electrodos.png)


**Adquisición en Tiempo Real:** El ESP32 captura la señal ECG y la transmite a una computadora o dispositivo donde se ejecuta un software de visualización y análisis en tiempo real, permitiendo una observación continua de la señal.


**Preprocesamiento**
## Cálculos para el Filtro Pasa-Bajos de Cuarto Orden

El diseño de un filtro pasa-bajos es crucial para eliminar el ruido en señales como el ECG. En este caso, se utilizó un filtro Butterworth de 4 orden. A continuación, se detallan los cálculos y consideraciones para determinar los parámetros del filtro. La elección de un filtro pasa-bajos se basa en la necesidad de eliminar el ruido de alta frecuencia, que puede interferir con la correcta identificación de los picos R en la señal ECG.

### Parámetros del Filtro

- **Frecuencia de Muestreo (fs)**: 1000 Hz
- **Frecuencia de Corte (fc)**: 30 Hz
- **Orden del Filtro (n)**: 4

### 2. Cálculo de la Frecuencia 

La frecuencia de corte  (w) se calcula utilizando la siguiente fórmula: w = fc / (fs/2)
w = 30 / (1000/2) = 30 / 500 = 0.06

### Cálculo de Coeficientes del Filtro

Para calcular los coeficientes del filtro Butterworth, se utiliza la función `butter` de la biblioteca:

from scipy.signal import butter

b, a = butter(4, w, 'low')

### Detección de Picos R
Los picos R en la señal filtrada se detectaron utilizando el método find_peaks de scipy.signal, con un umbral de altura ajustado a 0.5. Estos picos corresponden a los picos máximos de cada latido cardíaco, y su detección es fundamental para el cálculo de los intervalos R-R y la extracción de parámetros de HRV.

###  Cálculo de Intervalos R-R
Los intervalos R-R se calcularon como las diferencias entre las posiciones de los picos R, en segundos. Estos intervalos son representativos de la variabilidad del tiempo entre latidos y permiten evaluar el comportamiento del sistema nervioso autónomo.
Parámetros de Variabilidad de la Frecuencia Cardíaca (HRV)
A partir de los intervalos R-R, se calcularon los siguientes parámetros de HRV en el dominio del tiempo:

###  Media de intervalos R-R: Promedio del tiempo entre latidos.
### Desviación estándar de los intervalos R-R: Refleja la dispersión y la variabilidad general de la señal.
RMSSD : Mide la variabilidad a corto plazo, particularmente útil para evaluar la actividad del sistema parasimpático.
Porcentaje de diferencias consecutivas mayores a 30 ms: Este porcentaje se calcula comparando diferencias absolutas consecutivas de intervalos R-R con un umbral de 30 ms, un indicador común de la variabilidad en estudios de HRV.

###  Análisis de la Transformada Wavelet en Ventanas
Para un análisis más detallado en el dominio del tiempo-frecuencia, se aplicó la transformada wavelet continua utilizando la wavelet Morlet (cmor1.5-1.0). Este análisis permite visualizar cómo se distribuyen las frecuencias en cada segmento de la señal ECG.

La transformada wavelet se aplicó sobre ventanas de 5000 puntos, con un desplazamiento de 1000 puntos entre ventanas, para analizar la dinámica de la señal a través del tiempo.



###  📊 Resultados de Prueba
Estas son algunas de los resultados y ventanas realizadas ya que son demasiadas 
![](https://github.com/Nupan07/Lab4ECG/blob/main/Resultados.png)
![](https://github.com/Nupan07/Lab4ECG/blob/main/Ventana%201000-6000.png)
![](https://github.com/Nupan07/Lab4ECG/blob/main/Ventana69000-74000.png)

###  Espectrograma
  ![](https://github.com/Nupan07/Lab4ECG/blob/main/Espectograma.png)

Número de intervalos R-R: 349
Media de intervalos R-R: 0.214 s
Desviación estándar: 0.002 s
RMSSD (variabilidad de corto plazo): 0.001 s
Diferencias consecutivas > 30 ms: 0.3
Porcentaje de diferencias > 30 ms: 0.09 %

### Número de intervalos R-R: 349
Este número representa la cantidad total de intervalos de tiempo medidos entre picos R consecutivos. La identificación de 349 intervalos indica que se ha realizado una detección eficaz de los picos en la señal analizada.

### Media de intervalos R-R: 0.214 s
La media de 0.214 segundos sugiere un ritmo cardíaco promedio de aproximadamente 140 latidos por minuto (lpm). Este cálculo se realiza mediante la fórmula:  Frecuencia cardíaca = 60 / Media R-R (s)
Un ritmo cardíaco elevado puede ser indicativo de un estado de actividad o estrés, dependiendo del contexto en el que se tomó la señal.


**Desviación estándar:**  0.000 s
La desviación estándar, que mide la variabilidad de los intervalos R-R, resulta ser 0.000 s. Esto indica que todos los intervalos son prácticamente idénticos, sugiriendo un ritmo cardíaco extremadamente regular. Esta uniformidad podría ser característica de ciertas condiciones fisiológicas, como el reposo o la adaptación a un régimen de ejercicio específico.



**RMSSD (variabilidad de corto plazo):** 0.001 s
El RMSSD es un indicador de la variabilidad de la frecuencia cardíaca a corto plazo. Un valor de 0.001 s sugiere que existe poca variabilidad en los intervalos R-R, lo que puede estar relacionado con una respuesta de estrés o falta de adaptabilidad en el sistema cardiovascular. Esta métrica es crucial para entender la función autonómica del corazón.
Diferencias consecutivas > 30 ms: 0.3
Este valor representa la cantidad de diferencias entre intervalos R-R que superan el umbral de 30 ms. Un resultado de 0.3 indica que no se registraron diferencias significativas, lo que reafirma la estabilidad del ritmo cardíaco.

**Porcentaje de diferencias > 30 ms:** 0.09 %
El porcentaje se calcula dividiendo el número de diferencias que superan los 30 ms por el total de intervalos R-R, multiplicado por 100. Con un valor de 0.09 %, se observa que solo una fracción mínima de los intervalos presenta variabilidad significativa, corroborando la conclusión anterior de un ritmo cardíaco estable.



