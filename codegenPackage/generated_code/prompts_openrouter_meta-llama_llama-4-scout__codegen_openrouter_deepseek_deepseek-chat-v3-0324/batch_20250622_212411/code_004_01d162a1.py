"""
Generated Code Metadata:
========================
Original URL: https://berachain.stride.co
Prompt: "Design a basic HTML/CSS template for a domain sale landing page, inspired by the layout and content of Stride.co for sale listings."
Generated: DETERMINISTIC_01d162a1946f2379
Batch ID: 20250622_212411
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
    <title>Premium Domain for Sale | ExampleDomain.com</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }

        /* Container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header */
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 24px;
            font-weight: 700;
            color: #4a6bff;
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            text-decoration: none;
            color: #555;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #4a6bff;
        }

        /* Hero Section */
        .hero {
            padding: 80px 0;
            text-align: center;
            background-color: #fff;
            margin-bottom: 40px;
        }

        .domain-name {
            font-size: 48px;
            font-weight: 700;
            color: #222;
            margin-bottom: 20px;
        }

        .domain-tag {
            display: inline-block;
            background-color: #4a6bff;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 30px;
        }

        .price {
            font-size: 36px;
            font-weight: 700;
            color: #4a6bff;
            margin-bottom: 30px;
        }

        .cta-button {
            background-color: #4a6bff;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .cta-button:hover {
            background-color: #3a5bef;
        }

        /* Domain Details */
        .domain-details {
            background-color: #fff;
            border-radius: 10px;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }

        .section-title {
            font-size: 28px;
            margin-bottom: 30px;
            color: #222;
        }

        .details-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .detail-card {
            padding: 20px;
            border-radius: 8px;
            background-color: #f8f9fa;
        }

        .detail-card h3 {
            font-size: 18px;
            margin-bottom: 10px;
            color: #555;
        }

        .detail-card p {
            font-size: 16px;
            color: #333;
        }

        /* Footer */
        footer {
            background-color: #222;
            color: #fff;
            padding: 40px 0;
            text-align: center;
        }

        .footer-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .footer-links {
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }

        .footer-links a {
            color: #aaa;
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: #fff;
        }

        .copyright {
            color: #777;
            font-size: 14px;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .domain-name {
                font-size: 36px;
            }

            .price {
                font-size: 28px;
            }

            .header-content {
                flex-direction: column;
                gap: 20px;
            }

            .nav-links {
                gap: 15px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container header-content">
            <div class="logo">DomainMarket</div>
            <nav class="nav-links">
                <a href="#">Browse Domains</a>
                <a href="#">Sell Your Domain</a>
                <a href="#">About Us</a>
                <a href="#">Contact</a>
            </nav>
        </div>
    </header>

    <main class="container">
        <section class="hero">
            <h1 class="domain-name">ExampleDomain.com</h1>
            <span class="domain-tag">Premium Domain</span>
            <div class="price">$25,000</div>
            <button class="cta-button">Make an Offer</button>
        </section>

        <section class="domain-details">
            <h2 class="section-title">Domain Details</h2>
            <div class="details-grid">
                <div class="detail-card">
                    <h3>Domain Age</h3>
                    <p>Registered since 2010 (14 years)</p>
                </div>
                <div class="detail-card">
                    <h3>Extension</h3>
                    <p>.com (Most valuable TLD)</p>
                </div>
                <div class="detail-card">
                    <h3>Traffic Potential</h3>
                    <p>High - Great for branding and SEO</p>
                </div>
                <div class="detail-card">
                    <h3>Keywords</h3>
                    <p>Example, Domain, Premium, Brandable</p>
                </div>
                <div class="detail-card">
                    <h3>Similar Sales</h3>
                    <p>ExampleDomains.com sold for $30,000 in 2022</p>
                </div>
                <div class="detail-card">
                    <h3>Seller Notes</h3>
                    <p>This premium domain is perfect for startups, tech companies, or branding projects.</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container footer-content">
            <div class="logo">DomainMarket</div>
            <div class="footer-links">
                <a href="#">Terms</a>
                <a href="#">Privacy</a>
                <a href="#">FAQ</a>
                <a href="#">Contact</a>
            </div>
            <p class="copyright">© 2023 DomainMarket. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```
