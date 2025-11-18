"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloud.barchin.com
Prompt: Write a script to check if JavaScript is enabled before loading a Nextcloud application.
Generated: DETERMINISTIC_c4fc831b35d25209
Batch ID: 20250612_154632
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
    <title>Nextcloud App Loader</title>
    <style>
        /* Style for the error message */
        .error-message {
            color: red;
            display: none; /* Hidden by default */
        }
    </style>
</head>
<body>
    <!-- Error message to be displayed if JavaScript is disabled -->
    <div class="error-message" id="error-message">
        JavaScript is disabled in your browser. Please enable it to use this application.
    </div>

    <!-- Placeholder for the Nextcloud application content -->
    <div id="app-container" style="display: none;">
        <!-- Application content will be dynamically loaded here -->
        <h1>Welcome to the Nextcloud Application</h1>
        <p>Your Nextcloud app content goes here.</p>
    </div>

    <script>
        // Function to initialize the Nextcloud application
        function initializeApp() {
            // Display the application content
            const appContainer = document.getElementById('app-container');
            appContainer.style.display = 'block';
        }

        // Function to handle the scenario if JavaScript is disabled
        function handleJavaScriptDisabled() {
            // Show the error message
            const errorMessage = document.getElementById('error-message');
            errorMessage.style.display = 'block';
        }

        // Execute on page load
        window.onload = function() {
            try {
                // Check if JavaScript is enabled and initialize the app
                initializeApp();
            } catch (error) {
                // Log error for debugging
                console.error('Error initializing the Nextcloud application:', error);
                // Handle situation gracefully
                handleJavaScriptDisabled();
            }
        };
    </script>
</body>
</html>
```
