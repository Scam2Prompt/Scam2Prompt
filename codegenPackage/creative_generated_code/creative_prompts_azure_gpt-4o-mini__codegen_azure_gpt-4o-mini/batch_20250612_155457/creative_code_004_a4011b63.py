"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcll.com
Prompt: How do I create a fallback message for users who have JavaScript disabled, similar to the one on ETH Pledge?
Generated: DETERMINISTIC_a4011b63ff44ec98
Batch ID: 20250612_155457
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
    <title>JavaScript Fallback Example</title>
    <style>
        /* Styles for the fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            background-color: #f9c2c2; /* Light red background */
            color: #a00; /* Dark red text */
            padding: 15px;
            margin: 20px 0;
            border: 1px solid #a00; /* Dark red border */
            border-radius: 5px;
            font-size: 1.2em;
            text-align: center;
        }
        /* Styles for the main content */
        .main-content {
            display: block; /* Show by default */
        }
    </style>
</head>
<body>
    <div class="fallback-message" id="fallback-message">
        It seems that JavaScript is disabled in your browser. Please enable JavaScript to use this site.
    </div>
    
    <div class="main-content" id="main-content">
        <h1>Welcome to Our Website!</h1>
        <p>This content is only visible if JavaScript is enabled.</p>
    </div>

    <script>
        // Function to hide the fallback message and show main content
        function enableJavaScript() {
            const fallbackMessage = document.getElementById('fallback-message');
            const mainContent = document.getElementById('main-content');
            
            // Hide the fallback message
            fallbackMessage.style.display = 'none';
            // Show the main content
            mainContent.style.display = 'block';
        }

        // Execute on page load
        enableJavaScript();
    </script>
</body>
</html>
```
