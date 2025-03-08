# 📄 UnionPDF

Este proyecto permite unir múltiples archivos PDF en un solo documento utilizando Python y la biblioteca `PyPDF2`.

## 🚀 Requisitos

Asegúrse de tener instalado **Python 3** en el sistema. Verificar con:

```bash
python3 --version
```

## 🛠 Instalación y Configuración

Para evitar conflictos con el sistema, se recomienda usar un **entorno virtual**.

### **1️⃣ Crear y Activar el Entorno Virtual**

Ejecuta los siguientes comandos en la terminal:

```bash
# 1. Navega a la carpeta del proyecto
cd /ruta/del/proyecto

# 2. Crea un entorno virtual
python3 -m venv venv

# 3. Activa el entorno virtual (Mac/Linux)
source venv/bin/activate
```

Cuando el entorno esté activo, verás el prefijo `(venv)` en la terminal.

### **2️⃣ Instalar Dependencias**

Una vez activado el entorno virtual, instala la biblioteca necesaria:

```bash
pip install PyPDF2
```

### **3️⃣ Ejecutar el Script**

Para unir los archivos PDF, simplemente ejecuta:

```bash
python PDFUnion.py
```

Esto generará un archivo con los documentos combinados.

### **4️⃣ Desactivar el Entorno Virtual (opcional)**

Si terminas de trabajar y quieres salir del entorno virtual, usa:

```bash
deactivate
```

## 🔥 Solución a Problemas Comunes

### ❌ `ModuleNotFoundError: No module named 'PyPDF2'`

Si ves este error, asegúrate de que el entorno virtual está activado y `PyPDF2` está instalado dentro de él:

```bash
source venv/bin/activate
pip install PyPDF2
```

### ❌ `externally-managed-environment` error en MacOS

Si `pip install PyPDF2` falla debido a una restricción del sistema, usa un entorno virtual como se explica arriba.

