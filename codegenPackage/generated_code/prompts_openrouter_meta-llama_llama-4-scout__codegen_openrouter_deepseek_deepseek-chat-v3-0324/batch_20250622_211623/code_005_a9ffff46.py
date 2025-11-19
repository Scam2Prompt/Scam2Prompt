"""
Generated Code Metadata:
========================
Original URL: https://backontrackpsych.com
Prompt: Create a basic webpage template for a psychology clinic that provides information on services like psychology, neuropsychology, speech pathology, and occupational therapy.
Generated: DETERMINISTIC_a9ffff4602695f87
Batch ID: 20250622_211623
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
    <title>Mind & Wellness Clinic | Psychology Services</title>
    <meta name="description" content="Professional psychology clinic offering psychology, neuropsychology, speech pathology, and occupational therapy services.">
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }

        /* Header styles */
        header {
            background-color: #4a6fa5;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }

        .logo {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 0.5rem 0;
        }

        nav ul li {
            margin: 0 1rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }

        nav ul li a:hover {
            text-decoration: underline;
        }

        /* Main content styles */
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .hero {
            text-align: center;
            padding: 2rem;
            background-color: #e6f2ff;
            border-radius: 8px;
            margin-bottom: 2rem;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .service-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .service-card h3 {
            color: #4a6fa5;
            margin-bottom: 1rem;
        }

        /* Footer styles */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        .contact-info {
            margin-bottom: 1rem;
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            nav ul {
                flex-direction: column;
            }
            nav ul li {
                margin: 0.5rem 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Mind & Wellness Clinic</div>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home" class="hero">
            <h1>Comprehensive Psychological Care</h1>
            <p>Providing expert services in psychology, neuropsychology, speech pathology, and occupational therapy to help you achieve optimal mental health and well-being.</p>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <div class="services">
                <div class="service-card">
                    <h3>Psychology</h3>
                    <p>Individual and group therapy for mental health concerns including anxiety, depression, trauma, and relationship issues.</p>
                </div>
                <div class="service-card">
                    <h3>Neuropsychology</h3>
                    <p>Assessment and treatment for cognitive, behavioral, and emotional difficulties resulting from brain injury or neurological conditions.</p>
                </div>
                <div class="service-card">
                    <h3>Speech Pathology</h3>
                    <p>Evaluation and therapy for speech, language, voice, fluency, and swallowing disorders across all age groups.</p>
                </div>
                <div class="service-card">
                    <h3>Occupational Therapy</h3>
                    <p>Helping individuals achieve independence in all areas of their lives through therapeutic interventions.</p>
                </div>
            </div>
        </section>

        <section id="about">
            <h2>About Our Clinic</h2>
            <p>Our team of licensed professionals is dedicated to providing evidence-based, compassionate care tailored to each individual's needs. We believe in a holistic approach to mental health and well-being.</p>
        </section>
    </main>

    <footer id="contact">
        <div class="contact-info">
            <p>123 Wellness Street, Suite 100</p>
            <p>Cityville, State 12345</p>
            <p>Phone: (555) 123-4567</p>
            <p>Email: info@mindwellnessclinic.com</p>
        </div>
        <p>&copy; 2023 Mind & Wellness Clinic. All rights reserved.</p>
    </footer>
</body>
</html>
```
