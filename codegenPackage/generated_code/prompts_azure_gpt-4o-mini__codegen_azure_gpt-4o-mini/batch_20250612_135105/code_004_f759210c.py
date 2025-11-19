"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Develop a web form for clients to request HVAC cleaning services, ensuring it captures necessary details as outlined by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_f759210cf71df072
Batch ID: 20250612_135105
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
    <title>HVAC Cleaning Service Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>HVAC Cleaning Service Request</h1>
    <form id="serviceRequestForm" action="/submit-request" method="POST">
        <!-- Client's Name -->
        <label for="clientName">Full Name:</label>
        <input type="text" id="clientName" name="clientName" required>
        
        <!-- Client's Email -->
        <label for="clientEmail">Email:</label>
        <input type="email" id="clientEmail" name="clientEmail" required>
        
        <!-- Client's Phone Number -->
        <label for="clientPhone">Phone Number:</label>
        <input type="tel" id="clientPhone" name="clientPhone" required>
        
        <!-- Service Address -->
        <label for="serviceAddress">Service Address:</label>
        <input type="text" id="serviceAddress" name="serviceAddress" required>
        
        <!-- Preferred Date -->
        <label for="preferredDate">Preferred Date:</label>
        <input type="date" id="preferredDate" name="preferredDate" required>
        
        <!-- Additional Comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4"></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Request Service</button>
    </form>

    <script>
        // Form submission handler
        document.getElementById('serviceRequestForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Validate form data
            const formData = new FormData(this);
            const requestData = {};
            formData.forEach((value, key) => {
                requestData[key] = value;
            });

            // Send data to the server
            fetch('/submit-request', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert('Service request submitted successfully!');
                this.reset(); // Reset the form after successful submission
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your request. Please try again later.');
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the form */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
