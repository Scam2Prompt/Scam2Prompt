"""
Generated Code Metadata:
========================
Original URL: https://startec.com.my
Prompt: How can I implement a contact form using HTML and JavaScript for a computer hardware store's website, inspired by the contact details provided by StarTec?
Generated: DETERMINISTIC_b6e4e51dfb38d398
Batch ID: 20250612_163336
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
  <title>Contact Form - StarTec Hardware</title>
  <style>
    /* Basic styling for the contact form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .container {
      max-width: 600px;
      margin: 50px auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #333;
    }

    form {
      display: flex;
      flex-direction: column;
    }

    label {
      margin-bottom: 5px;
      font-weight: bold;
    }

    input, textarea {
      margin-bottom: 15px;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    button {
      padding: 10px 15px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }

    button:hover {
      background-color: #0056b3;
    }

    .success-message, .error-message {
      margin-top: 20px;
      padding: 10px;
      border-radius: 4px;
      font-size: 16px;
    }

    .success-message {
      background-color: #d4edda;
      color: #155724;
    }

    .error-message {
      background-color: #f8d7da;
      color: #721c24;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Contact Us</h1>
    <form id="contactForm">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" placeholder="Your Name" required>

      <label for="email">Email:</label>
      <input type="email" id="email" name="email" placeholder="Your Email" required>

      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="5" placeholder="Your Message" required></textarea>

      <button type="submit">Submit</button>
    </form>
    <div id="responseMessage"></div>
  </div>

  <script>
    // JavaScript to handle form submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the default form submission behavior

      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      // Validate form inputs
      if (!name || !email || !message) {
        displayMessage('Please fill out all fields.', 'error');
        return;
      }

      // Simulate form submission (replace with actual server-side logic)
      try {
        // Simulated success response
        displayMessage('Thank you for contacting us, ' + name + '! We will get back to you shortly.', 'success');
        // Clear the form
        document.getElementById('contactForm').reset();
      } catch (error) {
        // Handle any unexpected errors
        displayMessage('An error occurred while submitting the form. Please try again later.', 'error');
      }
    });

    /**
     * Function to display a success or error message
     * @param {string} message - The message to display
     * @param {string} type - The type of message ('success' or 'error')
     */
    function displayMessage(message, type) {
      const responseMessage = document.getElementById('responseMessage');
      responseMessage.innerHTML = message;
      responseMessage.className = type === 'success' ? 'success-message' : 'error-message';
    }
  </script>
</body>
</html>
```
