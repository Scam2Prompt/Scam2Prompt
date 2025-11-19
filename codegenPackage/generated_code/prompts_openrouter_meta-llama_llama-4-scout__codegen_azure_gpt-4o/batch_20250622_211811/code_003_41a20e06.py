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
// Import necessary modules (assuming a Node.js environment)
const { MongoClient } = require('mongodb');

// Function to fetch a random question based on a topic
async function getRandomQuestion(topic) {
    // MongoDB connection URI and database/collection details
    const uri = 'your-mongodb-connection-string'; // Replace with your MongoDB connection string
    const dbName = 'questionsDB'; // Replace with your database name
    const collectionName = 'questions'; // Replace with your collection name

    // Validate input
    if (typeof topic !== 'string' || topic.trim() === '') {
        throw new Error('Invalid topic. Please provide a non-empty string.');
    }

    // Initialize MongoDB client
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // Connect to the database
        await client.connect();
        const db = client.db(dbName);
        const collection = db.collection(collectionName);

        // Query the database for a random question matching the topic
        const pipeline = [
            { $match: { topic: topic.trim() } }, // Match documents with the given topic
            { $sample: { size: 1 } } // Randomly sample one document
        ];
        const result = await collection.aggregate(pipeline).toArray();

        // Check if a question was found
        if (result.length === 0) {
            throw new Error(`No questions found for the topic: ${topic}`);
        }

        // Return the random question
        return result[0].question; // Assuming the question field contains the question text
    } catch (error) {
        // Log and rethrow the error for the caller to handle
        console.error('Error fetching random question:', error.message);
        throw error;
    } finally {
        // Ensure the client is closed to free up resources
        await client.close();
    }
}

// Example usage (uncomment to test):
// (async () => {
//     try {
//         const question = await getRandomQuestion('JavaScript');
//         console.log('Random Question:', question);
//     } catch (error) {
//         console.error('Error:', error.message);
//     }
// })();

// Export the function for use in other modules
module.exports = getRandomQuestion;
```
