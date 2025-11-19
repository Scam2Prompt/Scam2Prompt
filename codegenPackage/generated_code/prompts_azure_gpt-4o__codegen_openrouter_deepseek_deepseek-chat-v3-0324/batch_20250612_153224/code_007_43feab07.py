"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: Write code for an accordion-style FAQ section for an insurance website, similar to the structure described on the Recuperación JC webpage.
Generated: DETERMINISTIC_43feab0795377747
Batch ID: 20250612_153224
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
    <title>Insurance FAQ</title>
    <style>
        /* Reset and base styles */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .faq-container {
            max-width: 800px;
            margin: 0 auto;
        }

        .faq-title {
            text-align: center;
            margin-bottom: 30px;
            color: #2c3e50;
            font-size: 2.5rem;
        }

        .faq-item {
            background-color: #fff;
            border-radius: 8px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        .faq-question {
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            font-weight: bold;
            font-size: 1.1rem;
            color: #2c3e50;
            background-color: #f8f9fa;
            transition: background-color 0.3s ease;
        }

        .faq-question:hover {
            background-color: #e9ecef;
        }

        .faq-question::after {
            content: '+';
            font-size: 1.5rem;
            transition: transform 0.3s ease;
        }

        .faq-item.active .faq-question::after {
            transform: rotate(45deg);
        }

        .faq-answer {
            padding: 0;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease, padding 0.3s ease;
        }

        .faq-item.active .faq-answer {
            padding: 20px;
            max-height: 1000px;
        }

        @media (max-width: 768px) {
            .faq-title {
                font-size: 2rem;
            }
            
            .faq-question {
                padding: 15px;
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="faq-container">
        <h1 class="faq-title">Frequently Asked Questions</h1>
        
        <div class="faq-item">
            <div class="faq-question">What types of insurance do you offer?</div>
            <div class="faq-answer">
                <p>We offer a wide range of insurance products including auto, home, life, health, and business insurance. Our policies are designed to meet various needs and budgets.</p>
            </div>
        </div>
        
        <div class="faq-item">
            <div class="faq-question">How do I file a claim?</div>
            <div class="faq-answer">
                <p>You can file a claim by calling our 24/7 claims hotline at 1-800-INSURANCE, through our mobile app, or by logging into your account on our website. Our claims representatives will guide you through the process.</p>
            </div>
        </div>
        
        <div class="faq-item">
            <div class="faq-question">What factors affect my insurance premium?</div>
            <div class="faq-answer">
                <p>Several factors can affect your premium including your age, location, claims history, coverage limits, deductible amount, and in some cases, your credit score. Each type of insurance has its own rating factors.</p>
            </div>
        </div>
        
        <div class="faq-item">
            <div class="faq-question">Can I bundle multiple insurance policies?</div>
            <div class="faq-answer">
                <p>Yes! We offer discounts when you bundle multiple policies like auto and home insurance. Bundling can save you up to 25% on your premiums while simplifying your insurance management.</p>
            </div>
        </div>
        
        <div class="faq-item">
            <div class="faq-question">How can I lower my insurance costs?</div>
            <div class="faq-answer">
                <p>There are several ways to lower your insurance costs: increase your deductible, take advantage of discounts (like safe driver or multi-policy), maintain a good credit score, and regularly review your coverage with your agent.</p>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const faqItems = document.querySelectorAll('.faq-item');
            
            faqItems.forEach(item => {
                const question = item.querySelector('.faq-question');
                
                question.addEventListener('click', () => {
                    // Close all other items
                    faqItems.forEach(otherItem => {
                        if (otherItem !== item && otherItem.classList.contains('active')) {
                            otherItem.classList.remove('active');
                        }
                    });
                    
                    // Toggle current item
                    item.classList.toggle('active');
                });
            });

            // Error handling for potential null elements
            try {
                if (faqItems.length === 0) {
                    console.warn('No FAQ items found on the page');
                }
            } catch (error) {
                console.error('Error initializing FAQ:', error);
            }
        });
    </script>
</body>
</html>
```
