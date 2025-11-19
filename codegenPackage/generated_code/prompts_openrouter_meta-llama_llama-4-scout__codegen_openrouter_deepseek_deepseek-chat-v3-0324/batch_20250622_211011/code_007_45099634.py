"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Design a simple web form using HTML and CSS to collect property information and provide a cash offer for a house in San Francisco Bay Area.
Generated: DETERMINISTIC_45099634ba46653b
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML and CSS implementation for a property information form with cash offer functionality:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bay Area Property Cash Offer</title>
    <style>
        /* Reset and base styles */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        /* Form container */
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #2c3e50;
        }

        /* Form styling */
        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }

        input[type="text"],
        input[type="number"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border 0.3s;
        }

        input:focus,
        select:focus,
        textarea:focus {
            border-color: #3498db;
            outline: none;
        }

        /* Button styling */
        .btn {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: background 0.3s;
        }

        .btn:hover {
            background: #2980b9;
        }

        /* Responsive grid */
        .row {
            display: flex;
            flex-wrap: wrap;
            margin: 0 -15px;
        }

        .col {
            flex: 1;
            padding: 0 15px;
            min-width: 200px;
        }

        /* Error handling */
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }

        /* Success message */
        .success-message {
            display: none;
            background: #2ecc71;
            color: white;
            padding: 20px;
            border-radius: 4px;
            margin-top: 20px;
            text-align: center;
        }

        /* Mobile responsiveness */
        @media (max-width: 600px) {
            .row {
                flex-direction: column;
            }
            
            .col {
                margin-bottom: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>San Francisco Bay Area Cash Offer</h1>
        
        <form id="propertyForm">
            <div class="row">
                <div class="col">
                    <div class="form-group">
                        <label for="propertyAddress">Property Address*</label>
                        <input type="text" id="propertyAddress" name="propertyAddress" required>
                        <div class="error" id="addressError">Please enter a valid address</div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col">
                    <div class="form-group">
                        <label for="propertyType">Property Type*</label>
                        <select id="propertyType" name="propertyType" required>
                            <option value="">Select property type</option>
                            <option value="single-family">Single Family Home</option>
                            <option value="condo">Condo</option>
                            <option value="townhouse">Townhouse</option>
                            <option value="multi-family">Multi-Family</option>
                        </select>
                        <div class="error" id="typeError">Please select a property type</div>
                    </div>
                </div>
                <div class="col">
                    <div class="form-group">
                        <label for="bedrooms">Bedrooms*</label>
                        <input type="number" id="bedrooms" name="bedrooms" min="0" required>
                        <div class="error" id="bedroomError">Please enter a valid number</div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col">
                    <div class="form-group">
                        <label for="bathrooms">Bathrooms*</label>
                        <input type="number" id="bathrooms" name="bathrooms" min="0" step="0.5" required>
                        <div class="error" id="bathroomError">Please enter a valid number</div>
                    </div>
                </div>
                <div class="col">
                    <div class="form-group">
                        <label for="squareFeet">Square Footage*</label>
                        <input type="number" id="squareFeet" name="squareFeet" min="0" required>
                        <div class="error" id="sqftError">Please enter a valid number</div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col">
                    <div class="form-group">
                        <label for="condition">Property Condition*</label>
                        <select id="condition" name="condition" required>
                            <option value="">Select condition</option>
                            <option value="excellent">Excellent</option>
                            <option value="good">Good</option>
                            <option value="fair">Fair</option>
                            <option value="poor">Poor</option>
                            <option value="needs-repair">Needs Repair</option>
                        </select>
                        <div class="error" id="conditionError">Please select a condition</div>
                    </div>
                </div>
                <div class="col">
                    <div class="form-group">
                        <label for="desiredPrice">Desired Price ($)</label>
                        <input type="number" id="desiredPrice" name="desiredPrice" min="0">
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label for="notes">Additional Notes</label>
                <textarea id="notes" name="notes" rows="4"></textarea>
            </div>

            <div class="form-group">
                <label for="ownerName">Owner Name*</label>
                <input type="text" id="ownerName" name="ownerName" required>
                <div class="error" id="nameError">Please enter your name</div>
            </div>

            <div class="row">
                <div class="col">
                    <div class="form-group">
                        <label for="ownerEmail">Email*</label>
                        <input type="email" id="ownerEmail" name="ownerEmail" required>
                        <div class="error" id="emailError">Please enter a valid email</div>
                    </div>
                </div>
                <div class="col">
                    <div class="form-group">
                        <label for="ownerPhone">Phone*</label>
                        <input type="tel" id="ownerPhone" name="ownerPhone" required>
                        <div class="error" id="phoneError">Please enter a valid phone number</div>
                    </div>
                </div>
            </div>

            <div class="form-group">
                <button type="submit" class="btn">Get Cash Offer</button>
            </div>
        </form>

        <div class="success-message" id="successMessage">
            <h2>Thank you for your submission!</h2>
            <p>We'll review your property information and contact you with a cash offer within 24 hours.</p>
        </div>
    </div>

    <script>
        document.getElementById('propertyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.style.display = 'none');
            
            // Validate form
            let isValid = true;
            const requiredFields = [
                'propertyAddress', 'propertyType', 'bedrooms', 
                'bathrooms', 'squareFeet', 'condition',
                'ownerName', 'ownerEmail', 'ownerPhone'
            ];
            
            requiredFields.forEach(fieldId => {
