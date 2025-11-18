"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.si
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on https://blur.si.
Generated: DETERMINISTIC_477966857459a23d
Batch ID: 20250612_151610
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
        /* Basic styling for the message */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
            text-align: center;
        }
    </style>
    <noscript>
        <style>
            /* Show message if JavaScript is disabled */
            .no-js-message {
                display: block; /* Display the message */
            }
        </style>
    </noscript>
</head>
<body>

    <!-- Message to be displayed if JavaScript is disabled -->
    <div class="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong> 
        Please enable JavaScript to use this website properly.
    </div>

    <script>
        // Function to initialize application
        function init() {
            try {
                // Check if JavaScript is working
                console.log("JavaScript is enabled.");
                // Your main application logic goes here
            } catch (error) {
                // Log any errors encountered during execution
                console.error("An error occurred during initialization: ", error);
            }
        }

        // Call the initialization function
        init();
    </script>

</body>
</html>
```
