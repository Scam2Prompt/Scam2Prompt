"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Generate code to create a promotional banner for special offers, such as "Entrenamiento Gratis para Generar Ingresos," on an e-commerce website.
Generated: DETERMINISTIC_3cafd1f9935d1ffa
Batch ID: 20250612_150618
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
  <title>Promotional Banner - Special Offers</title>
  <style>
    /* General styling for the banner */
    .promo-banner {
      background-color: #f8d210; /* Bright yellow for attention */
      color: #000; /* Black text for contrast */
      font-family: Arial, sans-serif;
      padding: 15px 20px;
      text-align: center;
      font-size: 1.2em;
      position: relative;
      border: 2px solid #000; /* Thin black border */
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    }

    /* Close button styling */
    .promo-banner-close {
      position: absolute;
      top: 10px;
      right: 15px;
      background-color: #000;
      color: #fff;
      border: none;
      border-radius: 50%;
      width: 25px;
      height: 25px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }

    .promo-banner-close:hover {
      background-color: #ff0000; /* Red hover effect for close button */
    }
  </style>
</head>
<body>

  <!-- Promotional banner section -->
  <div class="promo-banner" id="promoBanner">
    <span>🎉 Entrenamiento Gratis para Generar Ingresos 🎉</span>
    <button class="promo-banner-close" id="promoBannerClose">&times;</button>
  </div>

  <script>
    // JavaScript to handle banner functionality
    document.addEventListener('DOMContentLoaded', function () {
      const promoBanner = document.getElementById('promoBanner');
      const promoBannerClose = document.getElementById('promoBannerClose');

      // Close button event listener
      promoBannerClose.addEventListener('click', function () {
        promoBanner.style.display = 'none'; // Hide the banner
      });
    });
  </script>

</body>
</html>
```
