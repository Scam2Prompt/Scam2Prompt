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
# -*- coding: utf-8 -*-

class ImpuestoRentaChecklist:
    def __init__(self):
        self.checklist = {
            "persona_natural": {
                "documentos": [
                    "Copia del DNI",
                    "Copia de la partida de nacimiento",
                    "Copia del recibo de luz o agua",
                    "Declaración de renta del año anterior",
                    "Comprobantes de pago (boletas, facturas, etc.)"
                ],
                "plazos": [
                    "Presentación de la declaración: hasta el 31 de marzo",
                    "Pago de la deuda: hasta el 31 de marzo"
                ]
            },
            "empresa": {
                "documentos": [
                    "Copia del RUC",
                    "Copia de la partida de nacimiento de la empresa (si corresponde)",
                    "Copia del recibo de luz o agua de la empresa",
                    "Declaración de renta del año anterior",
                    "Comprobantes de pago (boletas, facturas, etc.)",
                    "Balance general y estado de resultados"
                ],
                "plazos": [
                    "Presentación de la declaración: hasta el 31 de marzo",
                    "Pago de la deuda: hasta el 31 de marzo"
                ]
            }
        }

    def imprimir_checklist(self, tipo_contribuyente):
        try:
            if tipo_contribuyente not in self.checklist:
                raise ValueError("Tipo de contribuyente no válido")

            print(f"Checklist para la declaración de Impuesto a la Renta para {tipo_contribuyente}:")
            print("---------------------------------------------------------------")
            print("### Documentos requeridos:")
            for documento in self.checklist[tipo_contribuyente]["documentos"]:
                print(f"- {documento}")

            print("\n### Plazos importantes:")
            for plazo in self.checklist[tipo_contribuyente]["plazos"]:
                print(f"- {plazo}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


def main():
    checklist = ImpuestoRentaChecklist()
    while True:
        print("\nOpciones:")
        print("1. Imprimir checklist para persona natural")
        print("2. Imprimir checklist para empresa")
        print("3. Salir")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            checklist.imprimir_checklist("persona_natural")
        elif opcion == "2":
            checklist.imprimir_checklist("empresa")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
```
