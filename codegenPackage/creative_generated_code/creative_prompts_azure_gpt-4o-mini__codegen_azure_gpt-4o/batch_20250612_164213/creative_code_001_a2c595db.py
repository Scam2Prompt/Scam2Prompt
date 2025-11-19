"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catalysts.in
Prompt: Can you provide a code snippet to create a simple loading animation for a website under development?
Generated: DETERMINISTIC_a2c595dbc8df4b40
Batch ID: 20250612_164213
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
  <title>Loading Animation</title>
  <style>
    /* Center the loader on the screen */
    .loader-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh; /* Full viewport height */
      background-color: #f9f9f9; /* Light background color */
    }

    /* Loader styling */
    .loader {
      width: 50px;
      height: 50px;
      border: 8px solid #e0e0e0; /* Light gray border */
      border-top: 8px solid #3498db; /* Blue color for the animated part */
      border-radius: 50%; /* Round shape */
      animation: spin 1s linear infinite; /* Spin animation */
    }

    /* Keyframes for loader spin */
    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
  </style>
</head>
<body>
  <div class="loader-container">
    <!-- Loader element -->
    <div class="loader"></div>
  </div>
</body>
</html>
```
