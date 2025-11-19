"""
Generated Code Metadata:
========================
Original URL: https://betty-moore-873.pages.dev
Prompt: Provide an example of using HTML and CSS to create an eye-catching call-to-action button for a special offer.
Generated: DETERMINISTIC_0718527be70a6141
Batch ID: 20250612_155140
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
  <title>Call-to-Action Button</title>
  <style>
    /* General reset for consistent styling */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    /* Styling for the call-to-action button */
    .cta-button {
      background: linear-gradient(45deg, #ff6b6b, #f06595); /* Gradient for eye-catching effect */
      color: #fff; /* White text for contrast */
      font-size: 1.5rem; /* Larger font size for emphasis */
      font-weight: bold; /* Bold text for readability */
      padding: 15px 30px; /* Padding for a comfortable click area */
      border: none; /* Remove default button border */
      border-radius: 50px; /* Rounded corners for modern look */
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
      cursor: pointer; /* Pointer cursor to indicate interactivity */
      transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth hover effect */
    }

    /* Hover effect for the button */
    .cta-button:hover {
      transform: scale(1.05); /* Slightly enlarge the button */
      box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15); /* Enhance shadow on hover */
    }

    /* Focus effect for accessibility */
    .cta-button:focus {
      outline: 2px solid #ff6b6b; /* Visible focus outline */
      outline-offset: 4px; /* Offset for better visibility */
    }
  </style>
</head>
<body>
  <!-- Call-to-action button with descriptive text -->
  <button class="cta-button" onclick="alert('Special Offer Activated!')">
    Claim Your Special Offer!
  </button>
</body>
</html>
```
