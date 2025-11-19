"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Create a Settled Collection fireplace design using HTML, CSS, and JavaScript, incorporating its hybrid style between a fireplace and furniture.
Generated: DETERMINISTIC_faa06c8cff3c88eb
Batch ID: 20250622_210650
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
  <title>Settled Collection Fireplace Design</title>
  <style>
    /* Base styles for the page */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    /* Container for the fireplace */
    .fireplace-container {
      width: 400px;
      height: 500px;
      background-color: #2c2c2c; /* Dark gray for the fireplace body */
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
      position: relative;
    }

    /* Fireplace opening */
    .fireplace-opening {
      width: 300px;
      height: 200px;
      background-color: #1a1a1a; /* Darker gray for the opening */
      border-radius: 5px;
      margin: 50px auto 0;
      position: relative;
      overflow: hidden;
    }

    /* Flames animation */
    .flame {
      position: absolute;
      bottom: 10px;
      width: 50px;
      height: 100px;
      background: radial-gradient(circle, #ff4500 0%, #ff6347 50%, transparent 100%);
      border-radius: 50%;
      animation: flicker 1.5s infinite;
    }

    .flame:nth-child(1) {
      left: 50px;
      animation-delay: 0.2s;
    }

    .flame:nth-child(2) {
      left: 125px;
      animation-delay: 0.4s;
    }

    .flame:nth-child(3) {
      left: 200px;
      animation-delay: 0.6s;
    }

    @keyframes flicker {
      0%, 100% {
        transform: scale(1);
        opacity: 0.8;
      }
      50% {
        transform: scale(1.2);
        opacity: 1;
      }
    }

    /* Furniture-like base */
    .fireplace-base {
      width: 400px;
      height: 50px;
      background-color: #3b3b3b; /* Slightly lighter gray for the base */
      border-radius: 0 0 10px 10px;
      position: absolute;
      bottom: 0;
    }

    /* Decorative top shelf */
    .fireplace-shelf {
      width: 420px;
      height: 20px;
      background-color: #3b3b3b;
      border-radius: 10px;
      position: absolute;
      top: 20px;
      left: -10px;
    }

    /* Optional decorative items */
    .decorative-item {
      width: 40px;
      height: 40px;
      background-color: #d4af37; /* Gold color for decoration */
      border-radius: 50%;
      position: absolute;
    }

    .decorative-item:nth-child(1) {
      top: -10px;
      left: 50px;
    }

    .decorative-item:nth-child(2) {
      top: -10px;
      right: 50px;
    }
  </style>
</head>
<body>
  <div class="fireplace-container">
    <!-- Decorative top shelf -->
    <div class="fireplace-shelf"></div>
    <!-- Decorative items -->
    <div class="decorative-item"></div>
    <div class="decorative-item"></div>
    <!-- Fireplace opening -->
    <div class="fireplace-opening">
      <!-- Flames -->
      <div class="flame"></div>
      <div class="flame"></div>
      <div class="flame"></div>
    </div>
    <!-- Furniture-like base -->
    <div class="fireplace-base"></div>
  </div>
</body>
</html>
```
