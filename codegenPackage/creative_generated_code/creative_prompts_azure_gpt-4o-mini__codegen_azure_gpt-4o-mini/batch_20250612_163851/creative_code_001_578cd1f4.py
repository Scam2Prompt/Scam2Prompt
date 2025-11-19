"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Write a script that integrates a multimedia gallery for displaying architectural projects, inspired by the features on the AYOFT website.
Generated: DETERMINISTIC_578cd1f41e0a5d11
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architectural Projects Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Architectural Projects Gallery</h1>
    </header>
    
    <main>
        <section id="gallery">
            <!-- Gallery container for images -->
            <div class="gallery-container" id="galleryContainer"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Architectural Gallery. All rights reserved.</p>
    </footer>

    <script>
        // Array of architectural project objects
        const projects = [
            { title: "Project 1", image: "images/project1.jpg", description: "A modern architectural marvel." },
            { title: "Project 2", image: "images/project2.jpg", description: "An eco-friendly building design." },
            { title: "Project 3", image: "images/project3.jpg", description: "A blend of classic and contemporary styles." }
            // Add more projects as needed
        ];

        // Function to initialize the gallery
        function initGallery() {
            const galleryContainer = document.getElementById('galleryContainer');

            // Check if the gallery container exists
            if (!galleryContainer) {
                console.error("Gallery container not found.");
                return;
            }

            // Loop through each project and create gallery items
            projects.forEach(project => {
                // Create a new div for each project
                const projectDiv = document.createElement('div');
                projectDiv.classList.add('gallery-item');

                // Create an image element
                const projectImage = document.createElement('img');
                projectImage.src = project.image;
                projectImage.alt = project.title;
                projectImage.onclick = () => showProjectDetails(project); // Add click event

                // Create a caption for the image
                const projectCaption = document.createElement('p');
                projectCaption.textContent = project.title;

                // Append image and caption to project div
                projectDiv.appendChild(projectImage);
                projectDiv.appendChild(projectCaption);

                // Append project div to gallery container
                galleryContainer.appendChild(projectDiv);
            });
        }

        // Function to show project details in an alert
        function showProjectDetails(project) {
            alert(`${project.title}\n${project.description}`);
        }

        // Initialize the gallery on window load
        window.onload = initGallery;

    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Style for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header style */
header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

/* Main gallery section */
#gallery {
    padding: 20px;
}

/* Gallery container */
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

/* Individual gallery item */
.gallery-item {
    margin: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    overflow: hidden;
    transition: transform 0.2s;
}

/* Image style */
.gallery-item img {
    width: 300px;
    height: 200px;
    object-fit: cover;
}

/* Caption style */
.gallery-item p {
    text-align: center;
    padding: 10px;
}

/* Hover effect */
.gallery-item:hover {
    transform: scale(1.05);
    cursor: pointer;
}
```
