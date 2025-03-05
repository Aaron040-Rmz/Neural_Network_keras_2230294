# 🧠 Red Neuronal con Keras 🧠

**Estudiante**: Aarón Enrique Ramírez González  
**Tarea 2**: Implementación de una red neuronal usando Keras para clasificación de imágenes.
**Materia**: Sistemas de Visión Artificial  

---

## 📝 Descripción

Este repositorio contiene la implementación de una **red neuronal** utilizando **Keras** (una librería de TensorFlow) para clasificar imágenes del conjunto de datos **MNIST**. El proyecto incluye:

- 🖼️ **Carga y visualización de imágenes** de dígitos escritos a mano.
- 🧩 **Preprocesamiento de datos** para preparar las imágenes y etiquetas.
- 🛠️ **Construcción de una red neuronal** con una capa oculta y una capa de salida.
- 🚀 **Entrenamiento y evaluación** del modelo para medir su precisión.

---

## 📋 Requisitos

Para ejecutar este proyecto, necesitas los siguientes requerimientos:

- **Python 3.12.4**: Es la versión utilizada para la realización del trabajo en cuestión.
- **NumPy**: Para cálculos numéricos y manejo de arreglos.
- **Matplotlib**: Para la generación de gráficas.
- **TensorFlow/Keras**: Para construir y entrenar la red neuronal.

Puedes instalar estas dependencias utilizando `pip`:

```bash
pip install numpy matplotlib tensorflow
```

## 🗂️ Estructura del Proyecto

El proyecto está organizado de la siguiente manera:
```bash
TAREA_2
│
├── src/
│   └── Neuronal_Network_Keras.py  # Script principal de la red neuronal
│
├── .gitignore                # Archivo para ignorar archivos no deseados
├── main.py                   # Script principal para ejecutar el proyecto
├── README.md                 # Este archivo
└── Requirements.txt          # Lista de dependencias del proyecto
```
## 🚀 ¿Cómo usar este repositorio?
Sigue estos pasos para ejecutar el proyecto en tu lab:

### Clona el repositorio 🖥️:
Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu computadora:

```bash
git clone https://github.com/Aaron040-Rmz/Neural_Network_keras_2230294
```
### Cree un nuevo entorno virtual
Se recomienda tener el entorno virtual generado en la carpeta principal para un fácil acceso, su activación y desactivación se realiza de la siguiente forma:

En PowerShell:
```
.\nombre_del_entorno\Scripts\Activate
deactivate
```
En Unix:
```
source nombre_del_entorno/bin/activate
deactivate
```
### Instala las dependencias 📦:
Asegúrate de tener instaladas las bibliotecas necesarias. Ejecuta el siguiente comando para instalarlas:

```bash
pip install -r Requirements.txt
```
### Ejecuta el script principal🚀:
Para entrenar y evaluar la red neuronal, ejecuta:

```bash
python main.py
```
### Visualiza los resultados 👀:

El script mostrará la precisión del modelo en la consola.

También se mostrará una imagen de ejemplo del conjunto de datos.

## 🛠️ Tecnologías Utilizadas
- **Python 3.12.4**: Lenguaje de programación principal.

- **TensorFlow/Keras**: Para construir y entrenar la red neuronal.

- **NumPy**: Para manejar operaciones numéricas.

- **Matplotlib**: Para visualizar imágenes y gráficos.

## 📊 ¿Qué hace el código?
El código realiza lo siguiente:

1. Carga el conjunto de datos MNIST, que contiene imágenes de dígitos escritos a mano.

2. Preprocesa los datos:

   * Aplana las imágenes de 28x28 píxeles a vectores de 784 valores.
   * Normaliza los valores de los píxeles al rango [0, 1].
   * Convierte las etiquetas a un formato especial (one-hot encoding).

3. Construye una red neuronal con:

   * Una capa de entrada de 784 nodos.
   * Una capa oculta de 512 neuronas con activación ReLU.
   * na capa de salida de 10 neuronas con activación softmax.

4. Entrena la red neuronal durante 10 épocas.

5. Evalúa el modelo con datos de prueba y muestra la precisión.

## 🙏 Agradecimientos
¡Gracias por visitar mi repositorio! 🎉
Espero que este proyecto te sea útil, que tengas un muy buen día, Dios te bendiga 😊