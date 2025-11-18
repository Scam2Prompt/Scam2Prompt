"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ham-drops.pages.dev
Prompt: Generate JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, as seen in "Hamster Kombat."
Generated: DETERMINISTIC_4bf710f012295a30
Batch ID: 20250612_151024
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
        /* Style for the fallback message */
        .no-js-message {
            display: none; /* Initially hidden */
            color: red;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <noscript>
        <!-- Content displayed when JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block; /* Show message if JavaScript is disabled */
            }
        </style>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to enjoy the full experience of Hamster Kombat!
        </div>
    </noscript>
</head>
<body>
    <!-- Main content -->
    <div id="content">
        <h1>Welcome to Hamster Kombat!</h1>
        <p>Prepare for the ultimate battle of hamsters.</p>
    </div>

    <script>
        // JavaScript runs successfully if it reaches this point
        document.addEventListener("DOMContentLoaded", () => {
            // Remove the fallback message (if any exists)
            const fallbackMessage = document.querySelector(".no-js-message");
            if (fallbackMessage) {
                fallbackMessage.style.display = "none";
            }
        });
    </script>
</body>
</html>
```
