"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pump-funs.pages.dev
Prompt: Generate code to toggle animations for token listings on a webpage, mimicking the "Show animations: On/Off" feature described on https://pump-funs.pages.dev.
Generated: DETERMINISTIC_bbd3987d90a91241
Batch ID: 20250612_151310
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
    <title>Token Listings Animation Toggle</title>
    <style>
        /* Basic styles for the token listings */
        .token-listing {
            transition: all 0.3s ease;
            opacity: 1;
        }
        .hidden {
            opacity: 0; /* Hide tokens when animations are off */
        }
    </style>
</head>
<body>

    <h1>Token Listings</h1>
    <button id="toggleAnimations">Show Animations: On</button>

    <div id="tokenContainer">
        <div class="token-listing">Token 1</div>
        <div class="token-listing">Token 2</div>
        <div class="token-listing">Token 3</div>
    </div>

    <script>
        // Initialize state for animation toggle
        let animationsEnabled = true;

        // Function to toggle animations
        function toggleAnimations() {
            animationsEnabled = !animationsEnabled; // Toggle state

            // Get all token listings
            const tokenListings = document.querySelectorAll('.token-listing');

            // Update button text and toggle animation class
            const button = document.getElementById('toggleAnimations');
            button.innerText = animationsEnabled ? 'Show Animations: On' : 'Show Animations: Off';

            tokenListings.forEach(token => {
                if (animationsEnabled) {
                    token.classList.remove('hidden'); // Show token
                } else {
                    token.classList.add('hidden'); // Hide token
                }
            });
        }

        // Add event listener for the toggle button
        document.getElementById('toggleAnimations').addEventListener('click', () => {
            try {
                toggleAnimations(); // Call the function to toggle animations
            } catch (error) {
                console.error('Error toggling animations:', error); // Log any errors
            }
        });
    </script>
</body>
</html>
```
