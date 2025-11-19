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
</head>
<body>
  <script>
    // Function to safely write a custom message into the webpage using document.write
    function insertMessage(message) {
      try {
        // Validate that the message is a non-empty string
        if (typeof message !== 'string' || message.trim() === '') {
          throw new Error('Invalid message: Message must be a non-empty string.');
        }

        // Insert the message into the webpage using document.write
        document.write('<p>' + message + '</p>');
      } catch (error) {
        // Handle errors gracefully
        console.error('Error inserting message:', error.message);
      }
    }

    // Example usage of the function
    insertMessage('Hello, welcome to my webpage!');
  </script>
</body>
</html>
```
