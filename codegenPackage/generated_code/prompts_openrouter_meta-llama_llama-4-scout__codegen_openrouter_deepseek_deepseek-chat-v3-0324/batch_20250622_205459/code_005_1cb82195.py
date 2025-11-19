"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Write a code example in HTML/CSS to create a responsive and accessible layout for a website promoting education and healthcare initiatives, similar to the NICER Foundation website.
Generated: DETERMINISTIC_1cb82195a336fca2
Batch ID: 20250622_205459
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1523050854058-8df90110c9f1": {
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
    <title>Community Initiatives Foundation</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-color: #2c7be5;
            --secondary-color: #00d97e;
            --dark-color: #12263f;
            --light-color: #f9fafc;
            --text-color: #495057;
            --white: #ffffff;
            --max-width: 1200px;
            --border-radius: 0.5rem;
            --box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--light-color);
        }

        /* Accessibility focus styles */
        a:focus, button:focus, input:focus {
            outline: 3px solid var(--primary-color);
            outline-offset: 2px;
        }

        /* Skip to content link for screen readers */
        .skip-link {
            position: absolute;
            left: -9999px;
            top: 0;
            background: var(--primary-color);
            color: var(--white);
            padding: 0.5rem;
            z-index: 100;
        }

        .skip-link:focus {
            left: 0;
        }

        /* Header styles */
        header {
            background-color: var(--white);
            box-shadow: var(--box-shadow);
            position: sticky;
            top: 0;
            z-index: 10;
        }

        .header-container {
            max-width: var(--max-width);
            margin: 0 auto;
            padding: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary-color);
            text-decoration: none;
        }

        .logo span {
            color: var(--secondary-color);
        }

        /* Navigation */
        nav ul {
            display: flex;
            list-style: none;
        }

        nav li {
            margin-left: 1.5rem;
        }

        nav a {
            text-decoration: none;
            color: var(--dark-color);
            font-weight: 500;
            transition: color 0.3s;
        }

        nav a:hover {
            color: var(--primary-color);
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--dark-color);
        }

        /* Hero section */
        .hero {
            background: linear-gradient(rgba(44, 123, 229, 0.8), rgba(44, 123, 229, 0.8)), 
                        url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1') center/cover;
            color: var(--white);
            padding: 4rem 1rem;
            text-align: center;
        }

        .hero-content {
            max-width: var(--max-width);
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 2rem;
        }

        .btn {
            display: inline-block;
            background-color: var(--secondary-color);
            color: var(--white);
            padding: 0.8rem 1.5rem;
            border-radius: var(--border-radius);
            text-decoration: none;
            font-weight: 600;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #00c571;
        }

        /* Main content */
        main {
            max-width: var(--max-width);
            margin: 2rem auto;
            padding: 0 1rem;
        }

        /* Initiatives section */
        .initiatives {
            margin: 3rem 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 2rem;
            color: var(--dark-color);
        }

        .initiatives-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .initiative-card {
            background-color: var(--white);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--box-shadow);
            transition: transform 0.3s;
        }

        .initiative-card:hover {
            transform: translateY(-5px);
        }

        .card-img {
            height: 200px;
            overflow: hidden;
        }

        .card-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .card-content {
            padding: 1.5rem;
        }

        .card-content h3 {
            margin-bottom: 0.5rem;
            color: var(--dark-color);
        }

        /* Stats section */
        .stats {
            background-color: var(--primary-color);
            color: var(--white);
            padding: 3rem 1rem;
            margin: 3rem 0;
        }

        .stats-container {
            max-width: var(--max-width);
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            text-align: center;
        }

        .stat-item h3 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        /* Newsletter section */
        .newsletter {
            background-color: var(--white);
            padding: 2rem;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            margin: 3rem 0;
        }

        .newsletter h2 {
            margin-bottom: 1rem;
            text-align: center;
        }

        .newsletter-form {
            display: flex;
            max-width: 600px;
            margin: 0 auto;
        }

        .newsletter-form input {
            flex: 1;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: var(--border-radius) 0 0 var(--border-radius);
            font-size: 1rem;
        }

        .newsletter-form button {
            padding: 0 1.5rem;
            background-color: var(--primary-color);
            color: var(--white);
            border: none;
            border-radius: 0 var(--border-radius) var(--border-radius) 0;
            cursor: pointer;
            font-weight: 600;
        }

        /* Footer */
        footer {
            background-color: var(--dark-color);
            color: var(--white);
            padding: 3rem 1rem;
        }

        .footer-container {
            max-width: var(--max-width);
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
        }

        .footer-logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--white);
            margin-bottom: 1rem;
            display: block;
        }

        .footer-logo span {
            color: var(--secondary-color);
        }

        .footer-links h3 {
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }

        .footer-links ul {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 0.5rem;
        }

        .footer-links a {
            color: #adb5bd;
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: var(--white);
        }

        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }

        .social-links a {
            color: var(--white);
            font-size: 1.5rem;
        }

        .copyright {
            text-align: center;
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
                text-align: center;
            }
