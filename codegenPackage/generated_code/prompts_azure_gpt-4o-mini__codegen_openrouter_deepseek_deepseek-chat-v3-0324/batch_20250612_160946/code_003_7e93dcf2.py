"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Create a sample layout using HTML and CSS for a web designer's portfolio that highlights their expertise in Adobe applications and web development.
Generated: DETERMINISTIC_7e93dcf2c7c54ffb
Batch ID: 20250612_160946
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
    <title>Design Portfolio | Adobe & Web Development Expert</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header Styles */
        header {
            background: linear-gradient(135deg, #6e48aa 0%, #9d50bb 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 1.5rem;
        }

        /* Navigation */
        nav {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
        }

        .logo {
            font-weight: bold;
            font-size: 1.5rem;
            color: #6e48aa;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #6e48aa;
        }

        /* Main Content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        section {
            margin-bottom: 3rem;
            padding: 2rem;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.05);
        }

        h2 {
            color: #6e48aa;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 0.5rem;
        }

        /* Skills Section */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .skill-card {
            background-color: #f9f9f9;
            padding: 1.5rem;
            border-radius: 6px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .skill-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .skill-card h3 {
            color: #6e48aa;
            margin-bottom: 0.5rem;
        }

        .skill-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #9d50bb;
        }

        /* Portfolio Section */
        .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .portfolio-item {
            position: relative;
            overflow: hidden;
            border-radius: 6px;
            height: 250px;
        }

        .portfolio-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }

        .portfolio-item:hover img {
            transform: scale(1.05);
        }

        .portfolio-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(110, 72, 170, 0.8);
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .portfolio-item:hover .portfolio-overlay {
            opacity: 1;
        }

        .portfolio-overlay h3 {
            margin-bottom: 0.5rem;
            font-size: 1.3rem;
        }

        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 2rem;
            align-items: center;
        }

        .profile-img {
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        /* Contact Section */
        .contact-form {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group.full-width {
            grid-column: span 2;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        input,
        textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        textarea {
            min-height: 150px;
        }

        button {
            background: linear-gradient(135deg, #6e48aa 0%, #9d50bb 100%);
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: opacity 0.3s;
        }

        button:hover {
            opacity: 0.9;
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
            display: flex;
            justify-content: center;
            margin: 1rem 0;
        }

        .social-links a {
            color: white;
            margin: 0 1rem;
            font-size: 1.5rem;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: #9d50bb;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
            }

            .nav-links {
                margin-top: 1rem;
            }

            .nav-links li {
                margin-left: 1rem;
                margin-right: 1rem;
            }

            .about-content {
                grid-template-columns: 1fr;
            }

            .contact-form {
                grid-template-columns: 1fr;
            }

            .form-group.full-width {
                grid-column: span 1;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>Jane Designer</h1>
            <p class="tagline">Adobe Creative Suite Expert & Web Developer</p>
        </div>
    </header>

    <nav>
        <div class="nav-container">
            <div class="logo">JD</div>
            <ul class="nav-links">
                <li><a href="#skills">Skills</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <main class="container">
        <section id="skills">
            <h2>My Skills</h2>
            <div class="skills-grid">
                <div class="skill-card">
                    <div class="skill-icon">PS</div>
                    <
