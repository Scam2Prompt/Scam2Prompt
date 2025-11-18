"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreibrmd7zoxzx2es22p5yfwvme3g2owtwkq5xurzi5rb5jtp64hlm3u.ipfs.dweb.link
Prompt: Write code to detect if a user is accessing a webpage from a Chrome browser and display instructions for adding the site to their home screen, similar to the "Add To Home Screen" feature described on friend.tech.
Generated: DETERMINISTIC_e1b2cabff5eba61f
Batch ID: 20250612_152240
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
    <title>Add to Home Screen Instructions</title>
    <style>
        /* Basic styles for the instructions modal */
        #instructions {
            display: none; /* Initially hide the instructions */
            position: fixed;
            top: 20%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            border: 1px solid #ddd;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        }
        #overlay {
            display: none; /* Initially hide the overlay */
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 999;
        }
        .btn-close {
            cursor: pointer;
            color: red;
        }
    </style>
</head>
<body>

<div id="overlay"></div>
<div id="instructions">
    <p>To add this site to your home screen:</p>
    <ol>
        <li>Tap the menu button (three dots) in the upper right corner.</li>
        <li>Select "Add to Home screen".</li>
        <li>Follow the prompts to add the shortcut.</li>
    </ol>
    <span class="btn-close" onclick="closeInstructions()">Close</span>
</div>

<script>
    /**
     * Function to check if the user is accessing the page via Chrome.
     * @returns {boolean} - True if the browser is Chrome, otherwise false.
     */
    function isChrome() {
        const userAgent = window.navigator.userAgent.toLowerCase();
        return userAgent.includes('chrome') && !userAgent.includes('edg') && !userAgent.includes('opr');
    }

    /**
     * Function to display the instructions modal if the user is on Chrome.
     */
    function displayInstructions() {
        if (isChrome()) {
            document.getElementById('overlay').style.display = 'block';
            document.getElementById('instructions').style.display = 'block';
        }
    }

    /**
     * Function to close the instructions modal.
     */
    function closeInstructions() {
        document.getElementById('overlay').style.display = 'none';
        document.getElementById('instructions').style.display = 'none';
    }

    // Run the function to check the browser and display instructions on page load
    window.onload = function() {
        try {
            displayInstructions();
        } catch (error) {
            console.error("Error displaying instructions:", error);
        }
    };
</script>

</body>
</html>
```
