from asammdf import MDF
import sys

# Ruta del archivo MF4 de entrada
input_mf4 = '00000001.MF4'
# Ruta del archivo ASC de salida
output_asc = '00000001.asc'

# Cargar el archivo MF4
mdf = MDF(input_mf4)

# Exportarlo a formato ASC
mdf.export(fmt='asc', filename=output_asc)

print(f"Conversión completa. Archivo guardado como: {output_asc}")
