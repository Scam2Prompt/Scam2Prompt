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
// Importing required libraries
const mongoose = require('mongoose');

// Connecting to MongoDB
mongoose.connect('mongodb://localhost:27017/connexa', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// User Profile Schema
const userProfileSchema = new mongoose.Schema({
    // Unique identifier for each user
    userId: {
        type: String,
        required: true,
        unique: true,
    },
    // User's full name
    fullName: {
        type: String,
        required: true,
    },
    // User's email address
    email: {
        type: String,
        required: true,
        unique: true,
        match: /.+\@.+\..+/ // Regex for validating email format
    },
    // User's phone number
    phoneNumber: {
        type: String,
        required: true,
        unique: true,
    },
    // User's preferences for global and local reach
    preferences: {
        // Boolean indicating if user prefers global reach
        globalReach: {
            type: Boolean,
            default: false,
        },
        // Boolean indicating if user prefers local reach
        localReach: {
            type: Boolean,
            default: true,
        },
        // Array of locations for local reach preferences
        localLocations: [{
            type: String,
            required: false,
        }],
    },
}, {
    // Timestamps for creation and updates
    timestamps: true,
});

// Creating User Profile Model
const UserProfile = mongoose.model('UserProfile', userProfileSchema);

// Function to create a new user profile
const createUserProfile = async (profileData) => {
    try {
        const userProfile = new UserProfile(profileData);
        const result = await userProfile.save();
        console.log('User Profile Created:', result);
    } catch (error) {
        console.error('Error creating User Profile:', error);
    }
};

// Exporting the UserProfile model and createUserProfile function
module.exports = {
    UserProfile,
    createUserProfile,
};
```
