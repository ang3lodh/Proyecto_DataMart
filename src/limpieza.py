import pandas as pd
import numpy as np
import logging

# Configuración de log profesional
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def limpiar_datos(df):
    logging.info(f"Filas iniciales: {len(df)}")
    df_clean = df.copy()

    # 1. Eliminar duplicados exactos
    df_clean = df_clean.drop_duplicates()
    
    # 2. Limpiar 'precio_unitario' (Quitar $ y puntos, convertir a float)
    df_clean['precio_unitario'] = df_clean['precio_unitario'].astype(str).str.replace(r'[\$\.]', '', regex=True)
    df_clean['precio_unitario'] = pd.to_numeric(df_clean['precio_unitario'], errors='coerce')
    
    # 3. Limpiar cantidades y descuentos (Reglas de negocio)
    df_clean['cantidad'] = df_clean['cantidad'].abs() # Valor absoluto para negativos
    df_clean.loc[df_clean['descuento_pct'] > 100, 'descuento_pct'] = 100.0
    
    # 4. Estandarizar Categorías (Evita inconsistencias como 'tech'/'Tecnologia')
    df_clean['categoria'] = df_clean['categoria'].astype(str).str.capitalize()
    df_clean['categoria'] = df_clean['categoria'].replace({
        'Tech': 'Tecnologia', 
        'Moda': 'Moda', 
        'Hogar': 'Hogar',
        'nan': 'Sin Categoria'
    })
    
    # 5. Estandarizar Fechas (A prueba de balas)
    df_clean['fecha_pedido'] = pd.to_datetime(df_clean['fecha_pedido'], errors='coerce', format='mixed')
    df_clean['fecha_despacho'] = pd.to_datetime(df_clean['fecha_despacho'], errors='coerce', format='mixed')
    
    # 6. Imputación de nulos críticos
    df_clean['region'] = df_clean['region'].fillna('Sin Region')
    
    # Usamos (con I mayúscula) para permitir nulos en columnas numéricas
    df_clean['id_pedido'] = df_clean['id_pedido'].astype('Int64')
    df_clean['cantidad'] = df_clean['cantidad'].astype('Int64')
    
    # Formatear fechas a cadena ISO AAAA-MM-DD
    df_clean['fecha_pedido'] = df_clean['fecha_pedido'].dt.strftime('%Y-%m-%d')
    df_clean['fecha_despacho'] = df_clean['fecha_despacho'].dt.strftime('%Y-%m-%d')
    
    # Ordenar columnas según requerimiento
    cols = ['id_pedido', 'fecha_pedido', 'rut_cliente', 'nombre_cliente', 'region', 
            'producto', 'categoria', 'cantidad', 'precio_unitario', 'descuento_pct', 
            'estado_pedido', 'fecha_despacho']
    
    # Aseguramos de limpiar 
    df_clean = df_clean[cols]
    
    logging.info(f"Filas finales tras limpieza: {len(df_clean)}")
    return df_clean
