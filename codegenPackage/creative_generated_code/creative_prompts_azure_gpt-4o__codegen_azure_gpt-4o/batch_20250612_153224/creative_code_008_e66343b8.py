"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolle.com.co
Prompt: Write a script to dynamically display Bollé's promotional banners, such as "Redescubre la Tierra con VOLT+ lenses," on a webpage.
Generated: DETERMINISTIC_e66343b8200173fd
Batch ID: 20250612_153224
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
  <title>Bollé Promotional Banner</title>
  <style>
    /* Basic styles for the banner */
    #promo-banner {
      display: none; /* Initially hidden */
      position: fixed;
      bottom: 0;
      width: 100%;
      background-color: #333;
      color: #fff;
      text-align: center;
      padding: 20px;
      font-size: 1.2em;
      z-index: 1000;
    }

    #promo-banner-close {
      position: absolute;
      top: 10px;
      right: 20px;
      background-color: #f00;
      color: #fff;
      border: none;
      cursor: pointer;
      padding: 5px 10px;
      font-size: 1em;
    }
  </style>
</head>
<body>
  <!-- Placeholder for the promo banner -->
  <div id="promo-banner">
    <button id="promo-banner-close">X</button>
    <span id="promo-text"></span>
  </div>

  <script>
    // Function to dynamically display Bollé's promotional banners.
    (function() {
      // Promotional messages array
      const promoMessages = [
        "Redescubre la Tierra con VOLT+ lenses",
        "Explora el mundo con Bollé's eco-friendly glasses",
        "Lentes VOLT+: Más claridad, menos reflejos"
      ];

      // Helper function to select a random promotional message
      function getRandomPromoMessage(messages) {
        return messages[Math.floor(Math.random() * messages.length)];
      }

      // DOM references
      const promoBanner = document.getElementById("promo-banner");
      const promoText = document.getElementById("promo-text");
      const closeButton = document.getElementById("promo-banner-close");

      // Error handling for DOM manipulation
      if (!promoBanner || !promoText || !closeButton) {
        console.error("Failed to find required DOM elements for the promotional banner.");
        return;
      }

      // Display the banner with a random promotional message
      promoText.textContent = getRandomPromoMessage(promoMessages);
      promoBanner.style.display = "block";

      // Event listener for the close button
      closeButton.addEventListener("click", function() {
        promoBanner.style.display = "none";
      });

      // Optional: Automatically hide the banner after a certain time (e.g., 10 seconds)
      setTimeout(() => {
        promoBanner.style.display = "none";
      }, 10000); // 10,000 ms = 10 seconds
    })();
  </script>
</body>
</html>
```
