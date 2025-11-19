"""
Generated Code Metadata:
========================
Original URL: https://certificatepros.com
Prompt: Create a template for a medical certificate using HTML and CSS, including placeholders for patient and doctor information, and a signature field.
Generated: DETERMINISTIC_f51668ebb01c0bd0
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Certificate</title>
    <style>
        /* General styles for the document */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }

        .certificate-container {
            border: 2px solid #000;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
            background-color: #f9f9f9;
        }

        .header {
            text-align: center;
            margin-bottom: 20px;
        }

        .header h1 {
            font-size: 24px;
            margin: 0;
        }

        .header p {
            font-size: 16px;
            margin: 0;
        }

        .content {
            margin-bottom: 20px;
        }

        .content p {
            margin: 10px 0;
        }

        .signature-section {
            margin-top: 30px;
            text-align: right;
        }

        .signature-line {
            border-top: 1px solid #000;
            width: 200px;
            margin: 10px 0;
        }

        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="certificate-container">
        <!-- Header Section -->
        <div class="header">
            <h1>Medical Certificate</h1>
            <p>Issued by: [Hospital/Clinic Name]</p>
        </div>

        <!-- Content Section -->
        <div class="content">
            <p><strong>Patient Name:</strong> [Patient Name]</p>
            <p><strong>Age:</strong> [Patient Age]</p>
            <p><strong>Gender:</strong> [Patient Gender]</p>
            <p><strong>Date of Examination:</strong> [Examination Date]</p>
            <p><strong>Diagnosis:</strong> [Diagnosis Details]</p>
            <p><strong>Remarks:</strong> [Additional Remarks]</p>
        </div>

        <!-- Signature Section -->
        <div class="signature-section">
            <p><strong>Doctor's Name:</strong> [Doctor Name]</p>
            <p><strong>License Number:</strong> [License Number]</p>
            <div class="signature-line"></div>
            <p>Signature</p>
        </div>

        <!-- Footer Section -->
        <div class="footer">
            <p>This certificate is issued as per the medical examination conducted.</p>
        </div>
    </div>
</body>
</html>
```
