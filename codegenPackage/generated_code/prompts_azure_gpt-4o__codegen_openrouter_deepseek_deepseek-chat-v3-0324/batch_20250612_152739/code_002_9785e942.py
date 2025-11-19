"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Generate a responsive web design template using HTML5 and CSS3 for a creative services company, incorporating elements like "Projects," "Clients," and "Investments," inspired by dionlineaja.id.
Generated: DETERMINISTIC_9785e942eb69de05
Batch ID: 20250612_152739
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1497366754035-f200968a6e72?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
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
    <title>Creative Services Company</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* Global Styles */
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --text-color: #333;
            --text-light: #fff;
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

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .btn {
            display: inline-block;
            background: var(--secondary-color);
            color: var(--text-light);
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn:hover {
            background: var(--primary-color);
            transform: translateY(-3px);
        }

        .btn-accent {
            background: var(--accent-color);
        }

        .section-title {
            text-align: center;
            margin-bottom: 40px;
            font-size: 2.5rem;
            color: var(--primary-color);
            position: relative;
        }

        .section-title::after {
            content: '';
            display: block;
            width: 100px;
            height: 4px;
            background: var(--secondary-color);
            margin: 10px auto;
        }

        /* Header */
        header {
            background-color: var(--primary-color);
            color: var(--text-light);
            padding: 20px 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: var(--text-light);
        }

        .logo span {
            color: var(--secondary-color);
        }

        nav ul {
            display: flex;
        }

        nav ul li {
            margin-left: 30px;
        }

        nav ul li a {
            color: var(--text-light);
            font-weight: 500;
            transition: color 0.3s ease;
        }

        nav ul li a:hover {
            color: var(--secondary-color);
        }

        .mobile-menu {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1497366754035-f200968a6e72?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') no-repeat center center/cover;
            color: var(--text-light);
            display: flex;
            align-items: center;
            text-align: center;
            padding-top: 80px;
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 30px;
        }

        /* Projects Section */
        .projects {
            padding: 100px 0;
            background-color: var(--text-light);
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .project-card {
            background: var(--light-color);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .project-card:hover {
            transform: translateY(-10px);
        }

        .project-img {
            height: 200px;
            overflow: hidden;
        }

        .project-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .project-card:hover .project-img img {
            transform: scale(1.1);
        }

        .project-info {
            padding: 20px;
        }

        .project-info h3 {
            margin-bottom: 10px;
            color: var(--primary-color);
        }

        /* Clients Section */
        .clients {
            padding: 100px 0;
            background-color: var(--light-color);
        }

        .clients-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            align-items: center;
        }

        .client-logo {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px;
            filter: grayscale(100%);
            opacity: 0.7;
            transition: all 0.3s ease;
        }

        .client-logo:hover {
            filter: grayscale(0);
            opacity: 1;
        }

        .client-logo img {
            max-width: 80%;
            max-height: 80%;
            object-fit: contain;
        }

        /* Investments Section */
        .investments {
            padding: 100px 0;
            background-color: var(--text-light);
        }

        .investment-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .investment-card {
            background: var(--light-color);
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }

        .investment-card:hover {
            transform: translateY(-10px);
        }

        .investment-icon {
            font-size: 3rem;
            color: var(--secondary-color);
            margin-bottom: 20px;
        }

        /* Contact Section */
        .contact {
            padding: 100px 0;
            background-color: var(--light-color);
        }

        .contact-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 50px;
        }

        .contact-info h3 {
            margin-bottom: 20px;
            font-size: 1.5rem;
        }

        .contact-info p {
            margin-bottom: 30px;
        }

        .contact-info ul li {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }

        .contact-info ul li i {
            margin-right: 10px;
            color: var(--secondary-color);
        }

        .contact-form .form-group {
            margin-bottom: 20px;
        }

        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-family: inherit;
        }

        .contact-form textarea {
            height: 150px;
            resize: vertical;
        }

        /* Footer */
        footer {
            background-color: var(--primary-color);
            color: var(--text-light);
            padding: 50px 0 20px;
            text-align: center;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        .footer-column
