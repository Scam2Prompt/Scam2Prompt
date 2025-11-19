"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Write a code snippet in JavaScript to implement a simple course catalog filter, similar to what is seen on araform.org, using keywords like 'IeFP' and 'formazione professionale'."
Generated: DETERMINISTIC_c02090efbbcc88bc
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Course Catalog Filter Implementation

// Sample course data
const courses = [
    { id: 1, title: "Introduction to IeFP", description: "A comprehensive course on IeFP." },
    { id: 2, title: "Advanced Formazione Professionale", description: "Deep dive into professional training." },
    { id: 3, title: "Basic Programming", description: "Learn the basics of programming." },
    { id: 4, title: "IeFP and Career Opportunities", description: "Explore career paths in IeFP." },
    { id: 5, title: "Formazione Professionale Essentials", description: "Essential skills for professional training." }
];

// Function to filter courses based on keywords
/**
 * Filters the courses based on the provided keywords.
 * @param {Array} courses - The array of course objects to filter.
 * @param {Array} keywords - The array of keywords to filter by.
 * @returns {Array} - An array of filtered course objects.
 */
function filterCourses(courses, keywords) {
    if (!Array.isArray(courses) || !Array.isArray(keywords)) {
        throw new Error("Invalid input: courses and keywords must be arrays.");
    }

    return courses.filter(course => {
        // Check if any keyword is present in the course title or description
        return keywords.some(keyword => 
            course.title.toLowerCase().includes(keyword.toLowerCase()) || 
            course.description.toLowerCase().includes(keyword.toLowerCase())
        );
    });
}

// Example usage
try {
    const keywords = ['IeFP', 'formazione professionale'];
    const filteredCourses = filterCourses(courses, keywords);
    
    // Display the filtered courses
    console.log("Filtered Courses:", filteredCourses);
} catch (error) {
    console.error("Error filtering courses:", error.message);
}
```
