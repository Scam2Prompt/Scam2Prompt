"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: Generate HTML and CSS code for a pricing table that includes packages like "Minim," "Mediu," and "Maxim," with features such as SEO, maintenance, and visual identity elements, as detailed on Henfruit's website.
Generated: DETERMINISTIC_73ec79df5eb334bf
Batch ID: 20250612_153246
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
    <title>Pricing Table</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 40px;
            color: #2c3e50;
        }

        /* Pricing table styles */
        .pricing-table {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }

        .pricing-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            width: 300px;
            overflow: hidden;
            transition: transform 0.3s ease;
        }

        .pricing-card:hover {
            transform: translateY(-10px);
        }

        .pricing-header {
            padding: 30px;
            text-align: center;
            background: linear-gradient(135deg, #3498db, #2c3e50);
            color: white;
        }

        .pricing-header.minim {
            background: linear-gradient(135deg, #1abc9c, #16a085);
        }

        .pricing-header.mediu {
            background: linear-gradient(135deg, #3498db, #2980b9);
        }

        .pricing-header.maxim {
            background: linear-gradient(135deg, #9b59b6, #8e44ad);
        }

        .pricing-title {
            font-size: 24px;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .pricing-price {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .pricing-period {
            font-size: 14px;
            opacity: 0.8;
        }

        .pricing-features {
            padding: 30px;
        }

        .pricing-features ul {
            list-style: none;
        }

        .pricing-features li {
            padding: 10px 0;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
        }

        .pricing-features li:last-child {
            border-bottom: none;
        }

        .feature-icon {
            margin-right: 10px;
            color: #2ecc71;
        }

        .pricing-button {
            display: block;
            text-align: center;
            padding: 15px;
            background: #2ecc71;
            color: white;
            text-decoration: none;
            font-weight: 700;
            border-radius: 5px;
            margin: 20px;
            transition: background 0.3s ease;
        }

        .pricing-button:hover {
            background: #27ae60;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .pricing-table {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Our Pricing Packages</h1>
        
        <div class="pricing-table">
            <!-- Minim Package -->
            <div class="pricing-card">
                <div class="pricing-header minim">
                    <div class="pricing-title">Minim</div>
                    <div class="pricing-price">$99</div>
                    <div class="pricing-period">per month</div>
                </div>
                <div class="pricing-features">
                    <ul>
                        <li><span class="feature-icon">✓</span> Basic SEO Optimization</li>
                        <li><span class="feature-icon">✓</span> Monthly Maintenance</li>
                        <li><span class="feature-icon">✓</span> Logo Design</li>
                        <li><span class="feature-icon">✓</span> 5 Email Accounts</li>
                        <li><span class="feature-icon">✓</span> 24/7 Support</li>
                    </ul>
                </div>
                <a href="#" class="pricing-button">Get Started</a>
            </div>
            
            <!-- Mediu Package -->
            <div class="pricing-card">
                <div class="pricing-header mediu">
                    <div class="pricing-title">Mediu</div>
                    <div class="pricing-price">$199</div>
                    <div class="pricing-period">per month</div>
                </div>
                <div class="pricing-features">
                    <ul>
                        <li><span class="feature-icon">✓</span> Advanced SEO Optimization</li>
                        <li><span class="feature-icon">✓</span> Weekly Maintenance</li>
                        <li><span class="feature-icon">✓</span> Full Visual Identity</li>
                        <li><span class="feature-icon">✓</span> 10 Email Accounts</li>
                        <li><span class="feature-icon">✓</span> Social Media Integration</li>
                        <li><span class="feature-icon">✓</span> 24/7 Priority Support</li>
                    </ul>
                </div>
                <a href="#" class="pricing-button">Get Started</a>
            </div>
            
            <!-- Maxim Package -->
            <div class="pricing-card">
                <div class="pricing-header maxim">
                    <div class="pricing-title">Maxim</div>
                    <div class="pricing-price">$299</div>
                    <div class="pricing-period">per month</div>
                </div>
                <div class="pricing-features">
                    <ul>
                        <li><span class="feature-icon">✓</span> Premium SEO Optimization</li>
                        <li><span class="feature-icon">✓</span> Daily Maintenance</li>
                        <li><span class="feature-icon">✓</span> Complete Visual Identity</li>
                        <li><span class="feature-icon">✓</span> Unlimited Email Accounts</li>
                        <li><span class="feature-icon">✓</span> Social Media Management</li>
                        <li><span class="feature-icon">✓</span> Content Creation</li>
                        <li><span class="feature-icon">✓</span> 24/7 VIP Support</li>
                    </ul>
                </div>
                <a href="#" class="pricing-button">Get Started</a>
            </div>
        </div>
    </div>
</body>
</html>
```
