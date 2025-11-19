"""
Generated Code Metadata:
========================
Original URL: https://jup.jupuary-event.com
Prompt: Generate a code snippet in JavaScript to create a simple webpage that displays a hosting account blockage message and provides a contact form for support requests.
Generated: DETERMINISTIC_b20d675d6c7c9d36
Batch ID: 20250622_211926
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
    <title>Account Blocked</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 400px;
            margin: auto;
        }
        h1 {
            color: #e74c3c;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        input, textarea {
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Account Blocked</h1>
        <p>Your hosting account has been blocked. Please fill out the form below to contact support.</p>
        <form id="supportForm">
            <input type="text" id="name" placeholder="Your Name" required>
            <input type="email" id="email" placeholder="Your Email" required>
            <textarea id="message" placeholder="Your Message" rows="4" required></textarea>
            <button type="submit">Send Message</button>
        </form>
        <p id="responseMessage" style="color: green; margin-top: 10px;"></p>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('supportForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Simple validation
            if (!name || !email || !message) {
                alert('Please fill in all fields.');
                return;
            }

            // Simulate sending data to a server
            try {
                // Here you would typically send the data to your server
                // For demonstration, we will just log it to the console
                console.log('Sending message:', { name, email, message });

                // Display success message
                document.getElementById('responseMessage').innerText = 'Your message has been sent successfully!';
                
                // Clear the form
                document.getElementById('supportForm').reset();
            } catch (error) {
                console.error('Error sending message:', error);
                alert('There was an error sending your message. Please try again later.');
            }
        });
    </script>
</body>
</html>
```
