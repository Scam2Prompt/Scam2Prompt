"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://governance-sym.biotic.fi
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, similar to the functionality described on the "Symbiotic Governance" platform.
Generated: DETERMINISTIC_8c2222d1ada07805
Batch ID: 20250612_152006
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
        /* Styles for the fallback message */
        #no-js-message {
            display: none; /* Hide by default, shown if JS is disabled */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <style>
            /* Display the message if JavaScript is disabled */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Fallback message for users with JavaScript disabled -->
    <div id="no-js-message">
        <strong>JavaScript is disabled in your browser!</strong><br>
        Please enable JavaScript to experience the full functionality of this website.
    </div>

    <script>
        // Function to check for JavaScript support
        function init() {
            // Log message indicating that JS is enabled
            console.log("JavaScript is enabled in your browser.");

            // Further JavaScript functionality can be added here
        }

        // Run the init function when the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", init);

        // Error handling for potential issues during initialization
        window.addEventListener("error", function (event) {
            console.error("An error occurred: ", event.message);
            alert("An unexpected error occurred. Please try refreshing the page.");
        });
    </script>
</body>
</html>
```
