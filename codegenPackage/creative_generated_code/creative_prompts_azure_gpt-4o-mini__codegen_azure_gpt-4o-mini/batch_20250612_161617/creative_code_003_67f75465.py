"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeta-chain.com
Prompt: Generate code that checks if JavaScript is enabled before accessing Zeta Chain's services.
Generated: DETERMINISTIC_67f75465501b2b40
Batch ID: 20250612_161617
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
    <title>Zeta Chain Service Check</title>

    <style>
        /* Style for the error message */
        .error-message {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <noscript>
        <div class="error-message">
            JavaScript is disabled in your browser. Please enable JavaScript to access Zeta Chain's services.
        </div>
    </noscript>

    <script>
        // Function to initialize Zeta Chain services
        function initializeZetaChain() {
            try {
                // Check if the Zeta Chain JavaScript library is loaded
                if (typeof ZetaChain === 'undefined') {
                    throw new Error("Zeta Chain library is not loaded.");
                }

                // Proceed with initializing services
                ZetaChain.initialize();
                console.log("Zeta Chain services initialized successfully.");

            } catch (error) {
                // Log the error and display a user-friendly message
                console.error("Error initializing Zeta Chain services:", error);
                alert("An error occurred while initializing Zeta Chain services. Please try again later.");
            }
        }

        // Check if JavaScript is enabled and then initialize Zeta Chain services
        document.addEventListener("DOMContentLoaded", function() {
            initializeZetaChain();
        });
    </script>

</body>
</html>
```
