"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doamnke.wuaze.com
Prompt: How do I create a fallback message for users with JavaScript disabled on my website?
Generated: DETERMINISTIC_01d409d5bf04bd4c
Batch ID: 20250612_162734
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
        /* Styles for the fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            border: 1px solid #f5c6cb; /* Light red border */
            margin: 20px 0;
        }
        
        /* Styles for the main content that requires JavaScript */
        .main-content {
            display: block; /* Show by default */
        }
    </style>
</head>
<body>
    <div id="fallback" class="fallback-message">
        <strong>Notice:</strong> It looks like JavaScript is disabled in your browser. Please enable JavaScript for a better experience on this website.
    </div>

    <div id="main" class="main-content">
        <h1>Welcome to Our Website</h1>
        <p>This content is only available if JavaScript is enabled.</p>
    </div>

    <script>
        // Function to hide the fallback message and show the main content
        function enableJavaScript() {
            const fallbackMessage = document.getElementById('fallback');
            const mainContent = document.getElementById('main');

            // Hide the fallback message
            fallbackMessage.style.display = 'none';
            // Show the main content
            mainContent.style.display = 'block';
        }

        // Call the function when the script loads
        enableJavaScript();
    </script>
</body>
</html>
```
