"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: "Design a simple web form using HTML and JavaScript that allows clients to input their information and select the type of document they need to apostille, similar to the one on the Schengen Apostille website."
Generated: DETERMINISTIC_6cb01804f0826bfa
Batch ID: 20250622_210655
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
    <title>Apostille Service Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
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
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
            resize: vertical;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background-color: #2980b9;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .success {
            color: green;
            font-size: 16px;
            text-align: center;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Apostille Service Request</h1>
        <form id="apostilleForm">
            <div class="form-group">
                <label for="fullName">Full Name*</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="fullNameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number*</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="country">Country*</label>
                <select id="country" name="country" required>
                    <option value="">Select Country</option>
                    <option value="US">United States</option>
                    <option value="UK">United Kingdom</option>
                    <option value="CA">Canada</option>
                    <option value="AU">Australia</option>
                    <option value="DE">Germany</option>
                    <option value="FR">France</option>
                    <option value="other">Other</option>
                </select>
                <div id="countryError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="documentType">Document Type*</label>
                <select id="documentType" name="documentType" required>
                    <option value="">Select Document Type</option>
                    <option value="birth-certificate">Birth Certificate</option>
                    <option value="marriage-certificate">Marriage Certificate</option>
                    <option value="divorce-decree">Divorce Decree</option>
                    <option value="death-certificate">Death Certificate</option>
                    <option value="academic-diploma">Academic Diploma</option>
                    <option value="court-document">Court Document</option>
                    <option value="power-of-attorney">Power of Attorney</option>
                    <option value="corporate-document">Corporate Document</option>
                    <option value="other">Other</option>
                </select>
                <div id="documentTypeError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="documentDescription">Document Description (if 'Other' selected)</label>
                <textarea id="documentDescription" name="documentDescription"></textarea>
            </div>

            <div class="form-group">
                <label for="urgency">Urgency Level*</label>
                <select id="urgency" name="urgency" required>
                    <option value="">Select Urgency</option>
                    <option value="standard">Standard (5-7 business days)</option>
                    <option value="express">Express (2-3 business days)</option>
                    <option value="urgent">Urgent (24 hours)</option>
                </select>
                <div id="urgencyError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="additionalInfo">Additional Information</label>
                <textarea id="additionalInfo" name="additionalInfo"></textarea>
            </div>

            <button type="submit" id="submitBtn">Submit Request</button>
        </form>

        <div id="successMessage" class="success">
            Thank you for your submission! We will contact you shortly.
        </div>
    </div>

    <script>
        document.getElementById('apostilleForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            const errorElements = document.querySelectorAll('.error');
            errorElements.forEach(element => {
                element.textContent = '';
            });

            // Validate form fields
            let isValid = true;
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const country = document.getElementById('country').value;
            const documentType = document.getElementById('documentType').value;
            const urgency = document.getElementById('urgency').value;

            if (!fullName) {
                document.getElementById('fullNameError').textContent = 'Full name is required';
                isValid = false;
            }

            if (!email) {
                document.getElementById('emailError').textContent = 'Email is required';
                isValid = false;
            } else if (!validateEmail(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address';
                isValid = false;
            }

            if (!phone) {
                document.getElementById('phoneError').textContent = 'Phone number is required';
                isValid = false;
            } else if (!validatePhone(phone)) {
                document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                isValid = false;
            }

            if (!country) {
                document.getElementById('countryError').textContent = 'Country is required';
                isValid = false;
            }

            if (!documentType) {
                document.getElementById('documentTypeError').textContent = 'Document type is required';
                isValid = false;
            }

            if (!urgency) {
                document.getElementById('urgencyError').textContent = 'Urgency level is required';
                isValid = false;
            }

            if (isValid) {
                // Form is valid, simulate submission
                document.getElementById('apostilleForm').style.display = 'none';
                document.getElementById('successMessage').style.display = 'block';
                
                // In a real application, you would send the data to a server here
                // For example:
                // const formData = new FormData(document.getElementById('apostilleForm'));
                // fetch('/submit-request', {
                //     method: 'POST',
                //     body: formData
                // })
                // .then(response => response.json())
                // .then(data => {
                //     document.getElementById('apostilleForm').style.display = 'none';
                //     document.getElementById('successMessage').style.display = 'block';
                // })
                // .catch(error => {
                //     alert('There was an error submitting your form. Please try again.');
                // });
            }
        });

        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }

        function validatePhone(phone) {
            const re = /^[\d\s\-\(\)\+]+$/;
            return re.test(phone);
        }
    </script>
</body>
</html>
```
