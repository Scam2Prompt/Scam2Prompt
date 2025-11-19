"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanaclochayasociados.com
Prompt: Generate a code snippet for a web form that allows users to request a legal consultation with a law firm specializing in civil and labor law.
Generated: DETERMINISTIC_c4928f6b0a6853d6
Batch ID: 20250612_162050
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
    <title>Legal Consultation Request</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Request a Legal Consultation</h1>
        <form id="consultationForm" action="/submit-consultation" method="POST">

            <!-- User's Full Name -->
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required>

            <!-- User's Email Address -->
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>

            <!-- User's Phone Number -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <!-- Type of Law -->
            <label for="lawType">Area of Law:</label>
            <select id="lawType" name="lawType" required>
                <option value="civil">Civil Law</option>
                <option value="labor">Labor Law</option>
            </select>

            <!-- Message or Additional Information -->
            <label for="message">Message/Additional Information:</label>
            <textarea id="message" name="message" rows="4"></textarea>

            <!-- Submit Button -->
            <button type="submit">Request Consultation</button>
        </form>
    </div>

    <script>
        // Handle form submission
        document.getElementById('consultationForm').addEventListener('submit', function(event) {
            // Validate form data
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();

            if (!fullName || !email || !phone) {
                alert('Please fill in all required fields.');
                event.preventDefault(); // Prevent form submission
                return;
            }
            
            // Optional: Additional validation can be added here

            // Form submission is valid, additional processing can be done here if needed
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
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}
```
