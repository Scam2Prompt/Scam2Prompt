"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Develop a code snippet in JavaScript to dynamically display a list of art courses offered by Ânima, such as "desenho artístico" and "design de joias," on a webpage.
Generated: DETERMINISTIC_fac49c52dacb1dad
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Code to dynamically display a list of art courses offered by Ânima on a webpage

// Dummy data representing art courses offered by Ânima
const artCourses = [
  "Desenho Artístico",
  "Design de Joias",
  "Escultura Contemporânea",
  "Pintura Digital",
  "Fotografia Artística"
];

// Function to dynamically create and display the list of art courses
function displayArtCourses(courses) {
  try {
    // Get the container element where the courses will be displayed
    const coursesContainer = document.getElementById("courses-container");

    if (!coursesContainer) {
      throw new Error("Element with ID 'courses-container' not found.");
    }

    // Create a <ul> element to hold the list of courses
    const ulElement = document.createElement("ul");
    ulElement.classList.add("courses-list"); // Add a class for styling

    // Loop through the courses and create <li> elements for each
    courses.forEach((course) => {
      const liElement = document.createElement("li");
      liElement.textContent = course; // Set the text content of the <li>
      ulElement.appendChild(liElement); // Append <li> to <ul>
    });

    // Clear the container and append the <ul> to it
    coursesContainer.innerHTML = ""; // Ensure the container is empty
    coursesContainer.appendChild(ulElement);
  } catch (error) {
    // Log any error that occurs during the execution
    console.error("Error displaying art courses:", error.message);
  }
}

// Call the function to display the courses after the page has loaded
document.addEventListener("DOMContentLoaded", () => {
  displayArtCourses(artCourses);
});
```

```html
<!-- HTML structure for the webpage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Art Courses Offered by Ânima</title>
  <style>
    /* Basic styling for the course list */
    .courses-list {
      list-style-type: none;
      padding: 0;
    }
    .courses-list li {
      margin: 5px 0;
      padding: 10px;
      background-color: #f4f4f4;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <h1>Art Courses Offered by Ânima</h1>
  <!-- Container for dynamically displaying courses -->
  <div id="courses-container"></div>
  <!-- Include the JavaScript file -->
  <script src="script.js"></script>
</body>
</html>
```
