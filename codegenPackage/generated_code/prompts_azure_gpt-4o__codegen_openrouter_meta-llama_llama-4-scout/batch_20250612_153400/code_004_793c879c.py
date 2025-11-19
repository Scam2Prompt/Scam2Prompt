"""
Generated Code Metadata:
========================
Original URL: https://rdmerakyat.com
Prompt: Write JavaScript code to create a dynamic interface for showcasing architectural projects, similar to the Études Architect App feature.
Generated: DETERMINISTIC_793c879c9874707f
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Project Showcase Interface

class Project {
  /**
   * Represents an architectural project.
   * @param {string} id - Unique project identifier.
   * @param {string} name - Project name.
   * @param {string} description - Project description.
   * @param {string[]} images - Array of project image URLs.
   */
  constructor(id, name, description, images) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.images = images;
  }
}

class ProjectShowcase {
  /**
   * Dynamic interface for showcasing architectural projects.
   */
  constructor() {
    this.projects = [];
    this.currentProjectIndex = 0;
  }

  /**
   * Adds a project to the showcase.
   * @param {Project} project - Project to add.
   */
  addProject(project) {
    this.projects.push(project);
  }

  /**
   * Renders the project showcase interface.
   */
  render() {
    const showcaseElement = document.getElementById('project-showcase');
    if (!showcaseElement) {
      throw new Error('Project showcase element not found');
    }

    // Clear existing content
    showcaseElement.innerHTML = '';

    // Render project navigation
    const navigationElement = document.createElement('div');
    navigationElement.classList.add('navigation');
    this.projects.forEach((project, index) => {
      const buttonElement = document.createElement('button');
      buttonElement.textContent = project.name;
      buttonElement.onclick = () => this.showProject(index);
      navigationElement.appendChild(buttonElement);
    });
    showcaseElement.appendChild(navigationElement);

    // Render current project
    this.showProject(this.currentProjectIndex);
  }

  /**
   * Shows a specific project in the showcase.
   * @param {number} index - Index of the project to show.
   */
  showProject(index) {
    if (index < 0 || index >= this.projects.length) {
      throw new Error('Invalid project index');
    }

    this.currentProjectIndex = index;
    const project = this.projects[index];
    const showcaseElement = document.getElementById('project-showcase');

    // Render project details
    const detailsElement = document.createElement('div');
    detailsElement.classList.add('project-details');
    detailsElement.innerHTML = `
      <h2>${project.name}</h2>
      <p>${project.description}</p>
      <div class="image-gallery">
        ${project.images.map((image) => `<img src="${image}" alt="${project.name}">`).join('')}
      </div>
    `;
    showcaseElement.appendChild(detailsElement);
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const showcase = new ProjectShowcase();

  // Create sample projects
  const project1 = new Project('1', 'Project 1', 'This is project 1', ['image1.jpg', 'image2.jpg']);
  const project2 = new Project('2', 'Project 2', 'This is project 2', ['image3.jpg', 'image4.jpg']);

  // Add projects to showcase
  showcase.addProject(project1);
  showcase.addProject(project2);

  // Render project showcase
  showcase.render();
});
```

```css
/* Styles for project showcase */
#project-showcase {
  max-width: 800px;
  margin: 40px auto;
}

.navigation {
  margin-bottom: 20px;
}

.navigation button {
  margin-right: 10px;
}

.project-details {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.image-gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.image-gallery img {
  width: 100px;
  height: 100px;
  margin: 10px;
  border-radius: 10px;
}
```

```html
<!-- HTML structure for project showcase -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Project Showcase</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="project-showcase"></div>
  <script src="script.js"></script>
</body>
</html>
```
