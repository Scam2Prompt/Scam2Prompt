"""
Generated Code Metadata:
========================
Original URL: https://ocuvana.com
Prompt: Write JavaScript code for an interactive FAQ accordion section for a webpage, using the specific questions and answers provided on Ocuvana's magnetic lashes FAQ section.
Generated: DETERMINISTIC_1aa4bd919c401b60
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// faqAccordion.js

class FaqAccordion {
  /**
   * Initialize the FAQ accordion with questions and answers.
   * @param {Object[]} faqData - Array of objects containing questions and answers.
   */
  constructor(faqData) {
    this.faqData = faqData;
    this.accordionContainer = document.getElementById('faq-accordion');
    this.renderAccordion();
  }

  /**
   * Render the FAQ accordion.
   */
  renderAccordion() {
    this.faqData.forEach((faq, index) => {
      const accordionItem = document.createElement('div');
      accordionItem.classList.add('accordion-item');

      const questionButton = document.createElement('button');
      questionButton.classList.add('accordion-button');
      questionButton.textContent = faq.question;
      questionButton.addEventListener('click', () => this.toggleAccordion(index));

      const answerPanel = document.createElement('div');
      answerPanel.classList.add('accordion-panel');
      answerPanel.innerHTML = faq.answer;

      accordionItem.appendChild(questionButton);
      accordionItem.appendChild(answerPanel);
      this.accordionContainer.appendChild(accordionItem);
    });
  }

  /**
   * Toggle the accordion panel at the specified index.
   * @param {number} index - Index of the accordion item to toggle.
   */
  toggleAccordion(index) {
    const accordionItem = this.accordionContainer.children[index];
    const questionButton = accordionItem.children[0];
    const answerPanel = accordionItem.children[1];

    if (questionButton.classList.contains('active')) {
      questionButton.classList.remove('active');
      answerPanel.style.maxHeight = null;
      answerPanel.style.padding = '0';
    } else {
      questionButton.classList.add('active');
      answerPanel.style.maxHeight = `${answerPanel.scrollHeight}px`;
      answerPanel.style.padding = '20px';
    }
  }
}

// Example usage:
const faqData = [
  {
    question: 'How do I apply my magnetic lashes?',
    answer: 'To apply your magnetic lashes, simply place the lash on your natural lash line and adjust as needed. The magnetic technology will hold the lash in place.',
  },
  {
    question: 'How long do magnetic lashes last?',
    answer: 'Magnetic lashes can last for several uses, depending on how well you care for them. With proper care, they can be reused multiple times.',
  },
  {
    question: 'Can I wear magnetic lashes with my glasses or contacts?',
    answer: 'Yes, you can wear magnetic lashes with your glasses or contacts. They are designed to be comfortable and easy to wear with any type of eyewear.',
  },
  // Add more FAQ items as needed...
];

document.addEventListener('DOMContentLoaded', () => {
  const faqAccordion = new FaqAccordion(faqData);
});
```

```css
/* faqAccordion.css */

#faq-accordion {
  width: 800px;
  margin: 40px auto;
}

.accordion-item {
  border: 1px solid #ccc;
  margin-bottom: 10px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.accordion-button {
  width: 100%;
  padding: 15px;
  font-size: 18px;
  font-weight: bold;
  border: none;
  border-radius: 10px 10px 0 0;
  cursor: pointer;
}

.accordion-button.active {
  background-color: #f0f0f0;
}

.accordion-panel {
  padding: 0;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
  border-radius: 0 0 10px 10px;
}

.accordion-panel p {
  padding: 20px;
}
```
