"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claytest.vercel.app
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like Claytest?
Generated: DETERMINISTIC_01770c8835b5f52e
Batch ID: 20250612_162504
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
    <title>JavaScript Check</title>
    <style>
        /* Styles to hide the content when JavaScript is disabled */
        .no-js {
            display: none;
        }
        .js {
            display: block;
        }
    </style>
    <noscript>
        <!-- Display message when JavaScript is disabled -->
        <style>
            .js {
                display: none;
            }
            .no-js {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Content shown when JavaScript is disabled -->
    <div class="no-js">
        <h1>JavaScript is disabled in your browser.</h1>
        <p>Please enable JavaScript for a better experience.</p>
    </div>

    <!-- Content shown when JavaScript is enabled -->
    <div class="js">
        <h1>Welcome!</h1>
        <p>JavaScript is enabled in your browser.</p>
    </div>

    <script>
        try {
            // Code to execute when JavaScript is enabled
            console.log("JavaScript is enabled.");
            // Additional JavaScript code can be placed here
        } catch (error) {
            console.error("An error occurred while checking JavaScript: ", error);
        }
    </script>
</body>
</html>
```
