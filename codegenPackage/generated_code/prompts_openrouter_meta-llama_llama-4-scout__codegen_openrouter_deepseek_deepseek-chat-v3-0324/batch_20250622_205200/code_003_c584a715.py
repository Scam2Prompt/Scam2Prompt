"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: What are some key features of a power washing service website, and provide an example of how to implement a gallery section using HTML and CSS, similar to Klean-Pro Utah's website?
Generated: DETERMINISTIC_c584a715407d6347
Batch ID: 20250622_205200
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/before-after-1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/fence-cleaning.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/house-wash.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/deck-cleaning.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/roof-cleaning.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/concrete-cleaning.jpg": {
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
    <title>Power Washing Services | Gallery</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 1rem 0;
        }
        
        nav ul li {
            margin: 0 1rem;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }
        
        nav ul li a:hover {
            color: #3498db;
        }
        
        /* Gallery section */
        .gallery-section {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .gallery-section h2 {
            text-align: center;
            margin-bottom: 2rem;
            color: #2c3e50;
            font-size: 2rem;
        }
        
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }
        
        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        
        .gallery-item:hover {
            transform: scale(1.03);
        }
        
        .gallery-item img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            display: block;
            transition: opacity 0.3s;
        }
        
        .gallery-item:hover img {
            opacity: 0.9;
        }
        
        .gallery-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 1rem;
            transform: translateY(100%);
            transition: transform 0.3s;
        }
        
        .gallery-item:hover .gallery-caption {
            transform: translateY(0);
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .gallery-grid {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            }
            
            nav ul {
                flex-direction: column;
            }
            
            nav ul li {
                margin: 0.5rem 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Power Washing Pro</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="gallery.html">Gallery</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <section class="gallery-section">
        <h2>Our Work Gallery</h2>
        <div class="gallery-grid">
            <div class="gallery-item">
                <img src="https://example.com/images/before-after-1.jpg" alt="Driveway before and after power washing">
                <div class="gallery-caption">
                    <h3>Driveway Restoration</h3>
                    <p>Complete transformation of a stained driveway</p>
                </div>
            </div>
            
            <div class="gallery-item">
                <img src="https://example.com/images/deck-cleaning.jpg" alt="Wooden deck after power washing">
                <div class="gallery-caption">
                    <h3>Deck Cleaning</h3>
                    <p>Restored wooden deck to like-new condition</p>
                </div>
            </div>
            
            <div class="gallery-item">
                <img src="https://example.com/images/house-wash.jpg" alt="House exterior after power washing">
                <div class="gallery-caption">
                    <h3>House Wash</h3>
                    <p>Removed years of dirt and grime buildup</p>
                </div>
            </div>
            
            <div class="gallery-item">
                <img src="https://example.com/images/roof-cleaning.jpg" alt="Roof before and after cleaning">
                <div class="gallery-caption">
                    <h3>Roof Cleaning</h3>
                    <p>Eliminated moss and algae growth</p>
                </div>
            </div>
            
            <div class="gallery-item">
                <img src="https://example.com/images/concrete-cleaning.jpg" alt="Concrete patio after cleaning">
                <div class="gallery-caption">
                    <h3>Concrete Cleaning</h3>
                    <p>Patio restored to original color</p>
                </div>
            </div>
            
            <div class="gallery-item">
                <img src="https://example.com/images/fence-cleaning.jpg" alt="Wooden fence after power washing">
                <div class="gallery-caption">
                    <h3>Fence Restoration</h3>
                    <p>Wood fence looks brand new</p>
                </div>
            </div>
        </div>
    </section>
</body>
</html>
```
