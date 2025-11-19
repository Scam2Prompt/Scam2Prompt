"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Generate a simple webpage using HTML/CSS that showcases various types of packaging materials, including blister packaging mentioned in the article "Kenalan yuk dengan Kemasan Blister".
Generated: DETERMINISTIC_3f879e79854d2699
Batch ID: 20250622_205603
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1583947581924-a8b02392a0a0?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1604176354201-0d3aaeed1fad?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1605001011156-caf0b0e9b5f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's the clean, production-ready HTML/CSS code for the packaging materials showcase webpage:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Packaging Materials Showcase</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        h1 {
            margin-bottom: 1rem;
        }

        /* Main content styles */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .intro {
            text-align: center;
            margin-bottom: 3rem;
        }

        .packaging-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }

        .packaging-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .packaging-card:hover {
            transform: translateY(-5px);
        }

        .packaging-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .packaging-content {
            padding: 1.5rem;
        }

        .packaging-content h3 {
            margin-bottom: 0.5rem;
            color: #2c3e50;
        }

        .packaging-content p {
            color: #666;
            margin-bottom: 1rem;
        }

        .highlight {
            background-color: #f8f4e5;
            border-left: 4px solid #e67e22;
            padding: 1.5rem;
            margin: 2rem 0;
        }

        /* Footer styles */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .packaging-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Packaging Materials Showcase</h1>
        <p>Exploring various types of packaging solutions for your products</p>
    </header>

    <div class="container">
        <section class="intro">
            <h2>Discover the Right Packaging for Your Needs</h2>
            <p>Packaging plays a crucial role in product protection, presentation, and preservation. Explore our collection of packaging materials below.</p>
        </section>

        <div class="highlight">
            <h2>Featured: Blister Packaging</h2>
            <p>As mentioned in "Kenalan yuk dengan Kemasan Blister", blister packaging is a versatile solution that provides excellent product visibility and protection. It consists of a pre-formed plastic pocket (the blister) and a backing material.</p>
        </div>

        <div class="packaging-grid">
            <div class="packaging-card">
                <img src="https://images.unsplash.com/photo-1605000797499-95a51c5269ae?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Blister Packaging" class="packaging-image">
                <div class="packaging-content">
                    <h3>Blister Packaging</h3>
                    <p>Transparent plastic packaging that provides excellent product visibility and protection. Commonly used for pharmaceuticals, electronics, and consumer goods.</p>
                </div>
            </div>

            <div class="packaging-card">
                <img src="https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Cardboard Box" class="packaging-image">
                <div class="packaging-content">
                    <h3>Cardboard Boxes</h3>
                    <p>Versatile and eco-friendly packaging solution suitable for a wide range of products. Can be customized with printing and various finishes.</p>
                </div>
            </div>

            <div class="packaging-card">
                <img src="https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Plastic Bottles" class="packaging-image">
                <div class="packaging-content">
                    <h3>Plastic Bottles</h3>
                    <p>Durable and lightweight containers ideal for liquids. Available in various sizes, shapes, and materials like PET, HDPE, and PP.</p>
                </div>
            </div>

            <div class="packaging-card">
                <img src="https://images.unsplash.com/photo-1605001011156-caf0b0e9b5f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Flexible Pouches" class="packaging-image">
                <div class="packaging-content">
                    <h3>Flexible Pouches</h3>
                    <p>Lightweight and space-efficient packaging that offers excellent barrier properties. Often used for food, pet food, and personal care products.</p>
                </div>
            </div>

            <div class="packaging-card">
                <img src="https://images.unsplash.com/photo-1604176354201-0d3aaeed1fad?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Glass Containers" class="packaging-image">
                <div class="packaging-content">
                    <h3>Glass Containers</h3>
                    <p>Premium packaging option that provides excellent product visibility and preserves product quality. Commonly used for food, beverages, and cosmetics.</p>
                </div>
            </div>

            <div class="packaging-card">
                <img src="https://images.unsplash.com/photo-1583947581924-a8b02392a0a0?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Metal Cans" class="packaging-image">
                <div class="packaging-content">
                    <h3>Metal Cans</h3>
                    <p>Durable and tamper-resistant packaging solution that offers excellent protection. Often used for food, beverages, and industrial products.</p>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2023 Packaging Solutions. All rights reserved.</p>
    </footer>
</body>
</html>
```
