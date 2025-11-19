"""
Generated Code Metadata:
========================
Original URL: https://haus-alpenrose.com
Prompt: Generate HTML and CSS code for a simple website homepage, similar to Haus Alpenrose, with sections for accommodations, location, and contact information.
Generated: DETERMINISTIC_c16930ba63053b8b
Batch ID: 20250622_205025
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/room2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/room3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/mountain-view.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/room1.jpg": {
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
    <title>Haus Alpenrose - Mountain Retreat</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }

        /* Header styles */
        header {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://example.com/mountain-view.jpg') no-repeat center center/cover;
            height: 100vh;
            color: white;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
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
            background: #4a6fa5;
            color: white;
            padding: 10px 30px;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            font-size: 1rem;
            transition: background 0.3s ease;
        }

        .btn:hover {
            background: #3a5a80;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: rgba(255, 255, 255, 0.9);
            padding: 15px 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav ul li {
            margin: 0 15px;
        }

        nav ul li a {
            text-decoration: none;
            color: #333;
            font-weight: bold;
            transition: color 0.3s ease;
        }

        nav ul li a:hover {
            color: #4a6fa5;
        }

        /* Main content sections */
        section {
            padding: 80px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        section h2 {
            text-align: center;
            margin-bottom: 40px;
            font-size: 2.2rem;
            color: #4a6fa5;
        }

        /* Accommodations section */
        .accommodations {
            background-color: white;
        }

        .room-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }

        .room-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .room-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .room-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .room-info {
            padding: 20px;
        }

        .room-info h3 {
            margin-bottom: 10px;
            color: #4a6fa5;
        }

        /* Location section */
        .location {
            background-color: #f1f1f1;
        }

        .location-content {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 40px;
        }

        .location-text {
            flex: 1;
            min-width: 300px;
        }

        .location-map {
            flex: 1;
            min-width: 300px;
            height: 400px;
            background-color: #ddd;
            border-radius: 8px;
            overflow: hidden;
        }

        /* Contact section */
        .contact {
            background-color: white;
        }

        .contact-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .contact-item i {
            font-size: 1.5rem;
            color: #4a6fa5;
        }

        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        .form-group input,
        .form-group textarea {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .form-group textarea {
            min-height: 150px;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 30px 20px;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 20px 0;
        }

        .social-links a {
            color: white;
            font-size: 1.5rem;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: #4a6fa5;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            header h1 {
                font-size: 2.2rem;
            }

            header p {
                font-size: 1rem;
            }

            nav ul {
                flex-direction: column;
                align-items: center;
                gap: 10px;
            }

            .location-content {
                flex-direction: column;
            }
        }
    </style>
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#accommodations">Accommodations</a></li>
            <li><a href="#location">Location</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <header id="home">
        <h1>Welcome to Haus Alpenrose</h1>
        <p>Experience the beauty of the Alps in our cozy mountain retreat. Perfect for families, couples, and solo travelers looking for peace and adventure.</p>
        <a href="#accommodations" class="btn">View Accommodations</a>
    </header>

    <section id="accommodations" class="accommodations">
        <h2>Our Accommodations</h2>
        <p style="text-align: center; margin-bottom: 30px;">Choose from our selection of comfortable rooms and apartments, all with stunning mountain views.</p>
        
        <div class="room-container">
            <div class="room-card">
                <img src="https://example.com/room1.jpg" alt="Double Room">
                <div class="room-info">
                    <h3>Double Room</h3>
                    <p>Spacious double room with balcony and mountain view. Perfect for couples.</p>
                    <p><strong>€120/night</strong></p>
                </div>
            </div>
            
            <div class="room-card">
                <img src="https://example.com/room2.jpg" alt="Family Apartment">
                <div class="room-info">
                    <h3>Family Apartment</h3>
                    <p>Two-bedroom apartment with kitchenette. Ideal for families up to 4 people.</p>
                    <p><strong>€180/night</strong></p>
                </div>
            </div>
            
            <div class="room-card">
                <img src="https://example.com/room3.jpg" alt="Single Room">
                <div class="room-info">
                    <h3>Single Room</h3>
                    <p>Cozy single room with all amenities.
