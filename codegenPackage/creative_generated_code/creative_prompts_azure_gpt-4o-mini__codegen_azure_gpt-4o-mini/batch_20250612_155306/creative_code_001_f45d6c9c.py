"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defivalidation.com
Prompt: Write a code snippet to implement a domain inquiry form that captures user information like country codes as seen on Defivalidation.com.
Generated: DETERMINISTIC_f45d6c9ca47ee37a
Batch ID: 20250612_155306
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
    <title>Domain Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <div class="container">
        <h1>Domain Inquiry Form</h1>
        <form id="inquiryForm" action="/submit-inquiry" method="POST">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required placeholder="Full Name">

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required placeholder="Email Address">

            <label for="countryCode">Country Code:</label>
            <select id="countryCode" name="countryCode" required>
                <option value="" disabled selected>Select your country</option>
                <option value="US">United States (+1)</option>
                <option value="CA">Canada (+1)</option>
                <option value="GB">United Kingdom (+44)</option>
                <option value="AU">Australia (+61)</option>
                <!-- Add more country codes as needed -->
            </select>

            <label for="domain">Domain Name:</label>
            <input type="text" id="domain" name="domain" required placeholder="Domain Name (e.g., example.com)">

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- For displaying response messages -->
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send request to the server
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json(); // Parse JSON response
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').textContent = data.message || 'Inquiry submitted successfully!';
                document.getElementById('responseMessage').classList.remove('hidden');
                this.reset(); // Reset form fields after submission
            })
            .catch(error => {
                // Display error message
                document.getElementById('responseMessage').textContent = 'Error: ' + error.message;
                document.getElementById('responseMessage').classList.remove('hidden');
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the container */
.container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

/* Style for form elements */
label {
    display: block;
    margin-bottom: 5px;
}

input, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
button {
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

/* Response message styling */
.hidden {
    display: none;
}

#responseMessage {
    margin-top: 20px;
    padding: 10px;
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    border-radius: 5px;
}
```
