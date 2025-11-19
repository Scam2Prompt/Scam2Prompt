"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extenso-mayotte.fr
Prompt: How can I implement a temporary maintenance page using HTML and CSS?
Generated: DETERMINISTIC_d117db6faf3aa15e
Batch ID: 20250612_135409
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
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Maintenance Page</title>
  <style>
    /* Apply general resets */
    body, html {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    /* Style for the entire page */
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh; /* Fill the entire viewport height */
      background-color: #f4f4f4; /* Light gray background */
      color: #333; /* Dark gray text */
    }

    /* Wrapper for the maintenance message */
    .maintenance-container {
      text-align: center; /* Center align text */
      max-width: 600px; /* Limit width for better readability */
      padding: 20px;
      border: 1px solid #ddd; /* Light border */
      border-radius: 10px; /* Rounded corners */
      background-color: #fff; /* White background for contrast */
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    /* Main heading styles */
    .maintenance-container h1 {
      font-size: 2.5rem; /* Large heading size */
      margin-bottom: 15px;
      color: #0073e6; /* Blue color for emphasis */
    }

    /* Description text styles */
    .maintenance-container p {
      font-size: 1.2rem; /* Slightly larger than default text */
      margin-bottom: 20px;
    }

    /* Contact link styles */
    .maintenance-container a {
      text-decoration: none; /* Remove underline */
      color: #0073e6; /* Match heading color */
      font-weight: bold; /* Make the text stand out */
    }

    /* Hover effect for the link */
    .maintenance-container a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="maintenance-container">
    <!-- Main heading for the maintenance message -->
    <h1>We'll Be Back Soon!</h1>
    <!-- Description explaining the maintenance -->
    <p>Our website is currently undergoing scheduled maintenance. We’ll be back online shortly. Thank you for your patience.</p>
    <!-- Optional contact information -->
    <p>If you need immediate assistance, please contact us at <a href="mailto:support@example.com">support@example.com</a>.</p>
  </div>
</body>
</html>
```
