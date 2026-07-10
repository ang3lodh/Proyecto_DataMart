import pandas as pd
from src.limpieza import limpiar_datos
from src.validacion import validar_datos
from src.carga_db import cargar_en_db  # Importa la nueva función

def run():
    # 1. Ingesta
    df = pd.read_csv('data/ventas_datamart.csv')
    
    # 2. Limpieza
    df = limpiar_datos(df)
    
    # 3. Validación
    df = validar_datos(df)
    
    # 4. Guardar CSV intermedio
    df.to_csv('data/ventas_clean.csv', index=False)
    
    # 5. Carga a BD (El paso final de la rúbrica)
    cargar_en_db('data/ventas_clean.csv')

if __name__ == "__main__":
    run()