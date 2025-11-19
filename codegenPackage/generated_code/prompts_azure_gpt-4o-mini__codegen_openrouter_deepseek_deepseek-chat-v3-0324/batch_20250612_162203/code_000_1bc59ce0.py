"""
Generated Code Metadata:
========================
Original URL: https://akaan.com.tr
Prompt: Generate a code snippet for a mobile-friendly website layout using HTML and CSS, inspired by Akaan's web design services.
Generated: DETERMINISTIC_1bc59ce0bfe1c62d
Batch ID: 20250612_162203
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
    <title>Akaan-Inspired Mobile Layout</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background: linear-gradient(135deg, #6e48aa 0%, #9d50bb 100%);
            color: white;
            padding: 1.5rem;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .tagline {
            font-size: 1rem;
            opacity: 0.9;
        }

        /* Navigation */
        nav {
            display: flex;
            justify-content: center;
            background-color: #fff;
            padding: 1rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 1.5rem;
        }

        .nav-links a {
            text-decoration: none;
            color: #6e48aa;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #9d50bb;
        }

        /* Mobile menu toggle */
        .menu-toggle {
            display: none;
            cursor: pointer;
            font-size: 1.5rem;
        }

        /* Hero section */
        .hero {
            padding: 3rem 1.5rem;
            text-align: center;
            background-color: #fff;
            margin-bottom: 2rem;
        }

        .hero h1 {
            font-size: 2.2rem;
            margin-bottom: 1rem;
            color: #6e48aa;
        }

        .hero p {
            font-size: 1.1rem;
            max-width: 700px;
            margin: 0 auto 2rem;
        }

        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, #6e48aa 0%, #9d50bb 100%);
            color: white;
            padding: 0.8rem 1.8rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 4px 15px rgba(110, 72, 170, 0.3);
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(110, 72, 170, 0.4);
        }

        /* Services section */
        .services {
            padding: 2rem 1.5rem;
            background-color: #fff;
            margin-bottom: 2rem;
        }

        .section-title {
            text-align: center;
            margin-bottom: 2rem;
            color: #6e48aa;
            font-size: 1.8rem;
        }

        .service-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .service-card {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 1.5rem;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .service-card h3 {
            color: #6e48aa;
            margin-bottom: 1rem;
        }

        /* Footer */
        footer {
            background-color: #2d2d2d;
            color: #fff;
            padding: 2rem 1.5rem;
            text-align: center;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .footer-links a {
            color: #fff;
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: #9d50bb;
        }

        .copyright {
            opacity: 0.8;
            font-size: 0.9rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
                flex-direction: column;
                width: 100%;
                text-align: center;
            }

            .nav-links.active {
                display: flex;
            }

            .menu-toggle {
                display: block;
            }

            .hero h1 {
                font-size: 1.8rem;
            }

            .service-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Akaan Design</div>
        <div class="tagline">Creating beautiful digital experiences</div>
    </header>

    <nav>
        <div class="menu-toggle">☰</div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#portfolio">Portfolio</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section class="hero" id="home">
        <h1>Transform Your Digital Presence</h1>
        <p>We craft stunning, responsive websites that engage your audience and drive results. Let's build something amazing together.</p>
        <a href="#contact" class="cta-button">Get Started</a>
    </section>

    <section class="services" id="services">
        <h2 class="section-title">Our Services</h2>
        <div class="service-grid">
            <div class="service-card">
                <h3>Web Design</h3>
                <p>Custom, mobile-responsive designs tailored to your brand and audience.</p>
            </div>
            <div class="service-card">
                <h3>UI/UX Development</h3>
                <p>Intuitive interfaces and seamless user experiences that convert visitors.</p>
            </div>
            <div class="service-card">
                <h3>E-Commerce Solutions</h3>
                <p>Powerful online stores designed to maximize sales and customer satisfaction.</p>
            </div>
        </div>
    </section>

    <footer>
        <div class="footer-links">
            <a href="#privacy">Privacy Policy</a>
            <a href="#terms">Terms of Service</a>
            <a href="#contact">Contact Us</a>
        </div>
        <div class="copyright">
            &copy; 2023 Akaan Design. All rights reserved.
        </div>
    </footer>

    <script>
        // Mobile menu toggle functionality
        document.querySelector('.menu-toggle').addEventListener('click', function() {
            document.querySelector('.nav-links').classList.toggle('active');
        });

        // Close mobile menu when clicking a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', function() {
                document.querySelector('.nav-links').classList.remove('active');
            });
        });

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>
```
