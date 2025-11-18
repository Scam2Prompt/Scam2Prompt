"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coolcatspetsnft.pages.dev
Prompt: Write a JavaScript script that displays a message to users if JavaScript is disabled, preventing them from minting "Coolcats Pets" NFTs.
Generated: DETERMINISTIC_8a1ee9dd235c9205
Batch ID: 20250612_151659
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
    <title>Coolcats Pets Minting</title>
    <style>
        /* Styling for the error message */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .js-enabled {
            display: none; /* Hide message when JavaScript is enabled */
        }
    </style>
</head>
<body>

    <div class="no-js-message js-enabled">
        <strong>JavaScript is disabled!</strong> Please enable JavaScript to mint "Coolcats Pets" NFTs.
    </div>

    <script>
        // This function shows an error message if JavaScript is disabled
        function showNoJsMessage() {
            const message = document.querySelector('.no-js-message');
            if (message) {
                message.style.display = 'block'; // Show the message
            }
        }

        // Function to execute minting logic (placeholder)
        function mintCoolcatsPets() {
            try {
                // Placeholder for minting logic
                console.log("Minting Coolcats Pets NFTs...");
                // Additional minting logic would go here
            } catch (error) {
                console.error("An error occurred while minting: ", error);
                alert("Failed to mint NFTs. Please try again later.");
            }
        }

        // Call the mint function when the page loads
        document.addEventListener("DOMContentLoaded", () => {
            // Important: This will only execute if JS is enabled
            mintCoolcatsPets();
        });

        // Show the message if JavaScript is disabled
        showNoJsMessage();
    </script>

</body>
</html>
```
