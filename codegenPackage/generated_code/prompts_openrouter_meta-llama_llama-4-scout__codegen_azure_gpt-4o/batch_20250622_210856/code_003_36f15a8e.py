"""
Generated Code Metadata:
========================
Original URL: https://launchlawinc.com
Prompt: Create a code snippet in HTML/CSS to design a simple and intuitive navigation menu for a website offering DIY legal forms, inspired by the layout on launchlawinc.com.
Generated: DETERMINISTIC_36f15a8e23b32c0c
Batch ID: 20250622_210856
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
  <title>DIY Legal Forms Navigation</title>
  <style>
    /* Reset some default browser styles */
    body, ul, li {
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Arial, sans-serif;
    }

    /* Navigation container styling */
    .nav-container {
      background-color: #2c3e50; /* Dark blue-gray background */
      padding: 10px 20px;
    }

    /* Navigation menu styling */
    .nav-menu {
      list-style: none; /* Remove bullet points */
      display: flex; /* Align items horizontally */
      justify-content: space-between; /* Space items evenly */
    }

    /* Individual menu item styling */
    .nav-menu li {
      margin: 0 10px;
    }

    .nav-menu a {
      text-decoration: none; /* Remove underline */
      color: #ecf0f1; /* Light gray text */
      font-size: 16px;
      padding: 8px 12px;
      border-radius: 4px;
      transition: background-color 0.3s ease, color 0.3s ease; /* Smooth hover effect */
    }

    /* Hover effect for menu items */
    .nav-menu a:hover {
      background-color: #3498db; /* Light blue background */
      color: #ffffff; /* White text */
    }

    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
      .nav-menu {
        flex-direction: column; /* Stack items vertically */
        align-items: center; /* Center items */
      }

      .nav-menu li {
        margin: 5px 0;
      }
    }
  </style>
</head>
<body>
  <!-- Navigation bar -->
  <nav class="nav-container">
    <ul class="nav-menu">
      <li><a href="#home">Home</a></li>
      <li><a href="#forms">Forms</a></li>
      <li><a href="#pricing">Pricing</a></li>
      <li><a href="#about">About Us</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>
</body>
</html>
```
