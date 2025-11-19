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
# -*- coding: utf-8 -*-
"""
Sample Homeowner's Insurance Policy Document Generator in Spanish for Torreón, Coahuila, Mexico.
Generates a policy document with coverage details for natural disasters and theft.
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class PolicyHolder:
    """Represents the policy holder's information."""
    nombre: str
    direccion: str
    ciudad: str = "Torreón"
    estado: str = "Coahuila"
    codigo_postal: str
    telefono: str
    email: Optional[str] = None

@dataclass
class Coverage:
    """Represents an insurance coverage item."""
    tipo: str
    descripcion: str
    limite: str
    deducible: str

def generate_policy_document(holder: PolicyHolder, coverages: List[Coverage]) -> str:
    """
    Generates a homeowner's insurance policy document in Spanish.
    
    Args:
        holder: PolicyHolder object with client information
        coverages: List of Coverage objects representing policy coverages
        
    Returns:
        str: Formatted policy document in Spanish
    """
    today = datetime.date.today()
    effective_date = today.strftime("%d/%m/%Y")
    expiration_date = (today + datetime.timedelta(days=365)).strftime("%d/%m/%Y")
    
    document = f"""
    PÓLIZA DE SEGURO PARA HOGAR
    Número de Póliza: MX-TOR-{today.year}-{hash(holder.nombre) % 10000:04d}
    
    INFORMACIÓN DEL ASEGURADO:
    Nombre: {holder.nombre}
    Dirección: {holder.direccion}
    Ciudad: {holder.ciudad}, {holder.estado}
    Código Postal: {holder.codigo_postal}
    Teléfono: {holder.telefono}
    Email: {holder.email or "No proporcionado"}
    
    VIGENCIA:
    Fecha de Inicio: {effective_date}
    Fecha de Vencimiento: {expiration_date}
    
    COBERTURAS:
    """
    
    for coverage in coverages:
        document += f"""
        - {coverage.tipo.upper()}:
          Descripción: {coverage.descripcion}
          Límite de Cobertura: {coverage.limite}
          Deducible: {coverage.deducible}
        """
    
    document += f"""
    CONDICIONES GENERALES:
    1. Esta póliza cubre la propiedad ubicada en {holder.direccion}, {holder.ciudad}, {holder.estado}.
    2. El pago de primas debe realizarse mensualmente antes del día 5 de cada mes.
    3. Cualquier reclamo debe reportarse dentro de las 72 horas posteriores al incidente.
    4. Se aplican exclusiones estándar según las leyes mexicanas de seguros.
    
    CLAÚSULAS ESPECIALES PARA TORREÓN:
    - Cobertura extendida por daños por inundación debido a temporada de lluvias.
    - Protección contra robos con violencia (incluye daños a la propiedad durante el evento).
    
    FIRMAS:
    ___________________________
    {holder.nombre}
    Asegurado
    
    ___________________________
    Seguros Torreón S.A. de C.V.
    Agente Autorizado
    
    Documento generado el: {effective_date}
    """
    
    return document

# Example usage
if __name__ == "__main__":
    try:
        # Sample policy holder data
        holder = PolicyHolder(
            nombre="María González Hernández",
            direccion="Calle Hidalgo 123, Colonia Centro",
            codigo_postal="27000",
            telefono="8711234567",
            email="maria.gonzalez@example.com"
        )
        
        # Sample coverages
        coverages = [
            Coverage(
                tipo="Daños Materiales",
                descripcion="Cubre daños a la estructura de la vivienda por incendio, explosión o fenómenos naturales",
                limite="$1,500,000 MXN",
                deducible="5% del valor del daño"
            ),
            Coverage(
                tipo="Robo",
                descripcion="Cubre pérdidas por robo de bienes dentro de la propiedad",
                limite="$500,000 MXN",
                deducible="2% del valor del bien"
            ),
            Coverage(
                tipo="Responsabilidad Civil",
                descripcion="Cubre daños a terceros dentro de la propiedad",
                limite="$1,000,000 MXN",
                deducible="N/A"
            )
        ]
        
        # Generate and print policy
        policy = generate_policy_document(holder, coverages)
        print(policy)
        
    except Exception as e:
        print(f"Error al generar la póliza: {str(e)}")
```
