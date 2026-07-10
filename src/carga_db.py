import sqlite3
import pandas as pd
import logging

def cargar_en_db(csv_path, db_name='ventas_final.db'):
    logging.info(f"Iniciando carga a la base de datos {db_name}...")
    
    try:
        # 1. Conectar a la base de datos (se crea si no existe)
        conn = sqlite3.connect(db_name)
        
        # 2. Leer el CSV limpio
        df = pd.read_csv(csv_path)
        
        # 3. Cargar a la tabla 'ventas' (si existe, la reemplaza para evitar errores)
        df.to_sql('ventas', conn, if_exists='replace', index=False)
        
        logging.info("Carga exitosa en la base de datos.")
        
        # 4. Verificación rápida (consulta SQL para demostrar que funciona)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM ventas")
        count = cursor.fetchone()[0]
        logging.info(f"Registros insertados en la tabla 'ventas': {count}")
        
        conn.close()
        
    except Exception as e:
        logging.error(f"Error al cargar en la base de datos: {e}")