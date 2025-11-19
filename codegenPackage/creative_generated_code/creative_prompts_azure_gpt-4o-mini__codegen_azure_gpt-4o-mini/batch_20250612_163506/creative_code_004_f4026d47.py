"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: Create a sample HTML page for showcasing a neon box advertisement, inspired by the product offerings at SIGMA Advertising.
Generated: DETERMINISTIC_f4026d47fb45f6d1
Batch ID: 20250612_163506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://sigmaadvertising.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Showcasing a neon box advertisement inspired by SIGMA Advertising.">
    <title>Neon Box Advertisement</title>
    <style>
        /* Basic reset for margins and paddings */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #111; /* Dark background for neon effect */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full height of the viewport */
        }

        /* Container for the neon box */
        .neon-box {
            position: relative;
            background-color: #222; /* Dark background for the box */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            overflow: hidden; /* Ensures no overflow of neon effects */
            color: #fff; /* White text color */
            box-shadow: 0 0 10px rgba(255, 0, 255, 0.5), 0 0 20px rgba(255, 0, 255, 0.5), 0 0 30px rgba(255, 0, 255, 0.5);
        }

        /* Neon text effect */
        .neon-text {
            font-size: 2.5em; /* Large font size for the title */
            text-transform: uppercase; /* Uppercase for emphasis */
            animation: glow 1.5s infinite alternate; /* Animation for glowing effect */
        }

        /* Keyframes for the glowing effect */
        @keyframes glow {
            0% {
                text-shadow: 0 0 5px rgba(255, 0, 255, 0.7), 0 0 10px rgba(255, 0, 255, 0.5), 0 0 15px rgba(255, 0, 255, 0.3);
            }
            100% {
                text-shadow: 0 0 10px rgba(255, 0, 255, 1.0), 0 0 20px rgba(255, 0, 255, 0.7), 0 0 30px rgba(255, 0, 255, 0.5);
            }
        }

        /* Button styling */
        .cta-button {
            background-color: #ff0080; /* Bright button color */
            color: #fff; /* White text color */
            border: none; /* No border */
            border-radius: 5px; /* Round corners */
            padding: 10px 20px; /* Padding for the button */
            font-size: 1em; /* Font size for button text */
            cursor: pointer; /* Pointer cursor on hover */
            transition: background-color 0.3s ease; /* Smooth transition for hover effect */
        }

        /* Button hover effect */
        .cta-button:hover {
            background-color: #e60073; /* Darken on hover */
        }
    </style>
</head>
<body>
    <div class="neon-box">
        <h1 class="neon-text">SIGMA Advertising</h1>
        <p>Your gateway to innovative marketing solutions!</p>
        <button class="cta-button" onclick="handleClick()">Learn More</button>
    </div>

    <script>
        /**
         * Handle button click event.
         * This function could be extended to perform actual navigation or actions.
         */
        function handleClick() {
            try {
                // Placeholder for future functionality
                alert("Redirecting to SIGMA Advertising page...");
                // In a real application, you might redirect the user:
                // window.location.href = "https://sigmaadvertising.com";
            } catch (error) {
                console.error("An error occurred during the click event:", error);
                alert("Something went wrong. Please try again later.");
            }
        }
    </script>
</body>
</html>
```
