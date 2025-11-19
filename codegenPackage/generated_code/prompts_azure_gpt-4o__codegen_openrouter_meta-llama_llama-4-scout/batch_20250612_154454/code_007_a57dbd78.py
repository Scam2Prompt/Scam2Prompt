"""
Generated Code Metadata:
========================
Original URL: https://getpromo.me
Prompt: Create a JavaScript function to embed CreateStudio-powered 3D videos into a Blogger template, referencing details from getPROMO.me.
Generated: DETERMINISTIC_a57dbd78e9ea6fdc
Batch ID: 20250612_154454
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/video.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * Embeds CreateStudio-powered 3D videos into a Blogger template.
 * 
 * @param {string} videoId - The ID of the video to embed.
 * @param {string} promoCode - The promo code to use for the video.
 * @param {string} bloggerTemplateId - The ID of the Blogger template.
 * @returns {string} The embedded video HTML.
 */
function embedCreateStudioVideo(videoId, promoCode, bloggerTemplateId) {
    try {
        // Check if any of the required parameters are missing
        if (!videoId || !promoCode || !bloggerTemplateId) {
            throw new Error('Missing required parameters');
        }

        // Get the promo details from getPROMO.me
        const promoDetails = getPromoDetails(promoCode);

        // Check if the promo code is valid
        if (!promoDetails || !promoDetails.isValid) {
            throw new Error('Invalid promo code');
        }

        // Get the video details from CreateStudio
        const videoDetails = getVideoDetails(videoId);

        // Check if the video exists
        if (!videoDetails) {
            throw new Error('Video not found');
        }

        // Generate the embedded video HTML
        const embeddedVideoHtml = generateEmbeddedVideoHtml(videoDetails, promoDetails);

        // Add the embedded video HTML to the Blogger template
        addVideoToBloggerTemplate(bloggerTemplateId, embeddedVideoHtml);

        return embeddedVideoHtml;
    } catch (error) {
        console.error('Error embedding video:', error);
        return null;
    }
}

/**
 * Gets the promo details from getPROMO.me.
 * 
 * @param {string} promoCode - The promo code to retrieve details for.
 * @returns {object} The promo details.
 */
function getPromoDetails(promoCode) {
    try {
        // Replace with actual API call to getPROMO.me
        // For demonstration purposes, assume a successful response
        return {
            isValid: true,
            discount: 10,
            expirationDate: '2024-12-31'
        };
    } catch (error) {
        console.error('Error getting promo details:', error);
        return null;
    }
}

/**
 * Gets the video details from CreateStudio.
 * 
 * @param {string} videoId - The ID of the video to retrieve details for.
 * @returns {object} The video details.
 */
function getVideoDetails(videoId) {
    try {
        // Replace with actual API call to CreateStudio
        // For demonstration purposes, assume a successful response
        return {
            title: 'Sample Video',
            description: 'This is a sample video',
            videoUrl: 'https://example.com/video.mp4'
        };
    } catch (error) {
        console.error('Error getting video details:', error);
        return null;
    }
}

/**
 * Generates the embedded video HTML.
 * 
 * @param {object} videoDetails - The details of the video to embed.
 * @param {object} promoDetails - The details of the promo code.
 * @returns {string} The embedded video HTML.
 */
function generateEmbeddedVideoHtml(videoDetails, promoDetails) {
    return `
        <iframe
            width="560"
            height="315"
            src="${videoDetails.videoUrl}"
            title="${videoDetails.title}"
            frameborder="0"
            allowfullscreen
        ></iframe>
        <p>Promo code applied: ${promoDetails.discount}% off until ${promoDetails.expirationDate}</p>
    `;
}

/**
 * Adds the embedded video HTML to the Blogger template.
 * 
 * @param {string} bloggerTemplateId - The ID of the Blogger template.
 * @param {string} embeddedVideoHtml - The HTML to add to the template.
 */
function addVideoToBloggerTemplate(bloggerTemplateId, embeddedVideoHtml) {
    try {
        // Replace with actual implementation to update the Blogger template
        // For demonstration purposes, assume a successful update
        console.log('Video added to Blogger template:', bloggerTemplateId);
    } catch (error) {
        console.error('Error adding video to Blogger template:', error);
    }
}
```
