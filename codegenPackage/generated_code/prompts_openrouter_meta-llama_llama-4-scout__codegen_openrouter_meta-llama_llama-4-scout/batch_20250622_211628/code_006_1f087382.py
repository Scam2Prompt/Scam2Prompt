"""
Generated Code Metadata:
========================
Original URL: https://liquideth-gift.org
Prompt: Design a NoSQL database schema using MongoDB to store and manage user-generated content, such as posts, comments, and engagement metrics, from a humor website.
Generated: DETERMINISTIC_1f08738213a3c863
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required MongoDB Node.js driver
const { MongoClient, ObjectId } = require('mongodb');

// Define database connection URL
const DB_URL = 'mongodb://localhost:27017';

// Define database name
const DB_NAME = 'humorWebsite';

// Define collection names
const POSTS_COLLECTION = 'posts';
const COMMENTS_COLLECTION = 'comments';
const ENGAGEMENT_COLLECTION = 'engagement';

// Connect to MongoDB
async function connectToMongoDB() {
    try {
        const client = new MongoClient(DB_URL);
        await client.connect();
        console.log('Connected to MongoDB');
        return client;
    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
        throw error;
    }
}

// Define schema for posts collection
const postSchema = {
    title: { type: String, required: true },
    content: { type: String, required: true },
    author: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
    comments: [{ type: ObjectId, ref: COMMENTS_COLLECTION }],
    engagement: { type: ObjectId, ref: ENGAGEMENT_COLLECTION }
};

// Define schema for comments collection
const commentSchema = {
    postId: { type: ObjectId, ref: POSTS_COLLECTION, required: true },
    author: { type: String, required: true },
    content: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
};

// Define schema for engagement collection
const engagementSchema = {
    postId: { type: ObjectId, ref: POSTS_COLLECTION, required: true },
    likes: { type: Number, default: 0 },
    dislikes: { type: Number, default: 0 },
    shares: { type: Number, default: 0 }
};

// Create indexes for efficient querying
async function createIndexes(client) {
    try {
        const db = client.db(DB_NAME);
        const postsCollection = db.collection(POSTS_COLLECTION);
        await postsCollection.createIndex({ title: 1 });
        await postsCollection.createIndex({ author: 1 });

        const commentsCollection = db.collection(COMMENTS_COLLECTION);
        await commentsCollection.createIndex({ postId: 1 });
        await commentsCollection.createIndex({ author: 1 });

        const engagementCollection = db.collection(ENGAGEMENT_COLLECTION);
        await engagementCollection.createIndex({ postId: 1 });
    } catch (error) {
        console.error('Error creating indexes:', error);
        throw error;
    }
}

// Main function to initialize database schema
async function initDatabaseSchema() {
    try {
        const client = await connectToMongoDB();
        await createIndexes(client);
        console.log('Database schema initialized');
    } catch (error) {
        console.error('Error initializing database schema:', error);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        await initDatabaseSchema();

        // Create a new post
        const client = await connectToMongoDB();
        const db = client.db(DB_NAME);
        const postsCollection = db.collection(POSTS_COLLECTION);
        const newPost = {
            title: 'Humorous Post',
            content: 'This is a humorous post.',
            author: 'John Doe'
        };
        const postResult = await postsCollection.insertOne(newPost);
        console.log('Post created:', postResult.ops[0]);

        // Create a new comment
        const commentsCollection = db.collection(COMMENTS_COLLECTION);
        const newComment = {
            postId: postResult.ops[0]._id,
            author: 'Jane Doe',
            content: 'This is a comment.'
        };
        const commentResult = await commentsCollection.insertOne(newComment);
        console.log('Comment created:', commentResult.ops[0]);

        // Update engagement metrics
        const engagementCollection = db.collection(ENGAGEMENT_COLLECTION);
        const newEngagement = {
            postId: postResult.ops[0]._id,
            likes: 10,
            dislikes: 2,
            shares: 5
        };
        const engagementResult = await engagementCollection.insertOne(newEngagement);
        console.log('Engagement metrics updated:', engagementResult.ops[0]);

        // Close MongoDB connection
        client.close();
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
```
