"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonbd.com
Prompt: Provide a code snippet that detects JavaScript support in a mobile browser and displays a message to users on cryptonbd.com.
Generated: DETERMINISTIC_865d00096445cf10
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
    <title>JavaScript Support Detection</title>
    <style>
        #js-message {
            display: none;
            background-color: #f0f8ff;
            border: 1px solid #b0e0e6;
            padding: 20px;
            margin: 20px;
            border-radius: 5px;
            text-align: center;
        }
    </style>
</head>
<body>

    <div id="js-message">JavaScript is enabled in your browser!</div>

    <script>
        // Function to detect JavaScript support
        function detectJavaScript() {
            try {
                // Check if the document object is accessible
                if (typeof document !== "undefined") {
                    // Show the message if JavaScript is supported
                    document.getElementById('js-message').style.display = 'block';
                } else {
                    throw new Error("Document is not defined");
                }
            } catch (error) {
                // Log the error for debugging purposes
                console.error("JavaScript detection error:", error);
            }
        }

        // Execute the detection function
        detectJavaScript();
    </script>
    
</body>
</html>
```
