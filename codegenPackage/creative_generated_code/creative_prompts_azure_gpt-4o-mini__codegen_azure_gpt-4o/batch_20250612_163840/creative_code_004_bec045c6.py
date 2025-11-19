"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltovken.com
Prompt: How do I create a mobile-friendly webpage that prompts users to enable JavaScript, similar to imltovken.com?
Generated: DETERMINISTIC_bec045c6ebcd4846
Batch ID: 20250612_163840
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
    <meta name="description" content="A mobile-friendly webpage that prompts users to enable JavaScript.">
    <title>Enable JavaScript Prompt</title>
    <style>
        /* Basic CSS for mobile-friendly design */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
            text-align: center;
        }
        .no-js {
            color: #333;
            padding: 20px;
            background: #fff;
            border: 2px solid #ccc;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        .no-js h1 {
            font-size: 1.5em;
            margin-bottom: 1em;
        }
        .no-js p {
            font-size: 1em;
            margin: 0;
        }
    </style>
    <script>
        // This script removes the "no-js" message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function () {
            const noJsElement = document.querySelector('.no-js');
            if (noJsElement) {
                noJsElement.style.display = 'none';
            }
        });
    </script>
</head>
<body>
    <!-- Message displayed only when JavaScript is disabled -->
    <div class="no-js">
        <h1>JavaScript is required</h1>
        <p>To use this webpage, please enable JavaScript in your browser settings.</p>
    </div>
</body>
</html>
```
