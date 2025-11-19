"""
Generated Code Metadata:
========================
Original URL: https://poocoinnex.weebly.com
Prompt: Generate HTML code for a barbershop website with a gallery section, featuring images of different hairstyles and beards, and including information about barbers like their experience and clipping style.
Generated: DETERMINISTIC_85919c3fd7c7d356
Batch ID: 20250622_205459
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1595476108010-b4d1f102b1b1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600334129128-685c5582fd35?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1595475884567-2a6d2a7b4c42?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1605497788044-5a32c7078486?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80": {
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
    <title>Classic Cuts Barbershop</title>
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
            background-color: #222;
            color: #fff;
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
            color: #fff;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #d4af37;
        }

        /* Main content styles */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        h1, h2, h3 {
            margin-bottom: 1rem;
            color: #222;
        }

        /* Gallery styles */
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
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
            height: 300px;
            object-fit: cover;
            display: block;
        }

        .gallery-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0, 0, 0, 0.7);
            color: #fff;
            padding: 1rem;
            transform: translateY(100%);
            transition: transform 0.3s;
        }

        .gallery-item:hover .gallery-caption {
            transform: translateY(0);
        }

        /* Barbers section */
        .barbers {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .barber-card {
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .barber-card:hover {
            transform: translateY(-5px);
        }

        .barber-card img {
            width: 100%;
            height: 250px;
            object-fit: cover;
        }

        .barber-info {
            padding: 1.5rem;
        }

        .barber-info h3 {
            color: #d4af37;
            margin-bottom: 0.5rem;
        }

        .barber-info p {
            margin-bottom: 0.5rem;
            color: #666;
        }

        .experience {
            font-weight: bold;
            color: #222 !important;
        }

        /* Footer styles */
        footer {
            background-color: #222;
            color: #fff;
            text-align: center;
            padding: 2rem 0;
            margin-top: 2rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
            }

            nav ul li {
                margin: 0.5rem 0;
            }

            .gallery {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Classic Cuts Barbershop</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#barbers">Our Barbers</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main class="container">
        <section id="home">
            <h2>Welcome to Classic Cuts</h2>
            <p>Where tradition meets modern style. Our expert barbers provide precision cuts and grooming services tailored to your individual needs.</p>
        </section>

        <section id="gallery">
            <h2>Our Work Gallery</h2>
            <div class="gallery">
                <div class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1595476108010-b4d1f102b1b1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Classic Haircut">
                    <div class="gallery-caption">
                        <h3>Classic Cut</h3>
                        <p>A timeless style with modern precision</p>
                    </div>
                </div>
                <div class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1605497788044-5a32c7078486?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Beard Trim">
                    <div class="gallery-caption">
                        <h3>Beard Trim</h3>
                        <p>Expert shaping and maintenance</p>
                    </div>
                </div>
                <div class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Fade Haircut">
                    <div class="gallery-caption">
                        <h3>Fade Cut</h3>
                        <p>Smooth transitions for a sharp look</p>
                    </div>
                </div>
                <div class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1605497788044-5a32c7078486?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Full Beard">
                    <div class="gallery-caption">
                        <h3>Full Beard</h3>
                        <p>Professional shaping and conditioning</p>
                    </div>
                </div>
                <div class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1595475884567-2a6d2a7b4c42?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Buzz Cut">
                    <div class="gallery-caption">
                        <h3>Buzz Cut</h3>
                        <p>Low maintenance with clean lines</p>
                    </div>
                </div>
                <div class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1600334129128-685c5582fd35?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Designer Cut">
                    <div class="gallery-caption">
                        <h3>Designer Cut</h3>
                        <p>Custom patterns and creative styling</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="barbers">
            <h2>Meet Our Barbers</h2>
            <div class="barbers">
                <div class="barber-card">
                    <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="Barber John">
                    <div class="barber-info">
                        <h3>John Smith</h3>
