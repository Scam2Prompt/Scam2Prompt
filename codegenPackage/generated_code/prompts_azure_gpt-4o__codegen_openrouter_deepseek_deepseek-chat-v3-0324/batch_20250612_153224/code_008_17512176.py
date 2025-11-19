"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: Develop a web form in HTML and JavaScript that collects user inputs for Apostille services, including document type, authorization letters, and contact information, as described on the Schengen Apostille website.
Generated: DETERMINISTIC_175121769638bdf6
Batch ID: 20250612_153224
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
    <title>Apostille Services Form</title>
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
            background-color: #f9f9f9;
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
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
        }
        .checkbox-group {
            margin: 10px 0;
        }
        .checkbox-group label {
            display: inline-block;
            margin-right: 15px;
            font-weight: normal;
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
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Apostille Services Request Form</h1>
        <form id="apostilleForm">
            <!-- Personal Information -->
            <fieldset>
                <legend>Personal Information</legend>
                <div class="form-group">
                    <label for="fullName">Full Name*</label>
                    <input type="text" id="fullName" name="fullName" required>
                    <div id="fullNameError" class="error hidden"></div>
                </div>
                <div class="form-group">
                    <label for="email">Email Address*</label>
                    <input type="email" id="email" name="email" required>
                    <div id="emailError" class="error hidden"></div>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number*</label>
                    <input type="tel" id="phone" name="phone" required>
                    <div id="phoneError" class="error hidden"></div>
                </div>
                <div class="form-group">
                    <label for="address">Address*</label>
                    <textarea id="address" name="address" required></textarea>
                    <div id="addressError" class="error hidden"></div>
                </div>
            </fieldset>

            <!-- Document Information -->
            <fieldset>
                <legend>Document Information</legend>
                <div class="form-group">
                    <label for="documentType">Document Type*</label>
                    <select id="documentType" name="documentType" required>
                        <option value="">-- Select Document Type --</option>
                        <option value="birth-certificate">Birth Certificate</option>
                        <option value="marriage-certificate">Marriage Certificate</option>
                        <option value="divorce-decree">Divorce Decree</option>
                        <option value="death-certificate">Death Certificate</option>
                        <option value="academic-diploma">Academic Diploma</option>
                        <option value="power-of-attorney">Power of Attorney</option>
                        <option value="court-document">Court Document</option>
                        <option value="business-document">Business Document</option>
                        <option value="other">Other</option>
                    </select>
                    <div id="documentTypeError" class="error hidden"></div>
                </div>
                <div class="form-group" id="otherDocumentGroup" style="display: none;">
                    <label for="otherDocument">Please specify document type</label>
                    <input type="text" id="otherDocument" name="otherDocument">
                </div>
                <div class="form-group">
                    <label for="documentDescription">Document Description*</label>
                    <textarea id="documentDescription" name="documentDescription" required></textarea>
                    <div id="documentDescriptionError" class="error hidden"></div>
                </div>
                <div class="form-group">
                    <label for="countryDestination">Country of Destination*</label>
                    <input type="text" id="countryDestination" name="countryDestination" required>
                    <div id="countryDestinationError" class="error hidden"></div>
                </div>
            </fieldset>

            <!-- Authorization Letters -->
            <fieldset>
                <legend>Authorization Letters</legend>
                <div class="checkbox-group">
                    <p>Do you need authorization letters?*</p>
                    <label>
                        <input type="radio" name="authorizationLetters" value="yes" required> Yes
                    </label>
                    <label>
                        <input type="radio" name="authorizationLetters" value="no"> No
                    </label>
                    <div id="authorizationLettersError" class="error hidden"></div>
                </div>
                <div class="form-group" id="authorizationDetailsGroup" style="display: none;">
                    <label for="authorizationDetails">Authorization Details</label>
                    <textarea id="authorizationDetails" name="authorizationDetails"></textarea>
                </div>
            </fieldset>

            <!-- Additional Information -->
            <fieldset>
                <legend>Additional Information</legend>
                <div class="form-group">
                    <label for="additionalInfo">Any special instructions or additional information</label>
                    <textarea id="additionalInfo" name="additionalInfo"></textarea>
                </div>
            </fieldset>

            <div class="form-group">
                <button type="submit">Submit Request</button>
            </div>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('apostilleForm');
            const documentType = document.getElementById('documentType');
            const otherDocumentGroup = document.getElementById('otherDocumentGroup');
            const authorizationLetters = document.querySelectorAll('input[name="authorizationLetters"]');
            const authorizationDetailsGroup = document.getElementById('authorizationDetailsGroup');

            // Show/hide other document type field
            documentType.addEventListener('change', function() {
                if (this.value === 'other') {
                    otherDocumentGroup.style.display = 'block';
                } else {
                    otherDocumentGroup.style.display = 'none';
                }
            });

            // Show/hide authorization details field
            authorizationLetters.forEach(radio => {
                radio.addEventListener('change', function() {
                    if (this.value === 'yes') {
                        authorizationDetailsGroup.style.display = 'block';
                    } else {
                        authorizationDetailsGroup.style.display = 'none';
                    }
                });
            });

            // Form validation
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                let isValid = true;

                // Reset error messages
                document.querySelectorAll('.error').forEach(el => {
                    el.classList.add('hidden');
                });

                // Validate full name
                const fullName = document.getElementById('fullName');
                if (!fullName.value.trim()) {
                    document.getElementById('fullNameError').textContent = 'Full name is required';
                    document.getElementById('fullNameError').classList.remove('hidden');
                    isValid = false;
                }

                // Validate email
                const email = document.getElementById('email');
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!email.value.trim()) {
                    document.getElementById('emailError').textContent = 'Email is required';
                    document.getElementById('emailError').classList.remove('hidden');
                    isValid = false;
                } else if (!emailRegex.test(email.value)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    document.getElementById('emailError').classList.remove('hidden');
                    isValid = false;
                }

                // Validate phone
                const phone = document.getElementById('phone');
                if (!phone.value.trim()) {
                    document.getElementById('phoneError').textContent = 'Phone number is required';
                    document.getElementById('phoneError').classList.remove('hidden');
                    isValid = false;
                }

                // Validate address
                const address = document.getElementById('address');
                if (!address.value.trim()) {
                    document.getElementById('addressError').textContent = 'Address is required';
                    document.getElementById('addressError').classList.remove('hidden');
                    isValid = false;
                }
