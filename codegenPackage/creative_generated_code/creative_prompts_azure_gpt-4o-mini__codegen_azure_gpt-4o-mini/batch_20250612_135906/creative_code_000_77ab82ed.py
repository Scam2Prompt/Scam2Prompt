"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Generate a code snippet that demonstrates how to implement a contact form for a pharmaceutical company, including fields for name, email, and message, similar to the contact details provided on the Perrigo Claims website.
Generated: DETERMINISTIC_77ab82ed04f35d58
Batch ID: 20250612_135906
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
    <title>Contact Us - Pharmaceutical Company</title>
    <link rel="stylesheet" href="styles.css"> <!-- External stylesheet for styling -->
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <form id="contactForm" action="/submit-contact" method="POST">
            <label for="name">Name <span class="required">*</span></label>
            <input type="text" id="name" name="name" required placeholder="Your Name">
            
            <label for="email">Email <span class="required">*</span></label>
            <input type="email" id="email" name="email" required placeholder="Your Email">

            <label for="message">Message <span class="required">*</span></label>
            <textarea id="message" name="message" required placeholder="Your Message" rows="5"></textarea>

            <button type="submit">Submit</button>
        </form>
        <div id="responseMessage"></div> <!-- Div to display response message -->
    </div>

    <script>
        // Add event listener to the form for submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            
            // Gather form data
            const formData = new FormData(event.target);
            
            // Send data to server
            fetch(event.target.action, {
                method: event.target.method,
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    // Throw an error for non-2xx responses
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                return response.json(); // Parse JSON response
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').innerText = 'Thank you for your message!';
                document.getElementById('contactForm').reset(); // Reset form
            })
            .catch(error => {
                // Handle errors and display error message
                document.getElementById('responseMessage').innerText = 'There was a problem with your submission. Please try again later.';
                console.error('There was a problem with the fetch operation:', error);
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the contact form */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

.container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    border: none;
    background-color: #28a745;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.required {
    color: red;
}
```
