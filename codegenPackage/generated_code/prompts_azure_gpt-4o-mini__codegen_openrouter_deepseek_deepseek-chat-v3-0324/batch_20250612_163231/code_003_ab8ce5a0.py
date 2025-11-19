"""
Generated Code Metadata:
========================
Original URL: https://phantomslens.com
Prompt: Create a function to filter and display projects in a portfolio based on categories like music and horror, as seen on PhantomsLens.
Generated: DETERMINISTIC_ab8ce5a09b48ebe1
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Portfolio Project Filter
 * Filters and displays projects based on selected categories.
 * 
 * @param {Array} projects - Array of project objects
 * @param {string} category - Category to filter by (e.g., 'music', 'horror')
 * @returns {Array} Filtered array of projects matching the category
 */
function filterProjects(projects, category) {
    // Validate input parameters
    if (!Array.isArray(projects)) {
        throw new TypeError('Projects must be an array');
    }
    if (typeof category !== 'string') {
        throw new TypeError('Category must be a string');
    }

    // Normalize category to lowercase for case-insensitive comparison
    const normalizedCategory = category.toLowerCase();

    // Filter projects by category
    return projects.filter(project => {
        // Ensure project has categories array
        if (!project.categories || !Array.isArray(project.categories)) {
            return false;
        }

        // Check if project includes the specified category
        return project.categories.some(
            projectCategory => projectCategory.toLowerCase() === normalizedCategory
        );
    });
}

/**
 * Display Projects
 * Renders filtered projects to the DOM.
 * 
 * @param {Array} projects - Array of project objects to display
 * @param {HTMLElement} container - DOM element to render projects into
 */
function displayProjects(projects, container) {
    // Validate input parameters
    if (!Array.isArray(projects)) {
        throw new TypeError('Projects must be an array');
    }
    if (!(container instanceof HTMLElement)) {
        throw new TypeError('Container must be a DOM element');
    }

    // Clear previous content
    container.innerHTML = '';

    // Handle empty results
    if (projects.length === 0) {
        container.innerHTML = '<p>No projects found in this category.</p>';
        return;
    }

    // Create and append project elements
    projects.forEach(project => {
        const projectElement = document.createElement('div');
        projectElement.className = 'project';
        projectElement.innerHTML = `
            <h3>${project.title || 'Untitled Project'}</h3>
            <p>${project.description || ''}</p>
            <div class="categories">
                ${project.categories ? project.categories.map(cat => 
                    `<span class="category-tag">${cat}</span>`
                ).join('') : ''}
            </div>
        `;
        container.appendChild(projectElement);
    });
}

/**
 * Initialize Portfolio Filter
 * Sets up event listeners for category filtering.
 * 
 * @param {Array} projects - Array of all project objects
 * @param {string} containerId - ID of the container element for projects
 * @param {string} filterContainerId - ID of the container for filter buttons
 */
function initPortfolioFilter(projects, containerId, filterContainerId) {
    try {
        // Get DOM elements
        const projectsContainer = document.getElementById(containerId);
        const filterContainer = document.getElementById(filterContainerId);

        // Validate elements exist
        if (!projectsContainer || !filterContainer) {
            throw new Error('Could not find required DOM elements');
        }

        // Display all projects initially
        displayProjects(projects, projectsContainer);

        // Get unique categories from all projects
        const allCategories = projects.reduce((categories, project) => {
            if (project.categories && Array.isArray(project.categories)) {
                project.categories.forEach(category => {
                    if (!categories.includes(category)) {
                        categories.push(category);
                    }
                });
            }
            return categories;
        }, []);

        // Create filter buttons
        allCategories.forEach(category => {
            const button = document.createElement('button');
            button.className = 'filter-btn';
            button.textContent = category;
            button.addEventListener('click', () => {
                const filteredProjects = filterProjects(projects, category);
                displayProjects(filteredProjects, projectsContainer);
            });
            filterContainer.appendChild(button);
        });

        // Add "All" button to reset filter
        const allButton = document.createElement('button');
        allButton.className = 'filter-btn active';
        allButton.textContent = 'All';
        allButton.addEventListener('click', () => {
            displayProjects(projects, projectsContainer);
        });
        filterContainer.prepend(allButton);

    } catch (error) {
        console.error('Error initializing portfolio filter:', error);
    }
}

// Example usage:
// const projects = [
//     {
//         title: 'Horror Film',
//         description: 'A chilling horror experience',
//         categories: ['horror', 'film']
//     },
//     {
//         title: 'Music Video',
//         description: 'An energetic music production',
//         categories: ['music', 'video']
//     }
// ];
// 
// document.addEventListener('DOMContentLoaded', () => {
//     initPortfolioFilter(projects, 'projects-container', 'filter-container');
// });
```
