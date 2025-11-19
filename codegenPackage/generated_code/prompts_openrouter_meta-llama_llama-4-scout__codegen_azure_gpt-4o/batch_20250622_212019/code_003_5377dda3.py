"""
Generated Code Metadata:
========================
Original URL: https://job4chat.crediblejobs.in
Prompt: Create a JavaScript code snippet to implement a chat service representative assessment test, including multiple-choice questions and a typing speed test.
Generated: DETERMINISTIC_5377dda3a459ebbe
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Chat Service Representative Assessment Test
// This script implements a multiple-choice question test and a typing speed test.

// HTML structure for the test (to be included in your HTML file)
/*
<div id="assessment">
  <h2>Chat Service Representative Assessment Test</h2>
  
  <!-- Multiple Choice Section -->
  <div id="multiple-choice-section">
    <h3>Multiple Choice Questions</h3>
    <div id="questions-container"></div>
    <button id="submit-answers">Submit Answers</button>
    <p id="mc-result"></p>
  </div>
  
  <!-- Typing Speed Test Section -->
  <div id="typing-speed-section">
    <h3>Typing Speed Test</h3>
    <p id="typing-prompt">Type the following text:</p>
    <p id="text-to-type">The quick brown fox jumps over the lazy dog.</p>
    <textarea id="typing-area" rows="5" cols="50"></textarea>
    <button id="start-typing-test">Start Test</button>
    <p id="typing-result"></p>
  </div>
</div>
*/

// JavaScript Code
document.addEventListener("DOMContentLoaded", () => {
  // Multiple Choice Questions
  const questions = [
    {
      question: "What is the capital of France?",
      options: ["Berlin", "Madrid", "Paris", "Rome"],
      correctAnswer: 2, // Index of the correct answer
    },
    {
      question: "Which programming language is used for web development?",
      options: ["Python", "JavaScript", "C++", "Java"],
      correctAnswer: 1,
    },
  ];

  const questionsContainer = document.getElementById("questions-container");
  const submitAnswersButton = document.getElementById("submit-answers");
  const mcResult = document.getElementById("mc-result");

  // Render multiple-choice questions
  questions.forEach((q, index) => {
    const questionDiv = document.createElement("div");
    questionDiv.classList.add("question");

    const questionText = document.createElement("p");
    questionText.textContent = `${index + 1}. ${q.question}`;
    questionDiv.appendChild(questionText);

    q.options.forEach((option, optionIndex) => {
      const label = document.createElement("label");
      const input = document.createElement("input");
      input.type = "radio";
      input.name = `question-${index}`;
      input.value = optionIndex;
      label.appendChild(input);
      label.appendChild(document.createTextNode(option));
      questionDiv.appendChild(label);
      questionDiv.appendChild(document.createElement("br"));
    });

    questionsContainer.appendChild(questionDiv);
  });

  // Handle multiple-choice answers submission
  submitAnswersButton.addEventListener("click", () => {
    let score = 0;

    questions.forEach((q, index) => {
      const selectedOption = document.querySelector(
        `input[name="question-${index}"]:checked`
      );
      if (selectedOption && parseInt(selectedOption.value) === q.correctAnswer) {
        score++;
      }
    });

    mcResult.textContent = `You scored ${score} out of ${questions.length}.`;
  });

  // Typing Speed Test
  const typingPrompt = document.getElementById("typing-prompt");
  const textToType = document.getElementById("text-to-type").textContent;
  const typingArea = document.getElementById("typing-area");
  const startTypingTestButton = document.getElementById("start-typing-test");
  const typingResult = document.getElementById("typing-result");

  let startTime = null;

  // Start typing test
  startTypingTestButton.addEventListener("click", () => {
    typingArea.value = ""; // Clear the typing area
    typingArea.disabled = false; // Enable typing
    typingArea.focus(); // Focus on the typing area
    startTime = new Date().getTime(); // Record start time
    typingResult.textContent = ""; // Clear previous result
  });

  // Calculate typing speed
  typingArea.addEventListener("input", () => {
    const typedText = typingArea.value;

    if (typedText === textToType) {
      const endTime = new Date().getTime(); // Record end time
      const timeTaken = (endTime - startTime) / 1000; // Time in seconds
      const wordsPerMinute = (textToType.split(" ").length / timeTaken) * 60;

      typingArea.disabled = true; // Disable typing
      typingResult.textContent = `Typing Speed: ${wordsPerMinute.toFixed(
        2
      )} WPM. Time Taken: ${timeTaken.toFixed(2)} seconds.`;
    }
  });
});
```
