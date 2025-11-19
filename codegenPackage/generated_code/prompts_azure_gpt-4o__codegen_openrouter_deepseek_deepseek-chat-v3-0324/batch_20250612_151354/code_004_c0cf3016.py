"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Suggest an API for managing certifications with QR codes, ensuring the generated codes are legally valid under Peruvian norms, as highlighted on the Enacip website.
Generated: DETERMINISTIC_c0cf301636321bc5
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from io import BytesIO
from datetime import datetime
import hashlib
import json
from typing import Optional, Dict
from fastapi import FastAPI, HTTPException, status, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field, validator
import pytz

app = FastAPI(
    title="Certification QR Code API",
    description="API for managing certifications with legally valid QR codes under Peruvian norms",
    version="1.0.0"
)

# Constants based on Peruvian regulations (ENACIP)
QR_CODE_VERSION = 1
QR_CODE_ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_M
QR_CODE_BOX_SIZE = 10
QR_CODE_BORDER = 4
PERU_TIMEZONE = pytz.timezone('America/Lima')

class CertificationData(BaseModel):
    """Model for certification data that will be encoded in the QR code."""
    certification_id: str = Field(..., min_length=1, max_length=50, description="Unique certification identifier")
    issuer_name: str = Field(..., min_length=1, max_length=100, description="Name of the issuing entity")
    recipient_name: str = Field(..., min_length=1, max_length=100, description="Name of the certification recipient")
    issue_date: str = Field(..., description="Issue date in ISO 8601 format")
    expiration_date: Optional[str] = Field(None, description="Expiration date in ISO 8601 format")
    additional_data: Optional[Dict[str, str]] = Field(None, description="Additional metadata for the certification")

    @validator('issue_date', 'expiration_date')
    def validate_date_format(cls, v):
        if v is None:
            return v
        try:
            datetime.fromisoformat(v)
        except ValueError:
            raise ValueError("Date must be in ISO 8601 format (YYYY-MM-DD)")
        return v

def generate_qr_code(data: str) -> BytesIO:
    """Generate a QR code from the given data."""
    qr = qrcode.QRCode(
        version=QR_CODE_VERSION,
        error_correction=QR_CODE_ERROR_CORRECTION,
        box_size=QR_CODE_BOX_SIZE,
        border=QR_CODE_BORDER,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, "PNG")
    img_bytes.seek(0)
    return img_bytes

def generate_verification_hash(data: CertificationData) -> str:
    """Generate a verification hash for the certification data."""
    data_str = json.dumps(data.dict(), sort_keys=True)
    return hashlib.sha256(data_str.encode()).hexdigest()

@app.post("/generate-certification/", response_class=StreamingResponse)
async def generate_certification(cert_data: CertificationData):
    """Generate a certification with a legally valid QR code under Peruvian norms."""
    try:
        # Validate dates are in Peru timezone
        issue_date = datetime.fromisoformat(cert_data.issue_date).astimezone(PERU_TIMEZONE)
        if cert_data.expiration_date:
            expiration_date = datetime.fromisoformat(cert_data.expiration_date).astimezone(PERU_TIMEZONE)
            if expiration_date < issue_date:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Expiration date must be after issue date"
                )

        # Generate verification hash
        verification_hash = generate_verification_hash(cert_data)
        
        # Prepare data for QR code
        qr_data = {
            **cert_data.dict(),
            "verification_hash": verification_hash,
            "qr_generation_date": datetime.now(PERU_TIMEZONE).isoformat()
        }
        
        # Generate QR code
        qr_code = generate_qr_code(json.dumps(qr_data))
        
        return StreamingResponse(
            qr_code,
            media_type="image/png",
            headers={
                "Content-Disposition": f"attachment; filename=certification_{cert_data.certification_id}.png",
                "X-Verification-Hash": verification_hash
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.post("/verify-certification/")
async def verify_certification(file: UploadFile = File(...)):
    """Verify a certification by scanning its QR code."""
    try:
        # Read QR code content
        from pyzbar.pyzbar import decode
        from PIL import Image
        
        contents = await file.read()
        img = Image.open(BytesIO(contents))
        decoded_data = decode(img)
        
        if not decoded_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No QR code found in the uploaded image"
            )
        
        qr_content = json.loads(decoded_data[0].data.decode())
        
        # Verify hash
        cert_data = CertificationData(**{k: v for k, v in qr_content.items() if k != "verification_hash" and k != "qr_generation_date"})
        expected_hash = generate_verification_hash(cert_data)
        
        if qr_content.get("verification_hash") != expected_hash:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid certification: Hash verification failed"
            )
        
        return {
            "valid": True,
            "certification_data": cert_data.dict(),
            "verification_date": datetime.now(PERU_TIMEZONE).isoformat()
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
