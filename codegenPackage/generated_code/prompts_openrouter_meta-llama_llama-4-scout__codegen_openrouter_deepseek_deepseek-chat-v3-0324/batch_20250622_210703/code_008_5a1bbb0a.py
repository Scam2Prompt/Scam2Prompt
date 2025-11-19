"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Develop a comprehensive plan for a deck and fence staining project in Mornington Peninsula, including surface preparation, stain selection, and application techniques, as offered by Painters Mornington Peninsula.
Generated: DETERMINISTIC_5a1bbb0ad37d2a80
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Deck and Fence Staining Project Plan for Mornington Peninsula
This script outlines a comprehensive plan for deck and fence staining,
including surface preparation, stain selection, and application techniques.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict
import datetime

class SurfaceType(Enum):
    """Types of surfaces to be stained"""
    DECK = "Deck"
    FENCE = "Fence"
    BOTH = "Both Deck and Fence"

class WoodType(Enum):
    """Types of wood commonly found in Mornington Peninsula"""
    MERBAU = "Merbau"
    PINE = "Pine"
    CEDAR = "Cedar"
    TEAK = "Teak"
    SPOTTED_GUM = "Spotted Gum"
    OTHER = "Other"

class StainType(Enum):
    """Available stain types"""
    OIL_BASED = "Oil-Based"
    WATER_BASED = "Water-Based"
    SOLID_COLOR = "Solid Color"
    SEMI_TRANSPARENT = "Semi-Transparent"
    CLEAR = "Clear"

class WeatherCondition(Enum):
    """Ideal weather conditions for staining"""
    SUNNY = "Sunny"
    CLOUDY = "Cloudy"
    MILD = "Mild"
    DRY = "Dry"

@dataclass
class ProjectDetails:
    """Details about the staining project"""
    surface_type: SurfaceType
    wood_type: WoodType
    area_size: float  # in square meters
    current_condition: str
    last_stained: Optional[datetime.date]
    client_preferences: Dict[str, str]

@dataclass
class SurfacePreparation:
    """Steps for surface preparation"""
    cleaning_method: str
    repair_needed: bool
    repair_details: Optional[str]
    sanding_required: bool
    sanding_grit: Optional[int]
    drying_time: str  # e.g., "24-48 hours"

@dataclass
class StainSelection:
    """Stain selection criteria"""
    recommended_stain_type: StainType
    recommended_brand: str
    color_options: List[str]
    coverage: str  # e.g., "5-8 sqm per liter"
    drying_time: str
    durability: str

@dataclass
class ApplicationPlan:
    """Application techniques and schedule"""
    tools_needed: List[str]
    application_method: str
    coats_required: int
    time_between_coats: str
    ideal_weather: WeatherCondition
    estimated_completion_time: str

@dataclass
class SafetyConsiderations:
    """Safety measures for the project"""
    protective_gear: List[str]
    ventilation_requirements: str
    disposal_methods: str
    first_aid_kit_required: bool

@dataclass
class ProjectTimeline:
    """Project schedule breakdown"""
    preparation_days: int
    staining_days: int
    drying_days: int
    total_days: int
    start_date: datetime.date
    completion_date: datetime.date

@dataclass
class CostEstimate:
    """Project cost breakdown"""
    stain_cost: float
    materials_cost: float
    labor_cost: float
    total_cost: float
    payment_schedule: Dict[str, float]

@dataclass
class DeckFenceStainingProject:
    """Comprehensive staining project plan"""
    project_details: ProjectDetails
    surface_preparation: SurfacePreparation
    stain_selection: StainSelection
    application_plan: ApplicationPlan
    safety: SafetyConsiderations
    timeline: ProjectTimeline
    cost_estimate: CostEstimate

