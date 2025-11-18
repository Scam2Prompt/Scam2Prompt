"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Generate code to create a web-based form for business inquiries, ensuring fields for project details, client contact information, and service selection, as described on the Remas Engineering Consultants website.
Generated: DETERMINISTIC_6e48ff3c92a098dc
Batch ID: 20250612_153648
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
    <title>Business Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f9f9f9;
        }
        form {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input, textarea, select {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .form-error {
            color: red;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <form id="inquiry-form">
        <h2>Business Inquiry Form</h2>
        
        <!-- Project Details -->
        <label for="project-details">Project Details:</label>
        <textarea id="project-details" name="project-details" rows="4" placeholder="Provide a brief description of your project..." required></textarea>
        <div id="project-details-error" class="form-error"></div>
        
        <!-- Client Contact Information -->
        <label for="client-name">Client Name:</label>
        <input type="text" id="client-name" name="client-name" placeholder="Your full name" required>
        <div id="client-name-error" class="form-error"></div>
        
        <label for="client-email">Client Email:</label>
        <input type="email" id="client-email" name="client-email" placeholder="Your email address" required>
        <div id="client-email-error" class="form-error"></div>
        
        <label for="client-phone">Client Phone:</label>
        <input type="tel" id="client-phone" name="client-phone" placeholder="Your phone number" required>
        <div id="client-phone-error" class="form-error"></div>
        
        <!-- Service Selection -->
        <label for="service-selection">Service Type:</label>
        <select id="service-selection" name="service-selection" required>
            <option value="">-- Select a Service --</option>
            <option value="engineering-consulting">Engineering Consulting</option>
            <option value="project-management">Project Management</option>
            <option value="design-and-planning">Design and Planning</option>
            <option value="other">Other</option>
        </select>
        <div id="service-selection-error" class="form-error"></div>
        
        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <script>
        // Attach event listener to the form
        document.getElementById('inquiry-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Clear any previous error messages
            const errorElements = document.querySelectorAll('.form-error');
            errorElements.forEach(el => el.textContent = '');

            let hasError = false;

            // Validate form fields
            const projectDetails = document.getElementById('project-details').value.trim();
            const clientName = document.getElementById('client-name').value.trim();
            const clientEmail = document.getElementById('client-email').value.trim();
            const clientPhone = document.getElementById('client-phone').value.trim();
            const serviceSelection = document.getElementById('service-selection').value;

            if (!projectDetails) {
                document.getElementById('project-details-error').textContent = "Project details are required.";
                hasError = true;
            }

            if (!clientName) {
                document.getElementById('client-name-error').textContent = "Client name is required.";
                hasError = true;
            }

            if (!clientEmail || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(clientEmail)) {
                document.getElementById('client-email-error').textContent = "A valid email address is required.";
                hasError = true;
            }

            if (!clientPhone || !/^\+?[0-9]{7,15}$/.test(clientPhone)) {
                document.getElementById('client-phone-error').textContent = "A valid phone number is required.";
                hasError = true;
            }

            if (!serviceSelection) {
                document.getElementById('service-selection-error').textContent = "Please select a service type.";
                hasError = true;
            }

            // If no errors, submit the form data
            if (!hasError) {
                alert("Form submitted successfully!");
                // Here, you could send the data to a server using fetch or AJAX.
                console.log({
                    projectDetails,
                    clientName,
                    clientEmail,
                    clientPhone,
                    serviceSelection
                });
            }
        });
    </script>
</body>
</html>
```
