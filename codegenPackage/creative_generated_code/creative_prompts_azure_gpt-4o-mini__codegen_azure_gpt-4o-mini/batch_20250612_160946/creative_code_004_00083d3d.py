"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnb8.cc
Prompt: How do I implement a fallback message for users with JavaScript disabled on my site?
Generated: DETERMINISTIC_00083d3dcf5d2094
Batch ID: 20250612_160946
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
    <title>Fallback Message Example</title>
    <style>
        /* Style for the fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <!-- Fallback message for users with JavaScript disabled -->
    <noscript>
        <div class="fallback-message">
            JavaScript is disabled in your browser. Please enable it for a better experience on this site.
        </div>
    </noscript>

    <h1>Welcome to Our Website</h1>
    <p>This is a JavaScript enabled site.</p>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Your main site functionality goes here
            console.log("JavaScript is enabled.");
        });
    </script>

</body>
</html>
```
