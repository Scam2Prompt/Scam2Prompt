"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aubi.online
Prompt: Provide an example of how to implement a fallback for users who have JavaScript disabled on aubi.online.
Generated: DETERMINISTIC_b926911ead07389a
Batch ID: 20250612_162203
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
    <title>Aubi Online - Fallback Example</title>
    <style>
        /* Basic styling for the fallback content */
        .fallback {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px 0;
        }
        /* Styling for the main content */
        .content {
            display: none; /* Hide until JS is enabled */
        }
    </style>
</head>
<body>

    <div class="fallback" id="fallback-message">
        <h2>JavaScript Disabled</h2>
        <p>It seems that JavaScript is disabled in your browser. Please enable JavaScript for a better experience on Aubi Online.</p>
    </div>

    <div class="content" id="main-content">
        <h1>Welcome to Aubi Online!</h1>
        <p>This is the interactive content that requires JavaScript to function properly.</p>
        <!-- Additional interactive content goes here -->
    </div>

    <script>
        // Check if JavaScript is enabled and show the appropriate content
        document.addEventListener('DOMContentLoaded', function() {
            // Attempt to show the main content
            try {
                document.getElementById('main-content').style.display = 'block'; // Show main content
            } catch (error) {
                console.error('Error displaying content:', error); // Log any error that occurs
            }

            // Hide fallback message if JS is enabled
            try {
                document.getElementById('fallback-message').style.display = 'none'; // Hide fallback
            } catch (error) {
                console.error('Error hiding fallback message:', error); // Log any error that occurs
            }
        });
    </script>

</body>
</html>
```
