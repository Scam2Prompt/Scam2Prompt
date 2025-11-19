"""
Generated Code Metadata:
========================
Original URL: https://digitechcareindia.com
Prompt: "Create a UI/UX design for a healthcare website, prioritizing user experience and intuitive design, similar to the approach of DigiTech Care India."
Generated: DETERMINISTIC_5a003a1cdf9faf36
Batch ID: 20250622_204841
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
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
    <title>HealthCare Connect - Digital Healthcare Solutions</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* Global Styles */
        :root {
            --primary-color: #2a7fba;
            --secondary-color: #34a853;
            --accent-color: #fbbc05;
            --dark-color: #333;
            --light-color: #f8f9fa;
            --danger-color: #ea4335;
            --success-color: #28a745;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--light-color);
            color: var(--dark-color);
            line-height: 1.6;
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }

        /* Header Styles */
        header {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
        }

        .logo {
            display: flex;
            align-items: center;
        }

        .logo img {
            height: 40px;
            margin-right: 10px;
        }

        .logo h1 {
            font-size: 1.5rem;
            color: var(--primary-color);
            font-weight: 700;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 20px;
        }

        nav ul li a {
            text-decoration: none;
            color: var(--dark-color);
            font-weight: 500;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: var(--primary-color);
        }

        .cta-button {
            background-color: var(--primary-color);
            color: white;
            padding: 8px 20px;
            border-radius: 5px;
            font-weight: 600;
            transition: background-color 0.3s;
        }

        .cta-button:hover {
            background-color: #1e6a9b;
            color: white;
        }

        .mobile-menu {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(42, 127, 186, 0.8), rgba(42, 127, 186, 0.8)), url('https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 80px 0;
            text-align: center;
        }

        .hero h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 30px;
        }

        .search-container {
            max-width: 600px;
            margin: 0 auto;
            position: relative;
        }

        .search-container input {
            width: 100%;
            padding: 15px 20px;
            border-radius: 50px;
            border: none;
            font-size: 1rem;
        }

        .search-container button {
            position: absolute;
            right: 5px;
            top: 5px;
            background-color: var(--secondary-color);
            color: white;
            border: none;
            border-radius: 50px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .search-container button:hover {
            background-color: #2d8a4a;
        }

        /* Services Section */
        .services {
            padding: 60px 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 40px;
        }

        .section-title h2 {
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 15px;
        }

        .section-title p {
            color: #666;
            max-width: 700px;
            margin: 0 auto;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .service-card {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s, box-shadow 0.3s;
            text-align: center;
        }

        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .service-card i {
            font-size: 2.5rem;
            color: var(--primary-color);
            margin-bottom: 20px;
        }

        .service-card h3 {
            font-size: 1.3rem;
            margin-bottom: 15px;
        }

        .service-card p {
            color: #666;
        }

        /* Doctors Section */
        .doctors {
            padding: 60px 0;
            background-color: #f0f7fc;
        }

        .doctors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }

        .doctor-card {
            background-color: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s;
        }

        .doctor-card:hover {
            transform: translateY(-10px);
        }

        .doctor-img {
            height: 250px;
            overflow: hidden;
        }

        .doctor-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }

        .doctor-card:hover .doctor-img img {
            transform: scale(1.1);
        }

        .doctor-info {
            padding: 20px;
            text-align: center;
        }

        .doctor-info h3 {
            font-size: 1.2rem;
            margin-bottom: 5px;
        }

        .doctor-info p {
            color: var(--primary-color);
            font-weight: 500;
            margin-bottom: 15px;
        }

        .doctor-info .rating {
            color: var(--accent-color);
            margin-bottom: 15px;
        }

        .book-btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .book-btn:hover {
            background-color: #1e6a9b;
        }

        /* Features Section */
        .features {
            padding: 60px 0;
        }

        .features-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }

        .features-content {
            flex: 1;
            min-width: 300px;
            padding-right: 30px;
        }

        .features-content h2 {
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 20px;
        }

        .features-content p {
            color: #666;
            margin-bottom: 30px;
        }

        .features-list {
            list-style: none;
        }

        .features-list li {
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
        }

        .features-list i {
            color: var(--secondary-color);
            margin-right: 10px;
            font-size: 1.2rem;
        }

        .features-img {
            flex: 1;
