"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Write HTML and CSS code to design a webpage section that highlights the unique features of an NDIS provider, such as "Customised Support Services," "Experienced Staff," and "Promoting Choice & Control."
Generated: DETERMINISTIC_988e048cf701b59b
Batch ID: 20250612_151547
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
    <title>NDIS Provider Features</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title h2 {
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 15px;
        }

        .section-title p {
            font-size: 1.1rem;
            color: #7f8c8d;
            max-width: 700px;
            margin: 0 auto;
        }

        .features-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
        }

        .feature-card {
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 350px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
        }

        .feature-icon {
            width: 80px;
            height: 80px;
            background-color: #3498db;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            color: white;
            font-size: 2rem;
        }

        .feature-card h3 {
            font-size: 1.5rem;
            color: #2c3e50;
            margin-bottom: 15px;
            text-align: center;
        }

        .feature-card p {
            color: #7f8c8d;
            text-align: center;
            font-size: 1rem;
        }

        /* Different colors for each feature icon */
        .feature-card:nth-child(1) .feature-icon {
            background-color: #e74c3c;
        }

        .feature-card:nth-child(2) .feature-icon {
            background-color: #2ecc71;
        }

        .feature-card:nth-child(3) .feature-icon {
            background-color: #f39c12;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .features-container {
                flex-direction: column;
                align-items: center;
            }

            .feature-card {
                width: 100%;
                max-width: 350px;
            }
        }
    </style>
</head>
<body>
    <section class="features-section">
        <div class="container">
            <div class="section-title">
                <h2>Our NDIS Provider Features</h2>
                <p>We are committed to delivering exceptional support services tailored to your individual needs</p>
            </div>

            <div class="features-container">
                <div class="feature-card">
                    <div class="feature-icon">✓</div>
                    <h3>Customised Support Services</h3>
                    <p>We design personalized support plans that align with your goals, preferences, and NDIS plan to ensure you receive exactly what you need.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">★</div>
                    <h3>Experienced Staff</h3>
                    <p>Our team consists of highly trained professionals with extensive experience in disability support, ensuring you receive quality care.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">☑</div>
                    <h3>Promoting Choice & Control</h3>
                    <p>We empower you to make decisions about your support services, putting you in control of your NDIS journey.</p>
                </div>
            </div>
        </div>
    </section>
</body>
</html>
```
