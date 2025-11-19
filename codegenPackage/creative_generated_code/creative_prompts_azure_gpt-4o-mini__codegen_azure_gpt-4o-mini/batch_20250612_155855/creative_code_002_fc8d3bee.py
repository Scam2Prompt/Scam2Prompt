"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Create a JavaScript function that facilitates community engagement by allowing users to sign up for environmental workshops and sustainability projects.
Generated: DETERMINISTIC_fc8d3bee6aab0a82
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to handle user signup for environmental workshops and sustainability projects
class CommunityEngagement {
    constructor() {
        // Holds the list of registered participants
        this.participants = [];
    }

    /**
     * Sign up a user for a workshop or project.
     * @param {Object} user - The user object containing user details.
     * @param {string} user.name - The name of the user.
     * @param {string} user.email - The email of the user.
     * @param {string} project - The project or workshop name.
     * @returns {string} - Confirmation message.
     * @throws {Error} - Throws an error if user details are invalid or if the user is already registered.
     */
    signUp(user, project) {
        // Validate user details
        if (!user || !user.name || !user.email) {
            throw new Error("Invalid user details. Name and email are required.");
        }
        
        // Check for duplicate registration
        const isRegistered = this.participants.some(participant => 
            participant.email === user.email && participant.project === project
        );
        
        if (isRegistered) {
            throw new Error("User is already registered for this project.");
        }

        // Register the user
        this.participants.push({ ...user, project });
        return `Successfully registered ${user.name} for ${project}.`;
    }

    /**
     * Get the list of registered participants for a specific project.
     * @param {string} project - The project or workshop name.
     * @returns {Array} - List of participants for the project.
     * @throws {Error} - Throws an error if project name is invalid.
     */
    getParticipants(project) {
        // Validate project name
        if (!project) {
            throw new Error("Project name is required.");
        }

        // Filter participants by project
        return this.participants.filter(participant => participant.project === project);
    }
}

// Example usage: 
try {
    const engagement = new CommunityEngagement();
    
    // User signups
    console.log(engagement.signUp({ name: "John Doe", email: "john@example.com" }, "Tree Planting Workshop"));
    console.log(engagement.signUp({ name: "Jane Smith", email: "jane@example.com" }, "Beach Cleanup"));

    // Fetch participants for a project
    const participants = engagement.getParticipants("Tree Planting Workshop");
    console.log("Participants for Tree Planting Workshop:", participants);
} catch (error) {
    console.error("Error:", error.message);
}
```
