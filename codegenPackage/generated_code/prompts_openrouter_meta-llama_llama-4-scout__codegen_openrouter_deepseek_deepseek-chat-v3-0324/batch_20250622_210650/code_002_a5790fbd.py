"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Generate a sample code for a simple health and wellness website that includes sections for blog posts, testimonials, and service descriptions, similar to the Get Up Energy website.
Generated: DETERMINISTIC_a5790fbd2b706d40
Batch ID: 20250622_210650
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1498837167922-ddd27525d352": {
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
    <title>Health & Wellness | Revitalize Your Life</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* Base Styles */
        :root {
            --primary-color: #4CAF50;
            --secondary-color: #2E7D32;
            --accent-color: #8BC34A;
            --light-color: #F1F8E9;
            --dark-color: #1B5E20;
            --text-color: #333;
            --white: #fff;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--light-color);
        }
        
        a {
            text-decoration: none;
            color: var(--secondary-color);
        }
        
        ul {
            list-style: none;
        }
        
        img {
            max-width: 100%;
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .btn {
            display: inline-block;
            background: var(--primary-color);
            color: var(--white);
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .btn:hover {
            background: var(--secondary-color);
            transform: translateY(-2px);
        }
        
        /* Header */
        header {
            background: var(--white);
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: var(--primary-color);
        }
        
        .nav-links {
            display: flex;
        }
        
        .nav-links li {
            margin-left: 30px;
        }
        
        .nav-links a {
            color: var(--text-color);
            font-weight: 500;
            transition: color 0.3s ease;
        }
        
        .nav-links a:hover {
            color: var(--primary-color);
        }
        
        .mobile-menu {
            display: none;
            font-size: 24px;
            cursor: pointer;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1498837167922-ddd27525d352');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            align-items: center;
            text-align: center;
            color: var(--white);
            margin-top: 80px;
        }
        
        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .hero p {
            font-size: 20px;
            margin-bottom: 30px;
        }
        
        /* Services Section */
        .services {
            padding: 80px 0;
            background: var(--white);
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .section-title h2 {
            font-size: 36px;
            color: var(--dark-color);
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
            background: var(--light-color);
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .service-card:hover {
            transform: translateY(-10px);
        }
        
        .service-icon {
            font-size: 50px;
            color: var(--primary-color);
            margin-bottom: 20px;
        }
        
        .service-card h3 {
            font-size: 24px;
            margin-bottom: 15px;
            color: var(--dark-color);
        }
        
        /* Testimonials Section */
        .testimonials {
            padding: 80px 0;
            background: var(--light-color);
        }
        
        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .testimonial-card {
            background: var(--white);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .testimonial-card p {
            font-style: italic;
            margin-bottom: 20px;
        }
        
        .client-info {
            display: flex;
            align-items: center;
        }
        
        .client-img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            margin-right: 15px;
        }
        
        .client-name {
            font-weight: bold;
        }
        
        .client-title {
            color: #666;
            font-size: 14px;
        }
        
        /* Blog Section */
        .blog {
            padding: 80px 0;
            background: var(--white);
        }
        
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .blog-card {
            background: var(--light-color);
            border-radius: 10px;
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        
        .blog-card:hover {
            transform: translateY(-10px);
        }
        
        .blog-img {
            height: 200px;
            object-fit: cover;
            width: 100%;
        }
        
        .blog-content {
            padding: 20px;
        }
        
        .blog-content h3 {
            margin-bottom: 10px;
            color: var(--dark-color);
        }
        
        .blog-meta {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            color: #666;
            font-size: 14px;
        }
        
        .read-more {
            display: inline-block;
            margin-top: 15px;
            font-weight: bold;
        }
        
        /* Newsletter Section */
        .newsletter {
            padding: 60px 0;
            background: var(--primary-color);
            color: var(--white);
            text-align: center;
        }
        
        .newsletter h2 {
            margin-bottom: 20px;
        }
        
        .newsletter p {
            max-width: 600px;
            margin: 0 auto 30px;
        }
        
        .newsletter-form {
            max-width: 500px;
            margin: 0 auto;
            display: flex;
        }
        
        .newsletter-form input {
            flex: 1;
            padding: 15px;
            border: none;
            border-radius: 5px 0 0 5px;
        }
        
        .newsletter-form button {
            padding: 15px 30px;
            background: var(--dark-color);
            color: var(--white);
            border: none;
            border-radius: 0 5px 5px 0;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .newsletter-form button:hover {
            background: var(--secondary-color);
        }
        
        /* Footer */
        footer {
            background: var(--dark-color);
            color: var(--white);
            padding: 60px 0 20px;
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
