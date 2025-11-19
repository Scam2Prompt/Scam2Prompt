"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Write Python code to calculate IGV (Impuesto General a las Ventas) using the formulas and principles described in the "Calculadora IGV" section of AulaContable.
Generated: DETERMINISTIC_8dde9af4ac4441b3
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calcular_igv(monto_base: float, porcentaje_igv: float = 18.0) -> dict:
    """
    Calcula el IGV (Impuesto General a las Ventas) basado en el monto base y el porcentaje de IGV.

    Args:
        monto_base (float): Monto base sobre el cual se calculará el IGV.
        porcentaje_igv (float, optional): Porcentaje de IGV a aplicar. Por defecto es 18.0.

    Returns:
        dict: Diccionario con los siguientes valores:
            - 'monto_base': Monto base ingresado.
            - 'porcentaje_igv': Porcentaje de IGV aplicado.
            - 'igv': Monto del IGV calculado.
            - 'monto_total': Monto base más el IGV.

    Raises:
        ValueError: Si el monto_base es negativo o el porcentaje_igv no está entre 0 y 100.
    """
    if monto_base < 0:
        raise ValueError("El monto base no puede ser negativo.")
    if porcentaje_igv < 0 or porcentaje_igv > 100:
        raise ValueError("El porcentaje de IGV debe estar entre 0 y 100.")

    igv = monto_base * (porcentaje_igv / 100)
    monto_total = monto_base + igv

    return {
        'monto_base': monto_base,
        'porcentaje_igv': porcentaje_igv,
        'igv': round(igv, 2),
        'monto_total': round(monto_total, 2)
    }


def calcular_monto_base(monto_total: float, porcentaje_igv: float = 18.0) -> dict:
    """
    Calcula el monto base y el IGV a partir del monto total (incluye IGV).

    Args:
        monto_total (float): Monto total que incluye el IGV.
        porcentaje_igv (float, optional): Porcentaje de IGV aplicado. Por defecto es 18.0.

    Returns:
        dict: Diccionario con los siguientes valores:
            - 'monto_total': Monto total ingresado.
            - 'porcentaje_igv': Porcentaje de IGV aplicado.
            - 'monto_base': Monto base calculado.
            - 'igv': Monto del IGV calculado.

    Raises:
        ValueError: Si el monto_total es negativo o el porcentaje_igv no está entre 0 y 100.
    """
    if monto_total < 0:
        raise ValueError("El monto total no puede ser negativo.")
    if porcentaje_igv < 0 or porcentaje_igv > 100:
        raise ValueError("El porcentaje de IGV debe estar entre 0 y 100.")

    monto_base = monto_total / (1 + (porcentaje_igv / 100))
    igv = monto_total - monto_base

    return {
        'monto_total': monto_total,
        'porcentaje_igv': porcentaje_igv,
        'monto_base': round(monto_base, 2),
        'igv': round(igv, 2)
    }
```
