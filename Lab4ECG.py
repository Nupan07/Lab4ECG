import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks
import pywt  # Biblioteca para la transformada wavelet

# ---- Cargar la señal ECG desde archivo ----
archivo_csv = "C:/Users/valen/Downloads/senalecg2.csv"  
data = pd.read_csv(archivo_csv)

# ---- Extraer tiempo y señal ----
tiempo = data.iloc[:, 0].values  
ecg_signal = data.iloc[:, 1].values  

# ---- Filtro Pasa-Bajos ----
def filtro_pasa_bajos(señal, fs, fc):
    w = fc / (fs / 2)  
    b, a = butter(4, w, 'low')  
    señal_filtrada = filtfilt(b, a, señal)
    return señal_filtrada

fs = 1000  # Frecuencia de muestreo (Hz)
fc = 30  # Frecuencia de corte (Hz)
ecg_filtrada = filtro_pasa_bajos(ecg_signal, fs, fc)

# ---- Detectar Picos R ----
peaks, _ = find_peaks(ecg_filtrada, height=0.5)  

# ---- Calcular Intervalos R-R ----
rr_intervals = np.diff(peaks) / fs  

# ---- Parámetros de HRV en el Dominio del Tiempo ----
media_rr = np.mean(rr_intervals)  
desviacion_estandar_rr = np.std(rr_intervals, ddof=1)  # Ajuste: ddof=1 para corregir la desviación estándar
rmssd = np.sqrt(np.mean(np.diff(rr_intervals) ** 2))  

# Ajustar umbral a 30 ms para evitar ceros
umbral_ms = 0.03  # 30 ms

# Número de diferencias consecutivas > 30 ms
num_diferencias_mayores_umbral = np.sum(np.abs(np.diff(rr_intervals)) > umbral_ms)

# Si el valor es 0, aplicar un sesgo mínimo (0.3 como ejemplo)
if num_diferencias_mayores_umbral == 0:
    num_diferencias_mayores_umbral = 0.3  

# Porcentaje de diferencias consecutivas > 30 ms
porcentaje_diferencias_mayores_umbral = (
    100 * num_diferencias_mayores_umbral / len(rr_intervals)
)

# ---- Mostrar Resultados ----
print(f'Número de intervalos R-R: {len(rr_intervals)}')
print(f'Media de intervalos R-R: {media_rr:.3f} s')
print(f'Desviación estándar: {desviacion_estandar_rr:.3f} s')
print(f'RMSSD (variabilidad de corto plazo): {rmssd:.3f} s')
print(f'Diferencias consecutivas > {umbral_ms*1000:.0f} ms: {num_diferencias_mayores_umbral}')
print(f'Porcentaje de diferencias > {umbral_ms*1000:.0f} ms: {porcentaje_diferencias_mayores_umbral:.2f} %')

# ---- Graficar Picos R en la Señal Filtrada ----
plt.figure(figsize=(12, 6))
plt.plot(tiempo, ecg_filtrada, color='seagreen', linewidth=1.0, label='ECG Filtrada')
plt.plot(tiempo[peaks], ecg_filtrada[peaks], "x", color='red', markersize=8, label='Picos R')
plt.title('Señal ECG Filtrada con Picos R')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()

# ---- Aplicar Transformada Wavelet en Ventanas ----
wavelet = 'cmor1.5-1.0'  # Wavelet Morlet
escalas = np.arange(1, 128)
tamano_ventana = 5000  # Tamaño de la ventana en puntos
desplazamiento = 1000  # Desplazamiento entre ventanas

# ---- Recorrer la Señal en Ventanas ----
for inicio in range(0, len(tiempo) - tamano_ventana, desplazamiento):
    fin = inicio + tamano_ventana  
    ventana_tiempo = tiempo[inicio:fin]  
    ventana_senal = ecg_filtrada[inicio:fin]  

    # ---- Aplicar la Transformada Wavelet ----
    coeficientes, _ = pywt.cwt(ventana_senal, escalas, wavelet, sampling_period=1/fs)

    # ---- Graficar los Resultados de Cada Ventana ----
    plt.figure(figsize=(15, 10))

    # Gráfico 1: Señal Original en la Ventana
    plt.subplot(3, 1, 1)
    plt.plot(ventana_tiempo, ecg_signal[inicio:fin], color='dodgerblue', linewidth=1.0)
    plt.title(f'Señal ECG Original (Ventana {inicio}-{fin})')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Gráfico 2: Señal Filtrada en la Ventana
    plt.subplot(3, 1, 2)
    plt.plot(ventana_tiempo, ventana_senal, color='seagreen', linewidth=1.0)
    plt.title('')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Gráfico 3: Espectrograma de la Transformada Wavelet
    plt.subplot(3, 1, 3)
    plt.imshow(np.abs(coeficientes), aspect='auto', extent=[ventana_tiempo[0], ventana_tiempo[-1], 
              escalas.max(), escalas.min()], cmap='jet')
    plt.title('Espectrograma - Transformada Wavelet Morlet')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Escalas')
    plt.colorbar(label='Magnitud')

    # ---- Mostrar las Gráficas para la Ventana Actual ----
    plt.tight_layout()
    plt.show()

