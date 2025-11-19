"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bmi-supply.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser before redirecting them to a specific page?
Generated: DETERMINISTIC_7b79a96b9ed6359c
Batch ID: 20250612_162228
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
    <noscript>
        <!-- This <noscript> section will display if JavaScript is disabled -->
        <meta http-equiv="refresh" content="0;url=/javascript-disabled.html">
        <style>
            /* Hide page content if JavaScript is disabled */
            body { display: none; }
        </style>
    </noscript>
    <script>
        // Redirect the user to a specific page if JavaScript is enabled
        try {
            window.location.href = "/javascript-enabled.html";
        } catch (error) {
            console.error("Error during JavaScript-enabled redirect:", error);
        }
    </script>
</head>
<body>
    <!-- Optional content here -->
</body>
</html>
```
