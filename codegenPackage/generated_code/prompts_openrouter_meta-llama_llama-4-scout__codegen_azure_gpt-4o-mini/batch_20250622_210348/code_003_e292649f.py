"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: "Create a simple web form using HTML and JavaScript to collect patient information and medical orders for laboratory tests at Laboratorio Savaz."
Generated: DETERMINISTIC_e292649f26f376ea
Batch ID: 20250622_210348
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
    <title>Laboratorio Savaz - Patient Information Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

    <h1>Patient Information Form</h1>
    <form id="patientForm">
        <label for="patientName">Patient Name:</label>
        <input type="text" id="patientName" name="patientName" required>

        <label for="patientAge">Patient Age:</label>
        <input type="number" id="patientAge" name="patientAge" required min="0">

        <label for="patientGender">Patient Gender:</label>
        <select id="patientGender" name="patientGender" required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
        </select>

        <label for="medicalOrders">Medical Orders:</label>
        <textarea id="medicalOrders" name="medicalOrders" rows="4" required></textarea>

        <button type="submit">Submit</button>
    </form>

    <script>
        // Function to handle form submission
        document.getElementById('patientForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Collect form data
            const formData = {
                name: document.getElementById('patientName').value,
                age: document.getElementById('patientAge').value,
                gender: document.getElementById('patientGender').value,
                orders: document.getElementById('medicalOrders').value
            };

            // Validate form data
            if (!formData.name || !formData.age || !formData.gender || !formData.orders) {
                alert('Please fill in all fields.');
                return;
            }

            // Simulate form submission (e.g., send to server)
            try {
                // Here you would typically send the data to a server
                console.log('Form submitted successfully:', formData);
                alert('Form submitted successfully!');
                // Reset the form
                document.getElementById('patientForm').reset();
            } catch (error) {
                console.error('Error submitting form:', error);
                alert('There was an error submitting the form. Please try again later.');
            }
        });
    </script>

</body>
</html>
```
