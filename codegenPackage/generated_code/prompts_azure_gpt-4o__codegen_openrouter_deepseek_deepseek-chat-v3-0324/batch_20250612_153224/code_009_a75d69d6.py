"""
Generated Code Metadata:
========================
Original URL: https://agenz.be
Prompt: Write code to create a custom blog theme that emphasizes storytelling and personal branding, as described in Agenz's services.
Generated: DETERMINISTIC_a75d69d6aec05a3c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Storytelling Blog Theme</title>
    <style>
        /* Base Styles */
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --text-color: #333;
            --text-light: #7f8c8d;
            --font-main: 'Georgia', serif;
            --font-heading: 'Playfair Display', serif;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-main);
            line-height: 1.6;
            color: var(--text-color);
            background-color: #f9f9f9;
        }

        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-heading);
            font-weight: 700;
            margin-bottom: 1rem;
            color: var(--dark-color);
        }

        p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }

        a {
            color: var(--secondary-color);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        a:hover {
            color: var(--accent-color);
        }

        /* Layout */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Header */
        header {
            background-color: var(--primary-color);
            color: white;
            padding: 2rem 0;
            position: relative;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-family: var(--font-heading);
            font-size: 2rem;
            font-weight: 700;
        }

        .logo a {
            color: white;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 2rem;
        }

        nav ul li a {
            color: white;
            font-weight: 500;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('hero-bg.jpg');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 8rem 0;
            text-align: center;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            color: white;
        }

        .hero p {
            font-size: 1.5rem;
            max-width: 800px;
            margin: 0 auto 2rem;
            color: var(--light-color);
        }

        .btn {
            display: inline-block;
            background-color: var(--accent-color);
            color: white;
            padding: 0.8rem 1.8rem;
            border-radius: 30px;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .btn:hover {
            background-color: #c0392b;
            transform: translateY(-3px);
            color: white;
        }

        /* Featured Story */
        .featured-story {
            padding: 5rem 0;
            background-color: white;
        }

        .story-card {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
        }

        .story-content {
            padding: 2rem;
        }

        .story-meta {
            color: var(--text-light);
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }

        .story-image {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .story-image img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.5s ease;
        }

        .story-image:hover img {
            transform: scale(1.05);
        }

        /* Recent Posts */
        .recent-posts {
            padding: 5rem 0;
            background-color: var(--light-color);
        }

        .posts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }

        .post-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .post-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
        }

        .post-image {
            height: 200px;
            overflow: hidden;
        }

        .post-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .post-card:hover .post-image img {
            transform: scale(1.1);
        }

        .post-content {
            padding: 1.5rem;
        }

        .post-title {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .post-excerpt {
            color: var(--text-light);
            margin-bottom: 1rem;
        }

        .read-more {
            font-weight: 600;
            font-size: 0.9rem;
        }

        /* About Section */
        .about {
            padding: 5rem 0;
            background-color: white;
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 3rem;
            align-items: center;
        }

        .author-image {
            border-radius: 50%;
            width: 250px;
            height: 250px;
            object-fit: cover;
            border: 5px solid var(--light-color);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        /* Newsletter */
        .newsletter {
            padding: 5rem 0;
            background-color: var(--secondary-color);
            color: white;
            text-align: center;
        }

        .newsletter h2 {
            color: white;
        }

        .newsletter-form {
            max-width: 600px;
            margin: 2rem auto 0;
        }

        .form-group {
            display: flex;
        }

        .form-group input {
            flex: 1;
            padding: 1rem;
            border: none;
            border-radius: 30px 0 0 30px;
            font-size: 1rem;
        }

        .form-group button {
            padding: 1rem 2rem;
            background-color: var(--accent-color);
            color: white;
            border: none;
            border-radius: 0 30px 30px 0;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .form-group button:hover {
            background-color: #c0392b;
        }

        /* Footer */
        footer {
            background-color: var(--dark-color);
            color: white;
            padding: 3rem 0;
            text-align: center;
        }

        .social-links {
            margin: 2rem 0;
        }

        .social-links a {
            display: inline-block;
            margin: 0 1rem;
            color: white;
            font-size: 1.5rem;
        }

        .copyright {
            color: var(--text-light);
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                margin-top: 1.5rem;
                justify-content: center;
            }

            nav ul li {
                margin: 0 1rem;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .story-card, .about-content {
                grid-template-columns: 1fr;
