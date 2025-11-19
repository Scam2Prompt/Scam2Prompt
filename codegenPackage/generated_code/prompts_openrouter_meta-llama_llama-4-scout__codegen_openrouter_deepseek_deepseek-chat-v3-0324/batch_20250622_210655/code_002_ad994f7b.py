"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Design a simple API to track and manage Styrofoam waste recycling, including endpoints for adding waste, processing it through a densifier, and calculating the economic benefits of recycling."
Generated: DETERMINISTIC_ad994f7b8d6d9aef
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Styrofoam Waste Recycling API",
    description="API for tracking and managing Styrofoam waste recycling",
    version="1.0.0"
)

# Database simulation
class WasteRecord(BaseModel):
    id: str
    weight_kg: float
    source: str
    date_received: datetime
    is_processed: bool = False
    processing_date: Optional[datetime] = None
    densifier_id: Optional[str] = None

class Densifier(BaseModel):
    id: str
    name: str
    capacity_kg: float
    operational_status: str = "active"

# In-memory storage
waste_db: List[WasteRecord] = []
densifiers_db: List[Densifier] = [
    Densifier(id="d1", name="Densifier-1", capacity_kg=100.0),
    Densifier(id="d2", name="Densifier-2", capacity_kg=200.0)
]

# Constants
RECYCLING_BENEFIT_PER_KG = 0.15  # $ per kg
PROCESSING_COST_PER_KG = 0.05    # $ per kg

# Models for requests
class WasteInput(BaseModel):
    weight_kg: float
    source: str

class ProcessRequest(BaseModel):
    waste_id: str
    densifier_id: str

class EconomicBenefitResponse(BaseModel):
    total_recycled_kg: float
    total_benefit: float
    total_cost: float
    net_benefit: float

@app.post("/waste", status_code=status.HTTP_201_CREATED)
async def add_waste(waste_input: WasteInput):
    """Add new Styrofoam waste to the system"""
    try:
        waste_id = str(uuid.uuid4())
        new_waste = WasteRecord(
            id=waste_id,
            weight_kg=waste_input.weight_kg,
            source=waste_input.source,
            date_received=datetime.now()
        )
        waste_db.append(new_waste)
        logger.info(f"Added new waste record: {waste_id}")
        return {"id": waste_id, "message": "Waste record created successfully"}
    except Exception as e:
        logger.error(f"Error adding waste: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add waste record"
        )

@app.get("/waste", response_model=List[WasteRecord])
async def get_all_waste(processed: Optional[bool] = None):
    """Get all waste records, optionally filtered by processing status"""
    try:
        if processed is not None:
            return [w for w in waste_db if w.is_processed == processed]
        return waste_db
    except Exception as e:
        logger.error(f"Error retrieving waste records: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve waste records"
        )

@app.post("/process", status_code=status.HTTP_200_OK)
async def process_waste(process_request: ProcessRequest):
    """Process waste through a densifier"""
    try:
        # Find waste record
        waste = next((w for w in waste_db if w.id == process_request.waste_id), None)
        if not waste:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Waste record not found"
            )
        
        if waste.is_processed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Waste already processed"
            )

        # Find densifier
        densifier = next((d for d in densifiers_db if d.id == process_request.densifier_id), None)
        if not densifier:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Densifier not found"
            )

        if densifier.operational_status != "active":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Densifier is not operational"
            )

        # Update waste record
        waste.is_processed = True
        waste.processing_date = datetime.now()
        waste.densifier_id = densifier.id
        
        logger.info(f"Processed waste {waste.id} through densifier {densifier.id}")
        return {"message": "Waste processed successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing waste: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process waste"
        )

@app.get("/economic-benefits", response_model=EconomicBenefitResponse)
async def calculate_economic_benefits():
    """Calculate economic benefits of recycling"""
    try:
        processed_waste = [w for w in waste_db if w.is_processed]
        total_recycled = sum(w.weight_kg for w in processed_waste)
        total_benefit = total_recycled * RECYCLING_BENEFIT_PER_KG
        total_cost = total_recycled * PROCESSING_COST_PER_KG
        net_benefit = total_benefit - total_cost
        
        return {
            "total_recycled_kg": total_recycled,
            "total_benefit": total_benefit,
            "total_cost": total_cost,
            "net_benefit": net_benefit
        }
    except Exception as e:
        logger.error(f"Error calculating economic benefits: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to calculate economic benefits"
        )

@app.get("/densifiers", response_model=List[Densifier])
async def get_all_densifiers():
    """Get all available densifiers"""
    try:
        return densifiers_db
    except Exception as e:
        logger.error(f"Error retrieving densifiers: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve densifiers"
        )
```
