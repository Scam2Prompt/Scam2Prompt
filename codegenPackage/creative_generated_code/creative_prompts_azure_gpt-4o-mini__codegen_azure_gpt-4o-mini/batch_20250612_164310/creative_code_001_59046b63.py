"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gpt-chat.info
Prompt: Write a code snippet for a contact form that handles errors, inspired by the "Lỗi: Không tìm thấy biểu mẫu liên hệ" message on the GPT-Chat page.
Generated: DETERMINISTIC_59046b636abc2043
Batch ID: 20250612_164310
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
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
        .success {
            color: green;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<h2>Contact Us</h2>
<form id="contactForm">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" required><br>
    
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br>
    
    <label for="message">Message:</label><br>
    <textarea id="message" name="message" required></textarea><br>
    
    <input type="submit" value="Submit">
    <div id="responseMessage" class="error"></div>
</form>

<script>
    // Function to handle form submission
    document.getElementById('contactForm').addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent default form submission
        
        const responseMessage = document.getElementById('responseMessage');
        responseMessage.textContent = ''; // Clear previous messages
        
        // Read form data
        const formData = new FormData(this);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            message: formData.get('message')
        };

        try {
            const response = await fetch('/submitContactForm', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            if (!response.ok) {
                throw new Error('Lỗi: Không tìm thấy biểu mẫu liên hệ'); // Custom error message
            }
            
            const result = await response.json();
            responseMessage.textContent = result.message || 'Your message has been sent successfully!';
            responseMessage.className = 'success';
        } catch (error) {
            // Display error message to the user
            responseMessage.textContent = error.message;
            responseMessage.className = 'error';
        }
    });
</script>

</body>
</html>
```
