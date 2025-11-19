"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Design a simple web page using HTML, CSS, and JavaScript to showcase the courses and services offered by a physics class institute like Sameer's Physics Classes.
Generated: DETERMINISTIC_0613623c0430f50a
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code for a simple web page showcasing courses and services for a physics class institute:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sameer's Physics Classes - Courses & Services</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }

        /* Header styles */
        header {
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            color: white;
            padding: 1.5rem 0;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        /* Navigation */
        nav {
            background-color: #333;
            padding: 1rem 0;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav ul li {
            margin: 0 1rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        nav ul li a:hover {
            background-color: #555;
        }

        /* Main content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1.5rem;
        }

        section {
            margin-bottom: 3rem;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        }

        h2 {
            color: #1a2a6c;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #eee;
        }

        /* Courses grid */
        .courses-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .course-card {
            border: 1px solid #ddd;
            border-radius: 6px;
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .course-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .course-img {
            height: 180px;
            background-color: #eee;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: #555;
        }

        .course-content {
            padding: 1.5rem;
        }

        .course-title {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
            color: #1a2a6c;
        }

        .course-desc {
            margin-bottom: 1rem;
            color: #666;
        }

        .course-price {
            font-weight: bold;
            color: #b21f1f;
        }

        /* Services list */
        .services-list {
            list-style: none;
        }

        .services-list li {
            padding: 1rem 0;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .services-list li:last-child {
            border-bottom: none;
        }

        .service-name {
            font-weight: bold;
            color: #1a2a6c;
        }

        /* Testimonials */
        .testimonials {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .testimonial-card {
            background-color: #f5f5f5;
            padding: 1.5rem;
            border-radius: 6px;
            position: relative;
        }

        .testimonial-card::before {
            content: '"';
            font-size: 4rem;
            position: absolute;
            top: 0;
            left: 10px;
            color: rgba(0, 0, 0, 0.1);
            line-height: 1;
        }

        .testimonial-text {
            margin-bottom: 1rem;
            font-style: italic;
        }

        .testimonial-author {
            font-weight: bold;
            text-align: right;
        }

        /* Contact form */
        .contact-form {
            display: grid;
            gap: 1rem;
        }

        .form-group {
            margin-bottom: 1rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        input, textarea, select {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        textarea {
            min-height: 120px;
        }

        button {
            background-color: #1a2a6c;
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #0d1a4a;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }

        .social-links {
            margin: 1rem 0;
        }

        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.5rem;
            text-decoration: none;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 0.5rem 0;
            }

            .logo {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Sameer's Physics Classes</div>
        <div class="tagline">Master Physics with Expert Guidance</div>
    </header>

    <nav>
        <ul>
            <li><a href="#courses">Courses</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#testimonials">Testimonials</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <div class="container">
        <section id="courses">
            <h2>Our Courses</h2>
            <div class="courses-grid">
                <div class="course-card">
                    <div class="course-img">JEE</div>
                    <div class="course-content">
                        <h3 class="course-title">JEE Physics</h3>
                        <p class="course-desc">Comprehensive course covering all JEE syllabus with problem-solving techniques.</p>
                        <p class="course-price">₹15,000/year</p>
                    </div>
                </div>
                <div class="course-card">
                    <div class="course-img">NEET</div>
                    <div class="course-content">
                        <h3 class="course-title">NEET Physics</h3>
                        <p class="course-desc">Focused preparation for NEET with conceptual clarity and MCQs practice.</p>
                        <p class="course-price">₹12,000/year</p>
                    </div>
                </div>
                <div class="course-card">
                    <div class="course-img">CBSE</div>
                    <div class="course-content">
                        <h3 class="course-title">CBSE Class 11-12</h3>
                        <p class="course-desc">Detailed coverage of CBSE
