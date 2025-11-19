"""
Generated Code Metadata:
========================
Original URL: https://aslusher.com
Prompt: Design a minimalistic webpage with a centered message and a contact link using HTML and CSS.
Generated: DETERMINISTIC_88abc879c7636bec
Batch ID: 20250622_212813
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
  <meta name="description" content="Minimalistic webpage with a centered message and contact link">
  <title>Minimalistic Webpage</title>
  <style>
    /* Reset default margin and padding */
    body, html {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Set full height for the viewport */
    html, body {
      height: 100%;
      font-family: Arial, sans-serif;
    }

    /* Center content vertically and horizontally */
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100%;
      text-align: center;
      background-color: #f4f4f4; /* Light background color */
    }

    /* Style for the message */
    .message {
      font-size: 1.5rem;
      color: #333; /* Dark text color */
      margin-bottom: 1rem;
    }

    /* Style for the contact link */
    .contact-link {
      font-size: 1rem;
      color: #007BFF; /* Blue link color */
      text-decoration: none;
      transition: color 0.3s ease;
    }

    /* Hover effect for the contact link */
    .contact-link:hover {
      color: #0056b3; /* Darker blue on hover */
    }
  </style>
</head>
<body>
  <div class="container">
    <div>
      <!-- Centered message -->
      <p class="message">Welcome to our minimalistic webpage!</p>
      <!-- Contact link -->
      <a href="mailto:contact@example.com" class="contact-link">Contact Us</a>
    </div>
  </div>
</body>
</html>
```
