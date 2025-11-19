"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobken.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Basic styling for messages */
        .message {
            font-size: 20px;
            margin: 20px;
            display: none; /* Hidden by default, will be shown by JavaScript */
        }
        .js-enabled {
            color: green;
        }
        .js-disabled {
            color: red;
        }
    </style>
</head>
<body>
    <div id="js-check" class="message js-enabled">JavaScript is enabled in your browser!</div>
    <noscript>
        <div id="js-check" class="message js-disabled">JavaScript is disabled in your browser!</div>
    </noscript>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            const jsMessage = document.getElementById("js-check");
            jsMessage.style.display = "block"; // Show the message if JS is enabled
        });
    </script>
</body>
</html>
```
ript enabled
                document.getElementById('js-enabled').style.display = 'block';
                // Hide message for JavaScript disabled
                document.getElementById('js-disabled').style.display = 'none';
            } catch (error) {
                // Log error to console if something goes wrong
                console.error('Error checking JavaScript status:', error);
            }
        }

        // Execute the function to check JavaScript status
        checkJavaScriptEnabled();
    </script>
    
</body>
</html>
```
