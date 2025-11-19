"""
Generated Code Metadata:
========================
Original URL: https://sdddd.pages.dev
Prompt: Write a code snippet to implement a simple gift-opening animation using JavaScript and HTML, inspired by the Day 5 Gifts idea on chimpers-dojo.
Generated: DETERMINISTIC_6e5d022205c9864f
Batch ID: 20250622_204752
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
            position: relative;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.5s ease;
        }
        #gift.open {
            transform: scale(1.1);
        }
        #ribbon {
            position: absolute;
            top: 0;
            left: 50%;
            width: 100%;
            height: 20px;
            background-color: #ff0000;
            transform: translateX(-50%);
            transition: height 0.5s ease;
        }
        #content {
            display: none;
            text-align: center;
            padding: 20px;
            font-size: 1.5em;
            color: #333;
        }
    </style>
</head>
<body>

<div id="gift">
    <div id="ribbon"></div>
    <div id="content">🎉 Surprise! 🎉</div>
</div>

<script>
    // Get references to the gift and content elements
    const gift = document.getElementById('gift');
    const ribbon = document.getElementById('ribbon');
    const content = document.getElementById('content');

    // Function to handle the gift opening animation
    function openGift() {
        // Add the 'open' class to animate the gift
        gift.classList.add('open');

        // Animate the ribbon height to simulate it falling
        ribbon.style.height = '0';

        // Show the content after a delay
        setTimeout(() => {
            content.style.display = 'block';
        }, 500); // Delay matches the ribbon animation duration
    }

    // Add event listener for click event to open the gift
    gift.addEventListener('click', openGift);
</script>

</body>
</html>
```
