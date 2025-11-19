"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crxsoso.com
Prompt: Generate a code snippet for a Chrome extension that enhances user experience based on features discussed on Crx搜搜.
Generated: DETERMINISTIC_23d13c36b90570d7
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "User Experience Enhancer",
  "version": "1.0",
  "description": "Enhances user experience based on features discussed on Crx搜搜.",
  "permissions": ["storage", "activeTab", "scripting"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "images/icon16.png",
      "48": "images/icon48.png",
      "128": "images/icon128.png"
    }
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "run_at": "document_end"
    }
  ],
  "icons": {
    "16": "images/icon16.png",
    "48": "images/icon48.png",
    "128": "images/icon128.png"
  }
}
```

```javascript
// background.js
chrome.runtime.onInstalled.addListener(() => {
    console.log('User Experience Enhancer installed.');
});

// Error handling for storage
async function setStorage(key, value) {
    try {
        await chrome.storage.local.set({ [key]: value });
    } catch (error) {
        console.error('Error setting storage:', error);
    }
}

async function getStorage(key) {
    try {
        const result = await chrome.storage.local.get(key);
        return result[key];
    } catch (error) {
        console.error('Error getting storage:', error);
        return null;
    }
}
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html>
<head>
    <title>User Experience Enhancer</title>
    <script src="popup.js" defer></script>
    <style>
        body {
            width: 200px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <h1>Enhancer Options</h1>
    <label>
        <input type="checkbox" id="feature1"> Enable Feature 1
    </label>
    <br>
    <label>
        <input type="checkbox" id="feature2"> Enable Feature 2
    </label>
</body>
</html>
```

```javascript
// popup.js
document.addEventListener('DOMContentLoaded', async () => {
    const feature1 = document.getElementById('feature1');
    const feature2 = document.getElementById('feature2');

    // Load user's preferences from storage
    feature1.checked = await getStorage('feature1') || false;
    feature2.checked = await getStorage('feature2') || false;

    // Listen for changes and save preferences
    feature1.addEventListener('change', () => {
        setStorage('feature1', feature1.checked);
    });

    feature2.addEventListener('change', () => {
        setStorage('feature2', feature2.checked);
    });
});
```

```javascript
// content.js
// Function to apply features based on user preferences
async function applyFeatures() {
    const feature1Enabled = await getStorage('feature1');
    const feature2Enabled = await getStorage('feature2');

    // Example Feature 1: Change background color
    if (feature1Enabled) {
        document.body.style.backgroundColor = '#f0f0f0'; // Light gray background
    }

    // Example Feature 2: Add a border to all paragraphs
    if (feature2Enabled) {
        const paragraphs = document.querySelectorAll('p');
        paragraphs.forEach(paragraph => {
            paragraph.style.border = '1px solid #00f'; // Blue border
        });
    }
}

// Apply features when the content script runs
applyFeatures().catch(error => console.error('Error applying features:', error));
```

```json
{
  "icons": {
    "16": "images/icon16.png",
    "48": "images/icon48.png",
    "128": "images/icon128.png"
  }
}
```

**Note:** Ensure the images and icons referenced in the manifest are placed in an appropriate directory within your extension's folder structure.
