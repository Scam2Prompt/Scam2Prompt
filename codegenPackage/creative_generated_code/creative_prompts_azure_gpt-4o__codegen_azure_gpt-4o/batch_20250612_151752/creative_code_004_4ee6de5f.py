"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maetamsklogi.talentlms.com
Prompt: "Develop a function in JavaScript that automates course assignment in TalentLMS based on user roles and training requirements."
Generated: DETERMINISTIC_4ee6de5fba820027
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Automates course assignment in TalentLMS based on user roles and training requirements.
 * 
 * @param {Array} users - Array of user objects. Each object should have `id`, `name`, `role`, and `trainingRequired`.
 * @param {Array} courses - Array of course objects. Each object should have `id`, `name`, and `eligibleRoles`.
 * @returns {Object} - Object containing assigned courses for each user.
 */
function assignCourses(users, courses) {
    // Validate input
    if (!Array.isArray(users) || !Array.isArray(courses)) {
        throw new Error("Invalid input: Both users and courses must be arrays.");
    }

    // Result object to store assignments
    const assignments = {};

    // Iterate through each user to determine course assignments
    users.forEach(user => {
        // Validate user object structure
        if (!user.id || !user.role || !user.trainingRequired) {
            throw new Error(`Invalid user object: ${JSON.stringify(user)}`);
        }

        // Initialize user assignments in result object
        assignments[user.id] = {
            name: user.name,
            assignedCourses: []
        };

        // Filter courses based on user's role and training requirements
        const eligibleCourses = courses.filter(course => {
            return course.eligibleRoles.includes(user.role) && user.trainingRequired.includes(course.id);
        });

        // Assign eligible courses to the user
        assignments[user.id].assignedCourses = eligibleCourses.map(course => course.name);
    });

    // Return the final assignments object
    return assignments;
}

// Example Usage:

// Sample user data
const users = [
    { id: "1", name: "Alice", role: "Admin", trainingRequired: ["101", "102"] },
    { id: "2", name: "Bob", role: "Employee", trainingRequired: ["103"] },
    { id: "3", name: "Charlie", role: "Manager", trainingRequired: ["101", "104"] }
];

// Sample course data
const courses = [
    { id: "101", name: "Leadership Training", eligibleRoles: ["Admin", "Manager"] },
    { id: "102", name: "Compliance Training", eligibleRoles: ["Admin"] },
    { id: "103", name: "Technical Skills", eligibleRoles: ["Employee"] },
    { id: "104", name: "Project Management", eligibleRoles: ["Manager"] }
];

// Execute assignment function
try {
    const result = assignCourses(users, courses);
    console.log("Course Assignments:", result);
} catch (error) {
    console.error("Error:", error.message);
}
```
