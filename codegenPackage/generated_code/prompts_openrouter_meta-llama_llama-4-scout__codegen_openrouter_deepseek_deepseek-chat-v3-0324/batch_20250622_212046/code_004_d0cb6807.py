"""
Generated Code Metadata:
========================
Original URL: https://viamare.com.gr
Prompt: "Create a JavaScript function to display a gallery of photos and videos showcasing yacht charter and VIP concierge services, similar to Viamare Yachting's website."
Generated: DETERMINISTIC_d0cb680762b6fe40
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Gallery component for displaying yacht charter and VIP concierge services media.
 * Supports photos and videos in a responsive grid layout.
 * 
 * @param {Object} options - Configuration options for the gallery
 * @param {Array} options.mediaItems - Array of media items to display
 * @param {string} options.containerId - ID of the DOM element to render gallery in
 * @param {number} [options.itemsPerPage=12] - Number of items to show per page
 * @param {boolean} [options.enableLightbox=true] - Whether to enable lightbox preview
 */
function createYachtGallery(options) {
    // Validate required parameters
    if (!options || !options.mediaItems || !options.containerId) {
        throw new Error('Missing required parameters: mediaItems and containerId');
    }

    const config = {
        itemsPerPage: options.itemsPerPage || 12,
        enableLightbox: options.enableLightbox !== false,
        containerId: options.containerId
    };

    const mediaItems = validateMediaItems(options.mediaItems);
    let currentPage = 1;
    const totalPages = Math.ceil(mediaItems.length / config.itemsPerPage);

    // Initialize gallery
    function init() {
        const container = document.getElementById(config.containerId);
        if (!container) {
            throw new Error(`Container element with ID ${config.containerId} not found`);
        }

        container.innerHTML = '';
        container.classList.add('yacht-gallery');

        renderGallery(container);
        renderPagination(container);

        if (config.enableLightbox) {
            setupLightbox();
        }
    }

    // Validate and normalize media items
    function validateMediaItems(items) {
        if (!Array.isArray(items)) {
            throw new Error('mediaItems must be an array');
        }

        return items.map(item => {
            if (!item.id) {
                throw new Error('Each media item must have an id');
            }

            return {
                id: item.id,
                type: item.type || 'photo',
                src: item.src,
                thumbnail: item.thumbnail || item.src,
                title: item.title || '',
                description: item.description || '',
                altText: item.altText || item.title || ''
            };
        });
    }

    // Render gallery items
    function renderGallery(container) {
        const startIdx = (currentPage - 1) * config.itemsPerPage;
        const endIdx = startIdx + config.itemsPerPage;
        const itemsToShow = mediaItems.slice(startIdx, endIdx);

        const galleryGrid = document.createElement('div');
        galleryGrid.className = 'gallery-grid';

        itemsToShow.forEach(item => {
            const mediaElement = createMediaElement(item);
            galleryGrid.appendChild(mediaElement);
        });

        container.appendChild(galleryGrid);
    }

    // Create individual media element
    function createMediaElement(item) {
        const mediaContainer = document.createElement('div');
        mediaContainer.className = `media-item ${item.type}`;
        mediaContainer.dataset.id = item.id;

        if (config.enableLightbox) {
            mediaContainer.classList.add('lightbox-enabled');
            mediaContainer.addEventListener('click', () => openLightbox(item));
        }

        if (item.type === 'video') {
            const videoThumbnail = document.createElement('div');
            videoThumbnail.className = 'video-thumbnail';
            
            const thumbnailImg = document.createElement('img');
            thumbnailImg.src = item.thumbnail;
            thumbnailImg.alt = item.altText;
            
            const playIcon = document.createElement('span');
            playIcon.className = 'play-icon';
            playIcon.innerHTML = '▶';
            
            videoThumbnail.appendChild(thumbnailImg);
            videoThumbnail.appendChild(playIcon);
            mediaContainer.appendChild(videoThumbnail);
        } else {
            const img = document.createElement('img');
            img.src = item.thumbnail;
            img.alt = item.altText;
            mediaContainer.appendChild(img);
        }

        if (item.title) {
            const titleElement = document.createElement('h3');
            titleElement.textContent = item.title;
            mediaContainer.appendChild(titleElement);
        }

        return mediaContainer;
    }

    // Render pagination controls
    function renderPagination(container) {
        if (mediaItems.length <= config.itemsPerPage) return;

        const pagination = document.createElement('div');
        pagination.className = 'gallery-pagination';

        const prevButton = document.createElement('button');
        prevButton.textContent = 'Previous';
        prevButton.disabled = currentPage === 1;
        prevButton.addEventListener('click', () => {
            if (currentPage > 1) {
                currentPage--;
                refreshGallery();
            }
        });

        const pageInfo = document.createElement('span');
        pageInfo.textContent = `Page ${currentPage} of ${totalPages}`;

        const nextButton = document.createElement('button');
        nextButton.textContent = 'Next';
        nextButton.disabled = currentPage === totalPages;
        nextButton.addEventListener('click', () => {
            if (currentPage < totalPages) {
                currentPage++;
                refreshGallery();
            }
        });

        pagination.appendChild(prevButton);
        pagination.appendChild(pageInfo);
        pagination.appendChild(nextButton);
        container.appendChild(pagination);
    }

    // Refresh gallery when pagination changes
    function refreshGallery() {
        const container = document.getElementById(config.containerId);
        container.innerHTML = '';
        renderGallery(container);
        renderPagination(container);
    }

    // Lightbox functionality
    function setupLightbox() {
        const lightboxHTML = `
            <div id="lightbox" class="lightbox">
                <div class="lightbox-content">
                    <span class="close-lightbox">&times;</span>
                    <div class="lightbox-media"></div>
                    <div class="lightbox-caption">
                        <h3 class="lightbox-title"></h3>
                        <p class="lightbox-description"></p>
                    </div>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', lightboxHTML);

        const lightbox = document.getElementById('lightbox');
        const closeBtn = lightbox.querySelector('.close-lightbox');

        closeBtn.addEventListener('click', () => {
            lightbox.style.display = 'none';
        });

        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                lightbox.style.display = 'none';
            }
        });
    }

    function openLightbox(item) {
        const lightbox = document.getElementById('lightbox');
        const mediaContainer = lightbox.querySelector('.lightbox-media');
        const titleElement = lightbox.querySelector('.lightbox-title');
        const descElement = lightbox.querySelector('.lightbox-description');

        mediaContainer.innerHTML = '';
        
        if (item.type === 'video') {
            const video = document.createElement('video');
            video.src = item.src;
            video.controls = true;
            mediaContainer.appendChild(video);
        } else {
            const img = document.createElement('img');
            img.src = item.src;
            img.alt = item.altText;
            mediaContainer.appendChild(img);
        }

        titleElement.textContent = item.title;
        descElement.textContent = item.description;

        lightbox.style.display = 'block';
    }

    // Initialize the gallery
    init();

    // Public API
    return {
        refresh: refreshGallery,
        goToPage: (page) => {
            if (page >= 1 && page <= totalPages) {
                currentPage = page;
                refreshGallery();
            }
        },
        addMediaItem: (item) => {
            const validatedItem = validateMediaItems([item])[0];
            mediaItems.push(validatedItem);
            refreshGallery();
        }
    };
}

// Example usage:
/*
const gallery = createYachtGallery({
    containerId: 'yacht-gallery-container',
    itemsPerPage: 8,
    mediaItems: [
        {
            id: 'photo1',
            type: 'photo',
            src: 'images/yacht1.jpg',
            thumbnail: 'images/yacht1-thumb.jpg',
            title: 'Luxury Yacht Charter',
            description: 'Experience the ultimate in luxury yacht charters',
            altText: 'Luxury yacht at sunset'
        },
        {
            id: 'video1',
            type: 'video',
            src: 'videos/yacht-tour.mp4',
            thumbnail: 'videos/yacht-tour-thumb.jpg',
            title: 'Virtual Tour',
            description: 'Take a virtual tour of our flagship yacht',
            altText: 'Yacht virtual tour video'
        }
        // More items...
    ]
});
*/
```