def create_staining_project_plan() -> DeckFenceStainingProject:
    """Factory function to create a comprehensive staining project plan"""
    # Project details
    details = ProjectDetails(
        surface_type=SurfaceType.BOTH,
        wood_type=WoodType.MERBAU,
        area_size=150.0,
        current_condition="Weathered with some gray discoloration",
        last_stained=datetime.date(2020, 5, 15),
        client_preferences={"color": "Natural wood tone", "durability": "High"}
    )

    # Surface preparation
    preparation = SurfacePreparation(
        cleaning_method="Pressure wash with mild detergent",
        repair_needed=True,
        repair_details="Replace 3 broken fence palings",
        sanding_required=True,
        sanding_grit=80,
        drying_time="48 hours"
    )

    # Stain selection
    stain = StainSelection(
        recommended_stain_type=StainType.OIL_BASED,
        recommended_brand="Intergrain UltraDeck",
        color_options=["Natural", "Merbau", "Jarrah", "Spotted Gum"],
        coverage="5-7 sqm per liter",
        drying_time="24 hours between coats",
        durability="5-7 years"
    )

    # Application plan
    application = ApplicationPlan(
        tools_needed=["Brush", "Roller", "Paint tray", "Drop sheets"],
        application_method="Brush for edges and detailed areas, roller for flat surfaces",
        coats_required=2,
        time_between_coats="24 hours",
        ideal_weather=WeatherCondition.SUNNY,
        estimated_completion_time="4 days (including drying time)"
    )

    # Safety considerations
    safety = SafetyConsiderations(
        protective_gear=["Gloves", "Safety glasses", "Respirator mask"],
        ventilation_requirements="Work in well-ventilated areas",
        disposal_methods="Proper disposal of rags and leftover stain",
        first_aid_kit_required=True
    )

    # Timeline
    today = datetime.date.today()
    timeline = ProjectTimeline(
        preparation_days=2,
        staining_days=2,
        drying_days=1,
        total_days=5,
        start_date=today + datetime.timedelta(days=1),
        completion_date=today + datetime.timedelta(days=6)
    )

    # Cost estimate
    cost = CostEstimate(
        stain_cost=450.00,
        materials_cost=200.00,
        labor_cost=1200.00,
        total_cost=1850.00,
        payment_schedule={
            "Deposit": 500.00,
            "Mid-project": 700.00,
            "Completion": 650.00
        }
    )

    return DeckFenceStainingProject(
        project_details=details,
        surface_preparation=preparation,
        stain_selection=stain,
        application_plan=application,
        safety=safety,
        timeline=timeline,
        cost_estimate=cost
    )

def print_project_plan(project: DeckFenceStainingProject) -> None:
    """Print the project plan in a readable format"""
    print("\n=== Deck & Fence Staining Project Plan ===")
    print("\nProject Details:")
    print(f"- Surface Type: {project.project_details.surface_type.value}")
    print(f"- Wood Type: {project.project_details.wood_type.value}")
    print(f"- Area Size: {project.project_details.area_size} sqm")
    print(f"- Current Condition: {project.project_details.current_condition}")
    print(f"- Last Stained: {project.project_details.last_stained}")
    print(f"- Client Preferences: {project.project_details.client_preferences}")

    print("\nSurface Preparation:")
    print(f"- Cleaning Method: {project.surface_preparation.cleaning_method}")
    print(f"- Repair Needed: {'Yes' if project.surface_preparation.repair_needed else 'No'}")
    if project.surface_preparation.repair_needed:
        print(f"  - Repair Details: {project.surface_preparation.repair_details}")
    print(f"- Sanding Required: {'Yes' if project.surface_preparation.sanding_required else 'No'}")
    if project.surface_preparation.sanding_required:
        print(f"  - Sanding Grit: {project.surface_preparation.sanding_grit}")
    print(f"- Drying Time: {project.surface_preparation.drying_time}")

    print("\nStain Selection:")
    print(f"- Recommended Stain Type: {project.stain_selection.recommended_stain_type.value}")
    print(f"- Recommended Brand: {project.stain_selection.recommended_brand}")
    print(f"- Color Options: {', '.join(project.stain_selection.color_options)}")
    print(f"- Coverage: {project.stain_selection.coverage}")
    print(f"- Drying Time: {project.stain_selection.drying_time}")
    print(f"- Durability: {project.stain_selection.durability}")

    print("\nApplication Plan:")
    print(f"- Tools Needed: {', '.join(project.application_plan.tools_needed)}")
    print(f"- Application Method: {project.application_plan.application_method}")
    print(f"- Coats Required: {project.application_plan.coats_required}")
    print(f"- Time Between Coats: {project.application_plan.time_between_coats}")
    print(f"- Ideal Weather: {project.application_plan.ideal_weather.value}")
    print(f"- Estimated Completion Time: {project.application_plan.estimated_completion_time}")

    print("\nSafety Considerations:")
