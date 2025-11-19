"""
Generated Code Metadata:
========================
Original URL: https://fastpaymentve.com
Prompt: Design a simple API to handle payment transactions using a QR code scanner, inspired by FastPayment's features.
Generated: DETERMINISTIC_89106218a17bc2a3
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging
import qrcode
from PIL import Image
from io import BytesIO
import base64

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define payment transaction model
class PaymentTransaction(BaseModel):
    """Payment transaction model"""
    amount: float
    payment_method: str
    qr_code: Optional[str] = None

# Define QR code model
class QRCode(BaseModel):
    """QR code model"""
    data: str
    image: Optional[str] = None

# Generate QR code
def generate_qr_code(data: str) -> str:
    """Generate QR code from data"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Payment transaction endpoint
@app.post("/payment-transactions/")
async def create_payment_transaction(payment_transaction: PaymentTransaction):
    try:
        # Validate payment transaction
        if payment_transaction.amount <= 0:
            raise HTTPException(status_code=400, detail="Invalid amount")

        # Generate QR code for payment transaction
        qr_code_data = f"PaymentTransaction-{payment_transaction.amount}-{payment_transaction.payment_method}"
        qr_code_image = generate_qr_code(qr_code_data)

        # Return payment transaction with QR code
        return {"transaction_id": 1, "amount": payment_transaction.amount, "payment_method": payment_transaction.payment_method, "qr_code": qr_code_image}
    except Exception as e:
        logger.error(f"Error creating payment transaction: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# QR code endpoint
@app.get("/qr-codes/{data}")
async def get_qr_code(data: str):
    try:
        # Generate QR code
        qr_code_image = generate_qr_code(data)
        return {"data": data, "image": qr_code_image}
    except Exception as e:
        logger.error(f"Error generating QR code: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Payment transaction status endpoint
@app.get("/payment-transactions/{transaction_id}")
async def get_payment_transaction_status(transaction_id: int):
    try:
        # Simulate payment transaction status
        status = "success"  # Replace with actual payment gateway status
        return {"transaction_id": transaction_id, "status": status}
    except Exception as e:
        logger.error(f"Error getting payment transaction status: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
```

```python
# main.py
from payment_api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
