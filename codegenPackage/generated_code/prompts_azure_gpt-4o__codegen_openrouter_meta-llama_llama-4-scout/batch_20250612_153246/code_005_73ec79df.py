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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pricing Table</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="pricing-table">
        <div class="pricing-table-header">
            <h2>Choose the plan that's right for you</h2>
        </div>
        <div class="pricing-table-content">
            <div class="pricing-table-item">
                <h3>Minim</h3>
                <p>$29 <span>/month</span></p>
                <ul>
                    <li><i class="checkmark"></i> SEO</li>
                    <li><i class="checkmark"></i> Basic Maintenance</li>
                    <li><i class="checkmark"></i> Limited Visual Identity</li>
                </ul>
                <button>Get Started</button>
            </div>
            <div class="pricing-table-item featured">
                <h3>Mediu</h3>
                <p>$49 <span>/month</span></p>
                <ul>
                    <li><i class="checkmark"></i> SEO</li>
                    <li><i class="checkmark"></i> Advanced Maintenance</li>
                    <li><i class="checkmark"></i> Enhanced Visual Identity</li>
                    <li><i class="checkmark"></i> Priority Support</li>
                </ul>
                <button>Get Started</button>
            </div>
            <div class="pricing-table-item">
                <h3>Maxim</h3>
                <p>$99 <span>/month</span></p>
                <ul>
                    <li><i class="checkmark"></i> SEO</li>
                    <li><i class="checkmark"></i> Comprehensive Maintenance</li>
                    <li><i class="checkmark"></i> Premium Visual Identity</li>
                    <li><i class="checkmark"></i> Dedicated Support</li>
                    <li><i class="checkmark"></i> Advanced Analytics</li>
                </ul>
                <button>Get Started</button>
            </div>
        </div>
    </div>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Pricing Table Styles */
.pricing-table {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.pricing-table-header {
    text-align: center;
    margin-bottom: 20px;
}

.pricing-table-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.pricing-table-item {
    flex-basis: calc(33.33% - 20px);
    margin: 10px;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.pricing-table-item.featured {
    background-color: #f7f7f7;
    border-color: #ccc;
}

.pricing-table-item h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

.pricing-table-item p {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

.pricing-table-item p span {
    font-size: 14px;
    font-weight: normal;
}

.pricing-table-item ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.pricing-table-item li {
    margin-bottom: 10px;
}

.checkmark {
    display: inline-block;
    width: 20px;
    height: 20px;
    background-color: #4CAF50;
    color: #fff;
    border-radius: 50%;
    text-align: center;
    line-height: 20px;
    font-size: 12px;
}

.pricing-table-item button {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
}

.pricing-table-item button:hover {
    background-color: #3e8e41;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .pricing-table-item {
        flex-basis: calc(50% - 20px);
    }
}

@media only screen and (max-width: 480px) {
    .pricing-table-item {
        flex-basis: 100%;
        margin: 10px 0;
    }
}
```
