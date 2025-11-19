"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Create a terms and conditions page for a cryptocurrency platform, including sections on eligible countries, campaign rules, and user responsibilities.
Generated: DETERMINISTIC_efc9b8cfdbeaf9af
Batch ID: 20250622_212746
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
    <title>Crypto Platform - Terms and Conditions</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        h2 {
            color: #3498db;
            margin-top: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        h3 {
            color: #2980b9;
            margin-top: 20px;
        }
        .section {
            background-color: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .last-updated {
            text-align: right;
            font-style: italic;
            color: #7f8c8d;
            margin-bottom: 20px;
        }
        .accept-btn {
            display: block;
            width: 200px;
            margin: 30px auto;
            padding: 10px;
            background-color: #2ecc71;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
        }
        .accept-btn:hover {
            background-color: #27ae60;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Terms and Conditions</h1>
    <div class="last-updated">Last Updated: <span id="current-date"></span></div>

    <div class="section">
        <h2>1. Introduction</h2>
        <p>Welcome to our cryptocurrency platform. These Terms and Conditions govern your use of our platform and services. By accessing or using our platform, you agree to be bound by these terms.</p>
    </div>

    <div class="section">
        <h2>2. Eligible Countries</h2>
        <p>Our services are available to users in the following countries:</p>
        <ul>
            <li>United States (excluding residents of New York and Texas)</li>
            <li>United Kingdom</li>
            <li>Canada (excluding Quebec)</li>
            <li>Australia</li>
            <li>European Union member states</li>
            <li>Singapore</li>
            <li>Japan</li>
        </ul>
        <p>Residents of countries not listed above are prohibited from using our platform. We reserve the right to modify this list at any time without prior notice.</p>
    </div>

    <div class="section">
        <h2>3. Campaign Rules</h2>
        <h3>3.1 General Rules</h3>
        <ul>
            <li>All participants must be at least 18 years old</li>
            <li>Only one account per individual is permitted</li>
            <li>Campaign rewards are non-transferable</li>
            <li>Platform reserves the right to disqualify any participant for suspicious activity</li>
        </ul>

        <h3>3.2 Referral Program</h3>
        <ul>
            <li>Referrals must be new, verified users</li>
            <li>Both referrer and referee must complete KYC verification</li>
            <li>Referral bonuses will be credited after referee completes first trade</li>
            <li>Referral bonuses may be subject to holding periods</li>
        </ul>

        <h3>3.3 Trading Competitions</h3>
        <ul>
            <li>Minimum trading volume requirements apply</li>
            <li>Wash trading will result in disqualification</li>
            <li>Prizes will be distributed within 14 business days after competition ends</li>
            <li>Platform may require winners to provide additional verification</li>
        </ul>
    </div>

    <div class="section">
        <h2>4. User Responsibilities</h2>
        <h3>4.1 Account Security</h3>
        <ul>
            <li>You are responsible for maintaining the confidentiality of your login credentials</li>
            <li>You must enable two-factor authentication where available</li>
            <li>You must immediately report any unauthorized access to your account</li>
        </ul>

        <h3>4.2 Compliance</h3>
        <ul>
            <li>You must comply with all applicable laws and regulations</li>
            <li>You must not use the platform for illegal activities</li>
            <li>You are responsible for any tax obligations related to your activities</li>
        </ul>

        <h3>4.3 Risk Acknowledgement</h3>
        <ul>
            <li>You acknowledge the volatile nature of cryptocurrency markets</li>
            <li>You understand that past performance is not indicative of future results</li>
            <li>You accept full responsibility for your trading decisions</li>
        </ul>
    </div>

    <div class="section">
        <h2>5. Platform Rights</h2>
        <ul>
            <li>We reserve the right to modify or terminate services at any time</li>
            <li>We may freeze accounts suspected of fraudulent activity</li>
            <li>We may update these terms with 30 days notice</li>
            <li>We are not responsible for losses due to market volatility</li>
        </ul>
    </div>

    <div class="section">
        <h2>6. Limitation of Liability</h2>
        <p>To the maximum extent permitted by law, our platform shall not be liable for any indirect, incidental, special, consequential or punitive damages, or any loss of profits or revenues, whether incurred directly or indirectly, or any loss of data, use, goodwill, or other intangible losses, resulting from:</p>
        <ul>
            <li>Your use or inability to use the service</li>
            <li>Any unauthorized access to or use of our servers and/or any personal information stored therein</li>
            <li>Any interruption or cessation of transmission to or from our service</li>
            <li>Any bugs, viruses, or the like that may be transmitted to or through our service</li>
        </ul>
    </div>

    <button class="accept-btn" id="accept-btn">I Accept</button>

    <script>
        // Set current date
        document.getElementById('current-date').textContent = new Date().toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });

        // Handle accept button click
        document.getElementById('accept-btn').addEventListener('click', function() {
            alert('Thank you for accepting our Terms and Conditions.');
            // In a real application, you would typically redirect or set a cookie/localStorage flag
            // window.location.href = '/dashboard';
        });
    </script>
</body>
</html>
```
