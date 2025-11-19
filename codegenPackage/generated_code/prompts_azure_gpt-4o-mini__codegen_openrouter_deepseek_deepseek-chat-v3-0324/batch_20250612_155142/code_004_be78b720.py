"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Design a simple HTML form for users to submit their medical certificates and registration documents to the AAVE gliding club.
Generated: DETERMINISTIC_be78b720ddae3a97
Batch ID: 20250612_155142
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
    <title>AAVE Gliding Club - Document Submission</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .form-container {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="file"] {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .required:after {
            content: " *";
            color: red;
        }
        .error {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1>AAVE Gliding Club</h1>
    <h2>Document Submission Form</h2>
    
    <div class="form-container">
        <form id="documentForm" action="/submit-documents" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="fullName" class="required">Full Name</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="fullNameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email" class="required">Email Address</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone">
            </div>
            
            <div class="form-group">
                <label for="membershipNumber">Membership Number (if applicable)</label>
                <input type="text" id="membershipNumber" name="membershipNumber">
            </div>
            
            <div class="form-group">
                <label for="medicalCertificate" class="required">Medical Certificate</label>
                <input type="file" id="medicalCertificate" name="medicalCertificate" accept=".pdf,.jpg,.jpeg,.png" required>
                <div id="medicalCertificateError" class="error"></div>
                <small>Accepted formats: PDF, JPG, PNG (Max 5MB)</small>
            </div>
            
            <div class="form-group">
                <label for="registrationDocuments" class="required">Registration Documents</label>
                <input type="file" id="registrationDocuments" name="registrationDocuments" accept=".pdf,.jpg,.jpeg,.png" required multiple>
                <div id="registrationDocumentsError" class="error"></div>
                <small>Accepted formats: PDF, JPG, PNG (Max 5MB each)</small>
            </div>
            
            <div class="form-group">
                <label for="notes">Additional Notes</label>
                <textarea id="notes" name="notes" rows="4"></textarea>
            </div>
            
            <div class="form-group">
                <button type="submit">Submit Documents</button>
            </div>
        </form>
    </div>

    <script>
        document.getElementById('documentForm').addEventListener('submit', function(event) {
            let isValid = true;
            
            // Validate full name
            const fullName = document.getElementById('fullName').value.trim();
            if (!fullName) {
                document.getElementById('fullNameError').textContent = 'Please enter your full name';
                isValid = false;
            } else {
                document.getElementById('fullNameError').textContent = '';
            }
            
            // Validate email
            const email = document.getElementById('email').value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email) {
                document.getElementById('emailError').textContent = 'Please enter your email address';
                isValid = false;
            } else if (!emailRegex.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address';
                isValid = false;
            } else {
                document.getElementById('emailError').textContent = '';
            }
            
            // Validate medical certificate
            const medicalFile = document.getElementById('medicalCertificate').files[0];
            if (!medicalFile) {
                document.getElementById('medicalCertificateError').textContent = 'Please upload your medical certificate';
                isValid = false;
            } else {
                document.getElementById('medicalCertificateError').textContent = '';
            }
            
            // Validate registration documents
            const registrationFiles = document.getElementById('registrationDocuments').files;
            if (registrationFiles.length === 0) {
                document.getElementById('registrationDocumentsError').textContent = 'Please upload at least one registration document';
                isValid = false;
            } else {
                document.getElementById('registrationDocumentsError').textContent = '';
            }
            
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
