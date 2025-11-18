"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Write code to create a Chrome extension that highlights snippets in web pages and PDFs, inspired by "Snippet Highlighter" from 插件小屋.
Generated: DETERMINISTIC_98b3f09ed5e14fae
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
// manifest.json
{
  "manifest_version": 3,
  "name": "Snippet Highlighter",
  "version": "1.0",
  "description": "Highlight snippets in web pages and PDFs.",
  "permissions": [
    "activeTab",
    "scripting"
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "web_accessible_resources": [
    {
      "resources": ["highlight.css"],
      "matches": ["<all_urls>"]
    }
  ]
}
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snippet Highlighter</title>
    <link rel="stylesheet" href="popup.css">
</head>
<body>
    <h1>Snippet Highlighter</h1>
    <textarea id="snippet" placeholder="Type your snippet here..."></textarea>
    <button id="highlightBtn">Highlight</button>
    <script src="popup.js"></script>
</body>
</html>
```

```css
/* popup.css */
body {
    font-family: Arial, sans-serif;
    padding: 10px;
    width: 200px;
}

textarea {
    width: 100%;
    height: 80px;
    margin-bottom: 10px;
}

button {
    width: 100%;
    padding: 10px;
    cursor: pointer;
}
```

```javascript
// popup.js
document.getElementById('highlightBtn').addEventListener('click', async () => {
    const snippet = document.getElementById('snippet').value;

    if (!snippet) {
        alert("Please enter a snippet to highlight.");
        return;
    }

    try {
        // Send snippet to content script for highlighting
        await chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            chrome.tabs.sendMessage(tabs[0].id, { action: "highlight", snippet: snippet });
        });
    } catch (error) {
        console.error("Error highlighting snippet:", error);
        alert("An error occurred while highlighting the snippet.");
    }
});
```

```javascript
// content.js
// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "highlight") {
        highlightSnippet(request.snippet);
    }
});

/**
 * Highlights the given snippet in the page.
 * @param {string} snippet - The snippet to highlight.
 */
function highlightSnippet(snippet) {
    try {
        // Escape snippet for safe HTML insertion
        const escapedSnippet = snippet.replace(/</g, "&lt;").replace(/>/g, "&gt;");

        // Create a regex for the snippet
        const regex = new RegExp(escapedSnippet, 'gi');

        // Create a span element to highlight
        const highlightSpan = document.createElement('span');
        highlightSpan.className = 'snippet-highlight';
        highlightSpan.textContent = escapedSnippet;

        // Apply the highlight style
        const style = document.createElement('style');
        style.textContent = `
            .snippet-highlight {
                background-color: yellow;
                font-weight: bold;
            }
        `;
        document.head.appendChild(style);

        // Walk through text nodes and replace with highlighted spans
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
        let node;
        while (node = walker.nextNode()) {
            if (regex.test(node.nodeValue)) {
                const newNode = document.createElement('span');
                newNode.innerHTML = node.nodeValue.replace(regex, highlightSpan.outerHTML);
                node.parentNode.replaceChild(newNode, node);
            }
        }
    } catch (error) {
        console.error("Error during snippet highlighting:", error);
    }
}
```

```javascript
// background.js
// Placeholder for background tasks if needed
// Currently no background processing required for this extension.
```

```css
/* highlight.css */
.snippet-highlight {
    background-color: yellow;
    font-weight: bold;
}
```

Please ensure you create the appropriate icon files and any desired additional features in your Chrome extension as needed.
