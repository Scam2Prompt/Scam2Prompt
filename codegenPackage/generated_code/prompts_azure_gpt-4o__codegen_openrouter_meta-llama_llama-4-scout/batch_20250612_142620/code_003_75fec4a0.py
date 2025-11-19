"""
Generated Code Metadata:
========================
Original URL: https://help-virgocx.teachable.com
Prompt: Create a privacy policy template for a Teachable-hosted course website that offers help and tutorials for Metamask users.
Generated: DETERMINISTIC_75fec4a08bc53e17
Batch ID: 20250612_142620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.contributor-covenant.org": {
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
<!-- privacy-policy.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - Metamask Tutorials</title>
</head>
<body>
    <h1>Privacy Policy</h1>

    <p>Effective Date: <span id="effective-date">September 1, 2024</span></p>

    <h2>Introduction</h2>

    <p>Welcome to our Metamask Tutorials website, hosted on Teachable. This Privacy Policy explains how we collect, use, and protect your personal data when you interact with our website and courses.</p>

    <h2>What Information Do We Collect?</h2>

    <p>We collect the following types of information from our users:</p>

    <ul>
        <li><strong>Personal Data:</strong> When you enroll in our courses, create an account, or contact us, we may collect:</li>
        <ul>
            <li>Your name and email address</li>
            <li>Your Metamask wallet address (if provided)</li>
            <li>Any additional information you choose to provide to us</li>
        </ul>
        <li><strong>Automated Data:</strong> We automatically collect:</li>
        <ul>
            <li>Your IP address and browser type</li>
            <li>Pages you visit on our website</li>
            <li>Time spent on our website</li>
        </ul>
    </ul>

    <h2>How Do We Use Your Information?</h2>

    <p>We use your information for the following purposes:</p>

    <ul>
        <li>To provide and improve our courses and services</li>
        <li>To communicate with you about our courses and services</li>
        <li>To fulfill your requests and provide support</li>
    </ul>

    <h2>Disclosure of Your Information</h2>

    <p>We may disclose your information in the following circumstances:</p>

    <ul>
        <li><strong>Teachable:</strong> We share your information with Teachable, our platform provider, to provide our courses and services.</li>
        <li><strong>Service Providers:</strong> We share your information with third-party service providers to help us operate our website and provide our services.</li>
        <li><strong>Law Enforcement:</strong> We may disclose your information in response to a valid legal request.</li>
    </ul>

    <h2>Your Rights and Choices</h2>

    <p>You have the following rights and choices:</p>

    <ul>
        <li><strong>Opt-out:</strong> You can opt-out of certain data collection and use.</li>
        <li><strong>Access:</strong> You can access your personal data.</li>
        <li><strong>Correction:</strong> You can correct your personal data.</li>
        <li><strong>Deletion:</strong> You can request deletion of your personal data.</li>
    </ul>

    <h2>Security</h2>

    <p>We take reasonable measures to protect your information, including:</p>

    <ul>
        <li>Encryption</li>
        <li>Secure servers</li>
    </ul>

    <h2>Changes to This Policy</h2>

    <p>We may update this policy. We will notify you of changes by updating this page.</p>

    <h2>Contact Us</h2>

    <p>If you have any questions or concerns, please contact us at <a href="mailto:support@metamasktutorials.com">support@metamasktutorials.com</a>.</p>

    <p><strong>Last Updated:</strong> <span id="last-updated">September 1, 2024</span></p>
</body>
</html>
```

```markdown
# CONTRIBUTING.md

## Code of Conduct

* We strive to create a welcoming and inclusive community.
* All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Contributing

* Fork the repository and submit a pull request.
* Ensure all tests pass and code is properly formatted.

## License

* This project is licensed under the MIT License.
```

```markdown
# CODE_OF_CONDUCT.md

## Our Pledge

We as members of the Metamask Tutorials community, contributors, and maintainers pledge to make participation in our community a harassment-free experience for everyone.

## Our Standards

* Use welcoming and inclusive language.
* Be respectful of differing viewpoints and experiences.
* Gracefully accept constructive criticism.

## Our Responsibilities

* Maintain confidentiality.
* Provide context for incidents.

## Scope

* This Code of Conduct applies within all community spaces.

## Reporting Guidelines

* Report incidents to support@metamasktutorials.com.

## Attribution

* This Code of Conduct is adapted from [Contributor Covenant](https://www.contributor-covenant.org).
```

```python
# generate_privacy_policy.py

from datetime import date

def generate_privacy_policy(effective_date, last_updated):
    policy = f"""<!-- privacy-policy.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - Metamask Tutorials</title>
</head>
<body>
    <h1>Privacy Policy</h1>

    <p>Effective Date: <span id="effective-date">{effective_date}</span></p>

    <!-- ... rest of policy ... -->

    <p><strong>Last Updated:</strong> <span id="last-updated">{last_updated}</span></p>
</body>
</html>
"""

    return policy

if __name__ == "__main__":
    today = date.today().strftime("%B %d, %Y")
    effective_date = "September 1, 2024"
    last_updated = today

    policy = generate_privacy_policy(effective_date, last_updated)

    with open("privacy-policy.html", "w") as f:
        f.write(policy)
```
