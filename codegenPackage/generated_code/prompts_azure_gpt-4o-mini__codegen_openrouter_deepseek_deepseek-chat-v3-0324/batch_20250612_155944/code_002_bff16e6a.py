"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Create a JavaScript function that dynamically generates a gallery of interior design projects, highlighting the vibrant and flexible spaces described by Linea 7.
Generated: DETERMINISTIC_bff16e6ae58041c4
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a dynamic gallery of interior design projects.
 * @param {Array} projects - Array of project objects containing project details.
 * @param {string} containerId - ID of the DOM element to contain the gallery.
 */
function generateDesignGallery(projects, containerId) {
    // Validate input parameters
    if (!Array.isArray(projects) || projects.length === 0) {
        console.error('Invalid projects array provided');
        return;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container element with ID '${containerId}' not found`);
        return;
    }

    try {
        // Clear existing content
        container.innerHTML = '';

        // Create gallery wrapper
        const galleryWrapper = document.createElement('div');
        galleryWrapper.className = 'design-gallery';

        // Process each project
        projects.forEach((project, index) => {
            // Validate project structure
            if (!project.id || !project.title || !project.images || !Array.isArray(project.images)) {
                console.warn(`Invalid project structure at index ${index}, skipping`);
                return;
            }

            // Create project card
            const projectCard = document.createElement('div');
            projectCard.className = 'project-card';
            projectCard.dataset.projectId = project.id;

            // Create title element
            const titleElement = document.createElement('h3');
            titleElement.className = 'project-title';
            titleElement.textContent = project.title;
            projectCard.appendChild(titleElement);

            // Create description if available
            if (project.description) {
                const descElement = document.createElement('p');
                descElement.className = 'project-description';
                descElement.textContent = project.description;
                projectCard.appendChild(descElement);
            }

            // Create image gallery
            const imageGallery = document.createElement('div');
            imageGallery.className = 'project-images';

            project.images.forEach((image, imgIndex) => {
                if (!image.url || !image.alt) {
                    console.warn(`Invalid image at index ${imgIndex} in project ${project.id}, skipping`);
                    return;
                }

                const imgElement = document.createElement('img');
                imgElement.src = image.url;
                imgElement.alt = image.alt;
                imgElement.className = 'project-image';
                imgElement.loading = 'lazy';

                // Add click handler for larger view if specified
                if (project.enlargeable) {
                    imgElement.style.cursor = 'pointer';
                    imgElement.addEventListener('click', () => showEnlargedImage(image.url, image.alt));
                }

                imageGallery.appendChild(imgElement);
            });

            projectCard.appendChild(imageGallery);
            galleryWrapper.appendChild(projectCard);
        });

        // Add gallery to container
        container.appendChild(galleryWrapper);

        // Add basic styles if not already present
        if (!document.querySelector('style[data-design-gallery]')) {
            const styleElement = document.createElement('style');
            styleElement.dataset.designGallery = true;
            styleElement.textContent = `
                .design-gallery {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                    gap: 20px;
                    padding: 20px;
                }
                .project-card {
                    border: 1px solid #eaeaea;
                    border-radius: 8px;
                    overflow: hidden;
                    transition: transform 0.3s ease;
                }
                .project-card:hover {
                    transform: translateY(-5px);
                }
                .project-title {
                    margin: 15px;
                    color: #333;
                }
                .project-description {
                    margin: 0 15px 15px;
                    color: #666;
                }
                .project-images {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    padding: 0 10px 10px;
                }
                .project-image {
                    max-width: 100%;
                    height: auto;
                    border-radius: 4px;
                }
            `;
            document.head.appendChild(styleElement);
        }
    } catch (error) {
        console.error('Error generating design gallery:', error);
        container.innerHTML = '<p class="error-message">Unable to load gallery. Please try again later.</p>';
    }
}

/**
 * Displays an enlarged version of an image.
 * @param {string} imageUrl - URL of the image to display.
 * @param {string} altText - Alternative text for the image.
 */
function showEnlargedImage(imageUrl, altText) {
    const overlay = document.createElement('div');
    overlay.className = 'image-overlay';
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0,0,0,0.8)';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';
    overlay.style.zIndex = '1000';
    overlay.style.cursor = 'pointer';

    const enlargedImg = document.createElement('img');
    enlargedImg.src = imageUrl;
    enlargedImg.alt = altText;
    enlargedImg.style.maxWidth = '90%';
    enlargedImg.style.maxHeight = '90%';
    enlargedImg.style.objectFit = 'contain';

    overlay.appendChild(enlargedImg);
    document.body.appendChild(overlay);

    overlay.addEventListener('click', () => {
        document.body.removeChild(overlay);
    });
}
```
