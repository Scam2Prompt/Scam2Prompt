"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fyatlux.com
Prompt: How do I check if JavaScript is enabled in my browser settings?
Generated: DETERMINISTIC_c42c3f021123be5e
Batch ID: 20250612_161616
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Basic styling for the message */
        #js-status {
            display: none; /* Hide by default */
            padding: 10px;
            border: 1px solid #ccc;
            margin-top: 20px;
        }
        .enabled {
            background-color: #d4edda; /* Light green for enabled */
            color: #155724; /* Dark green text */
        }
        .disabled {
            background-color: #f8d7da; /* Light red for disabled */
            color: #721c24; /* Dark red text */
        }
    </style>
</head>
<body>
    <h1>JavaScript Detection</h1>
    <div id="js-status"></div>

    <noscript>
        <!-- This message will show if JavaScript is disabled -->
        <style>
            #js-status {
                display: block; /* Show the message if JS is disabled */
                background-color: #f8d7da;
                color: #721c24;
                padding: 10px;
                border: 1px solid #f5c6cb;
                margin-top: 20px;
            }
        </style>
        <div>JavaScript is disabled in your browser settings. Please enable it for the best experience.</div>
    </noscript>

    <script>
        // Check if JavaScript is enabled and display appropriate message
        document.addEventListener("DOMContentLoaded", function() {
            const jsStatus = document.getElementById('js-status');
            jsStatus.style.display = 'block'; // Make the status visible
            
            // Indicate that JavaScript is enabled
            jsStatus.textContent = "JavaScript is enabled in your browser settings.";
            jsStatus.classList.add('enabled'); // Add enabled class for styling
        });
    </script>
</body>
</html>
```
