from PyPDF2 import PdfMerger

# Lista de archivos PDF a unir (coloca los nombres de tus archivos)
pdfs = ["document1.pdf", "document2.pdf", "document3.pdf"]

# Crear el objeto PdfMerger
merger = PdfMerger()

# Agregar cada archivo PDF al merger
for pdf in pdfs:
    merger.append(pdf)

# Guardar el archivo final con los PDFs combinados
merger.write("resultado.pdf")
merger.close()

print("PDFs combinados exitosamente en 'resultado.pdf'")
