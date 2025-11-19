"""
Generated Code Metadata:
========================
Original URL: https://azuki.zone
Prompt: Design a simple webpage that showcases a designer's works, contact information, and links to their social media profiles or blog, inspired by the layout of azuki.zone.
Generated: DETERMINISTIC_7ec3b3883e635d0d
Batch ID: 20250622_212142
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/600x400": {
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
    <title>Design Portfolio</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        body {
            background-color: #f8f8f8;
            color: #333;
            line-height: 1.6;
        }

        /* Container styles */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* Header styles */
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 3rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 1.5rem;
        }

        nav ul li a {
            text-decoration: none;
            color: #333;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #666;
        }

        /* Hero section */
        .hero {
            text-align: center;
            margin-bottom: 4rem;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 2rem;
            color: #666;
        }

        /* Works grid */
        .works {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }

        .work-item {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .work-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .work-item img {
            width: 100%;
            height: auto;
            display: block;
        }

        .work-info {
            padding: 1.5rem;
        }

        .work-info h3 {
            margin-bottom: 0.5rem;
        }

        .work-info p {
            color: #666;
        }

        /* Contact section */
        .contact {
            background: white;
            padding: 3rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 4rem;
        }

        .contact h2 {
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .contact-form {
            max-width: 500px;
            margin: 0 auto;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        .form-group textarea {
            min-height: 150px;
        }

        button {
            background: #333;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.3s;
        }

        button:hover {
            background: #555;
        }

        /* Social links */
        .social-links {
            text-align: center;
            margin-bottom: 3rem;
        }

        .social-links h2 {
            margin-bottom: 1.5rem;
        }

        .social-icons {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
        }

        .social-icons a {
            color: #333;
            font-size: 1.5rem;
            transition: color 0.3s;
        }

        .social-icons a:hover {
            color: #666;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 2rem 0;
            color: #666;
            font-size: 0.9rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                margin-top: 1rem;
                justify-content: center;
            }

            nav ul li {
                margin: 0 0.75rem;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .works {
                grid-template-columns: 1fr;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">Design Portfolio</div>
            <nav>
                <ul>
                    <li><a href="#works">Works</a></li>
                    <li><a href="#contact">Contact</a></li>
                    <li><a href="#social">Social</a></li>
                </ul>
            </nav>
        </header>

        <section class="hero">
            <h1>Creative Design Solutions</h1>
            <p>Bringing ideas to life through thoughtful design and attention to detail.</p>
        </section>

        <section id="works" class="works">
            <div class="work-item">
                <img src="https://via.placeholder.com/600x400" alt="Project 1">
                <div class="work-info">
                    <h3>Brand Identity</h3>
                    <p>Complete visual identity for a tech startup</p>
                </div>
            </div>
            <div class="work-item">
                <img src="https://via.placeholder.com/600x400" alt="Project 2">
                <div class="work-info">
                    <h3>Website Design</h3>
                    <p>Responsive e-commerce platform</p>
                </div>
            </div>
            <div class="work-item">
                <img src="https://via.placeholder.com/600x400" alt="Project 3">
                <div class="work-info">
                    <h3>Mobile App UI</h3>
                    <p>User interface for a fitness tracking app</p>
                </div>
            </div>
            <div class="work-item">
                <img src="https://via.placeholder.com/600x400" alt="Project 4">
                <div class="work-info">
                    <h3>Packaging Design</h3>
                    <p>Sustainable packaging for a food brand</p>
                </div>
            </div>
            <div class="work-item">
                <img src="https://via.placeholder.com/600x400" alt="Project 5">
                <div class="work-info">
                    <h3>Illustration Series</h3>
                    <p>Digital artwork for a book cover</p>
                </div>
            </div>
            <div class="work-item">
                <img src="https://via.placeholder.com/600x400" alt="Project 6">
                <div class="work-info">
                    <h3>Editorial Design</h3>
                    <p>Layout design for a magazine feature</p>
                </div>
            </div>
        </section>

        <section id="contact" class="contact">
            <h2>Get in Touch</h2>
            <form class="contact-form" id="contactForm">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Message</
