"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Generate JavaScript code for implementing a "Sort by" dropdown menu for an online course platform, as seen in the rabbie-wall--extension-docs interface.
Generated: DETERMINISTIC_61113d3f13992763
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Code to implement a "Sort by" dropdown menu for an online course platform

// Sample list of courses for demonstration purposes
const courses = [
    { title: "JavaScript Basics", rating: 4.7, dateAdded: "2023-01-15" },
    { title: "React Fundamentals", rating: 4.9, dateAdded: "2023-03-01" },
    { title: "Node.js Essentials", rating: 4.5, dateAdded: "2023-02-10" }
];

// Function to sort courses based on the selected criteria
function sortCourses(courses, criteria) {
    switch (criteria) {
        case 'rating':
            return courses.sort((a, b) => b.rating - a.rating); // Sort by rating (highest first)
        case 'title':
            return courses.sort((a, b) => a.title.localeCompare(b.title)); // Sort alphabetically by title
        case 'dateAdded':
            return courses.sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded)); // Sort by date added (newest first)
        default:
            throw new Error("Invalid sort criteria"); // Handle unexpected sort criteria
    }
}

// Create the dropdown menu and populate it with options
function createSortDropdown() {
    const dropdown = document.createElement("select");
    dropdown.id = "sortDropdown"; // Assign an ID for identification

    // Define available sorting options
    const options = [
        { value: "rating", text: "Rating (Highest First)" },
        { value: "title", text: "Title (A-Z)" },
        { value: "dateAdded", text: "Date Added (Newest First)" }
    ];

    // Populate the dropdown menu with options
    options.forEach(option => {
        const dropdownOption = document.createElement("option");
        dropdownOption.value = option.value;
        dropdownOption.textContent = option.text;
        dropdown.appendChild(dropdownOption);
    });

    // Attach change event listener to handle dropdown selection
    dropdown.addEventListener("change", (event) => {
        try {
            const sortedCourses = sortCourses(courses, event.target.value); // Sort courses based on selected criteria
            displayCourses(sortedCourses); // Update the UI with sorted courses
        } catch (error) {
            console.error("Error while sorting courses:", error.message); // Log errors if any
        }
    });

    return dropdown;
}

// Function to render the sorted courses list onto the webpage
function displayCourses(courses) {
    const courseContainer = document.getElementById("courseContainer");
    courseContainer.innerHTML = ""; // Clear previous content

    // Dynamically generate the course list
    courses.forEach(course => {
        const courseItem = document.createElement("div");
        courseItem.className = "course-item"; // Assign a CSS class for styling
        courseItem.textContent = `${course.title} - Rating: ${course.rating} - Added: ${course.dateAdded}`;
        courseContainer.appendChild(courseItem);
    });
}

// Initialize the webpage content
function initializePage() {
    const appContainer = document.getElementById("app");

    // Create and append the dropdown menu
    const sortDropdown = createSortDropdown();
    appContainer.appendChild(sortDropdown);

    // Create and append the initial courses list
    const courseContainer = document.createElement("div");
    courseContainer.id = "courseContainer"; // Assign an ID for identification
    appContainer.appendChild(courseContainer);

    // Display the initial unsorted list of courses
    displayCourses(courses);
}

// Ensure DOM content is loaded before initializing page
document.addEventListener("DOMContentLoaded", initializePage);
```

Make sure the HTML file includes a `<div id="app"></div>` element for this script to work correctly.
