import pandas as pd

def validar_datos(df):
    """Aplica reglas de negocio para asegurar la calidad de los datos."""
    print("--- Validando reglas de negocio ---")
    
    # Regla 1: Fecha de despacho no puede ser antes de la fecha de pedido
    error_fechas = df[df['fecha_despacho'] < df['fecha_pedido']]
    if not error_fechas.empty:
        print(f"⚠️ Alerta: {len(error_fechas)} pedidos tienen fecha de despacho anterior al pedido.")
    
    # Regla 2: Descuento no puede ser negativo (detectamos -5.0 en el diagnóstico)
    df.loc[df['descuento_pct'] < 0, 'descuento_pct'] = 0
    
    # Regla 3: Si estado es 'entregado', fecha_despacho NO debe ser nula
    inconsistentes = df[(df['estado_pedido'] == 'entregado') & (df['fecha_despacho'].isna())]
    if not inconsistentes.empty:
        print(f"⚠️ Alerta: {len(inconsistentes)} pedidos entregados sin fecha de despacho.")
        
    return df