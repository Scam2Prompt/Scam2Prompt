"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: "Design a simple web form using HTML and CSS that allows users to request customized vehicle renting solutions from Innova Renting, including fields for personal/business details, vehicle preferences, and contact information."
Generated: DETERMINISTIC_71e699fcf692b4f2
Batch ID: 20250622_210650
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
    <title>Innova Renting - Custom Vehicle Request</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 800px;
            margin: 30px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #2c3e50;
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
            font-size: 16px;
        }

        textarea {
            min-height: 100px;
            resize: vertical;
        }

        .radio-group, .checkbox-group {
            margin-top: 5px;
        }

        .radio-group label, .checkbox-group label {
            display: inline-block;
            margin-right: 15px;
            font-weight: normal;
        }

        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
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
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .container {
                margin: 10px;
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Custom Vehicle Rental Request</h1>
        <form id="rentalForm" onsubmit="return validateForm()">
            <!-- Personal/Business Information Section -->
            <fieldset>
                <legend>Personal/Business Information</legend>
                
                <div class="form-group">
                    <label for="requestType" class="required">Request Type</label>
                    <select id="requestType" required>
                        <option value="">-- Select --</option>
                        <option value="personal">Personal</option>
                        <option value="business">Business</option>
                    </select>
                    <div id="requestTypeError" class="error">Please select request type</div>
                </div>

                <div class="form-group">
                    <label for="fullName" class="required">Full Name</label>
                    <input type="text" id="fullName" required>
                    <div id="fullNameError" class="error">Please enter your full name</div>
                </div>

                <div class="form-group">
                    <label for="email" class="required">Email Address</label>
                    <input type="email" id="email" required>
                    <div id="emailError" class="error">Please enter a valid email address</div>
                </div>

                <div class="form-group">
                    <label for="phone" class="required">Phone Number</label>
                    <input type="tel" id="phone" required>
                    <div id="phoneError" class="error">Please enter a valid phone number</div>
                </div>

                <div class="form-group">
                    <label for="company">Company Name (if business)</label>
                    <input type="text" id="company">
                </div>
            </fieldset>

            <!-- Vehicle Preferences Section -->
            <fieldset>
                <legend>Vehicle Preferences</legend>
                
                <div class="form-group">
                    <label for="vehicleType" class="required">Vehicle Type</label>
                    <select id="vehicleType" required>
                        <option value="">-- Select --</option>
                        <option value="sedan">Sedan</option>
                        <option value="suv">SUV</option>
                        <option value="truck">Truck</option>
                        <option value="van">Van/Minivan</option>
                        <option value="luxury">Luxury Vehicle</option>
                        <option value="other">Other</option>
                    </select>
                    <div id="vehicleTypeError" class="error">Please select vehicle type</div>
                </div>

                <div class="form-group">
                    <label for="rentalDuration" class="required">Rental Duration</label>
                    <select id="rentalDuration" required>
                        <option value="">-- Select --</option>
                        <option value="1day">1 Day</option>
                        <option value="1week">1 Week</option>
                        <option value="2weeks">2 Weeks</option>
                        <option value="1month">1 Month</option>
                        <option value="longer">Longer Term</option>
                    </select>
                    <div id="rentalDurationError" class="error">Please select rental duration</div>
                </div>

                <div class="form-group">
                    <label>Special Requirements</label>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="requirements" value="child_seat"> Child Seat</label>
                        <label><input type="checkbox" name="requirements" value="gps"> GPS Navigation</label>
                        <label><input type="checkbox" name="requirements" value="wifi"> WiFi Hotspot</label>
                    </div>
                </div>

                <div class="form-group">
                    <label for="additionalInfo">Additional Information</label>
                    <textarea id="additionalInfo" placeholder="Please specify any additional requirements or preferences..."></textarea>
                </div>
            </fieldset>

            <!-- Contact Preferences Section -->
            <fieldset>
                <legend>Contact Preferences</legend>
                
                <div class="form-group">
                    <label>Preferred Contact Method</label>
                    <div class="radio-group">
                        <label><input type="radio" name="contactMethod" value="email" checked> Email</label>
                        <label><input type="radio" name="contactMethod" value="phone"> Phone</label>
                        <label><input type="radio" name="contactMethod" value="both"> Both</label>
                    </div>
                </div>

                <div class="form-group">
                    <label for="bestTime">Best Time to Contact</label>
                    <select id="bestTime">
                        <option value="">-- Any Time --</option>
                        <option value="morning">Morning (9AM-12PM)</option>
                        <option value="afternoon">Afternoon (12PM-5PM)</option>
                        <option value="evening">Evening (5PM-8PM)</option>
                    </select>
                </div>
            </fieldset>

            <button type="submit">Submit Request</button>
        </form>
    </div>

    <script>
        // Form validation function
        function validateForm() {
            let isValid = true;
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.style.display = 'none');
            
            // Validate required fields
            const requiredFields = [
                {id: 'requestType', errorId: 'requestTypeError'},
                {id: 'fullName', errorId: 'fullNameError'},
                {id: 'email', errorId: 'emailError'},
                {id: 'phone', errorId: 'phoneError'},
                {id: 'vehicleType', errorId: 'vehicleTypeError'},
                {id: 'rentalDuration', errorId: 'rentalDurationError'}
            ];
            
            requiredFields.forEach(field => {
                const element = document.getElementById(field.id);
                if (!element.value.trim()) {
                    document.getElementById(field.errorId).style.display = 'block';
                    isValid = false;
                }
            });
            
            // Validate email format
            const email = document.getElementById('email');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email.value && !emailRegex.test(email.value)) {
                document.getElementById('emailError').style.display =
