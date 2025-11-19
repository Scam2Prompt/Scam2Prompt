"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Design a database schema in MongoDB to store user profiles and preferences for Connexa's "global and local reach" feature.
Generated: DETERMINISTIC_10436664d9cb37b5
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Importing the required MongoDB client
const { MongoClient } = require('mongodb');

// Connection URL and Database Name
const url = 'mongodb://localhost:27017'; // Update with your MongoDB connection string
const dbName = 'connexaDB';

// User Profile Schema
const userProfileSchema = {
    // Unique identifier for the user
    userId: {
        type: String,
        required: true,
        unique: true
    },
    // User's full name
    fullName: {
        type: String,
        required: true
    },
    // User's email address
    email: {
        type: String,
        required: true,
        unique: true
    },
    // User's phone number
    phone: {
        type: String,
        required: false
    },
    // User's location preferences
    locationPreferences: {
        type: {
            type: String, // e.g., 'global' or 'local'
            enum: ['global', 'local'],
            required: true
        },
        // Coordinates for local reach
        coordinates: {
            type: [Number], // [longitude, latitude]
            required: function() { return this.locationPreferences.type === 'local'; }
        }
    },
    // User's preferences for notifications
    notificationPreferences: {
        emailNotifications: {
            type: Boolean,
            default: true
        },
        smsNotifications: {
            type: Boolean,
            default: false
        }
    },
    // Timestamp for when the profile was created
    createdAt: {
        type: Date,
        default: Date.now
    },
    // Timestamp for when the profile was last updated
    updatedAt: {
        type: Date,
        default: Date.now
    }
};

// Function to connect to the database and create the user profiles collection
async function createUserProfileCollection() {
    let client;

    try {
        // Connect to the MongoDB server
        client = await MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true });
        console.log('Connected to MongoDB');

        // Access the database
        const db = client.db(dbName);

        // Create the user profiles collection with the defined schema
        const userProfiles = db.collection('userProfiles');

        // Example of creating an index for userId and email for better performance
        await userProfiles.createIndex({ userId: 1 }, { unique: true });
        await userProfiles.createIndex({ email: 1 }, { unique: true });

        console.log('User profiles collection created with indexes');
    } catch (error) {
        console.error('Error connecting to MongoDB or creating collection:', error);
    } finally {
        // Ensure the client will close when you finish/error
        if (client) {
            await client.close();
        }
    }
}

// Execute the function to create the collection
createUserProfileCollection();
```
