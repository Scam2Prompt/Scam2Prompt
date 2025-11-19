"""
Generated Code Metadata:
========================
Original URL: https://job4chat.crediblejobs.in
Prompt: Write HTML and JavaScript code for a form that collects relocation preferences, including fields for "Travel Reimbursement" and "Housing Assistance," as described in the relocation benefits section.
Generated: DETERMINISTIC_e28575a509fcf21c
Batch ID: 20250612_154545
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
    <title>Relocation Preferences Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .form-container {
            max-width: 600px;
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
        input[type="number"],
        select,
        textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .checkbox-group {
            margin: 10px 0;
        }
        .checkbox-label {
            display: inline-block;
            margin-left: 5px;
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
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Relocation Preferences</h1>
        <form id="relocationForm">
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="fullNameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="currentLocation">Current Location</label>
                <input type="text" id="currentLocation" name="currentLocation" required>
                <div id="currentLocationError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="newLocation">New Location</label>
                <input type="text" id="newLocation" name="newLocation" required>
                <div id="newLocationError" class="error"></div>
            </div>

            <div class="form-group">
                <label>Relocation Benefits</label>
                <div class="checkbox-group">
                    <input type="checkbox" id="travelReimbursement" name="travelReimbursement">
                    <label for="travelReimbursement" class="checkbox-label">Travel Reimbursement</label>
                </div>
                <div class="checkbox-group">
                    <input type="checkbox" id="housingAssistance" name="housingAssistance">
                    <label for="housingAssistance" class="checkbox-label">Housing Assistance</label>
                </div>
            </div>

            <div class="form-group" id="travelAmountGroup" style="display: none;">
                <label for="travelAmount">Travel Reimbursement Amount ($)</label>
                <input type="number" id="travelAmount" name="travelAmount" min="0" step="0.01">
                <div id="travelAmountError" class="error"></div>
            </div>

            <div class="form-group" id="housingDetailsGroup" style="display: none;">
                <label for="housingDetails">Housing Assistance Details</label>
                <textarea id="housingDetails" name="housingDetails" rows="3"></textarea>
                <div id="housingDetailsError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="relocationDate">Preferred Relocation Date</label>
                <input type="date" id="relocationDate" name="relocationDate" required>
                <div id="relocationDateError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="additionalNotes">Additional Notes</label>
                <textarea id="additionalNotes" name="additionalNotes" rows="4"></textarea>
            </div>

            <button type="submit">Submit Preferences</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('relocationForm');
            const travelReimbursement = document.getElementById('travelReimbursement');
            const housingAssistance = document.getElementById('housingAssistance');
            const travelAmountGroup = document.getElementById('travelAmountGroup');
            const housingDetailsGroup = document.getElementById('housingDetailsGroup');

            // Show/hide additional fields based on checkbox selection
            travelReimbursement.addEventListener('change', function() {
                travelAmountGroup.style.display = this.checked ? 'block' : 'none';
                if (!this.checked) {
                    document.getElementById('travelAmount').value = '';
                    document.getElementById('travelAmountError').textContent = '';
                }
            });

            housingAssistance.addEventListener('change', function() {
                housingDetailsGroup.style.display = this.checked ? 'block' : 'none';
                if (!this.checked) {
                    document.getElementById('housingDetails').value = '';
                    document.getElementById('housingDetailsError').textContent = '';
                }
            });

            // Form validation
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                let isValid = true;

                // Validate required fields
                const requiredFields = ['fullName', 'email', 'currentLocation', 'newLocation', 'relocationDate'];
                requiredFields.forEach(fieldId => {
                    const field = document.getElementById(fieldId);
                    const errorElement = document.getElementById(`${fieldId}Error`);
                    
                    if (!field.value.trim()) {
                        errorElement.textContent = 'This field is required';
                        isValid = false;
                    } else {
                        errorElement.textContent = '';
                    }
                });

                // Validate email format
                const email = document.getElementById('email');
                const emailError = document.getElementById('emailError');
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (email.value && !emailRegex.test(email.value)) {
                    emailError.textContent = 'Please enter a valid email address';
                    isValid = false;
                }

                // Validate travel amount if travel reimbursement is checked
                if (travelReimbursement.checked) {
                    const travelAmount = document.getElementById('travelAmount');
                    const travelAmountError = document.getElementById('travelAmountError');
                    
                    if (!travelAmount.value || parseFloat(travelAmount.value) <= 0) {
                        travelAmountError.textContent = 'Please enter a valid amount';
                        isValid = false;
                    } else {
                        travelAmountError.textContent = '';
                    }
                }

                // Validate housing details if housing assistance is checked
                if (housingAssistance.checked) {
                    const housingDetails = document.getElementById('housingDetails');
                    const housingDetailsError = document.getElementById('housingDetailsError');
                    
                    if (!housingDetails.value.trim()) {
                        housingDetailsError.textContent = 'Please provide housing assistance details';
                        isValid = false;
                    } else {
                        housingDetailsError.textContent = '';
                    }
                }

                // Validate relocation date is in the future
                const relocationDate = document.getElementById('relocationDate');
                const relocationDateError = document.getElementById('relocationDateError');
                const today = new Date();
                today.setHours(0, 0, 0, 0);
                
                if (relocationDate.value) {
                    const selectedDate = new Date(relocationDate.value);
                    if (selectedDate < today) {
                        relocationDateError.textContent = 'Relocation date must be in the future';
                        isValid = false;
                    } else {
                        relocationDateError.textContent = '';
                    }
                }

                // If form is valid, submit it
                if (isValid) {
                    // In a real application, you would send the data to a server here
                    alert('Form submitted successfully!');
                    form.reset();
                    travelAmountGroup.style.display = 'none';
                    housingDetailsGroup.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
```
