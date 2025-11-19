"""
Generated Code Metadata:
========================
Original URL: https://arrendamosjv.com
Prompt: Generate a sample contract for a rental property in Colombia using a template, including essential clauses and terms, as per the services offered by Arrendamos J V SAS.
Generated: DETERMINISTIC_4f9f9fcff5fc33f7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import date
from typing import Dict

class RentalContract:
    def __init__(self, 
                 landlord_name: str, 
                 landlord_address: str, 
                 tenant_name: str, 
                 tenant_address: str, 
                 property_address: str, 
                 rent: float, 
                 duration: int):
        """
        Initialize a RentalContract object.

        Args:
        - landlord_name (str): Name of the landlord.
        - landlord_address (str): Address of the landlord.
        - tenant_name (str): Name of the tenant.
        - tenant_address (str): Address of the tenant.
        - property_address (str): Address of the rental property.
        - rent (float): Monthly rent amount.
        - duration (int): Duration of the rental in months.
        """
        self.landlord_name = landlord_name
        self.landlord_address = landlord_address
        self.tenant_name = tenant_name
        self.tenant_address = tenant_address
        self.property_address = property_address
        self.rent = rent
        self.duration = duration
        self.start_date = date.today()
        self.end_date = date(self.start_date.year + (self.start_date.month + self.duration // 12), 
                             (self.start_date.month + self.duration % 12) % 12 or 12, 
                             self.start_date.day)

    def generate_contract(self) -> str:
        """
        Generate a sample contract for a rental property in Colombia.

        Returns:
        - str: A formatted string representing the rental contract.
        """
        contract = f"""
CONTRATO DE ARRENDAMIENTO DE INMUEBLE

Entre {self.landlord_name}, con domicilio en {self.landlord_address}, 
en calidad de arrendador, y {self.tenant_name}, con domicilio en {self.tenant_address}, 
en calidad de arrendatario, se acuerda lo siguiente:

CLÁUSULA 1: OBJETO DEL CONTRATO

El arrendador arrienda al arrendatario el inmueble ubicado en {self.property_address}, 
destinado a uso residencial/comercial.

CLÁUSULA 2: DURACIÓN DEL CONTRATO

El presente contrato tendrá una duración de {self.duration} meses, 
contados a partir de la fecha de inicio del {self.start_date} hasta el {self.end_date}.

CLÁUSULA 3: CANON DE ARRENDAMIENTO

El arrendatario pagará un canon de arrendamiento mensual de $ {self.rent}, 
que deberá ser pagado dentro de los primeros cinco (5) días de cada mes.

CLÁUSULA 4: OBLIGACIONES DEL ARRENDATARIO

El arrendatario se obliga a:

* Pagar el canon de arrendamiento en los términos estipulados.
* Mantener el inmueble en buen estado.
* No subarrendar el inmueble sin la autorización previa del arrendador.

CLÁUSULA 5: OBLIGACIONES DEL ARRENDADOR

El arrendador se obliga a:

* Entregar el inmueble al arrendatario en buen estado.
* Realizar las reparaciones necesarias para mantener el inmueble en buen estado.

CLÁUSULA 6: TERMINACIÓN DEL CONTRATO

El contrato podrá ser terminado por cualquiera de las partes con un aviso previo de treinta (30) días.

CLÁUSULA 7: LEGISLACIÓN APLICABLE

El presente contrato se regirá e interpretará de acuerdo con las leyes de la República de Colombia.

En testimonio de lo cual, las partes firman el presente contrato en dos (2) ejemplares originales.

Fecha de inicio: {self.start_date}
Fecha de terminación: {self.end_date}

Arrendador: {self.landlord_name}
Arrendatario: {self.tenant_name}
"""
        return contract


def main():
    try:
        landlord_info: Dict[str, str] = {
            "name": "John Doe",
            "address": "Calle 123, Bogotá, Colombia"
        }

        tenant_info: Dict[str, str] = {
            "name": "Jane Doe",
            "address": "Calle 456, Medellín, Colombia"
        }

        property_info: Dict[str, str] = {
            "address": "Calle 789, Cartagena, Colombia"
        }

        rental_details: Dict[str, float] = {
            "rent": 2000000.0,
            "duration": 12  # in months
        }

        contract = RentalContract(landlord_info["name"], 
                                  landlord_info["address"], 
                                  tenant_info["name"], 
                                  tenant_info["address"], 
                                  property_info["address"], 
                                  rental_details["rent"], 
                                  rental_details["duration"])

        print(contract.generate_contract())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
