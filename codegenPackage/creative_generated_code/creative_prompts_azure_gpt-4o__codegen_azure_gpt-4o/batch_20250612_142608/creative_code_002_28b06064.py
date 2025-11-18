"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Recommend libraries or APIs for embedding interactive media blocks into a GitBook documentation site, as described in the Polymarket GitBook template.
Generated: DETERMINISTIC_28b06064a0df482c
Batch ID: 20250612_142608
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://codepen.io/your-username/pen/your-pen-id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/interactive-media": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.youtube.com/embed/${videoId}`;": {
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
 * This script demonstrates how to embed interactive media blocks into a GitBook documentation site
 * using HTML, JavaScript, and popular libraries/APIs such as YouTube iframe API, CodePen embeds, or external media services.
 * 
 * Note: Make sure this is integrated with your GitBook theme and deployed properly.
 */

// Import third-party libraries or APIs if necessary.
// For GitBook documentation, ensure these libraries are compatible with your deployment environment.

// Example: Embed interactive YouTube video
function embedYouTubeVideo(containerId, videoId) {
    try {
        const container = document.getElementById(containerId);
        if (!container) throw new Error("Container not found");

        const iframe = document.createElement('iframe');
        iframe.src = `https://www.youtube.com/embed/${videoId}`;
        iframe.width = '560';
        iframe.height = '315';
        iframe.frameBorder = '0';
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        iframe.allowFullscreen = true;

        container.appendChild(iframe);
    } catch (error) {
        console.error("Failed to embed YouTube video:", error);
    }
}

// Example: Embed CodePen project
function embedCodePen(containerId, penUrl) {
    try {
        const container = document.getElementById(containerId);
        if (!container) throw new Error("Container not found");

        const iframe = document.createElement('iframe');
        iframe.src = `${penUrl}/embed/preview/`;
        iframe.width = '100%';
        iframe.height = '400';
        iframe.frameBorder = '0';
        iframe.scrolling = 'no';
        iframe.allowFullscreen = true;

        container.appendChild(iframe);
    } catch (error) {
        console.error("Failed to embed CodePen project:", error);
    }
}

// Example: Embed external interactive media (e.g., custom iframe or HTML block)
function embedCustomIframe(containerId, iframeSrc, width = '100%', height = '400px') {
    try {
        const container = document.getElementById(containerId);
        if (!container) throw new Error("Container not found");

        const iframe = document.createElement('iframe');
        iframe.src = iframeSrc;
        iframe.width = width;
        iframe.height = height;
        iframe.frameBorder = '0';
        iframe.allowFullscreen = true;

        container.appendChild(iframe);
    } catch (error) {
        console.error("Failed to embed custom iframe:", error);
    }
}

// Usage Examples
document.addEventListener("DOMContentLoaded", () => {
    // Embed a YouTube video
    embedYouTubeVideo('youtube-container', 'dQw4w9WgXcQ'); // Replace with your video ID

    // Embed a CodePen project
    embedCodePen('codepen-container', 'https://codepen.io/your-username/pen/your-pen-id'); // Replace with your CodePen URL

    // Embed a custom iframe (e.g., external interactive media or application)
    embedCustomIframe('custom-container', 'https://example.com/interactive-media'); // Replace with your iframe source URL
});
```

```html
<!-- Include the following HTML structure in your GitBook content -->
<div id="youtube-container"></div>
<div id="codepen-container"></div>
<div id="custom-container"></div>

<!-- Ensure these divs exist in your GitBook content structure for proper embedding -->
```

```json
{
  "dependencies": {
    "GitBook": {
      "version": "^3.0.0"
    }
  }
}
```

Ensure that the hosting environment supports JavaScript execution, and serve the content securely using HTTPS for external media sources.
