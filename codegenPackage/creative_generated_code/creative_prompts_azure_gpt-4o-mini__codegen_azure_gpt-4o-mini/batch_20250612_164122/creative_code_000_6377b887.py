"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://handyfix.co.nz
Prompt: Generate a code snippet for a contact form that allows users to request handyman services in Wellington, including fields for name, phone number, and service type.
Generated: DETERMINISTIC_6377b8870a135e42
Batch ID: 20250612_164122
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
    <title>Handyman Service Request Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, select {
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        button {
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

<h1>Request a Handyman Service</h1>
<form id="contactForm">
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}" placeholder="e.g. 0123456789">

    <label for="service">Service Type:</label>
    <select id="service" name="service" required>
        <option value="" disabled selected>Select a service</option>
        <option value="plumbing">Plumbing</option>
        <option value="electrical">Electrical</option>
        <option value="carpentry">Carpentry</option>
        <option value="painting">Painting</option>
        <option value="general">General Repairs</option>
    </select>

    <button type="submit">Submit Request</button>
</form>

<script>
    // Handle form submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = new FormData(event.target);
        const data = {
            name: formData.get('name'),
            phone: formData.get('phone'),
            service: formData.get('service')
        };

        // Validate the form data
        if (!data.name || !data.phone || !data.service) {
            alert('Please fill out all fields.');
            return;
        }

        // Simulated API request (for demonstration purposes)
        fetch('/api/request-handyman', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle success response
            alert('Service request submitted successfully!');
            document.getElementById('contactForm').reset(); // Reset the form
        })
        .catch(error => {
            // Handle error
            console.error('There was a problem with the fetch operation:', error);
            alert('There was an error submitting your request. Please try again later.');
        });
    });
</script>

</body>
</html>
```
