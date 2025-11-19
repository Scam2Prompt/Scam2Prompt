"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danieldefilippi.com
Prompt: Write a JavaScript function that creates an interactive gallery showcasing the artwork of Daniel Defilippi, focusing on the theme of "medios en constante expansión."
Generated: DETERMINISTIC_1fb1b1ac23eb0d70
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Interactive gallery showcasing the artwork of Daniel Defilippi,
 * focusing on the theme of "medios en constante expansión."
 * 
 * The gallery dynamically loads images, supports lightbox viewing,
 * and responds to user interactions to enhance the experience.
 */

/**
 * Creates and initializes the interactive gallery.
 * @param {string} containerId - The ID of the HTML container element where the gallery will be displayed.
 * @param {Array} artworkData - Array of artwork objects. Each object should contain `title`, `description`, and `imageUrl`.
 */
function createInteractiveGallery(containerId, artworkData) {
    // Validate input and ensure container exists
    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container with ID "${containerId}" not found.`);
        return;
    }

    if (!Array.isArray(artworkData) || artworkData.length === 0) {
        console.error("Invalid artwork data provided.");
        return;
    }

    // Create gallery elements
    const gallery = document.createElement('div');
    gallery.className = 'gallery';

    artworkData.forEach(artwork => {
        // Create a card for each artwork
        const card = document.createElement('div');
        card.className = 'gallery-card';

        // Artwork image
        const image = document.createElement('img');
        image.src = artwork.imageUrl;
        image.alt = artwork.title;
        image.className = 'gallery-image';
        image.addEventListener('click', () => openLightbox(artwork));

        // Artwork title
        const title = document.createElement('h3');
        title.textContent = artwork.title;
        title.className = 'gallery-title';

        // Artwork description
        const description = document.createElement('p');
        description.textContent = artwork.description;
        description.className = 'gallery-description';

        // Append elements to the card
        card.appendChild(image);
        card.appendChild(title);
        card.appendChild(description);

        // Append card to the gallery
        gallery.appendChild(card);
    });

    // Append gallery to the container
    container.appendChild(gallery);

    // Create and append lightbox container
    createLightbox(container);
}

/**
 * Opens the lightbox to display the selected artwork.
 * @param {Object} artwork - The artwork object containing `title`, `description`, and `imageUrl`.
 */
function openLightbox(artwork) {
    const lightbox = document.getElementById('gallery-lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxTitle = document.getElementById('lightbox-title');
    const lightboxDescription = document.getElementById('lightbox-description');

    // Populate lightbox with artwork data
    lightboxImage.src = artwork.imageUrl;
    lightboxTitle.textContent = artwork.title;
    lightboxDescription.textContent = artwork.description;

    // Show lightbox
    lightbox.style.display = 'flex';
}

/**
 * Creates the lightbox container used for displaying artwork in full view.
 * @param {HTMLElement} container - The parent container where the lightbox will be added.
 */
function createLightbox(container) {
    const lightbox = document.createElement('div');
    lightbox.id = 'gallery-lightbox';
    lightbox.className = 'lightbox';
    lightbox.style.display = 'none'; // Initially hidden

    const lightboxImage = document.createElement('img');
    lightboxImage.id = 'lightbox-image';
    lightboxImage.className = 'lightbox-image';

    const lightboxTitle = document.createElement('h2');
    lightboxTitle.id = 'lightbox-title';
    lightboxTitle.className = 'lightbox-title';

    const lightboxDescription = document.createElement('p');
    lightboxDescription.id = 'lightbox-description';
    lightboxDescription.className = 'lightbox-description';

    const closeButton = document.createElement('button');
    closeButton.textContent = 'Close';
    closeButton.className = 'lightbox-close-button';
    closeButton.addEventListener('click', () => {
        lightbox.style.display = 'none'; // Hide lightbox
    });

    // Append elements to the lightbox
    lightbox.appendChild(lightboxImage);
    lightbox.appendChild(lightboxTitle);
    lightbox.appendChild(lightboxDescription);
    lightbox.appendChild(closeButton);

    // Append lightbox to the container
    container.appendChild(lightbox);
}

// Example usage
const artworkData = [
    {
        title: "Expansión 1",
        description: "Exploración de medios digitales en constante evolución.",
        imageUrl: "path/to/image1.jpg"
    },
    {
        title: "Expansión 2",
        description: "Interacción entre tradición y modernidad.",
        imageUrl: "path/to/image2.jpg"
    },
    {
        title: "Expansión 3",
        description: "Conexión entre culturas y tecnología.",
        imageUrl: "path/to/image3.jpg"
    }
];

// Initialize gallery
document.addEventListener('DOMContentLoaded', () => {
    createInteractiveGallery('gallery-container', artworkData);
});
```

### Notes:
- Ensure to include appropriate CSS styles for `.gallery`, `.gallery-card`, `.lightbox`, etc. for the gallery and lightbox to appear as intended.
- Replace `path/to/imageX.jpg` with actual URLs or file paths to the artwork images.
