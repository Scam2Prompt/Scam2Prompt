"""
Generated Code Metadata:
========================
Original URL: https://dflow.pages.dev
Prompt: "How can I implement a system like DFlow's to track user engagement across multiple phases of a project, using Node.js and MongoDB?"
Generated: DETERMINISTIC_bfec92d261f8c3ba
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// engagement-tracker.js

/**
 * Engagement Tracker System
 * =========================
 * 
 * This system tracks user engagement across multiple phases of a project.
 * 
 * @author [Your Name]
 */

// Import required modules
const mongoose = require('mongoose');
const { Schema } = mongoose;

// Connect to MongoDB
mongoose.connect('mongodb://localhost/engagement-tracker', { useNewUrlParser: true, useUnifiedTopology: true });

// Define the User Engagement Schema
const userEngagementSchema = new Schema({
  userId: { type: String, required: true },
  projectId: { type: String, required: true },
  phase: { type: String, required: true },
  engagementType: { type: String, required: true }, // e.g., 'view', 'click', 'submit'
  timestamp: { type: Date, default: Date.now }
});

// Define the User Engagement Model
const UserEngagement = mongoose.model('UserEngagement', userEngagementSchema);

// Define the Project Phase Schema
const projectPhaseSchema = new Schema({
  projectId: { type: String, required: true },
  phase: { type: String, required: true },
  startDate: { type: Date, required: true },
  endDate: { type: Date, required: true }
});

// Define the Project Phase Model
const ProjectPhase = mongoose.model('ProjectPhase', projectPhaseSchema);

// Function to track user engagement
async function trackEngagement(userId, projectId, phase, engagementType) {
  try {
    // Check if project phase exists
    const projectPhase = await ProjectPhase.findOne({ projectId, phase });
    if (!projectPhase) {
      throw new Error(`Project phase not found: ${projectId} - ${phase}`);
    }

    // Create a new user engagement document
    const userEngagement = new UserEngagement({ userId, projectId, phase, engagementType });
    await userEngagement.save();

    return userEngagement;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

// Function to get user engagement history
async function getEngagementHistory(userId, projectId) {
  try {
    const userEngagements = await UserEngagement.find({ userId, projectId })
      .sort({ timestamp: -1 })
      .populate('projectId', 'name');

    return userEngagements;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

// Function to create a new project phase
async function createProjectPhase(projectId, phase, startDate, endDate) {
  try {
    const projectPhase = new ProjectPhase({ projectId, phase, startDate, endDate });
    await projectPhase.save();

    return projectPhase;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Create a new project phase
    const projectPhase = await createProjectPhase('project-123', 'phase-1', new Date('2024-01-01'), new Date('2024-01-31'));

    // Track user engagement
    const userEngagement = await trackEngagement('user-123', 'project-123', 'phase-1', 'view');
    console.log(userEngagement);

    // Get user engagement history
    const engagementHistory = await getEngagementHistory('user-123', 'project-123');
    console.log(engagementHistory);
  } catch (error) {
    console.error(error);
  }
}

main();
```
