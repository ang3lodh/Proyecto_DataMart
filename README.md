# Pipeline de Datos - DataMart Chile S.A.



Este proyecto implementa un pipeline automatizado de ingesta, limpieza, validación semántica y carga de datos para el caso de retail de **DataMart Chile S.A.**



##  Tecnologías Utilizadas

- **Lenguaje:** Python 3.12

- **Librerías:** `pandas` (procesamiento), `sqlite3` (almacenamiento), `logging` (trazabilidad).

- **Entorno:** Visual Studio Code.



##  Etapas del Pipeline

El proceso está modularizado para facilitar el mantenimiento:



1. **Ingesta:** Lectura del archivo `data/ventas_datamart.csv`.

2. **Limpieza (`src/limpieza.py`):**

  - Eliminación de duplicados.

  - Normalización de precios (eliminación de símbolos).

  - Estandarización de categorías (ej. 'tech' a 'Tecnologia').

  - Corrección de formatos de fecha y manejo de valores nulos/negativos.

3. **Validación Semántica (`src/validacion.py`):**

  - Detección de pedidos con fechas ilógicas (despacho anterior a pedido).

  - Identificación de pedidos "entregados" sin fecha de despacho.

  - Control de descuentos fuera de rango (capado al 100%).

4. **Carga (`src/carga_db.py`):**

  - Exportación de resultados a un archivo `ventas_clean.csv` y carga automática en la base de datos `ventas_final.db` (SQLite).



##  Reporte de Errores Detectados

Durante la ejecución, el pipeline identificó:

- **Fechas inconsistentes:** 99 pedidos con fecha de despacho anterior a la fecha de pedido.

- **Registros incompletos:** 12 pedidos marcados como "entregado" sin fecha de despacho asociada.

*Estos casos han sido logueados para su revisión por el equipo de logística.*



##  Cómo ejecutar

1. Asegúrate de tener Python instalado.

2. Instala las dependencias:

  ```bash

  pip install pandas
