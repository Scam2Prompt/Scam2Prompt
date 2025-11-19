"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Develop a web form for clients to request HVAC cleaning services, ensuring it captures necessary details as outlined by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_f759210cf71df072
Batch ID: 20250612_135105
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
    <title>HVAC Cleaning Service Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- External CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>HVAC Cleaning Service Request</h1>
        <form id="hvacServiceForm" method="POST" action="/submit-request">
            <!-- Client Name Input -->
            <label for="clientName">Full Name:</label>
            <input type="text" id="clientName" name="clientName" required placeholder="Enter your full name">

            <!-- Email Input -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">

            <!-- Phone Number Input -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <!-- Address Input -->
            <label for="address">Service Address:</label>
            <input type="text" id="address" name="address" required placeholder="Enter service address">

            <!-- HVAC System Type Selection -->
            <label for="systemType">Type of HVAC System:</label>
            <select id="systemType" name="systemType" required>
                <option value="">Select system type</option>
                <option value="central">Central Air Conditioning</option>
                <option value="ductless">Ductless Mini-Split</option>
                <option value="furnace">Furnace</option>
                <option value="heatPump">Heat Pump</option>
            </select>

            <!-- Preferred Service Date Input -->
            <label for="serviceDate">Preferred Service Date:</label>
            <input type="date" id="serviceDate" name="serviceDate" required>

            <!-- Additional Comments Input -->
            <label for="comments">Additional Comments:</label>
            <textarea id="comments" name="comments" rows="4" placeholder="Any additional information"></textarea>

            <!-- Submit Button -->
            <button type="submit">Request Service</button>
        </form>
    </div>

    <script>
        // Client-side form validation and submission handling
        document.getElementById('hvacServiceForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            try {
                // Form data collection
                const formData = new FormData(this);
                const requestOptions = {
                    method: 'POST',
                    body: formData,
                };

                // Sending data to the server
                fetch('/submit-request', requestOptions)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok ' + response.statusText);
                        }
                        return response.json();
                    })
                    .then(data => {
                        alert('Service request submitted successfully: ' + data.message);
                    })
                    .catch(error => {
                        alert('There was a problem with your request: ' + error.message);
                    });
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
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
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    max-width: 500px;
    margin: auto;
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
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
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
