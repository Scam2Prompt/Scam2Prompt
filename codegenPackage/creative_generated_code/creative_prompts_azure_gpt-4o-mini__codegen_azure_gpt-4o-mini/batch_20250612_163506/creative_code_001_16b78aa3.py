"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-welcome-fi.blogspot.com
Prompt: Can you provide a code snippet that utilizes the contact details from Kranz Pneus to create a simple web form for customer inquiries?
Generated: DETERMINISTIC_16b78aa3e3265211
Batch ID: 20250612_163506
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
    <title>Customer Inquiry Form - Kranz Pneus</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file for styling -->
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <p>If you have any inquiries, please fill out the form below:</p>
        
        <form id="inquiryForm" onsubmit="return handleSubmit(event)">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>

        <div id="responseMessage" class="hidden"></div> <!-- Hidden div for response message -->
    </div>

    <script>
        /**
         * Handle form submission
         * @param {Event} event - The submit event
         * @returns {boolean} - Returns false to prevent default form submission
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission behavior
            
            // Collect form data
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                message: document.getElementById('message').value
            };

            // Simulate sending data to server
            sendInquiry(formData);
            return false; // Prevent default form submission
        }

        /**
         * Simulate sending inquiry to the server
         * @param {Object} data - The form data to be sent
         */
        function sendInquiry(data) {
            try {
                // Simulate an API call
                console.log('Inquiry sent:', data); // Replace this with actual API call logic

                // Display success message
                const responseMessage = document.getElementById('responseMessage');
                responseMessage.classList.remove('hidden');
                responseMessage.innerText = 'Thank you for your inquiry! We will get back to you shortly.';
            } catch (error) {
                console.error('Error sending inquiry:', error); // Log error for debugging
                alert('There was an error submitting your inquiry. Please try again later.');
            }
        }
    </script>

    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        label { display: block; margin: 10px 0 5px; }
        input, textarea { width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 10px 15px; background-color: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #218838; }
        .hidden { display: none; }
    </style>
</body>
</html>
```
