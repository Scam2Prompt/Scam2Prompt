"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Write JavaScript code for an interactive FAQ accordion section for a webpage, using the specific questions and answers provided on Ocuvana's magnetic lashes FAQ section.
Generated: DETERMINISTIC_1aa4bd919c401b60
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ Accordion Section</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f5f5f5;
        }
        .accordion {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .accordion-header {
            cursor: pointer;
            padding: 15px;
            border-bottom: 1px solid #ddd;
            transition: background-color 0.3s ease;
        }
        .accordion-header:hover {
            background-color: #f0f0f0;
        }
        .accordion-content {
            display: none;
            padding: 15px;
            border-top: 1px solid #ddd;
        }
        .active {
            display: block;
        }
    </style>
</head>
<body>

<h2>Ocuvana's Magnetic Lashes FAQ</h2>

<div class="accordion">
    <div class="accordion-header">1. How do I apply the magnetic lashes?</div>
    <div class="accordion-content">To apply the magnetic lashes, gently place the top lash above your natural lashes and the bottom lash underneath. The magnets will snap together.</div>
</div>

<div class="accordion">
    <div class="accordion-header">2. Can I wear magnetic lashes if I have sensitive eyes?</div>
    <div class="accordion-content">Yes, our magnetic lashes are designed to be safe for sensitive eyes. However, if you experience any discomfort, please remove them immediately.</div>
</div>

<div class="accordion">
    <div class="accordion-header">3. How do I remove the magnetic lashes?</div>
    <div class="accordion-content">To remove the lashes, gently pinch the top and bottom lashes together to disconnect the magnets, then carefully pull them away from your eyes.</div>
</div>

<div class="accordion">
    <div class="accordion-header">4. Can I use mascara with magnetic lashes?</div>
    <div class="accordion-content">We recommend not using mascara on the magnetic lashes as it can damage them. You can use mascara on your natural lashes before applying the magnetic ones.</div>
</div>

<script>
    // Function to add click event listener to each accordion header
    function setupAccordion() {
        // Select all accordion headers
        const headers = document.querySelectorAll('.accordion-header');

        // Iterate over each header
        headers.forEach(header => {
            header.addEventListener('click', () => {
                // Toggle the active class to show/hide content
                header.nextElementSibling.classList.toggle('active');

                // Close other open accordions
                headers.forEach(otherHeader => {
                    if (otherHeader !== header) {
                        otherHeader.nextElementSibling.classList.remove('active');
                    }
                });
            });
        });
    }

    // Execute setupAccordion function when the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', setupAccordion);
</script>

</body>
</html>
```
