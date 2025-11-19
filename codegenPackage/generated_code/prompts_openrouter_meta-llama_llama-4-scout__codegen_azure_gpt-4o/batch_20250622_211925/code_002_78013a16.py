"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Generate a sample insurance policy document in Spanish for a homeowner's insurance plan in Torreón, Coahuila, Mexico, incorporating details like coverage for natural disasters and theft.
Generated: DETERMINISTIC_78013a1671c1fe2a
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_insurance_policy(policy_holder_name, address, policy_number, start_date, end_date):
    """
    Generates a homeowner's insurance policy document in Spanish.

    Args:
        policy_holder_name (str): Name of the policyholder.
        address (str): Address of the insured property.
        policy_number (str): Unique policy number.
        start_date (datetime.date): Start date of the policy.
        end_date (datetime.date): End date of the policy.

    Returns:
        str: The insurance policy document in Spanish.
    """
    try:
        # Validate input types
        if not isinstance(policy_holder_name, str) or not isinstance(address, str) or not isinstance(policy_number, str):
            raise ValueError("Policy holder name, address, and policy number must be strings.")
        if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
            raise ValueError("Start date and end date must be datetime.date objects.")
        if start_date >= end_date:
            raise ValueError("Start date must be earlier than end date.")

        # Policy template in Spanish
        policy_template = f"""
        PÓLIZA DE SEGURO DE HOGAR
        ----------------------------------------
        Número de Póliza: {policy_number}
        Nombre del Titular: {policy_holder_name}
        Dirección de la Propiedad: {address}
        Ubicación: Torreón, Coahuila, México
        Fecha de Inicio: {start_date.strftime('%d/%m/%Y')}
        Fecha de Finalización: {end_date.strftime('%d/%m/%Y')}
        ----------------------------------------

        Cobertura:
        1. Desastres Naturales:
           - Terremotos, huracanes, inundaciones y otros eventos naturales.
        2. Robo:
           - Cobertura por robo de bienes dentro de la propiedad asegurada.
        3. Daños Accidentales:
           - Daños accidentales a la estructura de la propiedad.

        Condiciones Generales:
        - Esta póliza cubre únicamente la dirección especificada.
        - El titular debe notificar cualquier cambio en la propiedad asegurada.
        - En caso de siniestro, el titular debe presentar una reclamación dentro de los 30 días posteriores al evento.

        Contacto:
        - Para asistencia, comuníquese con nuestra línea de atención al cliente: 01-800-123-4567.
        - Correo electrónico: soporte@segurosmexico.com

        ----------------------------------------
        Gracias por confiar en Seguros México.
        """
        return policy_template

    except Exception as e:
        # Handle errors gracefully
        return f"Error al generar la póliza: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Sample data
    policy_holder_name = "Juan Pérez"
    address = "Calle Hidalgo #123, Colonia Centro"
    policy_number = "MX123456789"
    start_date = datetime.date(2023, 10, 1)
    end_date = datetime.date(2024, 10, 1)

    # Generate policy document
    policy_document = generate_insurance_policy(policy_holder_name, address, policy_number, start_date, end_date)
    print(policy_document)
```
