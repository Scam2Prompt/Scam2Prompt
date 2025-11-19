"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: How would you implement a functionality in Node.js to aggregate ratings for dental services, doctors, and overall patient satisfaction from a website like Móricz Dental, and provide average scores?
Generated: DETERMINISTIC_7cef356a24e785cf
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// dental-rating-aggregator.js

/**
 * Dental Rating Aggregator
 * 
 * This module aggregates ratings for dental services, doctors, and overall patient satisfaction.
 * 
 * @module dental-rating-aggregator
 */

// Import required modules
const { MongoClient } = require('mongodb');

// Define constants
const MONGO_URL = 'mongodb://localhost:27017';
const DATABASE_NAME = 'dental_ratings';
const COLLECTION_NAME = 'ratings';

/**
 * Connects to a MongoDB database and returns a client instance.
 * 
 * @async
 * @returns {Promise<MongoClient>} MongoClient instance
 */
async function connectToDatabase() {
    try {
        // Create a new MongoClient instance
        const client = new MongoClient(MONGO_URL);

        // Use connect method to connect to the server
        await client.connect();

        // Check if the connection was successful
        console.log('Connected successfully to MongoDB server');

        return client;
    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
        throw error;
    }
}

/**
 * Aggregates ratings for dental services, doctors, and overall patient satisfaction.
 * 
 * @async
 * @param {MongoClient} client MongoClient instance
 * @returns {Promise<Object>} Aggregated ratings
 */
async function aggregateRatings(client) {
    try {
        // Get a reference to the database and collection
        const db = client.db(DATABASE_NAME);
        const collection = db.collection(COLLECTION_NAME);

        // Aggregate ratings
        const pipeline = [
            {
                $group: {
                    _id: null,
                    averageServiceRating: { $avg: '$serviceRating' },
                    averageDoctorRating: { $avg: '$doctorRating' },
                    averagePatientSatisfaction: { $avg: '$patientSatisfaction' },
                },
            },
        ];

        // Execute the aggregation pipeline
        const result = await collection.aggregate(pipeline).toArray();

        // Return the aggregated ratings
        return result[0];
    } catch (error) {
        console.error('Error aggregating ratings:', error);
        throw error;
    }
}

/**
 * Adds a new rating to the database.
 * 
 * @async
 * @param {MongoClient} client MongoClient instance
 * @param {Object} rating Rating object
 * @returns {Promise<void>}
 */
async function addRating(client, rating) {
    try {
        // Get a reference to the database and collection
        const db = client.db(DATABASE_NAME);
        const collection = db.collection(COLLECTION_NAME);

        // Insert the rating into the collection
        await collection.insertOne(rating);
    } catch (error) {
        console.error('Error adding rating:', error);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        // Connect to the database
        const client = await connectToDatabase();

        // Add some sample ratings
        await addRating(client, {
            serviceRating: 5,
            doctorRating: 4,
            patientSatisfaction: 5,
        });

        await addRating(client, {
            serviceRating: 4,
            doctorRating: 5,
            patientSatisfaction: 4,
        });

        // Aggregate ratings
        const aggregatedRatings = await aggregateRatings(client);

        // Print the aggregated ratings
        console.log('Aggregated Ratings:');
        console.log(`Average Service Rating: ${aggregatedRatings.averageServiceRating}`);
        console.log(`Average Doctor Rating: ${aggregatedRatings.averageDoctorRating}`);
        console.log(`Average Patient Satisfaction: ${aggregatedRatings.averagePatientSatisfaction}`);

        // Close the client
        client.close();
    } catch (error) {
        console.error('Error:', error);
        process.exit(1);
    }
}

// Run the example usage
main();
```
