"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: "Develop an API for monitoring and controlling a water filtration system, incorporating features such as real-time water quality monitoring and automated filter replacement alerts."
Generated: DETERMINISTIC_149df9eb743214ea
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# water_filtration_api.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import logging
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Water Filtration System API",
    description="API for monitoring and controlling water filtration systems",
    version="1.0.0"
)

# Database simulation
class WaterQualityReading(BaseModel):
    timestamp: datetime
    ph_level: float
    turbidity: float  # in NTU
    chlorine_level: float  # in ppm
    flow_rate: float  # in L/min

class FilterStatus(BaseModel):
    filter_id: str
    installation_date: datetime
    last_replacement_date: Optional[datetime] = None
    estimated_lifespan_days: int
    current_usage_days: int
    needs_replacement: bool = False

# In-memory storage for simulation
water_quality_readings = []
filters = []

@app.post("/api/water-quality", status_code=status.HTTP_201_CREATED)
async def add_water_quality_reading(reading: WaterQualityReading):
    """
    Add a new water quality reading to the system.
    """
    try:
        water_quality_readings.append(reading)
        logger.info(f"New water quality reading added: {reading}")
        return {"message": "Water quality reading added successfully"}
    except Exception as e:
        logger.error(f"Error adding water quality reading: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add water quality reading"
        )

@app.get("/api/water-quality/latest")
async def get_latest_water_quality():
    """
    Get the latest water quality reading.
    """
    if not water_quality_readings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No water quality readings available"
        )
    return water_quality_readings[-1]

@app.get("/api/water-quality/history")
async def get_water_quality_history(limit: int = 10):
    """
    Get water quality history (most recent first).
    """
    if not water_quality_readings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No water quality readings available"
        )
    return water_quality_readings[-limit:]

@app.post("/api/filters", status_code=status.HTTP_201_CREATED)
async def add_filter(filter_data: FilterStatus):
    """
    Add a new filter to the system.
    """
    try:
        filters.append(filter_data)
        logger.info(f"New filter added: {filter_data}")
        return {"message": "Filter added successfully"}
    except Exception as e:
        logger.error(f"Error adding filter: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add filter"
        )

@app.get("/api/filters")
async def get_all_filters():
    """
    Get all filters in the system.
    """
    if not filters:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No filters available"
        )
    return filters

@app.get("/api/filters/{filter_id}")
async def get_filter_status(filter_id: str):
    """
    Get status of a specific filter by ID.
    """
    for filter in filters:
        if filter.filter_id == filter_id:
            return filter
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Filter not found"
    )

@app.put("/api/filters/{filter_id}/replace")
async def replace_filter(filter_id: str):
    """
    Mark a filter as replaced and reset its usage.
    """
    for filter in filters:
        if filter.filter_id == filter_id:
            filter.last_replacement_date = datetime.now()
            filter.current_usage_days = 0
            filter.needs_replacement = False
            logger.info(f"Filter {filter_id} marked as replaced")
            return {"message": f"Filter {filter_id} marked as replaced"}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Filter not found"
    )

@app.get("/api/filters/needs-replacement")
async def get_filters_needing_replacement():
    """
    Get all filters that need replacement.
    """
    filters_needing_replacement = [
        filter for filter in filters 
        if filter.needs_replacement or 
           filter.current_usage_days >= filter.estimated_lifespan_days
    ]
    if not filters_needing_replacement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No filters need replacement"
        )
    return filters_needing_replacement

@app.get("/api/system/status")
async def get_system_status():
    """
    Get overall system status including water quality and filter status.
    """
    if not water_quality_readings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No system data available"
        )
    
    latest_reading = water_quality_readings[-1]
    filters_needing_replacement = [
        filter.filter_id for filter in filters 
        if filter.needs_replacement or 
           filter.current_usage_days >= filter.estimated_lifespan_days
    ]
    
    return {
        "water_quality": latest_reading,
        "filters_needing_replacement": filters_needing_replacement,
        "total_filters": len(filters),
        "system_status": "operational"  # Simplified status
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
