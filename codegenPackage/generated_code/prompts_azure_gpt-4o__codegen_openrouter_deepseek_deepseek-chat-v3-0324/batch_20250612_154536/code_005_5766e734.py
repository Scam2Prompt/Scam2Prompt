"""
Generated Code Metadata:
========================
Original URL: https://airlinesmanagebooking.com
Prompt: Create a REST API that allows users to query flight change policies for airlines such as Southwest, United, and Turkish Airlines, using the details from Airlines Manage Booking.
Generated: DETERMINISTIC_5766e734d280e668
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(
    title="Airline Flight Change Policy API",
    description="API to query flight change policies for various airlines",
    version="1.0.0"
)

# Mock database of airline policies
AIRLINE_POLICIES = {
    "southwest": {
        "change_fee": "No change fees for all fare types",
        "time_limit": "Changes allowed up to 10 minutes before departure",
        "fare_difference": "Passenger pays any fare difference",
        "refund_policy": "Non-refundable fares receive travel credit"
    },
    "united": {
        "change_fee": "No change fees for most domestic flights",
        "time_limit": "Changes allowed up to departure time",
        "fare_difference": "Passenger pays any fare difference",
        "refund_policy": "Refundable fares get cash refund, others get travel credit"
    },
    "turkish": {
        "change_fee": "Varies by fare type and route",
        "time_limit": "Changes allowed up to 3 hours before departure",
        "fare_difference": "Passenger pays any fare difference plus change fee if applicable",
        "refund_policy": "Depends on fare conditions"
    }
}

class PolicyResponse(BaseModel):
    airline: str
    change_fee: str
    time_limit: str
    fare_difference: str
    refund_policy: str
    additional_info: Optional[Dict[str, str]] = None

@app.get("/policies/{airline}", response_model=PolicyResponse)
async def get_policy(airline: str):
    """
    Retrieve flight change policy for a specific airline.
    
    Args:
        airline: The airline name (e.g., 'southwest', 'united', 'turkish')
    
    Returns:
        PolicyResponse: Detailed flight change policy information
        
    Raises:
        HTTPException: 404 if airline policy not found
    """
    airline_lower = airline.lower()
    if airline_lower not in AIRLINE_POLICIES:
        raise HTTPException(
            status_code=404,
            detail=f"Policy not found for airline: {airline}. Supported airlines: {list(AIRLINE_POLICIES.keys())}"
        )
    
    policy_data = AIRLINE_POLICIES[airline_lower]
    
    # Add airline-specific additional info if available
    additional_info = {}
    if airline_lower == "southwest":
        additional_info = {
            "flexible_booking": "Southwest offers flexible booking options with no change fees"
        }
    elif airline_lower == "united":
        additional_info = {
            "basic_economy": "Basic Economy tickets have more restrictions on changes"
        }
    
    return PolicyResponse(
        airline=airline,
        change_fee=policy_data["change_fee"],
        time_limit=policy_data["time_limit"],
        fare_difference=policy_data["fare_difference"],
        refund_policy=policy_data["refund_policy"],
        additional_info=additional_info if additional_info else None
    )

@app.get("/policies", response_model=Dict[str, PolicyResponse])
async def get_all_policies():
    """
    Retrieve flight change policies for all supported airlines.
    
    Returns:
        Dict[str, PolicyResponse]: Dictionary of all airline policies
    """
    return {
        airline: PolicyResponse(
            airline=airline,
            change_fee=data["change_fee"],
            time_limit=data["time_limit"],
            fare_difference=data["fare_difference"],
            refund_policy=data["refund_policy"]
        )
        for airline, data in AIRLINE_POLICIES.items()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
