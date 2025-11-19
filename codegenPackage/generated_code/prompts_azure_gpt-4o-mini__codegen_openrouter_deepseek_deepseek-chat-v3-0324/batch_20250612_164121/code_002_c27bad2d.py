"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Create a sample HTML page that showcases a selection of custom championship belts, including images and descriptions, similar to the product display on Belts Mania.
Generated: DETERMINISTIC_c27bad2d955676c0
Batch ID: 20250612_164121
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/300x200?text=Lightweight": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Heavyweight": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Legacy": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=World+Champion": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Tag+Team": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Custom+Design": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML page showcasing custom championship belts:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Championship Belts Collection | Belts Mania</title>
    <meta name="description" content="Premium custom championship belts for sports, wrestling, and special events">
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }
        
        /* Header styles */
        header {
            background-color: #1a1a1a;
            color: #fff;
            padding: 1.5rem 0;
            text-align: center;
        }
        
        .logo {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .tagline {
            font-style: italic;
            color: #ccc;
        }
        
        /* Main content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        .page-title {
            text-align: center;
            margin-bottom: 2rem;
            color: #222;
        }
        
        /* Belt grid */
        .belt-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .belt-card {
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .belt-card:hover {
            transform: translateY(-5px);
        }
        
        .belt-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        
        .belt-info {
            padding: 1.5rem;
        }
        
        .belt-title {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
            color: #1a1a1a;
        }
        
        .belt-description {
            color: #666;
            margin-bottom: 1rem;
        }
        
        .belt-price {
            font-weight: bold;
            color: #b8860b;
            font-size: 1.2rem;
        }
        
        .cta-button {
            display: inline-block;
            background-color: #b8860b;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 1rem;
            transition: background-color 0.3s;
        }
        
        .cta-button:hover {
            background-color: #996515;
        }
        
        /* Footer */
        footer {
            background-color: #1a1a1a;
            color: #fff;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-bottom: 1rem;
        }
        
        .footer-links a {
            color: #ccc;
            text-decoration: none;
        }
        
        .footer-links a:hover {
            color: #b8860b;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .belt-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">BELTS MANIA</div>
        <div class="tagline">Custom Championship Belts for Champions</div>
    </header>
    
    <main class="container">
        <h1 class="page-title">Premium Championship Belts</h1>
        
        <div class="belt-grid">
            <!-- Belt 1 -->
            <div class="belt-card">
                <img src="https://via.placeholder.com/300x200?text=World+Champion" alt="World Champion Belt" class="belt-image">
                <div class="belt-info">
                    <h2 class="belt-title">World Champion Belt</h2>
                    <p class="belt-description">Our flagship design featuring 24k gold plating, genuine leather, and custom nameplate. The ultimate symbol of victory.</p>
                    <div class="belt-price">$1,299.99</div>
                    <a href="#order" class="cta-button">Customize Now</a>
                </div>
            </div>
            
            <!-- Belt 2 -->
            <div class="belt-card">
                <img src="https://via.placeholder.com/300x200?text=Heavyweight" alt="Heavyweight Championship Belt" class="belt-image">
                <div class="belt-info">
                    <h2 class="belt-title">Heavyweight Championship</h2>
                    <p class="belt-description">Extra-wide design with reinforced steel plates. Perfect for boxing, MMA, or wrestling champions.</p>
                    <div class="belt-price">$999.99</div>
                    <a href="#order" class="cta-button">Customize Now</a>
                </div>
            </div>
            
            <!-- Belt 3 -->
            <div class="belt-card">
                <img src="https://via.placeholder.com/300x200?text=Tag+Team" alt="Tag Team Championship Belt" class="belt-image">
                <div class="belt-info">
                    <h2 class="belt-title">Tag Team Championship</h2>
                    <p class="belt-description">Double-wide design with dual nameplates. Celebrate your team's dominance in style.</p>
                    <div class="belt-price">$1,499.99</div>
                    <a href="#order" class="cta-button">Customize Now</a>
                </div>
            </div>
            
            <!-- Belt 4 -->
            <div class="belt-card">
                <img src="https://via.placeholder.com/300x200?text=Legacy" alt="Legacy Championship Belt" class="belt-image">
                <div class="belt-info">
                    <h2 class="belt-title">Legacy Championship</h2>
                    <p class="belt-description">Vintage-inspired design with antique gold finish. For those who value tradition and prestige.</p>
                    <div class="belt-price">$1,199.99</div>
                    <a href="#order" class="cta-button">Customize Now</a>
                </div>
            </div>
            
            <!-- Belt 5 -->
            <div class="belt-card">
                <img src="https://via.placeholder.com/300x200?text=Custom+Design" alt="Custom Championship Belt" class="belt-image">
                <div class="belt-info">
                    <h2 class="belt-title">Custom Design</h2>
                    <p class="belt-description">Work with our designers to create a completely unique belt tailored to your organization's brand.</p>
                    <div class="belt-price">Starting at $1,999.99</div>
                    <a href="#order" class="cta-button">Start Design Process</a>
                </div>
            </div>
            
            <!-- Belt 6 -->
            <div class="belt-card">
                <img src="https://via.placeholder.com/300x200?text=Lightweight" alt="Lightweight Championship Belt" class="belt-image">
                <div class="belt-info">
                    <h2 class="belt-title">Lightweight Championship</h2>
                    <p class="belt-description">Sleek, streamlined design with aluminum plates for comfortable all-day wear.</p>
                    <div class="belt-price">$799.99</div>
                    <a href="#order" class="cta-button">Customize Now</a>
                </div>
            </div>
        </div>
    </main>
    
    <footer>
        <div class="footer-links">
            <a href="#">About Us</a>
            <a href="#">Contact</a>
            <a href="#">Shipping Info</a>
            <a href="#">FAQ</a>
            <a href="#">Terms</a>
        </div>
        <div>&copy; 2023 Belts Mania. All rights reserved.</div>
    </footer>
</body>
</html>
```
