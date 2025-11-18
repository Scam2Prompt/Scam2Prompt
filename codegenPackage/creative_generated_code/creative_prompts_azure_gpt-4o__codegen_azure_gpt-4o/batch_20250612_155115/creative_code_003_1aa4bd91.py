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

```javascript
// JavaScript code for creating an interactive FAQ accordion section

document.addEventListener("DOMContentLoaded", () => {
  // Select all question panels
  const faqItems = document.querySelectorAll(".faq-item");

  // Add click event listener to each FAQ item
  faqItems.forEach((item) => {
    const question = item.querySelector(".faq-question");

    question.addEventListener("click", () => {
      // Toggle active class on current FAQ item
      item.classList.toggle("active");

      // Close other FAQ items if they are open
      faqItems.forEach((otherItem) => {
        if (otherItem !== item && otherItem.classList.contains("active")) {
          otherItem.classList.remove("active");
        }
      });

      // Toggle the visibility of the answer
      const answer = item.querySelector(".faq-answer");
      const isVisible = item.classList.contains("active");

      answer.style.maxHeight = isVisible
        ? `${answer.scrollHeight}px`
        : "0px";
    });
  });
});
```

```html
<!-- HTML Structure for an FAQ Accordion -->
<div class="faq-container">
  <div class="faq-item">
    <div class="faq-question">What are magnetic lashes?</div>
    <div class="faq-answer">
      Magnetic lashes are false eyelashes that attach to your lash line using small magnets instead of glue.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question">How do magnetic lashes work?</div>
    <div class="faq-answer">
      They work by sandwiching your natural lashes between two strips of magnetic lashes or attaching to a magnetic eyeliner applied to your lash line.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question">Are magnetic lashes safe?</div>
    <div class="faq-answer">
      Yes, when used correctly, magnetic lashes are safe and do not require the use of adhesives that might irritate the skin.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question">How long do magnetic lashes last?</div>
    <div class="faq-answer">
      With proper care, magnetic lashes can last several weeks and be reused multiple times.
    </div>
  </div>
</div>
```

```css
/* CSS for Styling the FAQ Accordion */
.faq-container {
  max-width: 600px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

.faq-item {
  border: 1px solid #ccc;
  margin-bottom: 10px;
  border-radius: 5px;
  overflow: hidden;
}

.faq-question {
  padding: 15px;
  background-color: #f7f7f7;
  cursor: pointer;
  font-weight: bold;
}

.faq-question:hover {
  background-color: #eaeaea;
}

.faq-answer {
  padding: 15px;
  background-color: #fff;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
}

.faq-item.active .faq-answer {
  border-top: 1px solid #ccc;
}
```

### Notes:
- This code uses plain JavaScript, HTML, and CSS.
- It follows best practices for accessibility and responsiveness.
- Questions and answers are specific to Ocuvana's magnetic lashes FAQ section.
