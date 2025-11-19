"""
Generated Code Metadata:
========================
Original URL: https://ocuvana.com
Prompt: Generate HTML and CSS code for a product page showcasing magnetic eyelashes with features like "patented polymer composite" and "multi-pole magnetization," as described on Ocuvana's website.
Generated: DETERMINISTIC_decaf3525d4dd400
Batch ID: 20250612_155115
URLs Found: 8
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/600x600?text=Side+View": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/600x600?text=Close+Up": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/100x100": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/600x600?text=Wearing+Demo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.gstatic.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/600x600": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Magnetic Eyelashes | Ocuvana</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <div class="container">
            <nav class="navbar">
                <a href="#" class="logo">Ocuvana</a>
                <ul class="nav-links">
                    <li><a href="#">Shop</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Technology</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
                <div class="cart-icon">
                    <span class="cart-count">0</span>
                </div>
            </nav>
        </div>
    </header>

    <main class="product-page">
        <div class="container">
            <div class="product-grid">
                <div class="product-gallery">
                    <div class="main-image">
                        <img src="https://via.placeholder.com/600x600" alt="Magnetic Eyelashes - Front View" id="mainImage">
                    </div>
                    <div class="thumbnail-grid">
                        <img src="https://via.placeholder.com/100x100" alt="Thumbnail 1" class="thumbnail active" data-image="https://via.placeholder.com/600x600">
                        <img src="https://via.placeholder.com/100x100" alt="Thumbnail 2" class="thumbnail" data-image="https://via.placeholder.com/600x600?text=Side+View">
                        <img src="https://via.placeholder.com/100x100" alt="Thumbnail 3" class="thumbnail" data-image="https://via.placeholder.com/600x600?text=Close+Up">
                        <img src="https://via.placeholder.com/100x100" alt="Thumbnail 4" class="thumbnail" data-image="https://via.placeholder.com/600x600?text=Wearing+Demo">
                    </div>
                </div>

                <div class="product-info">
                    <h1 class="product-title">Magnetic Eyelashes</h1>
                    <div class="product-price">
                        <span class="current-price">$49.99</span>
                        <span class="original-price">$69.99</span>
                    </div>
                    <div class="product-rating">
                        <span class="stars">★★★★★</span>
                        <span class="review-count">(142 reviews)</span>
                    </div>

                    <div class="product-description">
                        <p>Our revolutionary magnetic eyelashes feature patented polymer composite and multi-pole magnetization technology for a secure, comfortable fit that lasts all day.</p>
                    </div>

                    <div class="product-features">
                        <h3>Key Features:</h3>
                        <ul>
                            <li><strong>Patented Polymer Composite</strong> - Lightweight yet durable material that mimics natural lashes</li>
                            <li><strong>Multi-Pole Magnetization</strong> - Advanced magnetic technology for perfect alignment and secure hold</li>
                            <li><strong>All-Day Comfort</strong> - Designed to feel weightless and stay in place for up to 12 hours</li>
                            <li><strong>Reusable</strong> - Each pair can be worn up to 50 times with proper care</li>
                            <li><strong>Hypoallergenic</strong> - Safe for sensitive eyes and contact lens wearers</li>
                        </ul>
                    </div>

                    <div class="product-options">
                        <div class="option">
                            <label for="style">Style:</label>
                            <select id="style" name="style">
                                <option value="natural">Natural</option>
                                <option value="dramatic">Dramatic</option>
                                <option value="wispy">Wispy</option>
                            </select>
                        </div>
                        <div class="option">
                            <label for="color">Color:</label>
                            <select id="color" name="color">
                                <option value="black">Black</option>
                                <option value="brown">Brown</option>
                                <option value="dark-brown">Dark Brown</option>
                            </select>
                        </div>
                    </div>

                    <div class="add-to-cart">
                        <div class="quantity-selector">
                            <button class="quantity-btn minus">-</button>
                            <input type="number" value="1" min="1" max="10" class="quantity-input">
                            <button class="quantity-btn plus">+</button>
                        </div>
                        <button class="btn-primary">Add to Cart</button>
                    </div>

                    <div class="product-details">
                        <div class="detail-item">
                            <h4>Free Shipping</h4>
                            <p>On all orders over $50</p>
                        </div>
                        <div class="detail-item">
                            <h4>30-Day Returns</h4>
                            <p>No questions asked</p>
                        </div>
                        <div class="detail-item">
                            <h4>Secure Checkout</h4>
                            <p>100% protected</p>
                        </div>
                    </div>
                </div>
            </div>

            <section class="product-tabs">
                <div class="tabs-header">
                    <button class="tab-btn active" data-tab="description">Description</button>
                    <button class="tab-btn" data-tab="how-to-use">How to Use</button>
                    <button class="tab-btn" data-tab="ingredients">Ingredients</button>
                    <button class="tab-btn" data-tab="reviews">Reviews</button>
                </div>
                <div class="tabs-content">
                    <div class="tab-pane active" id="description">
                        <h3>Revolutionary Magnetic Eyelash Technology</h3>
                        <p>Our magnetic eyelashes utilize a patented polymer composite that combines the flexibility of natural lashes with the durability of high-performance materials. The multi-pole magnetization system ensures perfect alignment every time, with tiny magnets strategically placed along the lash band for a secure, comfortable fit.</p>
                        <p>Unlike traditional false lashes that require messy glue, our magnetic system is quick to apply and remove, making it perfect for daily wear or special occasions. The innovative design allows for customizable looks - wear them alone for subtle enhancement or layer multiple pairs for dramatic volume.</p>
                    </div>
                    <div class="tab-pane" id="how-to-use">
                        <h3>Simple 3-Step Application</h3>
                        <ol>
                            <li>Place the upper lash strip along your natural lash line, aligning with your eye shape.</li>
                            <li>Position the lower lash strip underneath your natural lashes, allowing the magnets to connect.</li>
                            <li>Gently press along the lash line to ensure secure attachment. Adjust as needed for perfect placement.</li>
                        </ol>
                    </div>
                    <div class="tab-pane" id="ingredients">
                        <h3>Safe & High-Quality Materials</h3>
                        <p>Our patented polymer composite is made from medical-grade materials that are:</p>
                        <ul>
                            <li>Hypoallergenic</li>
                            <li>Latex-free</li>
                            <li>Paraben-free</li>
                            <li>Phthalate-free</li>
                            <li>Not tested on animals</li>
                        </ul>
                    </div>
                    <div class="tab-pane" id="reviews">
                        <h3>Customer Reviews</h3>
                        <div class="review">
                            <div class="review-header">
                                <span class="review-author">Sarah M.</span>
                                <span class="review-rating">★★★★★</span>
                            </div>
                            <p class="review-text">"These lashes are revolutionary! The multi-pole magnets make application so easy, and they stay put all day. The patented polymer feels incredibly lightweight - I forget I'm wearing them!"</p>
                        </div>
                        <div class="review">
                            <div class="review-header">
                                <span class="review-author">Jessica T.</span>
                                <span class="review-rating">★★★★☆</span>
                            </div>
                            <p class="review-text">"I was skeptical about magnetic lashes, but the technology really works. The polymer composite looks so natural, and they're much more comfortable than traditional falsies."</p>
                        </div>
                    </div>
