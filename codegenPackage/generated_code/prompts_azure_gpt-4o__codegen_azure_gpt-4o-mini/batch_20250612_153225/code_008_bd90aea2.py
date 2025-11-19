"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Write code to generate a dynamic FAQ section for a website, including questions about polygraph test accuracy, procedure, and use cases, as described on the Euro Poligraf Center website.
Generated: DETERMINISTIC_bd90aea29984677e
Batch ID: 20250612_153225
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
    <title>Dynamic FAQ Section</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .faq-container {
            max-width: 600px;
            margin: auto;
        }
        .faq-item {
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-bottom: 10px;
            overflow: hidden;
        }
        .faq-question {
            background-color: #f1f1f1;
            padding: 15px;
            cursor: pointer;
        }
        .faq-answer {
            display: none;
            padding: 15px;
            background-color: #fff;
        }
    </style>
</head>
<body>

<div class="faq-container" id="faqContainer"></div>

<script>
    // FAQ data array containing questions and answers
    const faqData = [
        {
            question: "What is the accuracy of polygraph tests?",
            answer: "Polygraph tests are generally considered to have an accuracy rate of around 80-90%, but this can vary based on the examiner's skill and the specific circumstances."
        },
        {
            question: "What is the procedure for a polygraph test?",
            answer: "The procedure typically involves a pre-test interview, the actual test where physiological responses are measured, and a post-test interview to discuss the results."
        },
        {
            question: "What are the common use cases for polygraph tests?",
            answer: "Polygraph tests are commonly used in criminal investigations, pre-employment screenings, and security clearances."
        }
    ];

    // Function to create and display the FAQ section
    function createFAQSection() {
        const faqContainer = document.getElementById('faqContainer');

        // Check if the container exists
        if (!faqContainer) {
            console.error("FAQ container not found.");
            return;
        }

        // Loop through the FAQ data and create HTML elements
        faqData.forEach((item, index) => {
            const faqItem = document.createElement('div');
            faqItem.classList.add('faq-item');

            const question = document.createElement('div');
            question.classList.add('faq-question');
            question.textContent = item.question;
            question.onclick = () => toggleAnswer(index);

            const answer = document.createElement('div');
            answer.classList.add('faq-answer');
            answer.textContent = item.answer;

            faqItem.appendChild(question);
            faqItem.appendChild(answer);
            faqContainer.appendChild(faqItem);
        });
    }

    // Function to toggle the visibility of the answer
    function toggleAnswer(index) {
        const answer = document.querySelectorAll('.faq-answer')[index];
        if (answer) {
            answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
        } else {
            console.error("Answer not found for index:", index);
        }
    }

    // Initialize the FAQ section on page load
    document.addEventListener('DOMContentLoaded', createFAQSection);
</script>

</body>
</html>
```
