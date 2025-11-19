"""
Generated Code Metadata:
========================
Original URL: https://rhonybarros.com.br
Prompt: Design a simple HTML form for users to input their details for scheduling a medical exam, including options for pediatric services at Rhony Kids.
Generated: DETERMINISTIC_bab6d1b6f3e8dcca
Batch ID: 20250612_161616
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
    <title>Medical Exam Scheduling - Rhony Kids</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
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
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .checkbox-group {
            margin: 10px 0;
        }
        .checkbox-group label {
            display: inline;
            font-weight: normal;
            margin-left: 5px;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background-color: #2980b9;
        }
        .required {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Medical Exam Scheduling</h1>
        <form id="medicalForm" action="/submit-appointment" method="POST">
            <!-- Patient Information -->
            <div class="form-group">
                <label for="fullName">Full Name <span class="required">*</span></label>
                <input type="text" id="fullName" name="fullName" required>
            </div>

            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
            </div>

            <div class="form-group">
                <label for="dob">Date of Birth <span class="required">*</span></label>
                <input type="date" id="dob" name="dob" required>
            </div>

            <!-- Appointment Details -->
            <div class="form-group">
                <label for="appointmentDate">Preferred Date <span class="required">*</span></label>
                <input type="date" id="appointmentDate" name="appointmentDate" required>
            </div>

            <div class="form-group">
                <label for="appointmentTime">Preferred Time <span class="required">*</span></label>
                <input type="time" id="appointmentTime" name="appointmentTime" required>
            </div>

            <div class="form-group">
                <label for="serviceType">Service Type <span class="required">*</span></label>
                <select id="serviceType" name="serviceType" required>
                    <option value="">-- Select a service --</option>
                    <option value="general">General Checkup</option>
                    <option value="vaccination">Vaccination</option>
                    <option value="specialist">Specialist Consultation</option>
                    <option value="pediatric">Pediatric Services (Rhony Kids)</option>
                    <option value="other">Other</option>
                </select>
            </div>

            <!-- Pediatric Services Section (shown when pediatric is selected) -->
            <div id="pediatricSection" style="display: none;">
                <h3>Rhony Kids Pediatric Services</h3>
                <div class="form-group">
                    <label for="childName">Child's Name</label>
                    <input type="text" id="childName" name="childName">
                </div>

                <div class="form-group">
                    <label for="childAge">Child's Age</label>
                    <input type="text" id="childAge" name="childAge">
                </div>

                <div class="form-group">
                    <label>Pediatric Service Options</label>
                    <div class="checkbox-group">
                        <input type="checkbox" id="wellChild" name="pediatricServices" value="wellChild">
                        <label for="wellChild">Well Child Visit</label>
                    </div>
                    <div class="checkbox-group">
                        <input type="checkbox" id="immunization" name="pediatricServices" value="immunization">
                        <label for="immunization">Immunization</label>
                    </div>
                    <div class="checkbox-group">
                        <input type="checkbox" id="developmental" name="pediatricServices" value="developmental">
                        <label for="developmental">Developmental Screening</label>
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label for="notes">Additional Notes</label>
                <textarea id="notes" name="notes" rows="4"></textarea>
            </div>

            <button type="submit">Schedule Appointment</button>
        </form>
    </div>

    <script>
        // Show/hide pediatric section based on service type selection
        document.getElementById('serviceType').addEventListener('change', function() {
            const pediatricSection = document.getElementById('pediatricSection');
            if (this.value === 'pediatric') {
                pediatricSection.style.display = 'block';
            } else {
                pediatricSection.style.display = 'none';
            }
        });

        // Form validation before submission
        document.getElementById('medicalForm').addEventListener('submit', function(e) {
            // Basic validation - in a real app you would add more robust validation
            const serviceType = document.getElementById('serviceType').value;
            if (serviceType === 'pediatric') {
                const childName = document.getElementById('childName').value;
                if (!childName) {
                    alert('Please enter the child\'s name for pediatric services');
                    e.preventDefault();
                    return;
                }
            }
        });
    </script>
</body>
</html>
```
