"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: "Write a code to calculate the optimal dosage of fertilizers and bio stimulants for a specific crop, considering factors like soil type and climate."
Generated: DETERMINISTIC_51c219112bca9b65
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, List, Optional, Tuple

class SoilType(Enum):
    SANDY = "sandy"
    CLAY = "clay"
    LOAMY = "loamy"
    SILTY = "silty"
    PEATY = "peaty"

class ClimateType(Enum):
    TROPICAL = "tropical"
    DRY = "dry"
    TEMPERATE = "temperate"
    CONTINENTAL = "continental"
    POLAR = "polar"

class CropType(Enum):
    WHEAT = "wheat"
    CORN = "corn"
    RICE = "rice"
    SOYBEAN = "soybean"
    POTATO = "potato"

class FertilizerType(Enum):
    NITROGEN = "nitrogen"
    PHOSPHORUS = "phosphorus"
    POTASSIUM = "potassium"
    COMPOST = "compost"

class BioStimulantType(Enum):
    HUMIC_ACID = "humic_acid"
    SEAWEED_EXTRACT = "seaweed_extract"
    MICROBIAL_INOCULANTS = "microbial_inoculants"
    AMINO_ACIDS = "amino_acids"

# Base requirements per crop (kg per hectare)
BASE_REQUIREMENTS = {
    CropType.WHEAT: {
        FertilizerType.NITROGEN: 120,
        FertilizerType.PHOSPHORUS: 60,
        FertilizerType.POTASSIUM: 50,
        FertilizerType.COMPOST: 2000
    },
    CropType.CORN: {
        FertilizerType.NITROGEN: 150,
        FertilizerType.PHOSPHORUS: 70,
        FertilizerType.POTASSIUM: 80,
        FertilizerType.COMPOST: 2500
    },
    CropType.RICE: {
        FertilizerType.NITROGEN: 100,
        FertilizerType.PHOSPHORUS: 50,
        FertilizerType.POTASSIUM: 40,
        FertilizerType.COMPOST: 3000
    },
    CropType.SOYBEAN: {
        FertilizerType.NITROGEN: 20,
        FertilizerType.PHOSPHORUS: 60,
        FertilizerType.POTASSIUM: 60,
        FertilizerType.COMPOST: 1500
    },
    CropType.POTATO: {
        FertilizerType.NITROGEN: 80,
        FertilizerType.PHOSPHORUS: 50,
        FertilizerType.POTASSIUM: 100,
        FertilizerType.COMPOST: 3500
    }
}

# Bio stimulant recommendations per crop (ml per hectare)
BIO_STIMULANT_RECOMMENDATIONS = {
    CropType.WHEAT: {
        BioStimulantType.HUMIC_ACID: 500,
        BioStimulantType.SEAWEED_EXTRACT: 300,
        BioStimulantType.MICROBIAL_INOCULANTS: 200,
        BioStimulantType.AMINO_ACIDS: 100
    },
    CropType.CORN: {
        BioStimulantType.HUMIC_ACID: 600,
        BioStimulantType.SEAWEED_EXTRACT: 400,
        BioStimulantType.MICROBIAL_INOCULANTS: 300,
        BioStimulantType.AMINO_ACIDS: 150
    },
    CropType.RICE: {
        BioStimulantType.HUMIC_ACID: 700,
        BioStimulantType.SEAWEED_EXTRACT: 500,
        BioStimulantType.MICROBIAL_INOCULANTS: 400,
        BioStimulantType.AMINO_ACIDS: 200
    },
    CropType.SOYBEAN: {
        BioStimulantType.HUMIC_ACID: 400,
        BioStimulantType.SEAWEED_EXTRACT: 200,
        BioStimulantType.MICROBIAL_INOCULANTS: 300,
        BioStimulantType.AMINO_ACIDS: 50
    },
    CropType.POTATO: {
        BioStimulantType.HUMIC_ACID: 800,
        BioStimulantType.SEAWEED_EXTRACT: 600,
        BioStimulantType.MICROBIAL_INOCULANTS: 500,
        BioStimulantType.AMINO_ACIDS: 300
    }
}

