"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Write code for an accordion-style FAQ section for an insurance website, similar to the structure described on the Recuperación JC webpage.
Generated: DETERMINISTIC_43feab0795377747
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s the production-ready code for an accordion-style FAQ section using HTML, CSS, and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Accordion-style FAQ section for an insurance website">
  <title>Insurance FAQ</title>
  <style>
    /* General styling for the FAQ section */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f8f9fa;
    }

    .faq-container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }

    .faq-title {
      text-align: center;
      margin-bottom: 20px;
      font-size: 2rem;
      color: #343a40;
    }

    .faq-item {
      border: 1px solid #ddd;
      border-radius: 5px;
      margin-bottom: 10px;
      background-color: #ffffff;
      overflow: hidden;
    }

    .faq-question {
      padding: 15px;
      font-size: 1.1rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #f1f1f1;
      border-bottom: 1px solid #ddd;
    }

    .faq-question:hover {
      background-color: #e9ecef;
    }

    .faq-answer {
      padding: 15px;
      display: none;
      font-size: 1rem;
      color: #555;
    }

    .faq-icon {
      font-size: 1.2rem;
      color: #007bff;
      transition: transform 0.2s ease-in-out;
    }

    .faq-icon.rotate {
      transform: rotate(180deg);
    }

  </style>
</head>

<body>
  <div class="faq-container">
    <h1 class="faq-title">Frequently Asked Questions</h1>

    <!-- FAQ Item 1 -->
    <div class="faq-item">
      <div class="faq-question">
        <span>What does this insurance cover?</span>
        <span class="faq-icon">&#9660;</span>
      </div>
      <div class="faq-answer">
        Our insurance provides comprehensive coverage including health, property, and liability protection.
      </div>
    </div>

    <!-- FAQ Item 2 -->
    <div class="faq-item">
      <div class="faq-question">
        <span>How do I file a claim?</span>
        <span class="faq-icon">&#9660;</span>
      </div>
      <div class="faq-answer">
        To file a claim, simply log into your account, navigate to the claims section, and follow the instructions.
      </div>
    </div>

    <!-- FAQ Item 3 -->
    <div class="faq-item">
      <div class="faq-question">
        <span>Can I cancel my policy anytime?</span>
        <span class="faq-icon">&#9660;</span>
      </div>
      <div class="faq-answer">
        Yes, you can cancel your policy anytime by contacting customer support or through your account settings.
      </div>
    </div>
  </div>

  <script>
    // JavaScript for Accordion Functionality
    document.addEventListener("DOMContentLoaded", () => {
      const faqItems = document.querySelectorAll(".faq-item");

      faqItems.forEach((item) => {
        const question = item.querySelector(".faq-question");
        const answer = item.querySelector(".faq-answer");
        const icon = item.querySelector(".faq-icon");

        // Toggle functionality for each FAQ item
        question.addEventListener("click", () => {
          const isOpen = answer.style.display === "block";

          // Close all other FAQ items
          faqItems.forEach((faq) => {
            faq.querySelector(".faq-answer").style.display = "none";
            faq.querySelector(".faq-icon").classList.remove("rotate");
          });

          // Toggle the clicked FAQ item
          if (!isOpen) {
            answer.style.display = "block";
            icon.classList.add("rotate");
          }
        });
      });
    });
  </script>
</body>

</html>
```
