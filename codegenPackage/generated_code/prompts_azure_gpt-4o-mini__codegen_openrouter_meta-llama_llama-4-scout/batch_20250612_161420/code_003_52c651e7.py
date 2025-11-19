"""
Generated Code Metadata:
========================
Original URL: https://del-pinar.com.ar
Prompt: Develop a RESTful API endpoint that provides information about check-in and check-out times for an apart hotel located in a forested area by the sea.
Generated: DETERMINISTIC_52c651e713222665
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Apart Hotel Check-in/Check-out API",
    description="Provides information about check-in and check-out times for an apart hotel",
    version="1.0.0"
)

class HotelInfo(BaseModel):
    """Hotel information model"""
    name: str
    location: str

class CheckInOut(BaseModel):
    """Check-in/Check-out times model"""
    check_in: datetime
    check_out: datetime

# In-memory data store for demonstration purposes
# Replace with a proper database in production
hotel_info = HotelInfo(
    name="Sea Forest Apart Hotel",
    location="By the sea, in a forest"
)

check_in_out_times = [
    CheckInOut(check_in=datetime(2024, 9, 16, 14, 0), check_out=datetime(2024, 9, 17, 12, 0)),
    CheckInOut(check_in=datetime(2024, 9, 17, 15, 0), check_out=datetime(2024, 9, 18, 11, 0)),
]

@app.get("/hotel/info")
async def get_hotel_info():
    """Get hotel information"""
    return hotel_info

@app.get("/check-in-out/times")
async def get_check_in_out_times():
    """Get check-in/check-out times"""
    return check_in_out_times

@app.post("/check-in-out/times")
async def create_check_in_out_time(check_in_out: CheckInOut):
    """Create a new check-in/check-out time"""
    check_in_out_times.append(check_in_out)
    return check_in_out_times[-1]

@app.get("/check-in-out/times/{check_in_out_id}")
async def get_check_in_out_time(check_in_out_id: int):
    """Get a check-in/check-out time by ID"""
    try:
        return check_in_out_times[check_in_out_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Check-in/Check-out time not found")

@app.put("/check-in-out/times/{check_in_out_id}")
async def update_check_in_out_time(check_in_out_id: int, check_in_out: CheckInOut):
    """Update a check-in/check-out time"""
    try:
        check_in_out_times[check_in_out_id] = check_in_out
        return check_in_out_times[check_in_out_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Check-in/Check-out time not found")

@app.delete("/check-in-out/times/{check_in_out_id}")
async def delete_check_in_out_time(check_in_out_id: int):
    """Delete a check-in/check-out time"""
    try:
        del check_in_out_times[check_in_out_id]
        return {"message": "Check-in/Check-out time deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Check-in/Check-out time not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with
# uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
