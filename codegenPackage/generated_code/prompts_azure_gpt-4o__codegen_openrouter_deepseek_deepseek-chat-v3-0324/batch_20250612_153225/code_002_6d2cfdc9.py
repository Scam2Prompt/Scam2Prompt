"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Generate code to create a web form for scheduling a polygraph test appointment, including fields for selecting test types like fidelity tests, fraud investigations, or legal cases, as mentioned on the Euro Poligraf Center website.
Generated: DETERMINISTIC_6d2cfdc93e535d25
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
    <title>Polygraph Test Appointment - Euro Poligraf Center</title>
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
        input[type="date"],
        input[type="time"],
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
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Schedule a Polygraph Test Appointment</h1>
        <form id="appointmentForm" onsubmit="return validateForm()">
            <!-- Personal Information -->
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

            <!-- Appointment Details -->
            <div class="form-group">
                <label for="testType" class="required">Test Type</label>
                <select id="testType" name="testType" required>
                    <option value="">-- Select Test Type --</option>
                    <option value="fidelity">Fidelity Test</option>
                    <option value="fraud">Fraud Investigation</option>
                    <option value="legal">Legal Case</option>
                    <option value="pre_employment">Pre-Employment Screening</option>
                    <option value="other">Other (Please Specify)</option>
                </select>
                <div id="testTypeError" class="error"></div>
            </div>

            <div class="form-group" id="otherTestTypeContainer" style="display: none;">
                <label for="otherTestType">Specify Test Type</label>
                <input type="text" id="otherTestType" name="otherTestType">
            </div>

            <div class="form-group">
                <label for="appointmentDate" class="required">Preferred Date</label>
                <input type="date" id="appointmentDate" name="appointmentDate" required>
                <div id="dateError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="appointmentTime" class="required">Preferred Time</label>
                <input type="time" id="appointmentTime" name="appointmentTime" required>
                <div id="timeError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="additionalInfo">Additional Information</label>
                <textarea id="additionalInfo" name="additionalInfo" placeholder="Please provide any additional details about your case or special requirements"></textarea>
            </div>

            <button type="submit">Schedule Appointment</button>
        </form>
    </div>

    <script>
        // Show/hide other test type field based on selection
        document.getElementById('testType').addEventListener('change', function() {
            const otherTestTypeContainer = document.getElementById('otherTestTypeContainer');
            if (this.value === 'other') {
                otherTestTypeContainer.style.display = 'block';
            } else {
                otherTestTypeContainer.style.display = 'none';
            }
        });

        // Form validation function
        function validateForm() {
            let isValid = true;
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');

            // Validate full name
            const fullName = document.getElementById('fullName').value.trim();
            if (!fullName) {
                document.getElementById('fullNameError').textContent = 'Full name is required';
                isValid = false;
            }

            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('emailError').textContent = 'Email is required';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address';
                isValid = false;
            }

            // Validate phone
            const phone = document.getElementById('phone').value.trim();
            if (!phone) {
                document.getElementById('phoneError').textContent = 'Phone number is required';
                isValid = false;
            } else if (!/^[\d\s\-+()]{10,}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                isValid = false;
            }

            // Validate test type
            const testType = document.getElementById('testType').value;
            if (!testType) {
                document.getElementById('testTypeError').textContent = 'Please select a test type';
                isValid = false;
            }

            // Validate date
            const appointmentDate = document.getElementById('appointmentDate').value;
            if (!appointmentDate) {
                document.getElementById('dateError').textContent = 'Please select a date';
                isValid = false;
            } else {
                const selectedDate = new Date(appointmentDate);
                const today = new Date();
                today.setHours(0, 0, 0, 0);
                if (selectedDate < today) {
                    document.getElementById('dateError').textContent = 'Date cannot be in the past';
                    isValid = false;
                }
            }

            // Validate time
            const appointmentTime = document.getElementById('appointmentTime').value;
            if (!appointmentTime) {
                document.getElementById('timeError').textContent = 'Please select a time';
                isValid = false;
            }

            if (isValid) {
                // In a real application, you would submit the form to a server here
                alert('Appointment request submitted successfully! We will contact you shortly to confirm.');
                document.getElementById('appointmentForm').reset();
            }

            return false; // Prevent actual form submission for this demo
        }
    </script>
</body>
</html>
```
