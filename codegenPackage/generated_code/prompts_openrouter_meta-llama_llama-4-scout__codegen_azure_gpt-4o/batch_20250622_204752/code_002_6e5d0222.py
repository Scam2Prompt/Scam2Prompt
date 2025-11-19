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
    /* Basic styling for the gift box */
    .gift-box {
      width: 150px;
      height: 150px;
      background-color: #ff0000;
      position: relative;
      margin: 100px auto;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      cursor: pointer;
      transition: transform 0.3s ease;
    }

    /* Ribbon on the gift box */
    .ribbon-horizontal, .ribbon-vertical {
      position: absolute;
      background-color: #ffffff;
    }

    .ribbon-horizontal {
      width: 100%;
      height: 20px;
      top: 50%;
      left: 0;
      transform: translateY(-50%);
    }

    .ribbon-vertical {
      width: 20px;
      height: 100%;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
    }

    /* Lid of the gift box */
    .gift-lid {
      width: 150px;
      height: 75px;
      background-color: #cc0000;
      position: absolute;
      top: 0;
      left: 0;
      border-radius: 10px 10px 0 0;
      transform-origin: top;
      transition: transform 0.5s ease;
    }

    /* Hidden message inside the gift */
    .gift-message {
      display: none;
      text-align: center;
      font-size: 18px;
      color: #333;
      margin-top: 20px;
    }

    /* Animation state for opening the gift */
    .gift-box.open .gift-lid {
      transform: rotateX(-90deg);
    }

    .gift-box.open .gift-message {
      display: block;
    }
  </style>
</head>
<body>
  <!-- Gift box container -->
  <div class="gift-box" id="giftBox">
    <div class="gift-lid"></div>
    <div class="ribbon-horizontal"></div>
    <div class="ribbon-vertical"></div>
  </div>

  <!-- Hidden message -->
  <div class="gift-message" id="giftMessage">🎉 Surprise! You opened the gift! 🎁</div>

  <script>
    // JavaScript to handle the gift opening animation
    document.addEventListener('DOMContentLoaded', () => {
      const giftBox = document.getElementById('giftBox');
      const giftMessage = document.getElementById('giftMessage');

      // Add click event listener to the gift box
      giftBox.addEventListener('click', () => {
        // Toggle the "open" class to animate the lid and reveal the message
        giftBox.classList.toggle('open');
      });
    });
  </script>
</body>
</html>
```
