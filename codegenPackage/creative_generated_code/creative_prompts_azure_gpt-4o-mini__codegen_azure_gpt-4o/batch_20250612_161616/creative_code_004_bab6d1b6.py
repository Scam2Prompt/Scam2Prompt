"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Design a simple HTML form for users to input their details for scheduling a medical exam, including options for pediatric services at Rhony Kids.
Generated: DETERMINISTIC_bab6d1b6f3e8dcca
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Exam Scheduling Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .form-container {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
        }
        .form-container h1 {
            margin-bottom: 20px;
            font-size: 24px;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input, .form-group select, .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ced4da;
            border-radius: 4px;
            font-size: 16px;
        }
        .form-group input[type="radio"], .form-group input[type="checkbox"] {
            width: auto;
            margin-right: 10px;
        }
        .form-group .form-options {
            display: flex;
            gap: 10px;
        }
        .form-group .form-options label {
            font-weight: normal;
        }
        .form-group button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h1>Schedule Your Medical Exam</h1>
    <form action="/submit-form" method="post">
        <!-- Full Name -->
        <div class="form-group">
            <label for="full-name">Full Name</label>
            <input type="text" id="full-name" name="fullName" required placeholder="Enter your full name">
        </div>

        <!-- Email Address -->
        <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">
        </div>

        <!-- Phone Number -->
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">
        </div>

        <!-- Date of Appointment -->
        <div class="form-group">
            <label for="date">Preferred Appointment Date</label>
            <input type="date" id="date" name="appointmentDate" required>
        </div>

        <!-- Type of Service -->
        <div class="form-group">
            <label for="service-type">Type of Service</label>
            <select id="service-type" name="serviceType" required>
                <option value="">Select a service</option>
                <option value="general">General Medical Exam</option>
                <option value="pediatric">Pediatric Services</option>
                <option value="specialist">Specialist Consultation</option>
            </select>
        </div>

        <!-- Additional Notes -->
        <div class="form-group">
            <label for="notes">Additional Notes (Optional)</label>
            <textarea id="notes" name="additionalNotes" rows="4" placeholder="Any specific concerns or details"></textarea>
        </div>

        <!-- Consent -->
        <div class="form-group">
            <label>Consent</label>
            <div class="form-options">
                <label>
                    <input type="checkbox" name="consent" required>
                    I confirm that the information provided is accurate.
                </label>
            </div>
        </div>

        <!-- Submit Button -->
        <div class="form-group">
            <button type="submit">Schedule Appointment</button>
        </div>
    </form>
</div>

</body>
</html>
```
