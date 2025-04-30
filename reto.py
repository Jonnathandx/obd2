import matplotlib.pyplot as plt

# Diccionarios para almacenar datos por PID
data = {
    '05': [],  # Temperatura del refrigerante del motor
    '0C': [],  # RPM
    '0D': [],  # Velocidad
    '2F': [],  # Nivel de combustible
    '0F': []   # Temperatura del aire de admisión
}

# Archivo .asc
file_path = '00000001.asc'

# Procesar el archivo
with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if '7e8' in line:
            parts = line.strip().split()
            if len(parts) < 10:
                continue

            try:
                timestamp = float(parts[0])
                data_bytes = parts[-8:]

                if data_bytes[1].upper() == '41':  # Modo 01 respuesta
                    pid = data_bytes[2].upper()
                    if pid in data:
                        if pid == '05':  # Temperatura del refrigerante del motor
                            A = int(data_bytes[3], 16)
                            value = A - 40
                        elif pid == '0C':  # RPM
                            A = int(data_bytes[3], 16)
                            B = int(data_bytes[4], 16)
                            value = (A * 256 + B) / 4
                        elif pid == '0D':  # Velocidad
                            value = int(data_bytes[3], 16)
                        elif pid == '2F':
                            A = int(data_bytes[3], 16)
                            value = A / 2.55
                        elif pid == '0F':  # Temperatura del aire de admisión
                            A = int(data_bytes[3], 16)
                            value = A - 40
                        data[pid].append((timestamp, value))
            except Exception:
                continue

# Información de los PIDs
pids_info = {
    '05': 'Temperatura del refrigerante del motor (°C)',
    '0C': 'RPM del Motor',
    '0D': 'Velocidad del Vehículo (km/h)',
    '2F': 'Nivel de combustible (%)',
    '0F': 'Temperatura del aire de admisión (°C)'
}

# Crear un gráfico por cada PID
for pid in ['05', '0C', '0D', '2F', '0F']:
    if data[pid]:
        times, values = zip(*data[pid])
        plt.figure(figsize=(10, 4))
        plt.plot(times, values, label=pids_info[pid], color='tab:blue')
        plt.title(pids_info[pid])
        plt.xlabel('Tiempo (s)')
        plt.ylabel(pids_info[pid])
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
