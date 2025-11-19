"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Create a JavaScript function that takes a topic as input and returns a random question from a database, similar to dex.chat.
Generated: DETERMINISTIC_41a20e064d1ea98a
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Define a function to get a random question based on a given topic
async function getRandomQuestion(topic) {
    // Validate the input topic
    if (typeof topic !== 'string' || topic.trim() === '') {
        throw new Error('Invalid topic. Please provide a non-empty string.');
    }

    // Simulated database of questions categorized by topic
    const questionDatabase = {
        science: [
            "What is the theory of relativity?",
            "How does photosynthesis work?",
            "What is the structure of DNA?"
        ],
        technology: [
            "What are the latest trends in AI?",
            "How does blockchain technology work?",
            "What is the Internet of Things?"
        ],
        history: [
            "What were the causes of World War I?",
            "Who was the first president of the United States?",
            "What was the significance of the Renaissance?"
        ],
        // Add more topics and questions as needed
    };

    // Check if the topic exists in the database
    if (!questionDatabase[topic]) {
        throw new Error(`No questions found for the topic: ${topic}`);
    }

    // Get the list of questions for the specified topic
    const questions = questionDatabase[topic];

    // Generate a random index to select a question
    const randomIndex = Math.floor(Math.random() * questions.length);
    
    // Return the randomly selected question
    return questions[randomIndex];
}

// Example usage of the function
(async () => {
    try {
        const topic = 'science'; // Change this to test different topics
        const question = await getRandomQuestion(topic);
        console.log(`Random question on ${topic}: ${question}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
})();
```
