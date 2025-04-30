# Análisis de datos OBD-II desde archivo .ASC

Este proyecto en Python permite analizar datos de diagnóstico automotriz capturados en formato `.asc` (trazas CAN) y graficar los parámetros clave del vehículo como RPM, velocidad, temperatura del motor y del aire de admisión.

## 📂 Archivo de entrada

Se espera un archivo `.asc` generado por una herramienta de captura CAN (como Vector o herramientas compatibles). Este archivo debe contener tramas OBD-II con identificadores estándar (`7E8` como ID de respuesta).

## 📈 Parámetros analizados

El script extrae y grafica los siguientes PIDs (Parameter IDs) bajo el modo de diagnóstico `01` (datos en tiempo real):

| PID  | Descripción                                 | Unidad         |
|------|---------------------------------------------|----------------|
| 05   | Temperatura del refrigerante del motor      | °C             |
| 0C   | Revoluciones por minuto (RPM)               | RPM            |
| 0D   | Velocidad del vehículo                      | km/h           |
| 0F   | Temperatura del aire de admisión            | °C             |

Cada uno se grafica en una ventana independiente usando Matplotlib.

## 🛠️ Requisitos

- Python 3.x
- `matplotlib`

Puedes instalar los requerimientos con:

```bash
pip install matplotlib
