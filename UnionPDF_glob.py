import glob

from PyPDF2 import PdfMerger

# Buscar todos los archivos PDF en la carpeta 'data'
files = glob.glob("data/*.pdf")

# Mostrar los archivos encontrados (opcional)
print("Archivos encontrados:", files)

# Crear el objeto PdfMerger
merger = PdfMerger()

# Agregar cada archivo PDF encontrado en la carpeta
for file in files:
    merger.append(file)

# Guardar el archivo final con los PDFs combinados
merger.write("merged.pdf")
merger.close()

print("PDFs combinados exitosamente en 'merged.pdf'")
