"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Write a Python script to generate a QR code for a calibration certificate, as seen on https://poverka-gazvoda.ru, given the company name and certificate details.
Generated: DETERMINISTIC_88cf78c5ad41b319
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import datetime
import os

def generate_qr_code(
    company_name: str,
    certificate_number: str,
    issue_date: datetime.date,
    expiry_date: datetime.date,
    output_path: str = "qr_codes",
    file_prefix: str = "certificate_"
) -> str:
    """
    Generates a styled QR code for a calibration certificate with the given details.
    
    Args:
        company_name: Name of the company issuing the certificate
        certificate_number: Unique certificate number
        issue_date: Date when certificate was issued
        expiry_date: Date when certificate expires
        output_path: Directory to save the QR code (default: 'qr_codes')
        file_prefix: Prefix for the output filename (default: 'certificate_')
    
    Returns:
        Path to the generated QR code image file
    
    Raises:
        ValueError: If any input parameter is invalid
        OSError: If there's an issue creating the output directory or saving the file
    """
    # Validate inputs
    if not company_name or not isinstance(company_name, str):
        raise ValueError("Company name must be a non-empty string")
    if not certificate_number or not isinstance(certificate_number, str):
        raise ValueError("Certificate number must be a non-empty string")
    if not isinstance(issue_date, datetime.date) or not isinstance(expiry_date, datetime.date):
        raise ValueError("Dates must be datetime.date objects")
    if issue_date > expiry_date:
        raise ValueError("Issue date cannot be after expiry date")

    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Format the QR code data
    qr_data = f"""Calibration Certificate
Company: {company_name}
Certificate No: {certificate_number}
Issued: {issue_date.strftime('%Y-%m-%d')}
Valid Until: {expiry_date.strftime('%Y-%m-%d')}"""

    # Configure QR code with styling
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create styled image
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            center_color=(70, 130, 180),  # Steel blue
            edge_color=(25, 25, 112)     # Midnight blue
        )
    )

    # Generate filename and save
    filename = f"{file_prefix}{certificate_number}.png"
    filepath = os.path.join(output_path, filename)
    img.save(filepath)

    return filepath

# Example usage
if __name__ == "__main__":
    try:
        # Example certificate data
        company = "Poverka Gazvoda"
        cert_num = "CERT-2023-001"
        issued = datetime.date(2023, 1, 15)
        expires = datetime.date(2024, 1, 14)
        
        # Generate QR code
        output_file = generate_qr_code(
            company_name=company,
            certificate_number=cert_num,
            issue_date=issued,
            expiry_date=expires
        )
        print(f"QR code generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating QR code: {str(e)}")
```
