"""
Generated Code Metadata:
========================
Original URL: https://zuwaentertainment.co.uk
Prompt: Generate a code snippet for a digital agency website that showcases creative works and includes a blog section.
Generated: DETERMINISTIC_24c79d12419443ea
Batch ID: 20250612_162658
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
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
    <title>Creative Digital Agency</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* Global Styles */
        :root {
            --primary-color: #4a6bff;
            --secondary-color: #ff6b6b;
            --dark-color: #333;
            --light-color: #f4f4f4;
            --max-width: 1200px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark-color);
            background-color: #fff;
        }

        a {
            text-decoration: none;
            color: var(--dark-color);
        }

        ul {
            list-style: none;
        }

        .container {
            max-width: var(--max-width);
            margin: auto;
            padding: 0 2rem;
            overflow: hidden;
        }

        .btn {
            display: inline-block;
            background: var(--primary-color);
            color: #fff;
            padding: 0.8rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn:hover {
            background: #3a56d4;
        }

        .btn-secondary {
            background: var(--secondary-color);
        }

        .btn-secondary:hover {
            background: #e05a5a;
        }

        .section-title {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 2rem;
            position: relative;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 4px;
            background: var(--primary-color);
        }

        /* Header */
        header {
            background: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            z-index: 100;
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary-color);
        }

        .logo span {
            color: var(--secondary-color);
        }

        nav ul {
            display: flex;
        }

        nav ul li {
            margin-left: 2rem;
        }

        nav ul li a {
            font-weight: 600;
            transition: color 0.3s ease;
        }

        nav ul li a:hover {
            color: var(--primary-color);
        }

        .mobile-menu {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Hero Section */
        #hero {
            height: 100vh;
            display: flex;
            align-items: center;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') no-repeat center center/cover;
            color: #fff;
            text-align: center;
            padding-top: 80px;
        }

        .hero-content {
            max-width: 800px;
            margin: auto;
        }

        .hero-content h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }

        .hero-content p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        /* Works Section */
        #works {
            padding: 5rem 0;
            background: var(--light-color);
        }

        .works-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }

        .work-item {
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .work-item:hover {
            transform: translateY(-10px);
        }

        .work-img {
            height: 200px;
            overflow: hidden;
        }

        .work-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .work-item:hover .work-img img {
            transform: scale(1.1);
        }

        .work-info {
            padding: 1.5rem;
        }

        .work-info h3 {
            margin-bottom: 0.5rem;
        }

        .work-info p {
            color: #666;
            margin-bottom: 1rem;
        }

        .work-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .work-tags span {
            background: #eee;
            padding: 0.3rem 0.8rem;
            border-radius: 50px;
            font-size: 0.8rem;
        }

        /* Blog Section */
        #blog {
            padding: 5rem 0;
        }

        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
        }

        .blog-card {
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .blog-img {
            height: 200px;
            overflow: hidden;
        }

        .blog-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .blog-content {
            padding: 1.5rem;
        }

        .blog-content .meta {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
            color: #666;
        }

        .blog-content h3 {
            margin-bottom: 1rem;
        }

        .blog-content p {
            margin-bottom: 1rem;
            color: #666;
        }

        /* Footer */
        footer {
            background: var(--dark-color);
            color: #fff;
            padding: 3rem 0;
            text-align: center;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .footer-column h3 {
            margin-bottom: 1rem;
            color: var(--primary-color);
        }

        .footer-column ul li {
            margin-bottom: 0.5rem;
        }

        .footer-column ul li a {
            color: #ccc;
            transition: color 0.3s ease;
        }

        .footer-column ul li a:hover {
            color: #fff;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 1rem;
        }

        .social-links a {
            color: #fff;
            font-size: 1.2rem;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: var(--primary-color);
        }

        .copyright {
            border-top: 1px solid #444;
            padding-top: 1rem;
            color: #aaa;
            font-size: 0.9rem;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .header-container {
                padding: 1rem;
            }

            nav {
                position: fixed;
                top: 80px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 80px);
                background: #fff;
                transition: all 0.3s ease;
            }

            nav.active {
                left: 0;
            }

            nav ul {
                flex-direction: column;
