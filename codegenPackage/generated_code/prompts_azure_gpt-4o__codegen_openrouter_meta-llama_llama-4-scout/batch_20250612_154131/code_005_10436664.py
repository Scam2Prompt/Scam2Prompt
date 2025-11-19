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
// MongoDB schema design for Connexa's user profiles and preferences

// Import required modules
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/connexa', { useNewUrlParser: true, useUnifiedTopology: true });

// Define user profile schema
const userProfileSchema = new mongoose.Schema({
  /**
   * Unique identifier for the user
   */
  userId: { type: String, required: true, unique: true },

  /**
   * User's basic information
   */
  name: { type: String },
  email: { type: String, unique: true },
  phone: { type: String },
  location: {
    /**
     * User's geographic location
     */
    city: { type: String },
    state: { type: String },
    country: { type: String },
    zip: { type: String }
  },

  /**
   * User's profile preferences
   */
  preferences: {
    /**
     * Global and local reach preferences
     */
    globalReach: { type: Boolean, default: false },
    localReach: { type: Boolean, default: false },
    topics: [{ type: String }] // topics of interest
  },

  /**
   * Timestamp for user profile creation and update
   */
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Define user profile model
const UserProfile = mongoose.model('UserProfile', userProfileSchema);

// Define user preference schema
const userPreferenceSchema = new mongoose.Schema({
  /**
   * Unique identifier for the user preference
   */
  userId: { type: String, required: true, ref: 'UserProfile' },

  /**
   * User's notification preferences
   */
  notifications: {
    email: { type: Boolean, default: true },
    push: { type: Boolean, default: true }
  },

  /**
   * User's communication preferences
   */
  communication: {
    frequency: { type: String, enum: ['daily', 'weekly', 'monthly'] },
    channels: [{ type: String, enum: ['email', 'sms', 'in-app'] }]
  },

  /**
   * Timestamp for user preference creation and update
   */
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Define user preference model
const UserPreference = mongoose.model('UserPreference', userPreferenceSchema);

// Create indexes for efficient querying
userProfileSchema.index({ userId: 1 }, { unique: true });
userProfileSchema.index({ email: 1 }, { unique: true });
userPreferenceSchema.index({ userId: 1 });

// Export models
module.exports = { UserProfile, UserPreference };
```
