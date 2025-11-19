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
// Architectural Projects Showcase App
class ArchitecturalProjectsApp {
  constructor() {
    this.projects = [];
    this.currentProjectIndex = 0;
    this.init();
  }

  // Initialize the app
  init() {
    this.fetchProjects();
    this.setupEventListeners();
    this.renderNavigation();
  }

  // Fetch projects from API or local data
  async fetchProjects() {
    try {
      // In a real app, this would be an API call
      // For demo purposes, we're using mock data
      this.projects = [
        {
          id: 1,
          title: "Urban Oasis",
          architect: "Studio A",
          year: 2023,
          description: "A sustainable residential complex blending urban living with green spaces.",
          images: ["project1-1.jpg", "project1-2.jpg", "project1-3.jpg"],
          location: "Berlin, Germany"
        },
        {
          id: 2,
          title: "The Glass Pavilion",
          architect: "Atelier B",
          year: 2022,
          description: "A transparent exhibition space that changes with natural light.",
          images: ["project2-1.jpg", "project2-2.jpg"],
          location: "Tokyo, Japan"
        },
        {
          id: 3,
          title: "Mountain Retreat",
          architect: "Design Collective C",
          year: 2021,
          description: "A minimalist cabin integrated into the alpine landscape.",
          images: ["project3-1.jpg", "project3-2.jpg", "project3-3.jpg"],
          location: "Swiss Alps"
        }
      ];

      this.renderProject();
    } catch (error) {
      console.error("Error fetching projects:", error);
      this.showError("Failed to load projects. Please try again later.");
    }
  }

  // Render current project
  renderProject() {
    if (!this.projects.length) return;

    const project = this.projects[this.currentProjectIndex];
    const projectContainer = document.getElementById('project-container');
    
    projectContainer.innerHTML = `
      <div class="project-header">
        <h1>${project.title}</h1>
        <div class="project-meta">
          <span>${project.architect}</span>
          <span>${project.year}</span>
          <span>${project.location}</span>
        </div>
      </div>
      <div class="project-gallery">
        ${project.images.map(img => `<img src="assets/${img}" alt="${project.title}">`).join('')}
      </div>
      <div class="project-description">
        <p>${project.description}</p>
      </div>
    `;
  }

  // Render navigation dots
  renderNavigation() {
    const navContainer = document.getElementById('project-nav');
    navContainer.innerHTML = this.projects
      .map((_, index) => 
        `<button class="nav-dot ${index === this.currentProjectIndex ? 'active' : ''}" 
                data-index="${index}"></button>`
      )
      .join('');
  }

  // Setup event listeners
  setupEventListeners() {
    // Navigation dots
    document.getElementById('project-nav').addEventListener('click', (e) => {
      if (e.target.classList.contains('nav-dot')) {
        this.currentProjectIndex = parseInt(e.target.dataset.index);
        this.renderProject();
        this.renderNavigation();
      }
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        this.navigate(-1);
      } else if (e.key === 'ArrowRight') {
        this.navigate(1);
      }
    });

    // Touch events for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    document.getElementById('project-container').addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, false);

    document.getElementById('project-container').addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      this.handleSwipe();
    }, false);
  }

  // Handle swipe gestures
  handleSwipe() {
    const threshold = 50;
    if (touchEndX < touchStartX - threshold) {
      this.navigate(1); // Swipe left
    } else if (touchEndX > touchStartX + threshold) {
      this.navigate(-1); // Swipe right
    }
  }

  // Navigate between projects
  navigate(direction) {
    this.currentProjectIndex += direction;
    
    // Wrap around
    if (this.currentProjectIndex < 0) {
      this.currentProjectIndex = this.projects.length - 1;
    } else if (this.currentProjectIndex >= this.projects.length) {
      this.currentProjectIndex = 0;
    }
    
    this.renderProject();
    this.renderNavigation();
  }

  // Show error message
  showError(message) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    document.getElementById('app').appendChild(errorElement);
  }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new ArchitecturalProjectsApp();
});
```
