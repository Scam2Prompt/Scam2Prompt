"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-doodles.claims
Prompt: Provide an example of using document.write() to insert a custom message into a webpage.
Generated: DETERMINISTIC_0f787d0deef0ea6f
Batch ID: 20250612_162701
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
    <title>Document Write Example</title>
    <script>
        // Function to insert a custom message into the webpage
        function insertMessage(message) {
            try {
                // Check if message is a valid string
                if (typeof message !== 'string') {
                    throw new Error('Invalid message: message must be a string.');
                }
                // Insert the message into the document using document.write
                document.write('<h1>' + message + '</h1>');
            } catch (error) {
                // Log error to the console
                console.error('Error inserting message:', error);
            }
        }

        // Call the function with a custom message
        // This will execute when the script loads
        insertMessage('Hello, welcome to my webpage!');
    </script>
</head>
<body>
    <!-- The message will be inserted here -->
</body>
</html>
```
