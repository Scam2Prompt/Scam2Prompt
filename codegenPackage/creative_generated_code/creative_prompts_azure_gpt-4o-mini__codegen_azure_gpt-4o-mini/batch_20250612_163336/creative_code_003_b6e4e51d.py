"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startec.com.my
Prompt: How can I implement a contact form using HTML and JavaScript for a computer hardware store's website, inspired by the contact details provided by StarTec?
Generated: DETERMINISTIC_b6e4e51dfb38d398
Batch ID: 20250612_163336
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
    <title>Contact Us - Computer Hardware Store</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>

    <header>
        <h1>Contact Us</h1>
        <p>Have questions? Reach out to us!</p>
    </header>

    <main>
        <form id="contactForm">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required></textarea>

            <button type="submit">Send Message</button>
        </form>
        <div id="responseMessage"></div> <!-- For displaying response messages -->
    </main>

    <footer>
        <p>&copy; 2023 Computer Hardware Store. All rights reserved.</p>
    </footer>

    <script>
        // Function to handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value
            };

            // Validate email format
            if (!validateEmail(formData.email)) {
                displayResponse('Invalid email format.', 'error');
                return;
            }

            // Simulate sending data to server (replace with real API endpoint)
            sendDataToServer(formData)
                .then(response => {
                    if (response.success) {
                        displayResponse('Your message has been sent successfully!', 'success');
                    } else {
                        displayResponse('There was an error sending your message. Please try again later.', 'error');
                    }
                })
                .catch(error => {
                    displayResponse('An unexpected error occurred. Please try again later.', 'error');
                    console.error('Error sending data:', error);
                });
        });

        // Function to validate email format
        function validateEmail(email) {
            const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return regex.test(email);
        }

        // Function to simulate sending data to a server
        function sendDataToServer(data) {
            return new Promise((resolve) => {
                // Simulate an API call with a delay
                setTimeout(() => {
                    // Simulated response
                    resolve({ success: true });
                }, 1000);
            });
        }

        // Function to display response messages
        function displayResponse(message, type) {
            const responseDiv = document.getElementById('responseMessage');
            responseDiv.textContent = message;
            responseDiv.className = type; // 'success' or 'error'
        }
    </script>

    <style>
        /* Basic styles for the contact form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        header, footer {
            text-align: center;
            margin-bottom: 20px;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
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
            border-radius: 5px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background-color: #218838;
        }
        #responseMessage {
            margin-top: 20px;
            text-align: center;
        }
        .success {
            color: green;
        }
        .error {
            color: red;
        }
    </style>

</body>
</html>
```
