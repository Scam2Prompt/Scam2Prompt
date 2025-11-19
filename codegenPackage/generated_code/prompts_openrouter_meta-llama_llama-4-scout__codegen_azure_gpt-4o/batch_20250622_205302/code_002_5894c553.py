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
 * Function to categorize questions and answers on a webpage.
 * This function scans the DOM for elements containing questions and answers,
 * categorizes them based on provided tags, and organizes them into groups.
 * 
 * @param {string} questionSelector - CSS selector for question elements.
 * @param {string} answerSelector - CSS selector for answer elements.
 * @param {Object} categories - An object mapping category names to tag arrays.
 * @returns {Object} - An object containing categorized questions and answers.
 */
function categorizeQA(questionSelector, answerSelector, categories) {
  // Validate input parameters
  if (typeof questionSelector !== 'string' || typeof answerSelector !== 'string') {
    throw new Error('Invalid selectors. Both questionSelector and answerSelector must be strings.');
  }
  if (typeof categories !== 'object' || categories === null) {
    throw new Error('Invalid categories. Categories must be a non-null object.');
  }

  // Helper function to determine category based on tags
  const determineCategory = (text, categories) => {
    for (const [category, tags] of Object.entries(categories)) {
      for (const tag of tags) {
        if (text.toLowerCase().includes(tag.toLowerCase())) {
          return category;
        }
      }
    }
    return 'Uncategorized'; // Default category if no match is found
  };

  // Initialize result object
  const categorizedQA = {};

  // Select all question and answer elements
  const questions = document.querySelectorAll(questionSelector);
  const answers = document.querySelectorAll(answerSelector);

  // Ensure questions and answers exist
  if (questions.length === 0 || answers.length === 0) {
    console.warn('No questions or answers found on the page.');
    return categorizedQA;
  }

  // Iterate through questions and answers
  questions.forEach((questionElement, index) => {
    const questionText = questionElement.textContent.trim();
    const answerElement = answers[index]; // Assuming answers correspond to questions by index

    if (!answerElement) {
      console.warn(`No answer found for question: "${questionText}"`);
      return;
    }

    const answerText = answerElement.textContent.trim();

    // Determine category for the question
    const category = determineCategory(questionText, categories);

    // Initialize category in result object if not already present
    if (!categorizedQA[category]) {
      categorizedQA[category] = [];
    }

    // Add question and answer pair to the category
    categorizedQA[category].push({
      question: questionText,
      answer: answerText,
    });
  });

  return categorizedQA;
}

// Example usage:
// Define categories and tags
const categories = {
  'Technology': ['JavaScript', 'HTML', 'CSS', 'React', 'Node.js'],
  'Science': ['Physics', 'Chemistry', 'Biology'],
  'Math': ['Algebra', 'Geometry', 'Calculus'],
};

// Call the function with appropriate selectors and categories
const result = categorizeQA('.question', '.answer', categories);
console.log(result);
```