# Soil type multipliers
SOIL_MULTIPLIERS = {
    SoilType.SANDY: {
        FertilizerType.NITROGEN: 1.2,
        FertilizerType.PHOSPHORUS: 1.1,
        FertilizerType.POTASSIUM: 1.3,
        FertilizerType.COMPOST: 1.5
    },
    SoilType.CLAY: {
        FertilizerType.NITROGEN: 0.9,
        FertilizerType.PHOSPHORUS: 1.0,
        FertilizerType.POTASSIUM: 0.8,
        FertilizerType.COMPOST: 0.7
    },
    SoilType.LOAMY: {
        FertilizerType.NITROGEN: 1.0,
        FertilizerType.PHOSPHORUS: 1.0,
        FertilizerType.POTASSIUM: 1.0,
        FertilizerType.COMPOST: 1.0
    },
    SoilType.SILTY: {
        FertilizerType.NITROGEN: 1.1,
        FertilizerType.PHOSPHORUS: 1.2,
        FertilizerType.POTASSIUM: 1.1,
        FertilizerType.COMPOST: 1.2
    },
    SoilType.PEATY: {
        FertilizerType.NITROGEN: 0.8,
        FertilizerType.PHOSPHORUS: 0.9,
        FertilizerType.POTASSIUM: 0.7,
        FertilizerType.COMPOST: 0.5
    }
}

# Climate type multipliers
CLIMATE_MULTIPLIERS = {
    ClimateType.TROPICAL: {
        FertilizerType.NITROGEN: 1.3,
        FertilizerType.PHOSPHORUS: 1.1,
        FertilizerType.POTASSIUM: 1.4,
        FertilizerType.COMPOST: 1.2
    },
    ClimateType.DRY: {
        FertilizerType.NITROGEN: 1.1,
        FertilizerType.PHOSPHORUS: 0.9,
        FertilizerType.POTASSIUM: 1.2,
        FertilizerType.COMPOST: 0.8
    },
    ClimateType.TEMPERATE: {
        FertilizerType.NITROGEN: 1.0,
        FertilizerType.PHOSPHORUS: 1.0,
        FertilizerType.POTASSIUM: 1.0,
        FertilizerType.COMPOST: 1.0
    },
    ClimateType.CONTINENTAL: {
        FertilizerType.NITROGEN: 0.9,
        FertilizerType.PHOSPHORUS: 1.1,
        FertilizerType.POTASSIUM: 0.8,
        FertilizerType.COMPOST: 0.9
    },
    ClimateType.POLAR: {
        FertilizerType.NITROGEN: 0.7,
        FertilizerType.PHOSPHORUS: 0.8,
        FertilizerType.POTASSIUM: 0.6,
        FertilizerType.COMPOST: 0.6
    }
}

class FertilizerCalculator:
    """
    Calculates optimal fertilizer and bio stimulant dosages for crops based on soil and climate.
    """
    
    def __init__(self, crop: CropType, soil: SoilType, climate: ClimateType, area_hectares: float):
        """
        Initialize calculator with crop, soil, climate, and area.
        
        Args:
            crop: Type of crop to calculate for
            soil: Soil type of the field
            climate: Climate type of the region
            area_hectares: Area to fertilize in hectares
        """
        self.crop = crop
        self.soil = soil
        self.climate = climate
        self.area_hectares = area_hectares
        
        if area_hectares <= 0:
            raise ValueError("Area must be greater than 0")
        
    def calculate_fertilizers(self) -> Dict[FertilizerType, float]:
        """
        Calculate optimal fertilizer amounts considering soil and climate.
        
        Returns:
            Dictionary mapping fertilizer types to required amounts in kg
        """
        try:
            base_requirements = BASE_REQUIREMENTS[self.crop]
            soil_multipliers = SOIL_MULTIPLIERS[self.soil]
            climate_multipliers = CLIMATE_MULTIPLIERS[self.climate]
            
            results = {}
            for fert_type, base
