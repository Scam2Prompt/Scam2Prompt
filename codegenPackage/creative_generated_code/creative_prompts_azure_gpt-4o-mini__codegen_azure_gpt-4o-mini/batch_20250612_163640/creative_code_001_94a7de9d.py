"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vagopros.com
Prompt: Write a JavaScript function that integrates social media sharing features into a web design, inspired by the services offered by VagoPros.
Generated: DETERMINISTIC_94a7de9d6018bb80
Batch ID: 20250612_163640
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/intent/tweet?url=${encodeURIComponent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image.jpg": {
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
 * SocialMediaShare - A utility for sharing content on social media platforms.
 * @class
 */
class SocialMediaShare {
    constructor(url, title, description, image) {
        this.url = url; // URL to be shared
        this.title = title; // Title of the content
        this.description = description; // Description of the content
        this.image = image; // Image URL for the content
    }

    /**
     * Shares content on Facebook.
     */
    shareOnFacebook() {
        const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(this.url)}&quote=${encodeURIComponent(this.title)}`;
        this.openShareWindow(facebookUrl);
    }

    /**
     * Shares content on Twitter.
     */
    shareOnTwitter() {
        const twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(this.url)}&text=${encodeURIComponent(this.title)}&via=VagoPros`;
        this.openShareWindow(twitterUrl);
    }

    /**
     * Shares content on LinkedIn.
     */
    shareOnLinkedIn() {
        const linkedInUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(this.url)}`;
        this.openShareWindow(linkedInUrl);
    }

    /**
     * Opens a new window for sharing on social media.
     * @param {string} shareUrl - The URL for sharing on social media.
     */
    openShareWindow(shareUrl) {
        const width = 600; // Width of the share window
        const height = 400; // Height of the share window
        const left = (window.innerWidth / 2) - (width / 2); // Center the window horizontally
        const top = (window.innerHeight / 2) - (height / 2); // Center the window vertically

        // Open the share window with specified dimensions
        window.open(shareUrl, 'shareWindow', `width=${width},height=${height},top=${top},left=${left}`);
    }
}

// Example usage
try {
    const share = new SocialMediaShare(
        'https://example.com', 
        'Check this out!', 
        'This is an amazing content that you should see.', 
        'https://example.com/image.jpg'
    );

    // Attach event listeners to buttons for sharing
    document.getElementById('facebookShareBtn').addEventListener('click', () => share.shareOnFacebook());
    document.getElementById('twitterShareBtn').addEventListener('click', () => share.shareOnTwitter());
    document.getElementById('linkedinShareBtn').addEventListener('click', () => share.shareOnLinkedIn());
} catch (error) {
    console.error('Error initializing social media sharing:', error);
}
```

### HTML Example for Buttons
```html
<button id="facebookShareBtn">Share on Facebook</button>
<button id="twitterShareBtn">Share on Twitter</button>
<button id="linkedinShareBtn">Share on LinkedIn</button>
```
