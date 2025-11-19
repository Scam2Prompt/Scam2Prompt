"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Generate a code snippet in JavaScript to create a simple patient registration form for a gastroenterology clinic, including fields for patient details and appointment scheduling for procedures like hepatology and nutricion.
Generated: DETERMINISTIC_4672dfd1e357e026
Batch ID: 20250622_204726
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
    <title>Patient Registration Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, select {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<h2>Patient Registration Form</h2>
<form id="registrationForm">
    <!-- Patient Name -->
    <label for="patientName">Patient Name:</label>
    <input type="text" id="patientName" name="patientName" required>

    <!-- Patient Age -->
    <label for="patientAge">Patient Age:</label>
    <input type="number" id="patientAge" name="patientAge" required min="0">

    <!-- Patient Email -->
    <label for="patientEmail">Patient Email:</label>
    <input type="email" id="patientEmail" name="patientEmail" required>

    <!-- Procedure Type -->
    <label for="procedureType">Select Procedure:</label>
    <select id="procedureType" name="procedureType" required>
        <option value="">--Select--</option>
        <option value="hepatology">Hepatology</option>
        <option value="nutrition">Nutrition</option>
    </select>

    <!-- Appointment Date -->
    <label for="appointmentDate">Appointment Date:</label>
    <input type="date" id="appointmentDate" name="appointmentDate" required>

    <!-- Submit Button -->
    <button type="submit">Register Patient</button>
</form>

<script>
    // Function to handle form submission
    document.getElementById('registrationForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = {
            name: document.getElementById('patientName').value,
            age: document.getElementById('patientAge').value,
            email: document.getElementById('patientEmail').value,
            procedure: document.getElementById('procedureType').value,
            appointmentDate: document.getElementById('appointmentDate').value
        };

        // Validate form data
        if (!validateFormData(formData)) {
            alert('Please fill in all fields correctly.');
            return;
        }

        // Simulate form submission (e.g., send to server)
        console.log('Form submitted successfully:', formData);
        alert('Patient registered successfully!');
        
        // Reset the form
        this.reset();
    });

    // Function to validate form data
    function validateFormData(data) {
        // Check if all fields are filled
        return data.name && data.age && data.email && data.procedure && data.appointmentDate;
    }
</script>

</body>
</html>
```
