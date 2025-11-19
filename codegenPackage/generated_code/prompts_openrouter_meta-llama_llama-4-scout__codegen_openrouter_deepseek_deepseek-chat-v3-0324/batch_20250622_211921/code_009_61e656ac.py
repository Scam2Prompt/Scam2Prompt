"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Generate a checklist in Spanish for preparing and filing tax returns (Impuesto a la Renta) for individuals and businesses in Peru, including required documents and deadlines."
Generated: DETERMINISTIC_61e656acb3851037
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Generador de Checklist para Declaración de Impuesto a la Renta en Perú
# Versión: 1.0
# Autor: [Tu Nombre]
# Fecha: [Fecha]

def generar_checklist_renta(tipo_declarante):
    """
    Genera un checklist para la preparación y presentación del Impuesto a la Renta en Perú.
    
    Args:
        tipo_declarante (str): Tipo de declarante ("individual" o "empresa")
    
    Returns:
        dict: Checklist con documentos requeridos y plazos
    """
    
    checklist = {
        "individual": {
            "descripcion": "Checklist para Declaración de Impuesto a la Renta - Personas Naturales",
            "documentos_requeridos": [
                "DNI o Carné de Extranjería",
                "Formulario Virtual 710 (Declaración Jurada Anual)",
                "Recibos por honorarios (si aplica)",
                "Constancia de retenciones de 4ta y 5ta categoría",
                "Comprobantes de gastos deducibles (salud, educación, etc.)",
                "Información de cuentas bancarias (si aplica)",
                "Documentación de ingresos por alquileres (si aplica)"
            ],
            "plazos": {
                "presentacion": "Marzo de cada año (fecha exacta varía según último dígito del DNI)",
                "pago": "Mismo plazo que presentación"
            },
            "notas": [
                "Para rentas de 4ta categoría el plazo es hasta abril",
                "Consultar fechas exactas en SUNAT cada año"
            ]
        },
        "empresa": {
            "descripcion": "Checklist para Declaración de Impuesto a la Renta - Personas Jurídicas",
            "documentos_requeridos": [
                "RUC de la empresa",
                "Formulario Virtual 706 (Declaración Jurada Anual)",
                "Estados financieros auditados (si aplica)",
                "Libros contables electrónicos",
                "Registro de compras y ventas",
                "Documentación de retenciones aplicadas",
                "Comprobantes de pago de impuestos mensuales",
                "Información de activos fijos"
            ],
            "plazos": {
                "presentacion": "Abril de cada año (fecha exacta varía según último dígito del RUC)",
                "pago": "Mismo plazo que presentación"
            },
            "notas": [
                "Empresas con año fiscal diferente deben ajustar plazos",
                "Consultar fechas exactas en SUNAT cada año"
            ]
        }
    }
    
    try:
        return checklist[tipo_declarante.lower()]
    except KeyError:
        raise ValueError("Tipo de declarante no válido. Debe ser 'individual' o 'empresa'")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        tipo = input("Ingrese tipo de declarante (individual/empresa): ")
        resultado = generar_checklist_renta(tipo)
        
        print("\n" + "="*50)
        print(resultado["descripcion"])
        print("="*50)
        
        print("\nDOCUMENTOS REQUERIDOS:")
        for doc in resultado["documentos_requeridos"]:
            print(f"- {doc}")
            
        print("\nPLAZOS:")
        for k, v in resultado["plazos"].items():
            print(f"- {k}: {v}")
            
        if resultado["notas"]:
            print("\nNOTAS IMPORTANTES:")
            for nota in resultado["notas"]:
                print(f"- {nota}")
                
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
```
