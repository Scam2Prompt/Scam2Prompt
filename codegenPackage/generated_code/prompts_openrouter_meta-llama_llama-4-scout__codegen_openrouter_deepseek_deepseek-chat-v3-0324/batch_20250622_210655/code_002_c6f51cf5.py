"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Generate a list of best practices for internet safety, as promoted by the "Internet sans crainte" initiative, and provide a code snippet in JavaScript to implement a simple online safety quiz.
Generated: DETERMINISTIC_c6f51cf5c752f2d4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Online Safety Quiz based on "Internet sans crainte" best practices
 * This quiz tests knowledge of internet safety best practices
 */

// Best practices from "Internet sans crainte" initiative
const bestPractices = [
    "Use strong, unique passwords for each account",
    "Enable two-factor authentication when available",
    "Keep software and operating systems updated",
    "Be cautious with personal information shared online",
    "Verify the credibility of sources before sharing information",
    "Use privacy settings on social networks",
    "Avoid clicking on suspicious links or attachments",
    "Use secure websites (HTTPS) for sensitive transactions",
    "Be respectful of others online (netiquette)",
    "Talk to trusted adults about online concerns"
];

// Quiz questions and answers
const quizQuestions = [
    {
        question: "What is the recommended approach for passwords?",
        options: [
            "Use the same password everywhere",
            "Use strong, unique passwords for each account",
            "Write passwords on sticky notes",
            "Share passwords with friends"
        ],
        correctAnswer: 1
    },
    {
        question: "What should you do when you receive a suspicious link?",
        options: [
            "Click it immediately",
            "Forward it to all your contacts",
            "Avoid clicking on it",
            "Post it on social media"
        ],
        correctAnswer: 2
    },
    {
        question: "How can you verify information found online?",
        options: [
            "Believe everything you read",
            "Check multiple credible sources",
            "Only trust social media posts",
            "Assume all websites are truthful"
        ],
        correctAnswer: 1
    },
    {
        question: "What should you do with your personal information online?",
        options: [
            "Share it publicly",
            "Post it on forums",
            "Be cautious about sharing it",
            "Include it in all your messages"
        ],
        correctAnswer: 2
    },
    {
        question: "What is good practice for social media?",
        options: [
            "Accept all friend requests",
            "Use privacy settings",
            "Post your location in real-time",
            "Share your login credentials"
        ],
        correctAnswer: 1
    }
];

class OnlineSafetyQuiz {
    constructor(questions) {
        this.questions = questions;
        this.currentQuestionIndex = 0;
        this.score = 0;
    }

    getCurrentQuestion() {
        return this.questions[this.currentQuestionIndex];
    }

    answerQuestion(answerIndex) {
        if (answerIndex === this.getCurrentQuestion().correctAnswer) {
            this.score++;
        }
        this.currentQuestionIndex++;
    }

    hasEnded() {
        return this.currentQuestionIndex >= this.questions.length;
    }

    getResults() {
        const percentage = Math.round((this.score / this.questions.length) * 100);
        let message = '';
        
        if (percentage >= 80) {
            message = 'Excellent! You know your internet safety best practices.';
        } else if (percentage >= 50) {
            message = 'Good, but there is room for improvement. Review the best practices.';
        } else {
            message = 'Please review internet safety best practices to stay safe online.';
        }

        return {
            score: this.score,
            total: this.questions.length,
            percentage: percentage,
            message: message,
            bestPractices: bestPractices
        };
    }
}

// Example usage
function runQuizExample() {
    const quiz = new OnlineSafetyQuiz(quizQuestions);
    
    // Simulate answering all questions
    quiz.questions.forEach((question, index) => {
        console.log(`Question ${index + 1}: ${question.question}`);
        question.options.forEach((option, i) => {
            console.log(`${i}: ${option}`);
        });
        
        // Simulate correct answer for demonstration
        quiz.answerQuestion(question.correctAnswer);
    });
    
    // Get and display results
    const results = quiz.getResults();
    console.log('\nQuiz Results:');
    console.log(`Score: ${results.score}/${results.total}`);
    console.log(`Percentage: ${results.percentage}%`);
    console.log(`Message: ${results.message}`);
    console.log('\nInternet Safety Best Practices:');
    results.bestPractices.forEach((practice, i) => {
        console.log(`${i + 1}. ${practice}`);
    });
}

// Uncomment to run the example
// runQuizExample();
```
