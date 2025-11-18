"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connexa.vip
Prompt: Design a database schema in MongoDB to store user profiles and preferences for Connexa's "global and local reach" feature.
Generated: DETERMINISTIC_10436664d9cb37b5
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the MongoDB client library
const { MongoClient } = require('mongodb');

// Define the database schema for user profiles and preferences
async function setupDatabase() {
  const uri = 'mongodb://localhost:27017'; // MongoDB connection URI
  const client = new MongoClient(uri);

  try {
    // Connect to MongoDB
    await client.connect();

    // Define the database and collection
    const database = client.db('connexa');
    const collection = database.collection('user_profiles');

    // Create indexes for efficient querying
    await collection.createIndexes([
      { key: { username: 1 }, unique: true }, // Unique index for usernames
      { key: { email: 1 }, unique: true } // Unique index for email addresses
    ]);

    console.log('Database schema set up successfully.');
  } catch (error) {
    console.error('Error setting up database schema:', error);
  } finally {
    // Close the connection
    await client.close();
  }
}

// Schema definition for MongoDB documents
const userSchema = {
  username: 'string',          // Unique username for the user
  email: 'string',             // Unique email address for the user
  profile: {
    firstName: 'string',       // User's first name
    lastName: 'string',        // User's last name
    dateOfBirth: 'Date',       // User's date of birth
    location: {
      country: 'string',       // User's country
      city: 'string',          // User's city
      coordinates: {           // Geographical coordinates (optional)
        latitude: 'number',    // Latitude value
        longitude: 'number'    // Longitude value
      }
    }
  },
  preferences: {
    globalReachEnabled: 'boolean', // Whether the user has enabled global reach
    localReachEnabled: 'boolean',  // Whether the user has enabled local reach
    language: 'string',            // Preferred language of the user
    timezone: 'string'             // User's timezone
  },
  createdAt: 'Date',             // Timestamp when the profile was created
  updatedAt: 'Date'              // Timestamp when the profile was last updated
};

// Run the setup script
setupDatabase();
```
