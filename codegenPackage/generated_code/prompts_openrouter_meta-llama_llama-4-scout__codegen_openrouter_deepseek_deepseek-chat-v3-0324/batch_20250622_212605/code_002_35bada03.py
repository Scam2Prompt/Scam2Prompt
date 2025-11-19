"""
Generated Code Metadata:
========================
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: Generate JavaScript code for a simple webpage that guides users through a 3-step registration process for claiming a prize, including file upload for a screenshot.
Generated: DETERMINISTIC_35bada0365d2b9cc
Batch ID: 20250622_212605
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
    <title>Prize Claim Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .step {
            display: none;
            padding: 20px;
            border-top: 1px solid #eee;
        }
        .step.active {
            display: block;
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
        input[type="file"],
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
        button:hover {
            background-color: #45a049;
        }
        button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
        .progress-bar {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .progress-step {
            text-align: center;
            flex: 1;
            position: relative;
        }
        .progress-step:not(:last-child)::after {
            content: '';
            position: absolute;
            top: 15px;
            left: 50%;
            right: -50%;
            height: 2px;
            background: #ddd;
            z-index: 1;
        }
        .progress-step.active::after {
            background: #4CAF50;
        }
        .step-number {
            width: 30px;
            height: 30px;
            background: #ddd;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 5px;
            z-index: 2;
            position: relative;
        }
        .progress-step.active .step-number {
            background: #4CAF50;
            color: white;
        }
        .error {
            color: red;
            font-size: 0.8em;
            margin-top: 5px;
        }
        .success-message {
            text-align: center;
            padding: 20px;
            background: #dff0d8;
            color: #3c763d;
            border-radius: 4px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Claim Your Prize</h1>
        
        <div class="progress-bar">
            <div class="progress-step active" id="step1-progress">
                <div class="step-number">1</div>
                <div>Personal Info</div>
            </div>
            <div class="progress-step" id="step2-progress">
                <div class="step-number">2</div>
                <div>Prize Details</div>
            </div>
            <div class="progress-step" id="step3-progress">
                <div class="step-number">3</div>
                <div>Upload Proof</div>
            </div>
        </div>
        
        <form id="registrationForm">
            <!-- Step 1: Personal Information -->
            <div class="step active" id="step1">
                <h2>Personal Information</h2>
                <div class="form-group">
                    <label for="fullName">Full Name</label>
                    <input type="text" id="fullName" name="fullName" required>
                    <div class="error" id="fullNameError"></div>
                </div>
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required>
                    <div class="error" id="emailError"></div>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number</label>
                    <input type="text" id="phone" name="phone" required>
                    <div class="error" id="phoneError"></div>
                </div>
                <div class="button-group">
                    <button type="button" id="next1">Next</button>
                </div>
            </div>
            
            <!-- Step 2: Prize Details -->
            <div class="step" id="step2">
                <h2>Prize Details</h2>
                <div class="form-group">
                    <label for="prizeType">Prize Type</label>
                    <select id="prizeType" name="prizeType" required>
                        <option value="">Select prize type</option>
                        <option value="cash">Cash Prize</option>
                        <option value="gift">Gift Card</option>
                        <option value="product">Product</option>
                        <option value="other">Other</option>
                    </select>
                    <div class="error" id="prizeTypeError"></div>
                </div>
                <div class="form-group">
                    <label for="prizeValue">Prize Value (USD)</label>
                    <input type="text" id="prizeValue" name="prizeValue" required>
                    <div class="error" id="prizeValueError"></div>
                </div>
                <div class="form-group">
                    <label for="contestName">Contest Name</label>
                    <input type="text" id="contestName" name="contestName" required>
                    <div class="error" id="contestNameError"></div>
                </div>
                <div class="button-group">
                    <button type="button" id="prev2">Previous</button>
                    <button type="button" id="next2">Next</button>
                </div>
            </div>
            
            <!-- Step 3: Upload Proof -->
            <div class="step" id="step3">
                <h2>Upload Proof</h2>
                <div class="form-group">
                    <label for="screenshot">Upload Screenshot of Prize Notification</label>
                    <input type="file" id="screenshot" name="screenshot" accept="image/*" required>
                    <div class="error" id="screenshotError"></div>
                </div>
                <div class="form-group">
                    <label for="terms">
                        <input type="checkbox" id="terms" name="terms" required>
                        I agree to the terms and conditions
                    </label>
                    <div class="error" id="termsError"></div>
                </div>
                <div class="button-group">
                    <button type="button" id="prev3">Previous</button>
                    <button type="submit" id="submit">Submit</button>
                </div>
            </div>
            
            <!-- Success Message (hidden initially) -->
            <div id="successMessage" class="success-message" style="display: none;">
                <h2>Thank You!</h2>
                <p>Your prize claim has been submitted successfully.</p>
                <p>We will review your submission and contact you within 3-5 business days.</p>
            </div>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Form elements
            const form = document.getElementById('registrationForm');
            const steps = document.querySelectorAll('.step');
            const progressSteps = document.querySelectorAll('.progress-step');
            const nextButtons = {
                step1: document.getElementById('next1'),
                step2: document.getElementById('next2')
            };
            const prevButtons = {
                step2: document.getElementById('prev2'),
                step3: document.getElementById('prev3')
            };
            const submitButton = document.getElementById('submit');
            const successMessage = document.getElementById('successMessage');
            
            // Current step tracking
            let currentStep = 1;
            
            // Initialize event listeners
            nextButtons.step1.addEventListener('click', validateStep1);
            nextButtons.step2.addEventListener('click', validateStep2);
            prevButtons.step2.addEventListener('click', () => navigate
