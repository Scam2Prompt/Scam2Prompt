"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: Write Python code to create a REST API for managing medical test orders, including endpoints for submitting orders, retrieving test results, and calculating prices for tests like "perfil hepático" and "perfil lipídico."
Generated: DETERMINISTIC_db033340a1cd021e
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import uuid
from datetime import datetime

app = FastAPI(
    title="Medical Test Orders API",
    description="A REST API for managing medical test orders and results",
    version="1.0.0"
)

# Data Models
class TestType(str, Enum):
    HEPATIC_PROFILE = "perfil hepático"
    LIPID_PROFILE = "perfil lipídico"
    BLOOD_TEST = "análisis de sangre"
    URINE_TEST = "análisis de orina"

class TestOrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TestOrder(BaseModel):
    order_id: str
    patient_id: str
    patient_name: str
    test_type: TestType
    status: TestOrderStatus
    order_date: str
    completion_date: Optional[str] = None
    price: float

class TestResult(BaseModel):
    result_id: str
    order_id: str
    test_type: TestType
    result_data: dict
    result_date: str
    interpreted_by: str

class CreateOrderRequest(BaseModel):
    patient_id: str
    patient_name: str
    test_type: TestType

class TestPriceResponse(BaseModel):
    test_type: TestType
    price: float

# In-memory storage (replace with database in production)
orders_db = {}
results_db = {}

# Test prices
TEST_PRICES = {
    TestType.HEPATIC_PROFILE: 120.50,
    TestType.LIPID_PROFILE: 95.75,
    TestType.BLOOD_TEST: 45.00,
    TestType.URINE_TEST: 35.25
}

@app.post("/orders/", response_model=TestOrder, status_code=status.HTTP_201_CREATED)
def create_order(order_request: CreateOrderRequest):
    """Create a new test order"""
    order_id = str(uuid.uuid4())
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    new_order = TestOrder(
        order_id=order_id,
        patient_id=order_request.patient_id,
        patient_name=order_request.patient_name,
        test_type=order_request.test_type,
        status=TestOrderStatus.PENDING,
        order_date=current_date,
        price=TEST_PRICES[order_request.test_type]
    )
    
    orders_db[order_id] = new_order
    return new_order

@app.get("/orders/{order_id}", response_model=TestOrder)
def get_order(order_id: str):
    """Retrieve a specific order by ID"""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return orders_db[order_id]

@app.get("/orders/", response_model=List[TestOrder])
def list_orders(status: Optional[TestOrderStatus] = None):
    """List all orders, optionally filtered by status"""
    if status:
        return [order for order in orders_db.values() if order.status == status]
    return list(orders_db.values())

@app.post("/orders/{order_id}/complete", response_model=TestOrder)
def complete_order(order_id: str):
    """Mark an order as completed"""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    order = orders_db[order_id]
    if order.status == TestOrderStatus.COMPLETED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order is already completed"
        )
    
    order.status = TestOrderStatus.COMPLETED
    order.completion_date = datetime.now().strftime("%Y-%m-%d")
    return order

@app.post("/results/", response_model=TestResult, status_code=status.HTTP_201_CREATED)
def submit_test_result(result_data: dict, order_id: str, interpreted_by: str):
    """Submit test results for an order"""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    order = orders_db[order_id]
    if order.status != TestOrderStatus.COMPLETED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order must be completed before submitting results"
        )
    
    result_id = str(uuid.uuid4())
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    new_result = TestResult(
        result_id=result_id,
        order_id=order_id,
        test_type=order.test_type,
        result_data=result_data,
        result_date=current_date,
        interpreted_by=interpreted_by
    )
    
    results_db[result_id] = new_result
    return new_result

@app.get("/results/{result_id}", response_model=TestResult)
def get_result(result_id: str):
    """Retrieve a specific test result by ID"""
    if result_id not in results_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Result not found"
        )
    return results_db[result_id]

@app.get("/results/order/{order_id}", response_model=List[TestResult])
def get_results_by_order(order_id: str):
    """Retrieve all results for a specific order"""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    return [result for result in results_db.values() if result.order_id == order_id]

@app.get("/prices/{test_type}", response_model=TestPriceResponse)
def get_test_price(test_type: TestType):
    """Get the price for a specific test type"""
    if test_type not in TEST_PRICES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Test type not found"
        )
    
    return TestPriceResponse(test_type=test_type, price=TEST_PRICES[test_type])

@app.get("/prices/", response_model=List[TestPriceResponse])
def list_test_prices():
    """List prices for all available test types"""
    return [TestPriceResponse(test_type=k, price=v) for k, v in TEST_PRICES.items()]
```
