"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Write a code snippet to generate a report for a real estate appraisal in Brazil, including the property's market value and characteristics, following the ABNT – NBR 14.653 standards.
Generated: DETERMINISTIC_f679b2fd0c352f67
Batch ID: 20250622_210443
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
Real Estate Appraisal Report Generator for Brazil (ABNT NBR 14.653)
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class PropertyCharacteristics:
    """Class representing property characteristics according to NBR 14.653"""
    address: str
    area: float  # m²
    registration_number: str  # Matrícula do imóvel
    zone: str  # Zona (urbana, rural, etc.)
    type: str  # Tipo (residencial, comercial, etc.)
    construction_year: int
    conservation_state: str  # Estado de conservação
    rooms: int
    bathrooms: int
    parking_spaces: int
    amenities: List[str]  # Lista de comodidades

@dataclass
class MarketValue:
    """Class representing market value calculation"""
    value: float
    currency: str = "BRL"
    valuation_date: datetime.date = datetime.date.today()
    valuation_method: str = "Comparativo de Mercado"  # Método de avaliação
    comparable_properties: List[Dict] = None  # Propriedades comparáveis

class AppraisalReport:
    """Class to generate real estate appraisal reports following ABNT NBR 14.653"""
    
    def __init__(self, property_data: PropertyCharacteristics, market_value: MarketValue):
        self.property = property_data
        self.market_value = market_value
        self.report_date = datetime.date.today()
        self.appraiser_info = {
            'name': '',
            'creci': '',  # CRECI number
            'contact': ''
        }
    
    def set_appraiser_info(self, name: str, creci: str, contact: str):
        """Set appraiser information"""
        self.appraiser_info['name'] = name
        self.appraiser_info['creci'] = creci
        self.appraiser_info['contact'] = contact
    
    def generate_report(self) -> Dict:
        """Generate appraisal report following NBR 14.653 standards"""
        try:
            report = {
                'header': self._generate_header(),
                'property_characteristics': self._generate_property_section(),
                'valuation': self._generate_valuation_section(),
                'conclusions': self._generate_conclusions(),
                'signatures': self._generate_signatures(),
                'standards_compliance': "ABNT NBR 14.653"
            }
            return report
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")
    
    def _generate_header(self) -> Dict:
        return {
            'title': "Laudo de Avaliação de Imóvel",
            'report_date': self.report_date.strftime("%d/%m/%Y"),
            'appraiser': self.appraiser_info['name'],
            'creci': self.appraiser_info['creci']
        }
    
    def _generate_property_section(self) -> Dict:
        return {
            'address': self.property.address,
            'registration': self.property.registration_number,
            'zone': self.property.zone,
            'type': self.property.type,
            'area': f"{self.property.area} m²",
            'construction_year': self.property.construction_year,
            'conservation_state': self.property.conservation_state,
            'rooms': self.property.rooms,
            'bathrooms': self.property.bathrooms,
            'parking_spaces': self.property.parking_spaces,
            'amenities': ", ".join(self.property.amenities)
        }
    
    def _generate_valuation_section(self) -> Dict:
        return {
            'valuation_date': self.market_value.valuation_date.strftime("%d/%m/%Y"),
            'market_value': f"R$ {self.market_value.value:,.2f}",
            'valuation_method': self.market_value.valuation_method,
            'comparable_properties': self.market_value.comparable_properties or []
        }
    
    def _generate_conclusions(self) -> Dict:
        return {
            'conclusion': f"O valor de mercado do imóvel avaliado é de R$ {self.market_value.value:,.2f} "
                         f"({self.market_value.currency}), conforme metodologia descrita.",
            'limitations': "Esta avaliação considera as condições de mercado na data do laudo."
        }
    
    def _generate_signatures(self) -> Dict:
        return {
            'appraiser': self.appraiser_info['name'],
            'creci': self.appraiser_info['creci'],
            'date': self.report_date.strftime("%d/%m/%Y"),
            'contact': self.appraiser_info['contact']
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create property characteristics
        property_data = PropertyCharacteristics(
            address="Av. Paulista, 1000 - São Paulo/SP",
            area=120.5,
            registration_number="12345-6",
            zone="Urbana",
            type="Residencial",
            construction_year=2010,
            conservation_state="Bom",
            rooms=3,
            bathrooms=2,
            parking_spaces=1,
            amenities=["Piscina", "Academia", "Churrasqueira"]
        )
        
        # Create market valuation
        comparable_properties = [
            {"address": "Av. Paulista, 900", "area": 110, "value": 1500000},
            {"address": "Av. Paulista, 1100", "area": 130, "value": 1700000}
        ]
        
        market_value = MarketValue(
            value=1600000,
            comparable_properties=comparable_properties
        )
        
        # Generate report
        report = AppraisalReport(property_data, market_value)
        report.set_appraiser_info(
            name="João Silva",
            creci="12345-SP",
            contact="joao@imobiliaria.com.br"
        )
        
        appraisal_report = report.generate_report()
        print(appraisal_report)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
