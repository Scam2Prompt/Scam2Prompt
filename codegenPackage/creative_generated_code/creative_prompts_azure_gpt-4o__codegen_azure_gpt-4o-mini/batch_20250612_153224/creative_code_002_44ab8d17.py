"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Generate code for a contact form with multiple versions (e.g., Contact v.1, Contact v.2) as described on the Recuperación JC website.
Generated: DETERMINISTIC_44ab8d1791dce131
Batch ID: 20250612_153224
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
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>

<body>
    <h1>Contact Us</h1>

    <!-- Contact Form Version 1 -->
    <form id="contactFormV1" class="contact-form" method="POST" action="/submit-contact">
        <h2>Contact Version 1</h2>
        <label for="nameV1">Name:</label>
        <input type="text" id="nameV1" name="name" required>

        <label for="emailV1">Email:</label>
        <input type="email" id="emailV1" name="email" required>

        <label for="messageV1">Message:</label>
        <textarea id="messageV1" name="message" required></textarea>

        <button type="submit">Send</button>
        <div id="responseV1" class="response"></div>
    </form>

    <!-- Contact Form Version 2 -->
    <form id="contactFormV2" class="contact-form" method="POST" action="/submit-contact-v2">
        <h2>Contact Version 2</h2>
        <label for="nameV2">Full Name:</label>
        <input type="text" id="nameV2" name="fullName" required>

        <label for="emailV2">Email Address:</label>
        <input type="email" id="emailV2" name="emailAddress" required>

        <label for="subjectV2">Subject:</label>
        <input type="text" id="subjectV2" name="subject" required>

        <label for="messageV2">Message:</label>
        <textarea id="messageV2" name="messageContent" required></textarea>

        <button type="submit">Send</button>
        <div id="responseV2" class="response"></div>
    </form>

    <script>
        // Function to handle form submission
        async function handleFormSubmission(formId, responseId) {
            const form = document.getElementById(formId);
            const responseDiv = document.getElementById(responseId);
            form.addEventListener('submit', async (event) => {
                event.preventDefault(); // Prevent default form submission

                const formData = new FormData(form); // Collect form data

                try {
                    const response = await fetch(form.action, {
                        method: form.method,
                        body: formData
                    });

                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }

                    const result = await response.text(); // Capture response text
                    responseDiv.textContent = 'Message sent successfully!'; // Success message
                } catch (error) {
                    console.error('There was a problem with the fetch operation:', error);
                    responseDiv.textContent = 'Error sending message. Please try again later.'; // Error message
                }
            });
        }

        // Initialize form submission handling
        handleFormSubmission('contactFormV1', 'responseV1');
        handleFormSubmission('contactFormV2', 'responseV2');
    </script>
</body>

</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #333;
}

.contact-form {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 15px;
    background-color: #28a745;
    border: none;
    border-radius: 5px;
    color: white;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.response {
    margin-top: 10px;
    font-size: 1rem;
    color: #d9534f; /* Bootstrap danger color for error messages */
}
```
