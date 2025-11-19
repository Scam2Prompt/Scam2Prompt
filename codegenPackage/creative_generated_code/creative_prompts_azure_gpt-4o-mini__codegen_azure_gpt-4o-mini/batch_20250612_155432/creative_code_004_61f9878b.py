"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo9969.infinityfreeapp.com
Prompt: How do I create a fallback for users without Javascript support in my web application?
Generated: DETERMINISTIC_61f9878b91b951b9
Batch ID: 20250612_155432
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
        /* Styles for the JavaScript-dependent content */
        .js-content {
            display: none; /* Hide by default */
        }
        
        /* Styles for the fallback content */
        .fallback-content {
            display: block; /* Show fallback by default */
            background-color: #f9f9f9;
            padding: 20px;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>

    <!-- Fallback content for users without JavaScript -->
    <div class="fallback-content">
        <h1>Welcome to Our Web Application!</h1>
        <p>This application requires JavaScript to function properly. Please enable JavaScript or update your browser.</p>
    </div>

    <!-- JavaScript-dependent content -->
    <div class="js-content" id="jsContent">
        <h1>Welcome to Our JavaScript Enhanced Web Application!</h1>
        <p>This content is only visible if JavaScript is enabled.</p>
        <button id="actionButton">Click Me!</button>
    </div>

    <script>
        // This function runs when the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", function() {
            try {
                // Show JavaScript content when JS is enabled
                document.querySelector('.js-content').style.display = 'block';
                
                // Hide fallback content
                document.querySelector('.fallback-content').style.display = 'none';

                // Add a click event listener to the button
                document.getElementById('actionButton').addEventListener('click', function() {
                    alert('JavaScript is working!');
                });

            } catch (error) {
                // Log error to the console for debugging
                console.error('An error occurred while initializing the JS content:', error);
            }
        });
    </script>
</body>
</html>
```
