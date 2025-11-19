"""
Generated Code Metadata:
========================
Original URL: https://market2024.qboda.es
Prompt: Design a web page to promote a wedding market event, similar to QBoda Market 2025, including essential details like date, time, location, and participating vendors.
Generated: DETERMINISTIC_d59bccf23468b412
Batch ID: 20250622_210703
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1519671482749-fd07b1b8a4d6?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1513106580091-1d82408b8cd6?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1520854221256-17451cc331bf?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap": {
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
    <title>QBoda Market 2025 - Wedding Market Event</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Montserrat', sans-serif;
        }
        
        body {
            background-color: #f9f3f3;
            color: #333;
            line-height: 1.6;
        }
        
        /* Header styles */
        header {
            background: linear-gradient(135deg, #f5c3d1, #d9a7c7);
            color: white;
            text-align: center;
            padding: 2rem 0;
            position: relative;
            overflow: hidden;
        }
        
        .header-content {
            position: relative;
            z-index: 2;
        }
        
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .subtitle {
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            font-weight: 300;
        }
        
        /* Main content styles */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .event-info {
            background-color: white;
            border-radius: 10px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 1.5rem;
        }
        
        .info-card {
            background-color: #f9f3f3;
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
        }
        
        .info-card h3 {
            color: #d9a7c7;
            margin-bottom: 1rem;
        }
        
        /* Vendors section */
        .vendors {
            background-color: white;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .vendor-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }
        
        .vendor-card {
            background-color: #f9f3f3;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        
        .vendor-card:hover {
            transform: translateY(-5px);
        }
        
        .vendor-img {
            height: 200px;
            background-size: cover;
            background-position: center;
        }
        
        .vendor-info {
            padding: 1.5rem;
        }
        
        .vendor-info h3 {
            color: #d9a7c7;
            margin-bottom: 0.5rem;
        }
        
        /* CTA section */
        .cta {
            text-align: center;
            margin: 3rem 0;
        }
        
        .btn {
            display: inline-block;
            background-color: #d9a7c7;
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            font-size: 1.1rem;
        }
        
        .btn:hover {
            background-color: #c38eb4;
            transform: scale(1.05);
        }
        
        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }
        
        .social-links {
            margin: 1rem 0;
        }
        
        .social-links a {
            color: white;
            margin: 0 10px;
            font-size: 1.5rem;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }
            
            .subtitle {
                font-size: 1.2rem;
            }
            
            .info-grid {
                grid-template-columns: 1fr;
            }
            
            .vendor-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <header>
        <div class="header-content">
            <h1>QBoda Market 2025</h1>
            <p class="subtitle">The Premier Wedding Market Event</p>
            <p>Discover everything you need for your perfect wedding day</p>
        </div>
    </header>
    
    <div class="container">
        <section class="event-info">
            <h2>Event Details</h2>
            <div class="info-grid">
                <div class="info-card">
                    <i class="fas fa-calendar-alt fa-3x" style="color: #d9a7c7; margin-bottom: 1rem;"></i>
                    <h3>Date</h3>
                    <p>Saturday, May 10, 2025</p>
                </div>
                <div class="info-card">
                    <i class="fas fa-clock fa-3x" style="color: #d9a7c7; margin-bottom: 1rem;"></i>
                    <h3>Time</h3>
                    <p>10:00 AM - 6:00 PM</p>
                </div>
                <div class="info-card">
                    <i class="fas fa-map-marker-alt fa-3x" style="color: #d9a7c7; margin-bottom: 1rem;"></i>
                    <h3>Location</h3>
                    <p>Grand Convention Center<br>123 Wedding Lane, Bridal City</p>
                </div>
                <div class="info-card">
                    <i class="fas fa-ticket-alt fa-3x" style="color: #d9a7c7; margin-bottom: 1rem;"></i>
                    <h3>Admission</h3>
                    <p>$15 per person<br>Free for wedding planners</p>
                </div>
            </div>
        </section>
        
        <section class="vendors">
            <h2>Featured Vendors</h2>
            <p>Meet the top wedding professionals who will be showcasing their services</p>
            
            <div class="vendor-grid">
                <div class="vendor-card">
                    <div class="vendor-img" style="background-image: url('https://images.unsplash.com/photo-1519671482749-fd07b1b8a4d6?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60');"></div>
                    <div class="vendor-info">
                        <h3>Blissful Blooms</h3>
                        <p>Floral Design & Decor</p>
                        <p>Specializing in romantic, garden-inspired arrangements</p>
                    </div>
                </div>
                
                <div class="vendor-card">
                    <div class="vendor-img" style="background-image: url('https://images.unsplash.com/photo-1513106580091-1d82408b8cd6?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60');"></div>
                    <div class="vendor-info">
                        <h3>Sweet Harmony Cakes</h3>
                        <p>Wedding Cakes & Desserts</p>
                        <p>Custom-designed cakes for your special day</p>
                    </div>
                </div>
                
                <div class="vendor-card">
                    <div class="vendor-img" style="background-image: url('https://images.unsplash.com/photo-1520854221256-17451cc331bf?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60');
