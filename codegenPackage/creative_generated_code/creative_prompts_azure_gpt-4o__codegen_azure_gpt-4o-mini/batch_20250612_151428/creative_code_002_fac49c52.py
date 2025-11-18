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
// Define an array of art courses offered by Ânima
const artCourses = [
    "Desenho Artístico",
    "Design de Joias",
    "Pintura em Tela",
    "Escultura",
    "Ilustração Digital"
];

// Function to dynamically display courses on the webpage
function displayArtCourses(courses) {
    // Get the container element where courses will be displayed
    const courseContainer = document.getElementById("course-container");
    
    // Clear any existing content in the container
    courseContainer.innerHTML = "";

    // Check if the courses array is valid
    if (!Array.isArray(courses) || courses.length === 0) {
        console.error("Invalid course list provided.");
        courseContainer.innerHTML = "<p>No courses available.</p>";
        return;
    }

    // Create a list element to hold the courses
    const listElement = document.createElement("ul");

    // Populate the list with course items
    courses.forEach(course => {
        // Create a list item for each course
        const listItem = document.createElement("li");
        listItem.textContent = course; // Set the text content to the course name
        listElement.appendChild(listItem); // Append the list item to the list
    });

    // Append the list to the container
    courseContainer.appendChild(listElement);
}

// Call the function to display the courses
document.addEventListener("DOMContentLoaded", () => {
    displayArtCourses(artCourses);
});
```

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Art Courses Offered by Ânima</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
        }
        #course-container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Art Courses Offered by Ânima</h1>
    <div id="course-container"></div>

    <script src="path/to/your/javascript-file.js"></script>
</body>
</html>
```
