"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Write code to integrate social media sharing buttons (Facebook, Twitter, Instagram, LinkedIn) into a wire mesh product website, as seen on the Baochuan Wire Mesh site.
Generated: DETERMINISTIC_fabd4b3ce7123deb
Batch ID: 20250612_151811
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://twitter.com/intent/tweet?url=https://example.com/product&text=Check+out+this+wire+mesh+product!": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u=https://example.com/product": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/product`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.instagram.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.linkedin.com/sharing/share-offsite/?url=https://example.com/product": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wire Mesh Product</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Baochuan Wire Mesh</h1>
    </header>

    <main>
        <section class="product-details">
            <h2>Product Name</h2>
            <p>Description of the wire mesh product.</p>
            <img src="product.jpg" alt="Wire Mesh Product" />
        </section>

        <section class="social-sharing">
            <h3>Share this product:</h3>
            <div class="share-buttons">
                <!-- Facebook Share Button -->
                <a href="https://www.facebook.com/sharer/sharer.php?u=https://example.com/product" 
                   target="_blank" 
                   rel="noopener noreferrer" 
                   aria-label="Share on Facebook">
                    <img src="facebook-icon.png" alt="Facebook" />
                </a>

                <!-- Twitter Share Button -->
                <a href="https://twitter.com/intent/tweet?url=https://example.com/product&text=Check+out+this+wire+mesh+product!" 
                   target="_blank" 
                   rel="noopener noreferrer" 
                   aria-label="Share on Twitter">
                    <img src="twitter-icon.png" alt="Twitter" />
                </a>

                <!-- Instagram Share Button -->
                <a href="https://www.instagram.com/" 
                   target="_blank" 
                   rel="noopener noreferrer" 
                   aria-label="Share on Instagram">
                    <img src="instagram-icon.png" alt="Instagram" />
                </a>

                <!-- LinkedIn Share Button -->
                <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://example.com/product" 
                   target="_blank" 
                   rel="noopener noreferrer" 
                   aria-label="Share on LinkedIn">
                    <img src="linkedin-icon.png" alt="LinkedIn" />
                </a>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Baochuan Wire Mesh. All rights reserved.</p>
    </footer>

    <script src="scripts.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General body styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

/* Header styles */
header {
    background-color: #007BFF;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

/* Product details section styling */
.product-details {
    padding: 20px;
}

/* Social sharing section styling */
.social-sharing {
    margin: 20px 0;
}

/* Share buttons styling */
.share-buttons a {
    margin: 0 10px;
    display: inline-block;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background-color: #f1f1f1;
}
```

```javascript
// scripts.js

// Optional: Enhance user experience by logging share events
document.querySelectorAll('.share-buttons a').forEach(button => {
    button.addEventListener('click', (event) => {
        console.log(`User clicked to share on ${event.currentTarget.getAttribute('aria-label')}`);
    });
});
```

Make sure to replace the placeholder URLs (`https://example.com/product`) and image sources (`facebook-icon.png`, etc.) with actual links and images relevant to your website.
