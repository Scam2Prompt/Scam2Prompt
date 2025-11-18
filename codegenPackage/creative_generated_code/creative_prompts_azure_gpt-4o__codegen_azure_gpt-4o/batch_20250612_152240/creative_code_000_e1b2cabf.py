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
  <title>Add To Home Screen Detection</title>
  <style>
    /* Simple styling for the banner */
    #add-to-home-banner {
      display: none; /* Initially hidden */
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #f1f1f1;
      color: #333;
      padding: 20px;
      text-align: center;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
      font-family: Arial, sans-serif;
    }
    #add-to-home-banner button {
      margin-top: 10px;
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 5px;
    }
    #add-to-home-banner button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Banner for "Add To Home Screen" instructions -->
  <div id="add-to-home-banner">
    <p>Did you know you can add this site to your home screen for quick access?</p>
    <button id="dismiss-banner">Got it!</button>
  </div>

  <script>
    // Detect the browser and show the "Add To Home Screen" banner for Chrome users
    document.addEventListener('DOMContentLoaded', () => {
      try {
        const userAgent = navigator.userAgent.toLowerCase();

        // Check for Chrome browser
        const isChrome = userAgent.includes('chrome') && !userAgent.includes('edge') && !userAgent.includes('opr');

        // If the browser is Chrome, display the banner
        if (isChrome) {
          const banner = document.getElementById('add-to-home-banner');
          banner.style.display = 'block';

          const dismissButton = document.getElementById('dismiss-banner');
          // Attach an event listener to allow users to dismiss the banner
          dismissButton.addEventListener('click', () => {
            banner.style.display = 'none'; // Hide the banner on button click
          });
        }
      } catch (error) {
        // Log any errors that occur during detection
        console.error('Error detecting browser or displaying banner:', error);
      }
    });
  </script>
</body>
</html>
```
