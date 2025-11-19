"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://governance-sym.biotic.fi
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_155306
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
    <title>JavaScript Detection</title>
    <style>
        /* Styles to hide the message if JavaScript is enabled */
        .no-js {
            display: block;
            color: red;
            font-weight: bold;
        }
        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message shown when JavaScript is disabled -->
    <div class="no-js" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <!-- Message shown when JavaScript is enabled -->
    <div class="js-enabled" id="js-message">
        JavaScript is enabled. Welcome to our web application!
    </div>

    <script>
        // Function to run when the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", function() {
            try {
                // Hide the JavaScript disabled message
                document.getElementById("no-js-message").style.display = "none";
                // Show the JavaScript enabled message
                document.getElementById("js-message").style.display = "block";
            } catch (error) {
                // Log any errors to the console for debugging
                console.error("An error occurred while checking JavaScript status: ", error);
            }
        });
    </script>
</body>
</html>
```
