"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Develop a web form for planning a visit to a church, incorporating elements from the First Baptist Church's visitor engagement strategies.
Generated: DETERMINISTIC_03a989c713eb66bd
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Church Visit Planning Form

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Baptist Church - Visit Planning Form</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #2a5c84;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
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
            font-size: 16px;
        }
        textarea {
            height: 100px;
        }
        .form-row {
            display: flex;
            gap: 20px;
        }
        .form-row .form-group {
            flex: 1;
        }
        button {
            background-color: #2a5c84;
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
            background-color: #1d4568;
        }
        .required:after {
            content: " *";
            color: red;
        }
        .error-message {
            color: red;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
        .success-message {
            display: none;
            background-color: #dff0d8;
            color: #3c763d;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Plan Your Visit to First Baptist Church</h1>
        
        <div class="success-message" id="successMessage">
            Thank you for planning your visit! We've received your information and will be in touch soon.
        </div>
        
        <form id="visitForm">
            <div class="form-row">
                <div class="form-group">
                    <label for="firstName" class="required">First Name</label>
                    <input type="text" id="firstName" name="firstName" required>
                    <div class="error-message" id="firstNameError">Please enter your first name</div>
                </div>
                <div class="form-group">
                    <label for="lastName" class="required">Last Name</label>
                    <input type="text" id="lastName" name="lastName" required>
                    <div class="error-message" id="lastNameError">Please enter your last name</div>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="email" class="required">Email</label>
                    <input type="email" id="email" name="email" required>
                    <div class="error-message" id="emailError">Please enter a valid email address</div>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number</label>
                    <input type="tel" id="phone" name="phone">
                </div>
            </div>
            
            <div class="form-group">
                <label for="visitDate" class="required">When would you like to visit?</label>
                <input type="date" id="visitDate" name="visitDate" required>
                <div class="error-message" id="visitDateError">Please select a date</div>
            </div>
            
            <div class="form-group">
                <label for="serviceType" class="required">Which service would you like to attend?</label>
                <select id="serviceType" name="serviceType" required>
                    <option value="">Select a service</option>
                    <option value="sunday-morning">Sunday Morning Worship (9:00 AM)</option>
                    <option value="sunday-evening">Sunday Evening Service (6:00 PM)</option>
                    <option value="wednesday-night">Wednesday Night Bible Study (7:00 PM)</option>
                    <option value="special-event">Special Event (Please specify below)</option>
                </select>
                <div class="error-message" id="serviceTypeError">Please select a service</div>
            </div>
            
            <div class="form-group" id="specialEventGroup" style="display: none;">
                <label for="specialEvent">Special Event Details</label>
                <input type="text" id="specialEvent" name="specialEvent">
            </div>
            
            <div class="form-group">
                <label for="groupSize">How many people will be in your group?</label>
                <input type="number" id="groupSize" name="groupSize" min="1" value="1">
            </div>
            
            <div class="form-group">
                <label for="children">Will you be bringing children?</label>
                <select id="children" name="children">
                    <option value="no">No</option>
                    <option value="yes">Yes</option>
                </select>
            </div>
            
            <div class="form-group" id="childrenAgesGroup" style="display: none;">
                <label for="childrenAges">Children's Ages</label>
                <input type="text" id="childrenAges" name="childrenAges" placeholder="e.g. 5, 7, 12">
            </div>
            
            <div class="form-group">
                <label for="questions">Any questions or special requests?</label>
                <textarea id="questions" name="questions"></textarea>
            </div>
            
            <div class="form-group">
                <label for="howHeard">How did you hear about us?</label>
                <select id="howHeard" name="howHeard">
                    <option value="">Select an option</option>
                    <option value="website">Website</option>
                    <option value="friend">Friend/Family</option>
                    <option value="social-media">Social Media</option>
                    <option value="community-event">Community Event</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <button type="submit">Submit Visit Plan</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Show/hide special event field based on service type selection
            const serviceTypeSelect = document.getElementById('serviceType');
            const specialEventGroup = document.getElementById('specialEventGroup');
            
            serviceTypeSelect.addEventListener('change', function() {
                if (this.value === 'special-event') {
                    specialEventGroup.style.display = 'block';
                } else {
                    specialEventGroup.style.display = 'none';
                }
            });
            
            // Show/hide children ages field based on children selection
            const childrenSelect = document.getElementById('children');
            const childrenAgesGroup = document.getElementById('childrenAgesGroup');
            
            childrenSelect.addEventListener('change', function() {
                if (this.value === 'yes') {
                    childrenAgesGroup.style.display = 'block';
                } else {
                    childrenAgesGroup.style.display = 'none';
                }
            });
            
            // Form validation and submission
            const visitForm = document.getElementById('visitForm');
            const successMessage = document.getElementById('successMessage');
            
            visitForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                const errorMessages = document.querySelectorAll('.error-message');
                errorMessages.forEach(msg => msg.style.display = 'none');
                
                let isValid = true;
                
                // Validate required fields
                if (!document.getElementById('firstName').value.trim()) {
                    document.getElementById('firstNameError').style.display = 'block';
                    isValid = false;
                }
                
                if (!document.getElementById('lastName').value.trim()) {
                    document.getElementById('lastNameError').style.display = 'block';
                    isValid = false;
                }
                
                const email = document.getElementById('email').value.trim();
                if (!email || !/^[^\s@]+@[^\s@]+\
