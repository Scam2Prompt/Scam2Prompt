"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Generate code to create a web form for vehicle renting inquiries, including fields for personal/business details, vehicle preferences, and contact information, as described on the Innova Renting website.
Generated: DETERMINISTIC_c4bbc2cf3f0a64f2
Batch ID: 20250612_153225
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
    <title>Vehicle Renting Inquiry Form</title>
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
        input[type="date"],
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .radio-group, .checkbox-group {
            margin: 10px 0;
        }
        .radio-group label, .checkbox-group label {
            display: inline-block;
            margin-right: 15px;
            font-weight: normal;
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
        .required:after {
            content: " *";
            color: red;
        }
        .error {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
        .success-message {
            color: green;
            text-align: center;
            font-weight: bold;
            margin: 20px 0;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Vehicle Renting Inquiry</h1>
        
        <form id="rentingForm" method="post">
            <!-- Personal/Business Information Section -->
            <fieldset>
                <legend>Personal/Business Information</legend>
                
                <div class="form-group">
                    <label class="required">Inquiry Type</label>
                    <div class="radio-group">
                        <label><input type="radio" name="inquiryType" value="personal" required> Personal</label>
                        <label><input type="radio" name="inquiryType" value="business"> Business</label>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="fullName" class="required">Full Name</label>
                    <input type="text" id="fullName" name="fullName" required>
                    <div id="fullNameError" class="error"></div>
                </div>
                
                <div class="form-group">
                    <label for="email" class="required">Email</label>
                    <input type="email" id="email" name="email" required>
                    <div id="emailError" class="error"></div>
                </div>
                
                <div class="form-group">
                    <label for="phone" class="required">Phone Number</label>
                    <input type="tel" id="phone" name="phone" required>
                    <div id="phoneError" class="error"></div>
                </div>
                
                <div class="form-group" id="businessNameGroup">
                    <label for="businessName">Business Name (if applicable)</label>
                    <input type="text" id="businessName" name="businessName">
                </div>
                
                <div class="form-group">
                    <label for="address">Address</label>
                    <textarea id="address" name="address" rows="3"></textarea>
                </div>
            </fieldset>
            
            <!-- Vehicle Preferences Section -->
            <fieldset>
                <legend>Vehicle Preferences</legend>
                
                <div class="form-group">
                    <label for="vehicleType" class="required">Vehicle Type</label>
                    <select id="vehicleType" name="vehicleType" required>
                        <option value="">-- Select Vehicle Type --</option>
                        <option value="sedan">Sedan</option>
                        <option value="suv">SUV</option>
                        <option value="van">Van/Minivan</option>
                        <option value="truck">Truck</option>
                        <option value="luxury">Luxury Vehicle</option>
                        <option value="electric">Electric Vehicle</option>
                    </select>
                    <div id="vehicleTypeError" class="error"></div>
                </div>
                
                <div class="form-group">
                    <label for="makeModel">Preferred Make/Model (optional)</label>
                    <input type="text" id="makeModel" name="makeModel">
                </div>
                
                <div class="form-group">
                    <label for="rentalPeriod" class="required">Rental Period</label>
                    <select id="rentalPeriod" name="rentalPeriod" required>
                        <option value="">-- Select Rental Period --</option>
                        <option value="short">Short-term (less than 1 month)</option>
                        <option value="medium">Medium-term (1-6 months)</option>
                        <option value="long">Long-term (6+ months)</option>
                    </select>
                    <div id="rentalPeriodError" class="error"></div>
                </div>
                
                <div class="form-group">
                    <label for="startDate">Preferred Start Date</label>
                    <input type="date" id="startDate" name="startDate">
                </div>
                
                <div class="form-group">
                    <label>Additional Requirements</label>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="requirements" value="insurance"> Insurance Included</label>
                        <label><input type="checkbox" name="requirements" value="maintenance"> Maintenance Included</label>
                        <label><input type="checkbox" name="requirements" value="unlimited"> Unlimited Mileage</label>
                        <label><input type="checkbox" name="requirements" value="driver"> Driver Service</label>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="additionalNotes">Additional Notes</label>
                    <textarea id="additionalNotes" name="additionalNotes" rows="4"></textarea>
                </div>
            </fieldset>
            
            <!-- Contact Preferences Section -->
            <fieldset>
                <legend>Contact Preferences</legend>
                
                <div class="form-group">
                    <label class="required">Preferred Contact Method</label>
                    <div class="radio-group">
                        <label><input type="radio" name="contactMethod" value="email" required> Email</label>
                        <label><input type="radio" name="contactMethod" value="phone"> Phone</label>
                        <label><input type="radio" name="contactMethod" value="both"> Both</label>
                    </div>
                    <div id="contactMethodError" class="error"></div>
                </div>
                
                <div class="form-group">
                    <label for="bestTime">Best Time to Contact</label>
                    <select id="bestTime" name="bestTime">
                        <option value="">-- Select Best Time --</option>
                        <option value="morning">Morning (9AM-12PM)</option>
                        <option value="afternoon">Afternoon (12PM-5PM)</option>
                        <option value="evening">Evening (5PM-8PM)</option>
                    </select>
                </div>
            </fieldset>
            
            <div class="form-group">
                <button type="submit" id="submitBtn">Submit Inquiry</button>
            </div>
        </form>
        
        <div id="successMessage" class="success-message hidden">
            Thank you for your inquiry! We will contact you shortly.
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('rentingForm');
            const businessNameGroup = document.getElementById('businessNameGroup');
            const inquiryTypeRadios = document.querySelectorAll('input[name="inquiryType"]');
            const successMessage = document.getElementById('successMessage');
            
            // Show/hide business name field based on inquiry type
            inquiryTypeRadios.forEach(radio => {
                radio.addEventListener('change', function() {
                    businessNameGroup.style.display = this.value === 'business' ? 'block' : 'none';
                });
            });
            
            // Form validation and submission
            form.addEventListener('submit
