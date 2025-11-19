"""
Generated Code Metadata:
========================
Original URL: https://aswers.icu
Prompt: "Write a JavaScript function to categorize questions and answers on a webpage."
Generated: DETERMINISTIC_5894c553b14aa1f4
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Categorizes questions and answers on a webpage.
 * 
 * @param {Array} qaArray - An array of question-answer objects.
 * @param {string} category - The category to filter questions and answers.
 * @returns {Array} - An array of categorized question-answer objects.
 * @throws {Error} - Throws an error if the input is not an array or if the category is not a string.
 */
function categorizeQA(qaArray, category) {
    // Validate input types
    if (!Array.isArray(qaArray)) {
        throw new Error('The first argument must be an array.');
    }
    if (typeof category !== 'string') {
        throw new Error('The second argument must be a string.');
    }

    // Filter the questions and answers based on the provided category
    const categorizedQA = qaArray.filter(qa => {
        return qa.category && qa.category.toLowerCase() === category.toLowerCase();
    });

    return categorizedQA;
}

// Example usage
try {
    const qaData = [
        { question: "What is JavaScript?", answer: "A programming language.", category: "Programming" },
        { question: "What is HTML?", answer: "A markup language.", category: "Web Development" },
        { question: "What is CSS?", answer: "A style sheet language.", category: "Web Development" },
        { question: "What is Node.js?", answer: "A JavaScript runtime.", category: "Programming" }
    ];

    const programmingQuestions = categorizeQA(qaData, "Programming");
    console.log(programmingQuestions);
} catch (error) {
    console.error('Error categorizing questions and answers:', error.message);
}
```
