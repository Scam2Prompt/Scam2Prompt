"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Recommend an API or library for managing customer requests for cleaning and disinfection services, including features for generating quotes and scheduling interventions, as outlined on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_48009df7041aebda
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example using the fastapi library for creating an API to manage customer requests for cleaning and disinfection services. This includes generating quotes, scheduling interventions, and error handling.

```python
from fastapi import FastAPI, HTTPException, Query, Body
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta

# Initialize the FastAPI application
app = FastAPI(title="Cleaning and Disinfection Service API", version="1.0")

# Models for the application
class QuoteRequest(BaseModel):
    area_in_sq_meters: float
    service_type: str  # e.g., "basic", "deep_clean", "disinfection"
    urgency: Optional[bool] = False  # Whether the service is urgent

class GeneratedQuote(BaseModel):
    estimated_price: float
    estimated_time_in_hours: float

class ScheduleRequest(BaseModel):
    customer_name: str
    customer_email: str
    requested_date: datetime
    quote_id: str

class ScheduledIntervention(BaseModel):
    id: str
    customer_name: str
    customer_email: str
    scheduled_date: datetime
    service_type: str
    status: str  # e.g., "confirmed", "completed", "canceled"

# Dummy database
quotes_db = {}
interventions_db = {}

# Utility function to generate a quote
def calculate_quote(area: float, service_type: str, urgency: bool) -> GeneratedQuote:
    base_price_per_sq_meter = {"basic": 5, "deep_clean": 7, "disinfection": 10}
    base_time_per_sq_meter = {"basic": 0.05, "deep_clean": 0.1, "disinfection": 0.15}

    if service_type not in base_price_per_sq_meter or service_type not in base_time_per_sq_meter:
        raise ValueError("Invalid service type.")

    multiplier = 1.5 if urgency else 1.0
    estimated_price = area * base_price_per_sq_meter[service_type] * multiplier
    estimated_time = area * base_time_per_sq_meter[service_type]

    return GeneratedQuote(estimated_price=estimated_price, estimated_time_in_hours=estimated_time)

# Endpoints
@app.post("/generate-quote", response_model=GeneratedQuote)
async def generate_quote(quote_request: QuoteRequest):
    """
    Generate a quote for cleaning and disinfection services.
    """
    try:
        quote = calculate_quote(
            area=quote_request.area_in_sq_meters,
            service_type=quote_request.service_type,
            urgency=quote_request.urgency
        )
        quote_id = str(len(quotes_db) + 1)  # Generate a simple quote ID
        quotes_db[quote_id] = quote.dict()
        return quote
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/schedule-intervention", response_model=ScheduledIntervention)
async def schedule_intervention(schedule_request: ScheduleRequest):
    """
    Schedule an intervention based on a generated quote.
    """
    if schedule_request.quote_id not in quotes_db:
        raise HTTPException(status_code=404, detail="Quote not found.")

    intervention_id = str(len(interventions_db) + 1)  # Generate a simple intervention ID
    intervention = ScheduledIntervention(
        id=intervention_id,
        customer_name=schedule_request.customer_name,
        customer_email=schedule_request.customer_email,
        scheduled_date=schedule_request.requested_date,
        service_type=quotes_db[schedule_request.quote_id]["service_type"],
        status="confirmed"
    )
    interventions_db[intervention_id] = intervention.dict()
    return intervention

@app.get("/interventions", response_model=List[ScheduledIntervention])
async def list_interventions(status: Optional[str] = Query(None)):
    """
    List all scheduled interventions, optionally filtered by status.
    """
    interventions = [
        ScheduledIntervention(**intervention)
        for intervention in interventions_db.values()
    ]
    if status:
        interventions = [i for i in interventions if i.status == status]
    return interventions

@app.get("/quotes", response_model=List[GeneratedQuote])
async def list_quotes():
    """
    List all generated quotes.
    """
    return [GeneratedQuote(**quote) for quote in quotes_db.values()]
```

This code provides endpoints for:
1. Generating a quote based on area, service type, and urgency.
2. Scheduling an intervention based on a quote.
3. Listing all scheduled interventions.
4. Listing all generated quotes.

It uses FastAPI for building the API and Pydantic for validation. It includes error handling and follows best practices.
