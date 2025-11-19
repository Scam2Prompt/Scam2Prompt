"""
Generated Code Metadata:
========================
Original URL: https://polymarket.gitbook.io
Prompt: Write a function to dynamically update images and media in GitBook documentation, utilizing the capabilities outlined in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_1f27b379ca9aee1f
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamically updates images and media in GitBook documentation.
 * Utilizes the Polymarket GitBook starter template capabilities.
 * 
 * @param {string} elementId - The ID of the element to update.
 * @param {string} newMediaUrl - The new URL of the media to display.
 * @param {string} [mediaType='image'] - Type of media ('image', 'video', 'iframe').
 * @throws {Error} If element is not found or URL is invalid.
 */
function updateGitBookMedia(elementId, newMediaUrl, mediaType = 'image') {
    // Validate inputs
    if (!elementId || !newMediaUrl) {
        throw new Error('Element ID and media URL are required');
    }

    const element = document.getElementById(elementId);
    if (!element) {
        throw new Error(`Element with ID ${elementId} not found`);
    }

    // Validate URL
    try {
        new URL(newMediaUrl);
    } catch (e) {
        throw new Error('Invalid media URL');
    }

    // Update media based on type
    switch (mediaType.toLowerCase()) {
        case 'image':
            if (element.tagName === 'IMG') {
                element.src = newMediaUrl;
                element.alt = `Updated image: ${newMediaUrl.split('/').pop()}`;
            } else {
                throw new Error('Element is not an image tag');
            }
            break;
            
        case 'video':
            if (element.tagName === 'VIDEO') {
                element.src = newMediaUrl;
                const source = element.querySelector('source');
                if (source) {
                    source.src = newMediaUrl;
                }
            } else {
                throw new Error('Element is not a video tag');
            }
            break;
            
        case 'iframe':
            if (element.tagName === 'IFRAME') {
                element.src = newMediaUrl;
            } else {
                throw new Error('Element is not an iframe tag');
            }
            break;
            
        default:
            throw new Error(`Unsupported media type: ${mediaType}`);
    }

    // Dispatch custom event for GitBook integration
    const event = new CustomEvent('gitbook:media:updated', {
        detail: {
            elementId,
            mediaUrl: newMediaUrl,
            mediaType
        }
    });
    document.dispatchEvent(event);
}

/**
 * Helper function to safely update media with error handling.
 * 
 * @param {string} elementId - The ID of the element to update.
 * @param {string} newMediaUrl - The new URL of the media to display.
 * @param {string} [mediaType='image'] - Type of media ('image', 'video', 'iframe').
 * @returns {boolean} True if update was successful, false otherwise.
 */
function safeUpdateGitBookMedia(elementId, newMediaUrl, mediaType = 'image') {
    try {
        updateGitBookMedia(elementId, newMediaUrl, mediaType);
        return true;
    } catch (error) {
        console.error('Failed to update GitBook media:', error.message);
        return false;
    }
}

// Export functions for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        updateGitBookMedia,
        safeUpdateGitBookMedia
    };
}
```
