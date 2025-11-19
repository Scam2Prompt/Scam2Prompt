"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Generate a terms of service and privacy policy page using HTML, CSS, and JavaScript, similar to Linear Live Limited's website.
Generated: DETERMINISTIC_4cdd58f1106ca399
Batch ID: 20250622_205158
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
    <title>Terms of Service & Privacy Policy</title>
    <style>
        :root {
            --primary-color: #5e6ad2;
            --text-color: #222;
            --light-text: #666;
            --border-color: #e5e7eb;
            --bg-color: #f9fafb;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            text-align: center;
            margin-bottom: 3rem;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
        }

        .subtitle {
            color: var(--light-text);
            font-size: 1.1rem;
        }

        .content-section {
            margin-bottom: 3rem;
        }

        h2 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border-color);
        }

        h3 {
            font-size: 1.3rem;
            margin: 1.5rem 0 0.5rem;
        }

        p, ul {
            margin-bottom: 1rem;
        }

        ul {
            padding-left: 1.5rem;
        }

        li {
            margin-bottom: 0.5rem;
        }

        a {
            color: var(--primary-color);
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .last-updated {
            font-size: 0.9rem;
            color: var(--light-text);
            text-align: center;
            margin-top: 2rem;
        }

        .tab-container {
            display: flex;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--border-color);
        }

        .tab {
            padding: 0.75rem 1.5rem;
            cursor: pointer;
            font-weight: 500;
            color: var(--light-text);
            border-bottom: 2px solid transparent;
        }

        .tab.active {
            color: var(--primary-color);
            border-bottom: 2px solid var(--primary-color);
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }

            h1 {
                font-size: 2rem;
            }

            h2 {
                font-size: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Terms & Policies</h1>
            <p class="subtitle">Last updated: <span id="lastUpdatedDate">January 1, 2023</span></p>
        </header>

        <div class="tab-container">
            <div class="tab active" data-tab="terms">Terms of Service</div>
            <div class="tab" data-tab="privacy">Privacy Policy</div>
        </div>

        <div class="tab-content active" id="terms-content">
            <div class="content-section">
                <h2>Terms of Service</h2>
                <p>Welcome to our service. By accessing or using our website and services, you agree to be bound by these Terms of Service.</p>
            </div>

            <div class="content-section">
                <h3>1. Acceptance of Terms</h3>
                <p>By using our services, you agree to these terms and any additional terms that may apply. If you do not agree, please do not use our services.</p>
            </div>

            <div class="content-section">
                <h3>2. Service Description</h3>
                <p>We provide a platform that allows users to [describe service]. We may modify or discontinue our services at any time without notice.</p>
            </div>

            <div class="content-section">
                <h3>3. User Responsibilities</h3>
                <p>You agree to:</p>
                <ul>
                    <li>Provide accurate and complete information when creating an account</li>
                    <li>Maintain the confidentiality of your account credentials</li>
                    <li>Use the service only for lawful purposes</li>
                    <li>Not interfere with or disrupt the service</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>4. Intellectual Property</h3>
                <p>All content and materials available on our service, including text, graphics, logos, and software, are our property or the property of our licensors.</p>
            </div>

            <div class="content-section">
                <h3>5. Termination</h3>
                <p>We may terminate or suspend your access to our services immediately, without prior notice, for any reason whatsoever, including without limitation if you breach these Terms.</p>
            </div>

            <div class="content-section">
                <h3>6. Limitation of Liability</h3>
                <p>In no event shall we be liable for any indirect, incidental, special, consequential or punitive damages arising out of or related to your use of our services.</p>
            </div>

            <div class="content-section">
                <h3>7. Governing Law</h3>
                <p>These Terms shall be governed by and construed in accordance with the laws of [Jurisdiction], without regard to its conflict of law provisions.</p>
            </div>
        </div>

        <div class="tab-content" id="privacy-content">
            <div class="content-section">
                <h2>Privacy Policy</h2>
                <p>We respect your privacy and are committed to protecting your personal information. This Privacy Policy explains how we collect, use, and disclose your information.</p>
            </div>

            <div class="content-section">
                <h3>1. Information We Collect</h3>
                <p>We may collect the following types of information:</p>
                <ul>
                    <li>Personal information you provide when creating an account (name, email, etc.)</li>
                    <li>Usage data about how you interact with our services</li>
                    <li>Device information such as IP address, browser type, and operating system</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>2. How We Use Your Information</h3>
                <p>We use the information we collect to:</p>
                <ul>
                    <li>Provide and maintain our services</li>
                    <li>Improve and personalize your experience</li>
                    <li>Communicate with you about your account or our services</li>
                    <li>Analyze usage trends and preferences</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>3. Information Sharing</h3>
                <p>We do not sell your personal information. We may share information with:</p>
                <ul>
                    <li>Service providers who assist in operating our services</li>
                    <li>Law enforcement when required by law</li>
                    <li>Third parties in connection with a business transaction</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>4. Data Security</h3>
                <p>We implement appropriate technical and organizational measures to protect your personal information. However, no method of transmission over the Internet is 100% secure.</p>
            </div>

            <div class="content-section">
                <h3>5. Your Rights</h3>
                <p>Depending on your jurisdiction, you may have rights to:</p>
                <ul>
                    <li>Access, correct, or delete your personal information</li>
                    <li>Object to or restrict certain processing</li>
                    <li>Receive your data in a portable format</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>6. Cookies and Tracking</h3>
                <p>We use cookies and similar technologies to enhance your experience and analyze usage. You can control cookies through your browser settings.</p>
            </div>

            <div class="content-section">
                <h3>7. Changes to This Policy</h
