"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Create a sample code to implement a web form that allows users to submit inquiries about Duplex Steel Pipes, referencing the features provided by Dinkar Alloys.
Generated: DETERMINISTIC_dbf9925afc3642e0
Batch ID: 20250612_155150
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
    <title>Duplex Steel Pipes Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Inquiry Form for Duplex Steel Pipes</h1>
        <form id="inquiryForm" method="POST" action="/submit-inquiry">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="inquiry">Inquiry:</label>
            <textarea id="inquiry" name="inquiry" rows="4" required></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="responseMessage"></div> <!-- Placeholder for response messages -->
    </div>

    <script>
        // Add an event listener to handle form submission
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send the form data to the server using Fetch API
            fetch(this.action, {
                method: this.method,
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json(); // Parse JSON response
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').innerText = 'Inquiry submitted successfully!';
                this.reset(); // Reset the form
            })
            .catch(error => {
                // Display error message
                document.getElementById('responseMessage').innerText = 'Error submitting inquiry: ' + error.message;
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
    margin-bottom: 10px;
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

#responseMessage {
    margin-top: 20px;
    text-align: center;
    font-weight: bold;
}
``` 

This code provides a simple web form for users to submit inquiries about Duplex Steel Pipes, with proper error handling and user feedback.
