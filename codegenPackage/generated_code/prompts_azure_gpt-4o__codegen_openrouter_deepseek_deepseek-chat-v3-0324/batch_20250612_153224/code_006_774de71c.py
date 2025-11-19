"""
Generated Code Metadata:
========================
Original URL: https://techcherio.com
Prompt: Develop a web design template for a hotel or restaurant website, inspired by TechCherio's web design offerings.
Generated: DETERMINISTIC_774de71c1560f72e
Batch ID: 20250612_153224
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa": {
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
    <title>Luxury Haven - Premium Hotel & Restaurant</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* Global Styles */
        :root {
            --primary-color: #8b5a2b;
            --secondary-color: #f8f1e5;
            --accent-color: #d4a76a;
            --dark-color: #333;
            --light-color: #fff;
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            line-height: 1.6;
            color: var(--dark-color);
            background-color: var(--secondary-color);
        }

        a {
            text-decoration: none;
            color: var(--primary-color);
            transition: var(--transition);
        }

        a:hover {
            color: var(--accent-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .btn {
            display: inline-block;
            background: var(--primary-color);
            color: var(--light-color);
            padding: 12px 25px;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            transition: var(--transition);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 14px;
        }

        .btn:hover {
            background: var(--accent-color);
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
            font-size: 2.5rem;
            color: var(--primary-color);
            position: relative;
        }

        .section-title::after {
            content: '';
            display: block;
            width: 80px;
            height: 4px;
            background: var(--accent-color);
            margin: 15px auto;
        }

        /* Header Styles */
        header {
            background-color: rgba(255, 255, 255, 0.9);
            position: fixed;
            width: 100%;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary-color);
        }

        .logo span {
            color: var(--accent-color);
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 30px;
        }

        nav ul li a {
            font-weight: 600;
            position: relative;
        }

        nav ul li a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            background: var(--accent-color);
            bottom: -5px;
            left: 0;
            transition: var(--transition);
        }

        nav ul li a:hover::after {
            width: 100%;
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--primary-color);
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1551882547-ff40c63fe5fa') no-repeat center center/cover;
            display: flex;
            align-items: center;
            text-align: center;
            color: var(--light-color);
            padding-top: 80px;
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            animation: fadeInUp 1s ease;
        }

        .hero-btns {
            display: flex;
            justify-content: center;
            gap: 20px;
            animation: fadeIn 1.5s ease;
        }

        .hero-btns .btn-secondary {
            background: transparent;
            border: 2px solid var(--light-color);
        }

        .hero-btns .btn-secondary:hover {
            background: var(--light-color);
            color: var(--dark-color);
        }

        /* About Section */
        .about {
            padding: 100px 0;
            background-color: var(--light-color);
        }

        .about-content {
            display: flex;
            align-items: center;
            gap: 50px;
        }

        .about-img {
            flex: 1;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .about-img img {
            width: 100%;
            height: auto;
            display: block;
            transition: var(--transition);
        }

        .about-img:hover img {
            transform: scale(1.05);
        }

        .about-text {
            flex: 1;
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--primary-color);
        }

        .about-text p {
            margin-bottom: 20px;
        }

        /* Rooms Section */
        .rooms {
            padding: 100px 0;
            background-color: var(--secondary-color);
        }

        .rooms-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
        }

        .room-card {
            background: var(--light-color);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: var(--transition);
        }

        .room-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .room-img {
            height: 250px;
            overflow: hidden;
        }

        .room-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }

        .room-card:hover .room-img img {
            transform: scale(1.1);
        }

        .room-info {
            padding: 25px;
        }

        .room-info h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
            color: var(--primary-color);
        }

        .room-info p {
            margin-bottom: 15px;
            color: #666;
        }

        .room-price {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 20px;
        }

        .room-price span {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--primary-color);
        }

        /* Restaurant Section */
        .restaurant {
            padding: 100px 0;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4') no-repeat center center/cover;
            color: var(--light-color);
            text-align: center;
        }

        .restaurant h2 {
            color: var(--light-color);
        }

        .restaurant p {
            max-width: 700px;
            margin: 0 auto 40px;
        }

        .menu-btn {
            background: var(--accent-color);
        }

        .menu-btn:hover {
            background: var(--primary-color);
        }

        /* Testimonials Section */
        .testimonials {
            padding: 100
