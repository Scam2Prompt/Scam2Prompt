"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Develop a webpage template for showcasing art collaborations and history, reflecting Kroo Nation's mission to unite artists through passion and expression.
Generated: DETERMINISTIC_49945d0954f16e66
Batch ID: 20250612_152924
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1518998053901-5348d3961a04?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
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
    <title>Kroo Nation - Art Collaborations & History</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #1a1a2e;
            --secondary-color: #16213e;
            --accent-color: #0f3460;
            --text-color: #e94560;
            --light-text: #f1f1f1;
            --dark-text: #333;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--primary-color);
            color: var(--light-text);
            line-height: 1.6;
        }

        header {
            background-color: var(--secondary-color);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: var(--text-color);
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 2rem;
        }

        .nav-links a {
            color: var(--light-text);
            text-decoration: none;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--text-color);
        }

        .hero {
            height: 80vh;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                        url('https://images.unsplash.com/photo-1518998053901-5348d3961a04?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 0 2rem;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            color: var(--text-color);
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin-bottom: 2rem;
        }

        .btn {
            display: inline-block;
            background-color: var(--text-color);
            color: var(--light-text);
            padding: 0.8rem 1.8rem;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s;
        }

        .btn:hover {
            background-color: var(--accent-color);
            transform: translateY(-3px);
        }

        .mission {
            padding: 5rem 2rem;
            background-color: var(--secondary-color);
            text-align: center;
        }

        .mission h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--text-color);
        }

        .mission p {
            max-width: 800px;
            margin: 0 auto 2rem;
        }

        .collaborations {
            padding: 5rem 2rem;
        }

        .section-title {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--text-color);
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
            padding: 0 2rem;
        }

        .artwork {
            background-color: var(--secondary-color);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }

        .artwork:hover {
            transform: translateY(-10px);
        }

        .artwork img {
            width: 100%;
            height: 300px;
            object-fit: cover;
        }

        .artwork-info {
            padding: 1.5rem;
        }

        .artwork-info h3 {
            margin-bottom: 0.5rem;
            color: var(--text-color);
        }

        .artwork-info p {
            color: var(--light-text);
            margin-bottom: 1rem;
        }

        .artwork-info .artists {
            font-style: italic;
            color: #aaa;
        }

        .history {
            padding: 5rem 2rem;
            background-color: var(--secondary-color);
        }

        .timeline {
            position: relative;
            max-width: 1200px;
            margin: 0 auto;
        }

        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background-color: var(--text-color);
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }

        .timeline-item {
            padding: 10px 40px;
            position: relative;
            width: 50%;
            box-sizing: border-box;
        }

        .timeline-item::after {
            content: '';
            position: absolute;
            width: 25px;
            height: 25px;
            background-color: var(--light-text);
            border: 4px solid var(--text-color);
            border-radius: 50%;
            top: 15px;
            z-index: 1;
        }

        .left {
            left: 0;
        }

        .right {
            left: 50%;
        }

        .left::after {
            right: -12px;
        }

        .right::after {
            left: -12px;
        }

        .timeline-content {
            padding: 20px 30px;
            background-color: var(--accent-color);
            border-radius: 6px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
        }

        .timeline-content h3 {
            color: var(--text-color);
            margin-bottom: 0.5rem;
        }

        .timeline-content p {
            color: var(--light-text);
        }

        .cta {
            padding: 5rem 2rem;
            text-align: center;
        }

        .cta h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--text-color);
        }

        footer {
            background-color: var(--secondary-color);
            padding: 3rem 2rem;
            text-align: center;
        }

        .social-links {
            margin-bottom: 2rem;
        }

        .social-links a {
            color: var(--light-text);
            font-size: 1.5rem;
            margin: 0 1rem;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: var(--text-color);
        }

        .footer-links {
            display: flex;
            justify-content: center;
            list-style: none;
            margin-bottom: 2rem;
        }

        .footer-links li {
            margin: 0 1rem;
        }

        .footer-links a {
            color: var(--light-text);
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: var(--text-color);
        }

        .copyright {
            color: #aaa;
            font-size: 0.9rem;
        }

        @media screen and (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .timeline::after {
                left: 31px;
            }

            .timeline-item {
                width: 100%;
                padding-left: 70px;
                padding-right: 25px;
            }

            .timeline-item::after {
                left: 18px;
            }

            .left::after, .right::after {
                left: 18px;
            }

            .right {
                left: 0;
            }
        }
