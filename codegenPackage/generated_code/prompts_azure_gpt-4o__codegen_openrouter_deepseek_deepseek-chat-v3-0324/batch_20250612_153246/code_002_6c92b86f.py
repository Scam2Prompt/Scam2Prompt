"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Generate HTML and CSS code for a gallery page showcasing backyard inspiration and hot tub setups, inspired by the design and layout of the Oasis Hot Tubs video gallery.
Generated: DETERMINISTIC_6c92b86ffff1484d
Batch ID: 20250612_153246
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1600566752228-1c5cb335b9e1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600566752229-3c5cb335b9e2?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600566752230-3c5cb335b9e3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600566752355-35792bedcfea?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600566752227-513cfb1b7830?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
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
    <title>Backyard Oasis Gallery | Hot Tub Inspiration</title>
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
            background-color: #2c3e50;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        /* Gallery container */
        .gallery-container {
            max-width: 1200px;
            margin: 3rem auto;
            padding: 0 20px;
        }

        /* Filter controls */
        .filter-controls {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .filter-btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
        }

        .filter-btn:hover, .filter-btn.active {
            background-color: #2980b9;
        }

        /* Gallery grid */
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }

        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .gallery-item:hover {
            transform: translateY(-5px);
        }

        .gallery-item img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            display: block;
        }

        .gallery-item-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 1rem;
            transform: translateY(100%);
            transition: transform 0.3s ease;
        }

        .gallery-item:hover .gallery-item-overlay {
            transform: translateY(0);
        }

        .gallery-item-title {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }

        .gallery-item-desc {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .gallery-grid {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 2rem;
            }
            
            .subtitle {
                font-size: 1rem;
            }
            
            .filter-controls {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>Backyard Oasis Gallery</h1>
            <p class="subtitle">Inspiration for your perfect hot tub retreat</p>
        </div>
    </header>

    <main class="gallery-container">
        <div class="filter-controls">
            <button class="filter-btn active" data-filter="all">All Designs</button>
            <button class="filter-btn" data-filter="modern">Modern</button>
            <button class="filter-btn" data-filter="rustic">Rustic</button>
            <button class="filter-btn" data-filter="tropical">Tropical</button>
            <button class="filter-btn" data-filter="minimalist">Minimalist</button>
        </div>

        <div class="gallery-grid">
            <!-- Gallery Item 1 -->
            <div class="gallery-item" data-category="modern">
                <img src="https://images.unsplash.com/photo-1600566752227-513cfb1b7830?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Modern hot tub with clean lines">
                <div class="gallery-item-overlay">
                    <h3 class="gallery-item-title">Contemporary Retreat</h3>
                    <p class="gallery-item-desc">Sleek modern design with geometric landscaping</p>
                </div>
            </div>

            <!-- Gallery Item 2 -->
            <div class="gallery-item" data-category="rustic">
                <img src="https://images.unsplash.com/photo-1600566752355-35792bedcfea?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Rustic wooden hot tub">
                <div class="gallery-item-overlay">
                    <h3 class="gallery-item-title">Mountain Cabin Style</h3>
                    <p class="gallery-item-desc">Natural wood hot tub with stone surround</p>
                </div>
            </div>

            <!-- Gallery Item 3 -->
            <div class="gallery-item" data-category="tropical">
                <img src="https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Tropical hot tub with palm trees">
                <div class="gallery-item-overlay">
                    <h3 class="gallery-item-title">Island Paradise</h3>
                    <p class="gallery-item-desc">Lush tropical plants surround this relaxing oasis</p>
                </div>
            </div>

            <!-- Gallery Item 4 -->
            <div class="gallery-item" data-category="minimalist">
                <img src="https://images.unsplash.com/photo-1600566752228-1c5cb335b9e1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Minimalist hot tub design">
                <div class="gallery-item-overlay">
                    <h3 class="gallery-item-title">Zen Simplicity</h3>
                    <p class="gallery-item-desc">Clean lines and neutral tones create tranquility</p>
                </div>
            </div>

            <!-- Gallery Item 5 -->
            <div class="gallery-item" data-category="modern">
                <img src="https://images.unsplash.com/photo-1600566752229-3c5cb335b9e2?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Modern rooftop hot tub">
                <div class="gallery-item-overlay">
                    <h3 class="gallery-item-title">Urban Escape</h3>
                    <p class="gallery-item-desc">Rooftop hot tub with city skyline views</p>
                </div>
            </div>

            <!-- Gallery Item 6 -->
            <div class="gallery-item" data-category="rustic">
                <img src="https://images.unsplash.com/photo-1600566752230-3c5cb335b9e3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Rustic hot tub in forest">
                <div class="gallery-item-overlay">
                    <h3 class="gallery-item-title">Forest Sanctuary</
