"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rbby-wollet.teachable.com
Prompt: Provide code to implement a "Sort by" feature for filtering course products on a Teachable-based website.
Generated: DETERMINISTIC_a4aa8331c9178c89
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// sortCourses.js

/**
 * Sorts an array of course objects based on the specified sorting criteria.
 * 
 * @param {Array} courses - An array of course objects to be sorted.
 * @param {string} sortBy - The criteria by which to sort the courses.
 * @returns {Array} - A new array of sorted course objects.
 * 
 * @throws {Error} - Throws an error if the sortBy criteria is invalid.
 */
function sortCourses(courses, sortBy) {
    // Check if courses is an array
    if (!Array.isArray(courses)) {
        throw new TypeError('Expected an array of courses.');
    }

    // Create a copy of the courses array to avoid mutating the original
    const sortedCourses = [...courses];

    // Determine the sorting logic based on the sortBy parameter
    switch (sortBy) {
        case 'name':
            sortedCourses.sort((a, b) => a.name.localeCompare(b.name));
            break;
        case 'date':
            sortedCourses.sort((a, b) => new Date(b.date) - new Date(a.date));
            break;
        case 'price':
            sortedCourses.sort((a, b) => a.price - b.price);
            break;
        default:
            throw new Error(`Invalid sort criteria: ${sortBy}. Expected 'name', 'date', or 'price'.`);
    }

    return sortedCourses;
}

// Example usage
try {
    const courses = [
        { name: 'Course A', date: '2023-01-15', price: 100 },
        { name: 'Course B', date: '2022-12-20', price: 150 },
        { name: 'Course C', date: '2023-03-10', price: 90 },
    ];

    // Sort courses by name
    const sortedByName = sortCourses(courses, 'name');
    console.log('Sorted by name:', sortedByName);

    // Sort courses by date
    const sortedByDate = sortCourses(courses, 'date');
    console.log('Sorted by date:', sortedByDate);

    // Sort courses by price
    const sortedByPrice = sortCourses(courses, 'price');
    console.log('Sorted by price:', sortedByPrice);
} catch (error) {
    console.error('Error sorting courses:', error.message);
}
```
