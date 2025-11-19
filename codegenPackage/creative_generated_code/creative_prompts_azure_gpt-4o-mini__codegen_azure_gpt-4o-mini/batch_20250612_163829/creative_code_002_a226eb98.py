"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bot12.cc
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_163829
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
        /* Styles for the message */
        #js-enabled {
            display: none; /* Initially hidden */
            color: green;
            font-weight: bold;
        }
        #js-disabled {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <!-- Message displayed if JavaScript is enabled -->
    <div id="js-enabled">JavaScript is enabled in your browser.</div>
    
    <!-- Message displayed if JavaScript is disabled -->
    <noscript>
        <div id="js-disabled">JavaScript is disabled in your browser. Please enable it for the best experience.</div>
    </noscript>

    <script>
        // Function to display a message confirming JavaScript is enabled
        function checkJavaScriptEnabled() {
            // Select the message element for JavaScript enabled
            const jsEnabledMessage = document.getElementById('js-enabled');
            // Display the message
            jsEnabledMessage.style.display = 'block';
        }

        // Execute the function to show that JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
     // Call the example function
                showAlert();
            } catch (error) {
                // Log any errors to the console
                console.error("An error occurred:", error);
            }
        });
    </script>
</body>
</html>
```
