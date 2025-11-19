"""
Generated Code Metadata:
========================
Original URL: https://tesla-promo.epizy.com
Prompt: Design a basic web hosting plan comparison table that includes iFastNet Web Hosting's features, such as free domain name, unlimited disk space, and modern cPanel.
Generated: DETERMINISTIC_68ba8715e92f3c48
Batch ID: 20250622_211952
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
    <title>Web Hosting Plan Comparison</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        .comparison-table th, .comparison-table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .comparison-table th {
            background-color: #f4f4f4;
            font-weight: bold;
        }
        .comparison-table tr:hover {
            background-color: #f9f9f9;
        }
        .feature-name {
            font-weight: bold;
            width: 30%;
        }
        .plan-name {
            font-weight: bold;
            color: #2c3e50;
        }
        .highlight {
            background-color: #e8f4fc;
        }
        .checkmark {
            color: #27ae60;
            font-weight: bold;
        }
        .xmark {
            color: #e74c3c;
            font-weight: bold;
        }
        .tier-label {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.8em;
            font-weight: bold;
            color: white;
        }
        .starter {
            background-color: #3498db;
        }
        .business {
            background-color: #2ecc71;
        }
        .enterprise {
            background-color: #9b59b6;
        }
    </style>
</head>
<body>
    <h1>Web Hosting Plan Comparison</h1>
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Feature</th>
                <th class="plan-name">Starter <span class="tier-label starter">Basic</span></th>
                <th class="plan-name">Business <span class="tier-label business">Recommended</span></th>
                <th class="plan-name">Enterprise <span class="tier-label enterprise">Premium</span></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="feature-name">Free Domain Name</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
            </tr>
            <tr>
                <td class="feature-name">Unlimited Disk Space</td>
                <td class="xmark">✗</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
            </tr>
            <tr>
                <td class="feature-name">Modern cPanel</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
            </tr>
            <tr>
                <td class="feature-name">Unlimited Bandwidth</td>
                <td class="xmark">✗</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
            </tr>
            <tr>
                <td class="feature-name">Email Accounts</td>
                <td>5</td>
                <td>Unlimited</td>
                <td>Unlimited</td>
            </tr>
            <tr>
                <td class="feature-name">Free SSL Certificate</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
            </tr>
            <tr>
                <td class="feature-name">24/7 Support</td>
                <td class="checkmark">✓</td>
                <td class="checkmark">✓</td>
                <td class="highlight">Premium Support</td>
            </tr>
            <tr>
                <td class="feature-name">Money-back Guarantee</td>
                <td>30 days</td>
                <td>30 days</td>
                <td>45 days</td>
            </tr>
        </tbody>
    </table>

    <script>
        // This script could be expanded to add interactive features
        document.addEventListener('DOMContentLoaded', function() {
            // Example: Add click event to table rows for mobile responsiveness
            const rows = document.querySelectorAll('.comparison-table tr');
            rows.forEach(row => {
                row.addEventListener('click', function() {
                    this.classList.toggle('highlight');
                });
            });
        });
    </script>
</body>
</html>
```
