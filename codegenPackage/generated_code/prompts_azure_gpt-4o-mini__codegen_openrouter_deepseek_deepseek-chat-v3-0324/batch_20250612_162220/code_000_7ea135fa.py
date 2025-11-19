"""
Generated Code Metadata:
========================
Original URL: https://mannamarkets.com
Prompt: Generate code for a vending machine API that supports 24/7 accessibility and diverse product offerings similar to Manna Markets.
Generated: DETERMINISTIC_7ea135fa6c572502
Batch ID: 20250612_162220
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
from datetime import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Manna Markets Vending Machine API",
    description="API for 24/7 accessible vending machines with diverse product offerings",
    version="1.0.0"
)

# Database simulation
class Product(BaseModel):
    id: str
    name: str
    price: float
    quantity: int
    category: str
    last_restocked: datetime

class Transaction(BaseModel):
    id: str
    product_id: str
    amount_paid: float
    change_given: float
    timestamp: datetime
    status: str  # "completed", "failed", "refunded"

# In-memory "database"
products_db = {}
transactions_db = {}

# Initialize with some sample products
def initialize_db():
    sample_products = [
        {"id": str(uuid.uuid4()), "name": "Water Bottle", "price": 1.50, "quantity": 20, "category": "beverages", "last_restocked": datetime.now()},
        {"id": str(uuid.uuid4()), "name": "Energy Bar", "price": 2.00, "quantity": 15, "category": "snacks", "last_restocked": datetime.now()},
        {"id": str(uuid.uuid4()), "name": "Sandwich", "price": 3.50, "quantity": 10, "category": "meals", "last_restocked": datetime.now()},
    ]
    
    for product in sample_products:
        products_db[product["id"]] = product

initialize_db()

# Models for API requests/responses
class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    category: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category: Optional[str] = None

class PurchaseRequest(BaseModel):
    product_id: str
    amount_paid: float

class RestockRequest(BaseModel):
    product_id: str
    quantity: int

# Helper functions
def get_product(product_id: str) -> Optional[Product]:
    product = products_db.get(product_id)
    if product:
        return Product(**product)
    return None

def create_transaction(product_id: str, amount_paid: float, change: float, status: str) -> Transaction:
    transaction = {
        "id": str(uuid.uuid4()),
        "product_id": product_id,
        "amount_paid": amount_paid,
        "change_given": change,
        "timestamp": datetime.now(),
        "status": status
    }
    transactions_db[transaction["id"]] = transaction
    return Transaction(**transaction)

# API Endpoints
@app.get("/products", response_model=List[Product], tags=["Products"])
def list_products():
    """List all available products"""
    return [Product(**product) for product in products_db.values()]

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product_by_id(product_id: str):
    """Get details of a specific product"""
    product = get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
def create_product(product_data: ProductCreate):
    """Add a new product to the vending machine"""
    product_id = str(uuid.uuid4())
    product = {
        "id": product_id,
        **product_data.dict(),
        "last_restocked": datetime.now()
    }
    products_db[product_id] = product
    logger.info(f"Created new product: {product_id}")
    return Product(**product)

@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
def update_product(product_id: str, product_data: ProductUpdate):
    """Update product information"""
    product = get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    update_data = product_data.dict(exclude_unset=True)
    updated_product = product.dict()
    updated_product.update(update_data)
    products_db[product_id] = updated_product
    
    logger.info(f"Updated product: {product_id}")
    return Product(**updated_product)

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
def delete_product(product_id: str):
    """Remove a product from the vending machine"""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    del products_db[product_id]
    logger.info(f"Deleted product: {product_id}")

@app.post("/purchase", response_model=Transaction, tags=["Transactions"])
def purchase_product(purchase: PurchaseRequest):
    """Process a product purchase"""
    product = get_product(purchase.product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    if product.quantity <= 0:
        transaction = create_transaction(
            purchase.product_id,
            purchase.amount_paid,
            purchase.amount_paid,
            "failed"
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product out of stock",
            headers={"X-Transaction-ID": transaction.id}
        )
    
    if purchase.amount_paid < product.price:
        transaction = create_transaction(
            purchase.product_id,
            purchase.amount_paid,
            purchase.amount_paid,
            "failed"
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient funds",
            headers={"X-Transaction-ID": transaction.id}
        )
    
    # Process successful purchase
    change = purchase.amount_paid - product.price
    updated_quantity = product.quantity - 1
    
    # Update product quantity
    products_db[purchase.product_id]["quantity"] = updated_quantity
    
    # Create transaction record
    transaction = create_transaction(
        purchase.product_id,
        purchase.amount_paid,
        change,
        "completed"
    )
    
    logger.info(f"Processed purchase for product: {purchase.product_id}")
    return transaction

@app.post("/restock", response_model=Product, tags=["Products"])
def restock_product(restock: RestockRequest):
    """Restock a product in the vending machine"""
    product = get_product(restock.product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    if restock.quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Restock quantity must be positive"
        )
    
    # Update product quantity and restock time
    updated_quantity = product.quantity + restock.quantity
    products_db[restock.product_id]["quantity"] = updated_quantity
    products_db[restock.product_id]["last_restocked"] = datetime.now()
    
    logger.info(f"Restocked product: {restock.product_id} with {restock.quantity} units")
    return Product(**products_db[restock.product_id])

@app.get("/transactions", response_model=List[Transaction], tags=["Transactions"])
def list_transactions():
    """List all transactions"""
    return [Transaction(**tx) for tx in transactions_db.values()]

@app.get("/transactions/{transaction_id}", response_model=Transaction, tags=["Transactions"])
def get_transaction(transaction_id: str):
    """Get details of a specific transaction"""
    transaction = transactions_db.get(transaction_id)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    return Transaction(**transaction)

@app.get("/health", tags=["System"])
def health_check():
    """Check system health"""
    return {"status": "healthy", "timestamp": datetime.now()}
```
