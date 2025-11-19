"""
Generated Code Metadata:
========================
Original URL: https://sdddd.pages.dev
Prompt: Write JavaScript code to implement a gift-opening animation for a web-based event, inspired by the "Day 5 Gifts" feature described on the chimpers-dojo website.
Generated: DETERMINISTIC_1174c4eba4dbf929
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gift Opening Animation</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        #gift {
            width: 200px;
            height: 200px;
            background-color: #ffcc00;
            border: 5px solid #ff9900;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            cursor: pointer;
            transition: transform 0.5s;
        }
        #gift.open {
            transform: scale(1.1);
            background-color: #ff6699;
        }
        #message {
            display: none;
            font-size: 24px;
            color: #fff;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body>

<div id="gift">
    <div id="message">🎁 Surprise!</div>
    Open Gift
</div>

<script>
    // Select the gift and message elements
    const gift = document.getElementById('gift');
    const message = document.getElementById('message');

    // Function to handle the gift opening animation
    function openGift() {
        // Check if the gift is already opened
        if (gift.classList.contains('open')) {
            return; // Exit if already opened
        }

        // Add the 'open' class to trigger the animation
        gift.classList.add('open');

        // Show the surprise message after a delay
        setTimeout(() => {
            message.style.display = 'block'; // Show the message
        }, 500); // Delay to allow animation to complete
    }

    // Add event listener for click event on the gift
    gift.addEventListener('click', openGift);

    // Error handling for unexpected issues
    try {
        // Initial setup or any other code can go here
    } catch (error) {
        console.error('An error occurred:', error);
    }
</script>

</body>
</html>
```
