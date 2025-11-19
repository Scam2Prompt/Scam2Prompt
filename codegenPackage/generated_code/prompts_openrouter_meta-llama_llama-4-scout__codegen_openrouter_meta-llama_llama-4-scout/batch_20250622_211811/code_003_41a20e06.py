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
/**
 * Retrieves a random question from the database based on the provided topic.
 * 
 * @param {string} topic - The topic for which to retrieve a random question.
 * @returns {Promise<string>} A promise resolving to a random question from the database.
 */

const db = require('./db'); // Assuming a database module

/**
 * Retrieves a random question from the database based on the provided topic.
 * 
 * @param {string} topic - The topic for which to retrieve a random question.
 * @returns {Promise<string>} A promise resolving to a random question from the database.
 */
async function getRandomQuestion(topic) {
    try {
        // Validate input topic
        if (typeof topic !== 'string' || topic.trim() === '') {
            throw new Error('Invalid topic provided');
        }

        // Query database for questions on the given topic
        const questions = await db.query(`SELECT question FROM questions WHERE topic = $1`, [topic]);

        // Check if any questions were found
        if (questions.rows.length === 0) {
            throw new Error(`No questions found for topic: ${topic}`);
        }

        // Select a random question from the results
        const randomIndex = Math.floor(Math.random() * questions.rows.length);
        const randomQuestion = questions.rows[randomIndex].question;

        return randomQuestion;
    } catch (error) {
        // Log the error and rethrow
        console.error(`Error retrieving random question: ${error.message}`);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        const topic = 'javascript';
        const question = await getRandomQuestion(topic);
        console.log(`Random question on ${topic}: ${question}`);
    } catch (error) {
        console.error(`Failed to retrieve question: ${error.message}`);
    }
}

main();
```
