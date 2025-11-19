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
// Interactive Quiz for 상일미디어고 students - Environmental Science

// Quiz data structure
const quizData = [
    {
        question: "What is the primary greenhouse gas emitted by human activities?",
        options: ["Carbon Dioxide", "Methane", "Nitrous Oxide", "Ozone"],
        answer: "Carbon Dioxide"
    },
    {
        question: "Which of the following is a renewable energy source?",
        options: ["Coal", "Natural Gas", "Solar", "Nuclear"],
        answer: "Solar"
    },
    {
        question: "What is the main cause of ocean acidification?",
        options: ["Plastic Pollution", "Carbon Dioxide Absorption", "Oil Spills", "Overfishing"],
        answer: "Carbon Dioxide Absorption"
    },
    {
        question: "Which gas is primarily responsible for the depletion of the ozone layer?",
        options: ["Carbon Dioxide", "Chlorofluorocarbons (CFCs)", "Methane", "Nitrous Oxide"],
        answer: "Chlorofluorocarbons (CFCs)"
    },
    {
        question: "What is the term for the variety of life in the world or in a particular habitat?",
        options: ["Biodiversity", "Ecosystem", "Habitat", "Population"],
        answer: "Biodiversity"
    }
];

// Function to start the quiz
function startQuiz() {
    let score = 0; // Initialize score
    const totalQuestions = quizData.length; // Total number of questions

    // Loop through each question
    quizData.forEach((item, index) => {
        // Prompt user with the question and options
        const userAnswer = prompt(`${index + 1}. ${item.question}\nOptions:\n${item.options.join('\n')}`);
        
        // Validate user input
        if (userAnswer === null) {
            alert("Quiz cancelled.");
            return; // Exit if user cancels
        }

        // Check if the answer is correct
        if (userAnswer.trim() === item.answer) {
            score++; // Increment score for correct answer
        }
    });

    // Display final score
    alert(`Quiz completed! Your score: ${score} out of ${totalQuestions}`);
}

// Error handling for starting the quiz
try {
    startQuiz();
} catch (error) {
    console.error("An error occurred while starting the quiz:", error);
    alert("An unexpected error occurred. Please try again later.");
}
```
