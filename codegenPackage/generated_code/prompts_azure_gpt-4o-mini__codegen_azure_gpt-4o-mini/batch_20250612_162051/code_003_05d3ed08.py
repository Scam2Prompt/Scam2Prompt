"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Develop a simple web form that collects user information for solar consultation, similar to the form provided by PowerFive Solar, ensuring it captures property type and roof type.
Generated: DETERMINISTIC_05d3ed08e3c9da22
Batch ID: 20250612_162051
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
    <title>Solar Consultation Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Solar Consultation Request</h1>
        <form id="consultationForm" action="/submit" method="POST">
            <!-- User's name input -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <!-- User's email input -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <!-- User's phone number input -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <!-- Property type selection -->
            <label for="propertyType">Property Type:</label>
            <select id="propertyType" name="propertyType" required>
                <option value="" disabled selected>Select your property type</option>
                <option value="Residential">Residential</option>
                <option value="Commercial">Commercial</option>
                <option value="Industrial">Industrial</option>
            </select>

            <!-- Roof type selection -->
            <label for="roofType">Roof Type:</label>
            <select id="roofType" name="roofType" required>
                <option value="" disabled selected>Select your roof type</option>
                <option value="Flat">Flat</option>
                <option value="Pitched">Pitched</option>
                <option value="Gabled">Gabled</option>
                <option value="Hip">Hip</option>
                <option value="Other">Other</option>
            </select>

            <!-- Submit button -->
            <button type="submit">Request Consultation</button>
        </form>
    </div>

    <script>
        // Form submission event listener
        document.getElementById('consultationForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Gather form data
            const formData = new FormData(this);

            // Send form data to the server
            fetch(this.action, {
                method: this.method,
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Handle success response
                alert('Consultation request submitted successfully!');
                this.reset(); // Reset the form
            })
            .catch(error => {
                // Handle error response
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
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
