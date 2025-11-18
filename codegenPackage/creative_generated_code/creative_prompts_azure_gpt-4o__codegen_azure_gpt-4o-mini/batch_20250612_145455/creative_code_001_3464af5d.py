"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigbonus.eu
Prompt: Create a script that checks for JavaScript compatibility and redirects users to an alternative page if JavaScript is disabled.
Generated: DETERMINISTIC_3464af5d117546fb
Batch ID: 20250612_145455
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
    <title>JavaScript Compatibility Check</title>
    <style>
        /* Style to show a message when JavaScript is disabled */
        .noscript-message {
            display: none;
            text-align: center;
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="noscript-message" id="noscript-message">
        <strong>JavaScript is disabled in your browser.</strong>
        <p>You are being redirected to an alternative page.</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // If JavaScript is enabled, hide the no-script message
            document.getElementById('noscript-message').style.display = 'none';
        });

        // Function to redirect to an alternative page
        function redirectToAlternative() {
            // Use a try-catch block for error handling
            try {
                // Redirect to an alternative page
                window.location.href = "alternative.html"; // Replace with your alternative page URL
            } catch (error) {
                console.error("Redirection failed:", error);
                alert("An error occurred while redirecting. Please try again later.");
            }
        }

        // Redirect if JavaScript is not enabled within a certain timeout
        setTimeout(function() {
            // Check if the no-script message is still displayed (indicating JS is disabled)
            if (document.getElementById('noscript-message').style.display === 'block') {
                redirectToAlternative();
            }
        }, 1000);
    </script>

    <noscript>
        <style>
            /* Show the no-script message if JavaScript is disabled */
            #noscript-message {
                display: block;
            }
        </style>
    </noscript>
    
</body>
</html>
```
