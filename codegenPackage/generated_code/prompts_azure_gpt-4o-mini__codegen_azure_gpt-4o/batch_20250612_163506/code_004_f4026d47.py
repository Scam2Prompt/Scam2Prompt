"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Create a sample HTML page for showcasing a neon box advertisement, inspired by the product offerings at SIGMA Advertising.
Generated: DETERMINISTIC_f4026d47fb45f6d1
Batch ID: 20250612_163506
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
    <meta name="description" content="A sample neon box advertisement inspired by SIGMA Advertising.">
    <title>Neon Box Advertisement</title>
    <style>
        /* General reset for consistent styling */
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #121212; /* Dark background for neon effect */
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        /* Neon box container */
        .neon-box {
            position: relative;
            width: 300px;
            height: 150px;
            background-color: #000;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
        }

        /* Neon text styling */
        .neon-text {
            font-size: 24px;
            font-weight: bold;
            color: #00ffcc; /* Neon greenish-blue */
            text-transform: uppercase;
            text-shadow: 
                0 0 5px #00ffcc,
                0 0 10px #00ffcc,
                0 0 20px #00ffcc,
                0 0 40px #00ffcc,
                0 0 80px #00ffcc;
        }

        /* Glow effect for the box */
        .neon-box::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 10px;
            box-shadow: 
                0 0 10px #00ffcc,
                0 0 20px #00ffcc,
                0 0 40px #00ffcc,
                0 0 80px #00ffcc;
            z-index: -1; /* Place behind the box */
        }
    </style>
</head>
<body>
    <!-- Neon box advertisement -->
    <div class="neon-box">
        <div class="neon-text">SIGMA Ads</div>
    </div>
</body>
</html>
```
