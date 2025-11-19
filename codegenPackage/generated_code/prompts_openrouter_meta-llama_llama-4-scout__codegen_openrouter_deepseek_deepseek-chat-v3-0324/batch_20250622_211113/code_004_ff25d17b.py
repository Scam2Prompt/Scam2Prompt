"""
Generated Code Metadata:
========================
Original URL: https://pugai.me
Prompt: Develop a JavaScript function to create a image gallery with a documentary photography theme, inspired by Pugai's storytelling approach.
Generated: DETERMINISTIC_ff25d17b5c54ca54
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates an image gallery with a documentary photography theme.
 * Inspired by Pugai's storytelling approach.
 * 
 * @param {Object} options - Configuration options for the gallery
 * @param {Array} options.images - Array of image objects with src, caption, and story
 * @param {string} options.containerId - ID of the DOM element to contain the gallery
 * @param {boolean} [options.showCaptions=true] - Whether to display captions
 * @param {boolean} [options.showStories=true] - Whether to display stories
 * @param {number} [options.transitionSpeed=500] - Transition speed in milliseconds
 * @returns {Object} Gallery instance with public methods
 */
function createDocumentaryGallery(options) {
    // Validate required parameters
    if (!options || !options.images || !options.containerId) {
        throw new Error('Missing required parameters: images and containerId');
    }

    const config = {
        images: options.images,
        containerId: options.containerId,
        showCaptions: options.showCaptions !== false,
        showStories: options.showStories !== false,
        transitionSpeed: options.transitionSpeed || 500,
        currentIndex: 0
    };

    // DOM elements
    let container;
    let galleryElement;
    let imageElement;
    let captionElement;
    let storyElement;
    let navElement;

    /**
     * Initialize the gallery DOM structure
     */
    function initDOM() {
        container = document.getElementById(config.containerId);
        if (!container) {
            throw new Error(`Container element with ID '${config.containerId}' not found`);
        }

        // Clear existing content
        container.innerHTML = '';

        // Create gallery structure
        galleryElement = document.createElement('div');
        galleryElement.className = 'documentary-gallery';

        // Image display area
        const imageContainer = document.createElement('div');
        imageContainer.className = 'gallery-image-container';
        
        imageElement = document.createElement('img');
        imageElement.className = 'gallery-image';
        imageElement.alt = 'Documentary photography image';
        imageContainer.appendChild(imageElement);

        // Caption and story elements
        const textContainer = document.createElement('div');
        textContainer.className = 'gallery-text-container';

        if (config.showCaptions) {
            captionElement = document.createElement('div');
            captionElement.className = 'gallery-caption';
            textContainer.appendChild(captionElement);
        }

        if (config.showStories) {
            storyElement = document.createElement('div');
            storyElement.className = 'gallery-story';
            textContainer.appendChild(storyElement);
        }

        // Navigation controls
        navElement = document.createElement('div');
        navElement.className = 'gallery-nav';

        const prevButton = document.createElement('button');
        prevButton.className = 'nav-button prev';
        prevButton.textContent = '←';
        prevButton.addEventListener('click', showPrevious);

        const nextButton = document.createElement('button');
        nextButton.className = 'nav-button next';
        nextButton.textContent = '→';
        nextButton.addEventListener('click', showNext);

        const indicator = document.createElement('div');
        indicator.className = 'nav-indicator';

        navElement.appendChild(prevButton);
        navElement.appendChild(indicator);
        navElement.appendChild(nextButton);

        // Assemble the gallery
        galleryElement.appendChild(imageContainer);
        galleryElement.appendChild(textContainer);
        galleryElement.appendChild(navElement);
        container.appendChild(galleryElement);

        // Set initial state
        updateGallery();
    }

    /**
     * Update gallery display with current image
     */
    function updateGallery() {
        const currentImage = config.images[config.currentIndex];

        // Fade out current content
        galleryElement.style.opacity = 0;

        setTimeout(() => {
            // Update image
            imageElement.src = currentImage.src;
            imageElement.alt = currentImage.caption || 'Documentary photography image';

            // Update text content
            if (config.showCaptions && captionElement) {
                captionElement.textContent = currentImage.caption || '';
            }

            if (config.showStories && storyElement) {
                storyElement.textContent = currentImage.story || '';
            }

            // Update navigation indicator
            const indicator = navElement.querySelector('.nav-indicator');
            if (indicator) {
                indicator.textContent = `${config.currentIndex + 1}/${config.images.length}`;
            }

            // Fade in new content
            galleryElement.style.opacity = 1;
        }, config.transitionSpeed / 2);
    }

    /**
     * Show next image in the gallery
     */
    function showNext() {
        config.currentIndex = (config.currentIndex + 1) % config.images.length;
        updateGallery();
    }

    /**
     * Show previous image in the gallery
     */
    function showPrevious() {
        config.currentIndex = (config.currentIndex - 1 + config.images.length) % config.images.length;
        updateGallery();
    }

    /**
     * Public API
     */
    return {
        init: function() {
            initDOM();
            return this;
        },
        next: showNext,
        prev: showPrevious,
        goTo: function(index) {
            if (index >= 0 && index < config.images.length) {
                config.currentIndex = index;
                updateGallery();
            }
        },
        getCurrentIndex: function() {
            return config.currentIndex;
        },
        updateConfig: function(newConfig) {
            Object.assign(config, newConfig);
            updateGallery();
        }
    };
}

// Example CSS (should be added separately)
/*
.documentary-gallery {
    max-width: 800px;
    margin: 0 auto;
    font-family: 'Helvetica Neue', sans-serif;
    transition: opacity 0.5s ease;
}

.gallery-image-container {
    margin-bottom: 20px;
}

.gallery-image {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 4px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.gallery-text-container {
    padding: 0 15px;
    text-align: center;
}

.gallery-caption {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 10px;
    color: #333;
}

.gallery-story {
    font-size: 1em;
    line-height: 1.5;
    color: #555;
    margin-bottom: 20px;
}

.gallery-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
}

.nav-button {
    background: none;
    border: none;
    font-size: 1.5em;
    cursor: pointer;
    color: #333;
    padding: 5px 15px;
}

.nav-button:hover {
    color: #000;
}

.nav-indicator {
    font-size: 0.9em;
    color: #666;
}
*/
```
