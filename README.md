# Análisis de datos OBD-II desde archivo .MF4

Este proyecto en Python permite analizar datos de diagnóstico automotriz capturados en formato `.asc` (trazas CAN) y graficar los parámetros clave del vehículo como RPM, velocidad, temperatura del motor y del aire de admisión.

## 📂 Archivo de entrada
Se espera un archivo `.mf4` generado por una herramienta de captura CAN (como Vector o herramientas compatibles) para la convesión a `.asc`. Este último archivo debe contener tramas OBD-II con identificadores estándar (`7E8` como ID de respuesta).

## 📈 Parámetros analizados

El script extrae y grafica los siguientes PIDs (Parameter IDs) bajo el modo de diagnóstico `01` (datos en tiempo real):

| PID  | Descripción                                 | Unidad         |
|------|---------------------------------------------|----------------|
| 05   | Temperatura del refrigerante del motor      | °C             |
| 0C   | Revoluciones por minuto (RPM)               | RPM            |
| 0D   | Velocidad del vehículo                      | km/h           |
| 2F   | Nivel de combustible                        | %              |
| 0F   | Temperatura del aire de admisión            | °C             |

Cada uno se grafica en una ventana independiente usando Matplotlib.

## 🛠️ Requisitos

- Python 3.x
- `matplotlib`
- `asammdf`

Puedes instalar los requerimientos con:

```bash
sudo apt install python3-matplot
sudo apt install python3-asammdf
