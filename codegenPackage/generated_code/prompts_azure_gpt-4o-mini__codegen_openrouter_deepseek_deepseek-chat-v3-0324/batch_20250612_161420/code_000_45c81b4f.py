"""
Generated Code Metadata:
========================
Original URL: https://ohibo.it
Prompt: Generate a web design project proposal for a branding agency similar to OHIBÒ, focusing on brand identity and social media management.
Generated: DETERMINISTIC_45c81b4f15cfa09d
Batch ID: 20250612_161420
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap": {
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
    <title>Branding Agency Proposal</title>
    <style>
        /* Global Styles */
        :root {
            --primary-color: #2a2a72;
            --secondary-color: #ff9f1c;
            --accent-color: #e71d36;
            --light-color: #f8f9fa;
            --dark-color: #212529;
            --font-main: 'Helvetica Neue', Arial, sans-serif;
            --font-heading: 'Montserrat', sans-serif;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-main);
            line-height: 1.6;
            color: var(--dark-color);
            background-color: var(--light-color);
        }

        /* Typography */
        h1, h2, h3, h4 {
            font-family: var(--font-heading);
            margin-bottom: 1rem;
            color: var(--primary-color);
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 700;
        }

        h2 {
            font-size: 2rem;
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
        }

        h3 {
            font-size: 1.5rem;
            color: var(--accent-color);
        }

        p {
            margin-bottom: 1rem;
        }

        /* Layout */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            background-color: var(--primary-color);
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: var(--secondary-color);
        }

        .intro {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .service-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .service-card:hover {
            transform: translateY(-5px);
        }

        .service-icon {
            font-size: 2rem;
            color: var(--secondary-color);
            margin-bottom: 1rem;
        }

        .process {
            margin-bottom: 2rem;
        }

        .process-steps {
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .step {
            flex: 1;
            min-width: 200px;
            background-color: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: relative;
        }

        .step-number {
            position: absolute;
            top: -15px;
            left: -15px;
            background-color: var(--accent-color);
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }

        .pricing {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }

        .pricing-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1.5rem;
        }

        .pricing-table th, .pricing-table td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        .pricing-table th {
            background-color: var(--primary-color);
            color: white;
        }

        .pricing-table tr:hover {
            background-color: #f5f5f5;
        }

        .highlight {
            background-color: rgba(255, 159, 28, 0.1);
            border-left: 4px solid var(--secondary-color);
            padding: 1rem;
            margin: 1rem 0;
        }

        .cta {
            text-align: center;
            padding: 2rem;
            background-color: var(--primary-color);
            color: white;
            border-radius: 8px;
        }

        .btn {
            display: inline-block;
            padding: 0.8rem 1.5rem;
            background-color: var(--secondary-color);
            color: var(--dark-color);
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }

        .btn:hover {
            background-color: #e68a19;
            transform: translateY(-2px);
        }

        footer {
            text-align: center;
            padding: 2rem 0;
            background-color: var(--dark-color);
            color: white;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .services {
                grid-template-columns: 1fr;
            }

            .process-steps {
                flex-direction: column;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">LUMINA</div>
            <h1>Brand Identity & Social Media Proposal</h1>
            <p>Elevating your brand through strategic design and digital presence</p>
        </div>
    </header>

    <main class="container">
        <section class="intro">
            <h2>Project Overview</h2>
            <p>Thank you for considering LUMINA for your branding needs. This proposal outlines our approach to developing a comprehensive brand identity and social media strategy that will position your brand for success in today's competitive market.</p>
            
            <div class="highlight">
                <h3>Our Promise</h3>
                <p>We deliver distinctive brand identities that resonate with your target audience and social media strategies that drive engagement and growth. Our process is collaborative, transparent, and results-driven.</p>
            </div>
        </section>

        <section class="services">
            <h2>Our Services</h2>
            <div class="service-card">
                <div class="service-icon">
                    <i class="fas fa-palette"></i>
                </div>
                <h3>Brand Identity</h3>
                <p>Comprehensive visual identity including logo design, color palette, typography, and brand guidelines to ensure consistent application across all touchpoints.</p>
            </div>

            <div class="service-card">
                <div class="service-icon">
                    <i class="fas fa-hashtag"></i>
                </div>
                <h3>Social Media Strategy</h3>
                <p>Customized content calendar, platform-specific strategies, and engagement tactics to build your online community and amplify your brand voice.</p>
            </div>

            <div class="service-card">
                <div class="service-icon">
                    <i class="fas fa-chart-line"></i>
                </div>
                <h3>Performance Analytics</h3>
                <p>Monthly reports with key metrics, insights, and actionable recommendations to optimize your social media performance.</p>
            </div>
        </section>

        <section class="process">
            <h2>Our Process</h2>
            <p>We follow a structured yet flexible approach to ensure your brand identity and social media strategy align perfectly with your business goals.</p>
            
            <div class="process-steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3>Discovery</h3>
                    <p>In-depth research and workshops to understand your business
