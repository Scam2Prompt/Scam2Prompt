"""
Generated Code Metadata:
========================
Original URL: https://betty-moore-873.pages.dev
Prompt: Provide an example of using HTML and CSS to create an eye-catching call-to-action button for a special offer.
Generated: DETERMINISTIC_0718527be70a6141
Batch ID: 20250612_155140
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
    <title>Special Offer CTA</title>
    <style>
        /* Base button styling */
        .cta-button {
            display: inline-block;
            padding: 15px 30px;
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            color: #ffffff;
            background: linear-gradient(135deg, #ff8a00, #e52e71);
            border-radius: 50px;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        /* Hover effect */
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
            background: linear-gradient(135deg, #e52e71, #ff8a00);
        }

        /* Active/click effect */
        .cta-button:active {
            transform: translateY(1px);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }

        /* Pulse animation */
        @keyframes pulse {
            0% {
                box-shadow: 0 0 0 0 rgba(229, 46, 113, 0.7);
            }
            70% {
                box-shadow: 0 0 0 15px rgba(229, 46, 113, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(229, 46, 113, 0);
            }
        }

        /* Adding pulse animation to button */
        .cta-button.pulse {
            animation: pulse 2s infinite;
        }

        /* Special offer badge */
        .offer-badge {
            position: absolute;
            top: -10px;
            right: -10px;
            background-color: #ffcc00;
            color: #333;
            font-size: 12px;
            font-weight: bold;
            padding: 3px 8px;
            border-radius: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <div style="text-align: center; margin-top: 50px;">
        <button class="cta-button pulse">
            Limited Time Offer!
            <span class="offer-badge">50% OFF</span>
        </button>
    </div>
</body>
</html>
```
