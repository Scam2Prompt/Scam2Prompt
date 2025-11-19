"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Generate a code snippet for a web form that allows users to request a free measure and quote for cabinetry services, including fields for name, phone, email, and message.
Generated: DETERMINISTIC_56efb21599f66dce
Batch ID: 20250612_164115
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
    <title>Free Measure and Quote Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request a Free Measure and Quote</h1>
        <form id="quoteRequestForm" action="/submit-quote-request" method="POST">
            <!-- Name Field -->
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your name">

            <!-- Phone Field -->
            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <!-- Email Field -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">

            <!-- Message Field -->
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required placeholder="Enter your message"></textarea>

            <!-- Submit Button -->
            <button type="submit">Request Quote</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- Placeholder for response messages -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('quoteRequestForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

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
                // Display success message
                document.getElementById('responseMessage').innerText = 'Your request has been submitted successfully!';
                document.getElementById('responseMessage').classList.remove('hidden');
                this.reset(); // Reset the form
            })
            .catch(error => {
                // Display error message
                document.getElementById('responseMessage').innerText = 'There was a problem with your request: ' + error.message;
                document.getElementById('responseMessage').classList.remove('hidden');
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

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.hidden {
    display: none;
}

#responseMessage {
    margin-top: 20px;
    text-align: center;
    color: #d9534f; /* Default to red for error messages */
}
```
