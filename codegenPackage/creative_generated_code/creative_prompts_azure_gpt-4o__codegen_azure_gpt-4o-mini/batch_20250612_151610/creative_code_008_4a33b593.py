"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Write a JavaScript function to automate the creation of branded infographics for corporate media training sessions, inspired by Cara Productions' training services.
Generated: DETERMINISTIC_4a33b593bb6f521c
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a branded infographic for corporate media training sessions.
 * 
 * @param {Object} options - Configuration options for the infographic.
 * @param {string} options.title - Title of the infographic.
 * @param {string} options.subtitle - Subtitle to provide additional context.
 * @param {Array<string>} options.bulletPoints - Key points to include in the infographic.
 * @param {string} options.brandColor - The primary color for branding.
 * @param {string} options.logoUrl - URL of the brand logo.
 * @returns {HTMLCanvasElement} - The generated infographic as a canvas element.
 * @throws Will throw an error if required options are missing or invalid.
 */
function createBrandedInfographic(options) {
    // Validate input options
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options provided. Please provide a valid options object.');
    }
    const { title, subtitle, bulletPoints, brandColor, logoUrl } = options;

    if (!title || !Array.isArray(bulletPoints) || bulletPoints.length === 0 || !brandColor || !logoUrl) {
        throw new Error('Missing required options: title, bulletPoints, brandColor, and logoUrl must be provided.');
    }

    // Create a canvas element
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');

    // Set canvas dimensions
    canvas.width = 800;
    canvas.height = 600;

    // Draw background
    ctx.fillStyle = brandColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Set text styles
    ctx.font = 'bold 24px Arial';
    ctx.fillStyle = '#FFFFFF'; // White text for contrast
    ctx.textAlign = 'center';

    // Draw title
    ctx.fillText(title, canvas.width / 2, 50);

    // Draw subtitle
    ctx.font = 'italic 18px Arial';
    ctx.fillText(subtitle, canvas.width / 2, 100);

    // Draw bullet points
    ctx.font = '16px Arial';
    ctx.textAlign = 'left';
    const bulletPointYStart = 130; // Starting Y position for bullet points
    bulletPoints.forEach((point, index) => {
        ctx.fillText(`• ${point}`, 50, bulletPointYStart + index * 30);
    });

    // Load and draw logo
    const logoImage = new Image();
    logoImage.src = logoUrl;
    logoImage.onload = () => {
        ctx.drawImage(logoImage, 600, 450, 160, 100); // Position and size of the logo
    };

    return canvas;
}

// Example usage: Create an infographic
try {
    const infographic = createBrandedInfographic({
        title: 'Media Training Best Practices',
        subtitle: 'Elevate Your Media Skills',
        bulletPoints: [
            'Understand your audience',
            'Craft your message',
            'Practice delivery',
            'Receive feedback',
        ],
        brandColor: '#007ACC',
        logoUrl: 'https://example.com/logo.png'
    });

    // Append the infographic to the document body (or any other container)
    document.body.appendChild(infographic);
} catch (error) {
    console.error('Error creating infographic:', error.message);
}
```
