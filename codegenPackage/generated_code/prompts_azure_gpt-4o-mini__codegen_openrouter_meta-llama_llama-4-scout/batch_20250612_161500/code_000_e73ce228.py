"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: Generate a code snippet for a web application that allows users to request printing services for items like flyers and business cards, similar to the offerings of Detalj Reklam.
Generated: DETERMINISTIC_e73ce228601b3396
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Printing Service Request Web Application**
=============================================

**models.py**
```python
from enum import Enum
from typing import Optional

class PrintingServiceType(str, Enum):
    FLYER = "flyer"
    BUSINESS_CARD = "business_card"

class PrintingServiceRequest:
    def __init__(self, 
                 service_type: PrintingServiceType, 
                 quantity: int, 
                 paper_type: str, 
                 size: str, 
                 design: Optional[str] = None):
        self.service_type = service_type
        self.quantity = quantity
        self.paper_type = paper_type
        self.size = size
        self.design = design

    def __str__(self):
        return f"Printing Service Request: {self.service_type}, Quantity: {self.quantity}"
```

**database.py**
```python
import sqlite3
from typing import List

class PrintingServiceDatabase:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS printing_service_requests
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             service_type TEXT, 
             quantity INTEGER, 
             paper_type TEXT, 
             size TEXT, 
             design TEXT)
        ''')
        self.conn.commit()

    def insert_request(self, request: PrintingServiceRequest):
        self.cursor.execute('''
            INSERT INTO printing_service_requests (service_type, quantity, paper_type, size, design)
            VALUES (?, ?, ?, ?, ?)
        ''', (request.service_type.value, request.quantity, request.paper_type, request.size, request.design))
        self.conn.commit()

    def get_all_requests(self) -> List[PrintingServiceRequest]:
        self.cursor.execute('SELECT * FROM printing_service_requests')
        rows = self.cursor.fetchall()
        requests = []
        for row in rows:
            request = PrintingServiceRequest(
                PrintingServiceType(row[1]), 
                row[2], 
                row[3], 
                row[4], 
                row[5]
            )
            requests.append(request)
        return requests

    def close(self):
        self.conn.close()
```

**services.py**
```python
from .models import PrintingServiceRequest, PrintingServiceType
from .database import PrintingServiceDatabase

class PrintingService:
    def __init__(self, db_name: str):
        self.db = PrintingServiceDatabase(db_name)

    def request_printing_service(self, request: PrintingServiceRequest):
        try:
            self.db.insert_request(request)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def get_all_requests(self):
        return self.db.get_all_requests()

    def close(self):
        self.db.close()
```

**app.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import PrintingServiceRequest, PrintingServiceType
from .services import PrintingService

app = FastAPI()

class PrintingServiceRequestDTO(BaseModel):
    service_type: str
    quantity: int
    paper_type: str
    size: str
    design: str | None = None

    @classmethod
    def to_entity(cls, dto: 'PrintingServiceRequestDTO'):
        return PrintingServiceRequest(
            PrintingServiceType(dto.service_type), 
            dto.quantity, 
            dto.paper_type, 
            dto.size, 
            dto.design
        )

printing_service = PrintingService('printing_service.db')

@app.post("/printing-service/requests")
async def create_printing_service_request(request: PrintingServiceRequestDTO):
    try:
        entity = PrintingServiceRequestDTO.to_entity(request)
        if printing_service.request_printing_service(entity):
            return {"message": "Printing service request created successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to create printing service request")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/printing-service/requests")
async def get_all_printing_service_requests():
    try:
        requests = printing_service.get_all_requests()
        return [{"service_type": request.service_type.value, 
                 "quantity": request.quantity, 
                 "paper_type": request.paper_type, 
                 "size": request.size, 
                 "design": request.design} for request in requests]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("shutdown")
async def shutdown_event():
    printing_service.close()
```

**main.py**
```python
import uvicorn
from .app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
