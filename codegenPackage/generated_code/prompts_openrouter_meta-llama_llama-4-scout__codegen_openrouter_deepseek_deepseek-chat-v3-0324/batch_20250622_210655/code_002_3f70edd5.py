"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Generate a JavaScript code snippet to create a web page for a luxury villa in Corfu, featuring its gallery, services, and booking information, including check-in and check-out times.
Generated: DETERMINISTIC_3f70edd57af26f90
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
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
    <title>Luxury Villa in Corfu | Paradise Retreat</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            color: #333;
            line-height: 1.6;
        }
        
        header {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('villa-hero.jpg');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            padding: 0 20px;
        }
        
        header h1 {
            font-size: 3rem;
            margin-bottom: 20px;
        }
        
        header p {
            font-size: 1.2rem;
            max-width: 800px;
            margin-bottom: 30px;
        }
        
        .btn {
            display: inline-block;
            background: #d4af37;
            color: white;
            padding: 10px 30px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background 0.3s;
        }
        
        .btn:hover {
            background: #c9a227;
        }
        
        nav {
            background: #333;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }
        
        nav ul li {
            padding: 20px;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        
        nav ul li a:hover {
            color: #d4af37;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        section {
            padding: 60px 0;
        }
        
        h2 {
            text-align: center;
            margin-bottom: 40px;
            font-size: 2.5rem;
            color: #333;
        }
        
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .gallery img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-radius: 5px;
            transition: transform 0.3s;
        }
        
        .gallery img:hover {
            transform: scale(1.03);
        }
        
        .services {
            background: #f9f9f9;
        }
        
        .service-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .service-card {
            background: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        
        .service-card i {
            font-size: 2.5rem;
            color: #d4af37;
            margin-bottom: 20px;
        }
        
        .service-card h3 {
            margin-bottom: 15px;
        }
        
        .booking-form {
            background: white;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px;
            border-radius: 5px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        
        .form-row {
            display: flex;
            gap: 20px;
        }
        
        .form-row .form-group {
            flex: 1;
        }
        
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 30px 0;
            margin-top: 60px;
        }
        
        @media (max-width: 768px) {
            header h1 {
                font-size: 2rem;
            }
            
            nav ul {
                flex-direction: column;
                align-items: center;
            }
            
            .form-row {
                flex-direction: column;
                gap: 0;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <header>
        <h1>Luxury Villa in Corfu</h1>
        <p>Experience unparalleled luxury in our stunning villa overlooking the Ionian Sea</p>
        <a href="#booking" class="btn">Book Now</a>
    </header>
    
    <nav>
        <ul>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#booking">Booking</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <section id="gallery">
        <div class="container">
            <h2>Gallery</h2>
            <div class="gallery">
                <img src="villa1.jpg" alt="Luxury villa exterior">
                <img src="villa2.jpg" alt="Infinity pool with sea view">
                <img src="villa3.jpg" alt="Master bedroom">
                <img src="villa4.jpg" alt="Dining area">
                <img src="villa5.jpg" alt="Private beach access">
                <img src="villa6.jpg" alt="Sunset view from terrace">
            </div>
        </div>
    </section>
    
    <section id="services" class="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service-grid">
                <div class="service-card">
                    <i class="fas fa-concierge-bell"></i>
                    <h3>24/7 Concierge</h3>
                    <p>Our dedicated concierge team is available around the clock to cater to your every need.</p>
                </div>
                <div class="service-card">
                    <i class="fas fa-umbrella-beach"></i>
                    <h3>Private Beach Access</h3>
                    <p>Exclusive access to a secluded beach with complimentary sun loungers and umbrellas.</p>
                </div>
                <div class="service-card">
                    <i class="fas fa-car"></i>
                    <h3>Airport Transfer</h3>
                    <p>Luxury vehicle transfers to and from Corfu International Airport included in your stay.</p>
                </div>
                <div class="service-card">
                    <i class="fas fa-utensils"></i>
                    <h3>Private Chef</h3>
                    <p>Optional private chef service to prepare gourmet meals tailored to your preferences.</p>
                </div>
                <div class="service-card">
                    <i class="fas fa-spa"></i>
                    <h3>Spa Services</h3>
                    <p>In-villa spa treatments available upon request for ultimate relaxation.</p>
                </div>
                <div class="service-card">
                    <i class="fas fa-water"></i>
                    <h3>Boat Excursions</h3>
                    <p>Private boat tours to explore Corfu's stunning coastline and hidden coves.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section id="booking">
        <div class="container">
            <h2>Booking Information</h2>
            <div class="booking-form">
                <form id="bookingForm">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="checkin">Check-in Date</label>
                            <input type="date" id="checkin" name="checkin" required>
                        </div>
