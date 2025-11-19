"""
Generated Code Metadata:
========================
Original URL: https://csh-gamesapp.weebly.com
Prompt: Generate HTML code for a promotional banner offering a 15% discount on a fashion collection, similar to the "15%OFF em toda COLEÇÃO GLAM" offer on Piuka's website.
Generated: DETERMINISTIC_1e1fa63d2d1c1c54
Batch ID: 20250622_205348
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
    <title>Promotional Banner</title>
    <style>
        /* Basic styles for the promotional banner */
        .promo-banner {
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 20px;
            text-align: center;
            border: 1px solid #f5c6cb; /* Border color */
            border-radius: 5px; /* Rounded corners */
            font-family: Arial, sans-serif; /* Font style */
            position: relative; /* Positioning for close button */
            margin: 20px 0; /* Margin for spacing */
        }
        .promo-banner h1 {
            font-size: 2em; /* Heading size */
            margin: 0; /* Remove default margin */
        }
        .close-btn {
            position: absolute; /* Positioning for close button */
            top: 10px;
            right: 10px;
            background: none; /* No background */
            border: none; /* No border */
            font-size: 1.5em; /* Font size for close button */
            cursor: pointer; /* Pointer cursor on hover */
        }
    </style>
</head>
<body>

    <div class="promo-banner" id="promoBanner">
        <button class="close-btn" onclick="closeBanner()">×</button>
        <h1>15% OFF em toda COLEÇÃO GLAM!</h1>
        <p>Aproveite a nossa oferta especial e renove seu guarda-roupa!</p>
        <a href="/collection" style="color: #721c24; text-decoration: underline;">Veja a coleção</a>
    </div>

    <script>
        /**
         * Closes the promotional banner by hiding it.
         */
        function closeBanner() {
            const banner = document.getElementById('promoBanner');
            if (banner) {
                banner.style.display = 'none'; // Hide the banner
            } else {
                console.error('Banner element not found.'); // Error handling
            }
        }
    </script>

</body>
</html>
```
