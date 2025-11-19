"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Create a simple web page using HTML and CSS that provides information about the services offered by Darul Raza, including istikhaara, taweezat, and social welfare programs.
Generated: DETERMINISTIC_9d071082f11c13e0
Batch ID: 20250622_205627
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
    <title>Darul Raza - Spiritual and Social Services</title>
    <style>
        /* Global Styles */
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

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header Styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            margin-bottom: 10px;
            font-size: 2.5rem;
        }

        /* Navigation Styles */
        nav {
            background-color: #34495e;
            padding: 15px 0;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav ul li {
            margin: 0 15px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #f1c40f;
        }

        /* Main Content Styles */
        main {
            padding: 40px 0;
        }

        section {
            margin-bottom: 40px;
            background-color: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        section h2 {
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f1c40f;
        }

        section p {
            margin-bottom: 15px;
        }

        .service-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .service-card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            border-left: 4px solid #f1c40f;
        }

        .service-card h3 {
            color: #2c3e50;
            margin-bottom: 10px;
        }

        /* Footer Styles */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px 0;
            margin-top: 40px;
        }

        footer p {
            margin-bottom: 10px;
        }

        /* Responsive Styles */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 5px 0;
            }

            header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Darul Raza</h1>
            <p>Spiritual Guidance and Social Welfare</p>
        </div>
    </header>

    <nav>
        <div class="container">
            <ul>
                <li><a href="#istikhaara">Istikhaara</a></li>
                <li><a href="#taweezat">Taweezat</a></li>
                <li><a href="#welfare">Social Welfare</a></li>
            </ul>
        </div>
    </nav>

    <main class="container">
        <section id="about">
            <h2>About Darul Raza</h2>
            <p>Darul Raza is a spiritual and social welfare organization dedicated to providing guidance and support to those in need. Our services are rooted in Islamic traditions and aim to help individuals navigate life's challenges while maintaining faith and dignity.</p>
        </section>

        <section id="istikhaara">
            <h2>Istikhaara Services</h2>
            <p>Istikhaara is a special prayer for seeking guidance from Allah when making important decisions in life.</p>
            
            <div class="service-grid">
                <div class="service-card">
                    <h3>Personal Istikhaara</h3>
                    <p>Guidance for personal matters including marriage, career choices, and relocation decisions.</p>
                </div>
                <div class="service-card">
                    <h3>Business Istikhaara</h3>
                    <p>Seeking divine guidance for business ventures, partnerships, and financial decisions.</p>
                </div>
                <div class="service-card">
                    <h3>Istikhaara Teachings</h3>
                    <p>Learn how to perform Istikhaara prayer yourself with our comprehensive guidance.</p>
                </div>
            </div>
        </section>

        <section id="taweezat">
            <h2>Taweezat Services</h2>
            <p>Taweez are spiritual remedies prepared according to Islamic teachings for protection and healing.</p>
            
            <div class="service-grid">
                <div class="service-card">
                    <h3>Protection Taweez</h3>
                    <p>For protection against evil eye, black magic, and negative energies.</p>
                </div>
                <div class="service-card">
                    <h3>Healing Taweez</h3>
                    <p>For physical and spiritual healing, prepared with specific Quranic verses.</p>
                </div>
                <div class="service-card">
                    <h3>Marital Harmony</h3>
                    <p>Taweez to promote love, understanding and harmony in marital relationships.</p>
                </div>
            </div>
        </section>

        <section id="welfare">
            <h2>Social Welfare Programs</h2>
            <p>Our social welfare initiatives aim to uplift the community through various charitable activities.</p>
            
            <div class="service-grid">
                <div class="service-card">
                    <h3>Orphan Support</h3>
                    <p>Financial and emotional support for orphans, including education sponsorship.</p>
                </div>
                <div class="service-card">
                    <h3>Food Distribution</h3>
                    <p>Regular distribution of food packages to needy families in the community.</p>
                </div>
                <div class="service-card">
                    <h3>Medical Assistance</h3>
                    <p>Financial aid for medical treatments and organizing free medical camps.</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>© 2023 Darul Raza. All rights reserved.</p>
            <p>Contact: info@darulraza.org | Phone: +123 456 7890</p>
        </div>
    </footer>
</body>
</html>
```
