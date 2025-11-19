"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Develop a simple HTML page that showcases featured properties, including images and descriptions, inspired by the layout and content of Presval's property showcase.
Generated: DETERMINISTIC_50d60b781d043c50
Batch ID: 20250612_162325
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
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
    <title>Featured Properties Showcase</title>
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

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            padding: 30px 0;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #7f8c8d;
            margin-bottom: 30px;
        }

        /* Property grid */
        .properties-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .property-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .property-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .property-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
        }

        .property-details {
            padding: 20px;
        }

        .property-title {
            font-size: 1.5rem;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .property-location {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            color: #7f8c8d;
        }

        .property-location i {
            margin-right: 5px;
        }

        .property-description {
            margin-bottom: 20px;
            color: #555;
        }

        .property-price {
            font-size: 1.3rem;
            font-weight: bold;
            color: #e74c3c;
            margin-bottom: 15px;
        }

        .property-features {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        .feature {
            background: #f0f0f0;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        .view-details {
            display: inline-block;
            padding: 10px 20px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: background 0.3s ease;
        }

        .view-details:hover {
            background: #2980b9;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .properties-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Featured Properties</h1>
            <p class="subtitle">Discover your dream home from our curated selection</p>
        </header>

        <div class="properties-grid">
            <!-- Property 1 -->
            <div class="property-card">
                <img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" 
                     alt="Modern Family Home" class="property-image">
                <div class="property-details">
                    <h2 class="property-title">Modern Family Home</h2>
                    <div class="property-location">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Greenwood Heights, NY</span>
                    </div>
                    <p class="property-description">
                        This stunning modern home features an open floor plan, high ceilings, and floor-to-ceiling windows that flood the space with natural light.
                    </p>
                    <div class="property-features">
                        <span class="feature">4 Beds</span>
                        <span class="feature">3 Baths</span>
                        <span class="feature">2,500 sqft</span>
                        <span class="feature">Garage</span>
                    </div>
                    <div class="property-price">$1,250,000</div>
                    <a href="#" class="view-details">View Details</a>
                </div>
            </div>

            <!-- Property 2 -->
            <div class="property-card">
                <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" 
                     alt="Luxury Penthouse" class="property-image">
                <div class="property-details">
                    <h2 class="property-title">Luxury Penthouse</h2>
                    <div class="property-location">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Downtown, Chicago</span>
                    </div>
                    <p class="property-description">
                        Experience urban luxury in this spacious penthouse with panoramic city views, high-end finishes, and premium amenities including a rooftop pool.
                    </p>
                    <div class="property-features">
                        <span class="feature">3 Beds</span>
                        <span class="feature">2.5 Baths</span>
                        <span class="feature">2,100 sqft</span>
                        <span class="feature">Doorman</span>
                    </div>
                    <div class="property-price">$2,800,000</div>
                    <a href="#" class="view-details">View Details</a>
                </div>
            </div>

            <!-- Property 3 -->
            <div class="property-card">
                <img src="https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" 
                     alt="Coastal Retreat" class="property-image">
                <div class="property-details">
                    <h2 class="property-title">Coastal Retreat</h2>
                    <div class="property-location">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Malibu, CA</span>
                    </div>
                    <p class="property-description">
                        Beachfront property with direct access to private beach. Features include a chef's kitchen, infinity pool, and expansive outdoor living spaces.
                    </p>
                    <div class="property-features">
                        <span class="feature">5 Beds</span>
                        <span class="feature">4.5 Baths</span>
                        <span class="feature">4,200 sqft</span>
                        <span class="feature">Ocean View</span>
                    </div>
                    <div class="property-price">$5,750,000</div>
                    <a href="#" class="view-details">View Details</a>
                </div>
            </div>

            <!-- Property 4 -->
            <div class="property-card">
                <img src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" 
                     alt="Mountain Cabin" class="property-image">
                <div class="property-details">
                    <h2 class="property-title">Mountain Cabin</h2>
                    <div class="property-location">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Aspen, CO</span>
                    </div>
                    <p class="property-description">
                        Rustic yet modern cabin nestled in the mountains. Features include a stone fireplace, wrap-around deck, and access to hiking trails right from your backyard.
                    </p>
                    <div class="property-features">
                        <span class
