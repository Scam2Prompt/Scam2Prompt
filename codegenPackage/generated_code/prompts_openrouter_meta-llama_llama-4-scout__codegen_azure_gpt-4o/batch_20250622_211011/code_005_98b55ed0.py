"""
Generated Code Metadata:
========================
Original URL: https://ssdsd.netlify.app
Prompt: Write a code snippet in JavaScript to create an interactive quiz for 상일미디어고 students, specifically for the 환경 (Environmental Science) subject.
Generated: DETERMINISTIC_98b55ed06d0eb81f
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Interactive Quiz for 상일미디어고 Students - 환경 (Environmental Science)

// HTML structure for the quiz (to be included in your HTML file)
/*
<div id="quiz-container">
  <h1>환경 Quiz</h1>
  <div id="question-container"></div>
  <div id="options-container"></div>
  <button id="next-button" disabled>Next</button>
  <p id="result"></p>
</div>
*/

// JavaScript code for the quiz
document.addEventListener("DOMContentLoaded", () => {
  // Quiz questions and answers
  const quizQuestions = [
    {
      question: "What is the primary cause of global warming?",
      options: ["Deforestation", "Greenhouse gases", "Overpopulation", "Nuclear energy"],
      correctAnswer: 1, // Index of the correct answer
    },
    {
      question: "Which of the following is a renewable energy source?",
      options: ["Coal", "Natural gas", "Solar energy", "Petroleum"],
      correctAnswer: 2,
    },
    {
      question: "What does 'reduce, reuse, recycle' aim to minimize?",
      options: ["Water usage", "Waste production", "Energy consumption", "Air pollution"],
      correctAnswer: 1,
    },
  ];

  let currentQuestionIndex = 0;
  let score = 0;

  const questionContainer = document.getElementById("question-container");
  const optionsContainer = document.getElementById("options-container");
  const nextButton = document.getElementById("next-button");
  const resultContainer = document.getElementById("result");

  // Function to load a question
  const loadQuestion = () => {
    const currentQuestion = quizQuestions[currentQuestionIndex];
    questionContainer.textContent = currentQuestion.question;

    // Clear previous options
    optionsContainer.innerHTML = "";

    // Render options
    currentQuestion.options.forEach((option, index) => {
      const optionButton = document.createElement("button");
      optionButton.textContent = option;
      optionButton.classList.add("option-button");
      optionButton.addEventListener("click", () => handleOptionClick(index));
      optionsContainer.appendChild(optionButton);
    });

    // Disable the next button until an option is selected
    nextButton.disabled = true;
  };

  // Function to handle option click
  const handleOptionClick = (selectedIndex) => {
    const currentQuestion = quizQuestions[currentQuestionIndex];

    // Highlight correct and incorrect answers
    const optionButtons = document.querySelectorAll(".option-button");
    optionButtons.forEach((button, index) => {
      if (index === currentQuestion.correctAnswer) {
        button.style.backgroundColor = "green"; // Correct answer
      } else if (index === selectedIndex) {
        button.style.backgroundColor = "red"; // Incorrect answer
      }
      button.disabled = true; // Disable all buttons after selection
    });

    // Update score if the answer is correct
    if (selectedIndex === currentQuestion.correctAnswer) {
      score++;
    }

    // Enable the next button
    nextButton.disabled = false;
  };

  // Function to handle the next button click
  const handleNextClick = () => {
    currentQuestionIndex++;

    if (currentQuestionIndex < quizQuestions.length) {
      loadQuestion();
    } else {
      // Quiz is finished
      questionContainer.textContent = "Quiz Completed!";
      optionsContainer.innerHTML = "";
      nextButton.style.display = "none"; // Hide the next button
      resultContainer.textContent = `Your score: ${score}/${quizQuestions.length}`;
    }
  };

  // Attach event listener to the next button
  nextButton.addEventListener("click", handleNextClick);

  // Load the first question
  loadQuestion();
});
```
