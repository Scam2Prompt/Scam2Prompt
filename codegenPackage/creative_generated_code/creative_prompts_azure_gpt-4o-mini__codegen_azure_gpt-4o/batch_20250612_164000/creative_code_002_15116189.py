"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://estcacademy.com
Prompt: Create a JavaScript function that displays a list of available courses from ESTC Academy focused on emergencies and skill training.
Generated: DETERMINISTIC_15116189b19a110f
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display a list of available courses from ESTC Academy
 * focused on emergencies and skill training.
 * 
 * This function retrieves the courses from a mock data source
 * and displays them in a formatted list.
 */

// Mock data representing ESTC Academy courses
const estcCourses = [
    { id: 1, name: "Basic First Aid Training", duration: "4 hours" },
    { id: 2, name: "Fire Safety and Prevention", duration: "6 hours" },
    { id: 3, name: "CPR Certification Course", duration: "3 hours" },
    { id: 4, name: "Emergency Response Planning", duration: "8 hours" },
    { id: 5, name: "Disaster Management Workshop", duration: "5 hours" }
];

/**
 * Function to fetch available courses from ESTC Academy
 * @returns {Array} - List of course objects
 */
function fetchCourses() {
    try {
        // Simulate fetching courses (can be replaced with an API call in production)
        return estcCourses;
    } catch (error) {
        console.error("Error fetching courses:", error.message);
        return [];
    }
}

/**
 * Function to display the list of available courses
 */
function displayCourses() {
    const courses = fetchCourses();

    // Check if there are any courses available
    if (courses.length === 0) {
        console.log("No courses available at the moment.");
        return;
    }

    console.log("Available Courses from ESTC Academy:");
    console.log("------------------------------------");

    // Loop through the courses and display them
    courses.forEach(course => {
        console.log(`Course ID: ${course.id}`);
        console.log(`Name: ${course.name}`);
        console.log(`Duration: ${course.duration}`);
        console.log("------------------------------------");
    });
}

// Call the function to display courses
displayCourses();
```
