"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Generate code using JavaScript to display a dynamic list of available vocational courses (IeFP, IFTS) on a website, pulling data from a JSON file structured similarly to the course offerings on Araform.
Generated: DETERMINISTIC_9eb5f5d2cdf89d29
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// courses.json (Example JSON file structure)
// {
//   "courses": [
//     {
//       "id": 1,
//       "name": "Web Development Basics",
//       "type": "IeFP",
//       "duration": "6 months"
//     },
//     {
//       "id": 2,
//       "name": "Advanced Programming",
//       "type": "IFTS",
//       "duration": "1 year"
//     }
//   ]
// }

// JavaScript Code for dynamically displaying vocational courses

document.addEventListener("DOMContentLoaded", () => {
  const coursesContainer = document.getElementById("coursesContainer");

  // Function to fetch and display courses
  async function fetchAndDisplayCourses() {
    try {
      // Fetch data from the JSON file
      const response = await fetch("courses.json");
      
      // Handle HTTP errors
      if (!response.ok) {
        throw new Error(`Failed to fetch courses: ${response.status} ${response.statusText}`);
      }

      // Parse JSON data
      const data = await response.json();

      // Ensure the required structure exists
      if (!data.courses || !Array.isArray(data.courses)) {
        throw new Error("Invalid JSON structure: 'courses' key not found or not an array");
      }

      // Clear existing content (if any)
      coursesContainer.innerHTML = "";

      // Create and append course elements dynamically
      data.courses.forEach((course) => {
        const courseElement = document.createElement("div");
        courseElement.className = "course";

        // Course details
        courseElement.innerHTML = `
          <h3>${course.name}</h3>
          <p>Type: ${course.type}</p>
          <p>Duration: ${course.duration}</p>
        `;

        // Append to container
        coursesContainer.appendChild(courseElement);
      });
    } catch (error) {
      // Log and display error
      console.error("Error fetching or displaying courses:", error);
      coursesContainer.innerHTML = `<p class="error">Failed to load courses. Please try again later.</p>`;
    }
  }

  // Call the function to fetch and display courses
  fetchAndDisplayCourses();
});

// Note: This script assumes an HTML structure like below:
// <div id="coursesContainer"></div>

// Example CSS to style the courses (optional)
/*
<style>
  #coursesContainer {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .course {
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 5px;
    background-color: #f9f9f9;
    width: calc(33% - 2rem);
  }

  .course h3 {
    margin: 0.5rem 0;
  }

  .error {
    color: red;
    font-weight: bold;
  }
</style>
*/
```
