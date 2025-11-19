"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Write code to create a Chrome extension that highlights snippets in web pages and PDFs, inspired by "Snippet Highlighter" from 插件小屋.
Generated: DETERMINISTIC_98b3f09ed5e14fae
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Snippet Highlighter",
  "version": "1.0",
  "description": "Highlight text snippets on web pages and PDFs",
  "permissions": ["activeTab", "scripting", "storage"],
  "host_permissions": ["<all_urls>"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "css": ["highlight.css"]
    }
  ]
}

// background.js
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ highlights: [] });
});

// content.js
document.addEventListener('mouseup', handleTextSelection);

function handleTextSelection() {
  const selection = window.getSelection();
  if (!selection || selection.toString().trim() === '') return;

  const range = selection.getRangeAt(0);
  const selectedText = selection.toString();
  
  if (isValidSelection(range)) {
    highlightSelection(range, selectedText);
  }
}

function isValidSelection(range) {
  return range && !range.collapsed;
}

function highlightSelection(range, text) {
  const span = document.createElement('span');
  span.className = 'snippet-highlight';
  span.dataset.text = text;
  span.style.backgroundColor = 'rgba(255, 255, 0, 0.5)';
  
  range.surroundContents(span);
  saveHighlight(span, text);
}

function saveHighlight(element, text) {
  const rect = element.getBoundingClientRect();
  const highlight = {
    text: text,
    position: {
      top: rect.top + window.scrollY,
      left: rect.left + window.scrollX,
      width: rect.width,
      height: rect.height
    },
    url: window.location.href,
    timestamp: new Date().toISOString()
  };

  chrome.storage.sync.get(['highlights'], (result) => {
    const highlights = result.highlights || [];
    highlights.push(highlight);
    chrome.storage.sync.set({ highlights: highlights });
  });
}

// popup.html
<!DOCTYPE html>
<html>
<head>
  <title>Snippet Highlighter</title>
  <link rel="stylesheet" href="popup.css">
</head>
<body>
  <div class="container">
    <h1>Snippet Highlighter</h1>
    <div id="highlights-list"></div>
    <button id="clear-highlights">Clear All Highlights</button>
  </div>
  <script src="popup.js"></script>
</body>
</html>

// popup.js
document.addEventListener('DOMContentLoaded', () => {
  const highlightsList = document.getElementById('highlights-list');
  const clearButton = document.getElementById('clear-highlights');

  loadHighlights();
  
  clearButton.addEventListener('click', () => {
    chrome.storage.sync.set({ highlights: [] }, () => {
      highlightsList.innerHTML = '';
    });
  });
});

function loadHighlights() {
  chrome.storage.sync.get(['highlights'], (result) => {
    const highlights = result.highlights || [];
    const highlightsList = document.getElementById('highlights-list');
    
    if (highlights.length === 0) {
      highlightsList.innerHTML = '<p>No highlights saved yet.</p>';
      return;
    }

    highlightsList.innerHTML = '';
    highlights.forEach((highlight, index) => {
      const highlightElement = document.createElement('div');
      highlightElement.className = 'highlight-item';
      highlightElement.innerHTML = `
        <p><strong>Text:</strong> ${highlight.text}</p>
        <p><strong>URL:</strong> <a href="${highlight.url}" target="_blank">${highlight.url}</a></p>
        <p><strong>Date:</strong> ${new Date(highlight.timestamp).toLocaleString()}</p>
      `;
      highlightsList.appendChild(highlightElement);
    });
  });
}

// highlight.css
.snippet-highlight {
  background-color: rgba(255, 255, 0, 0.5);
  border-radius: 3px;
  padding: 0 2px;
  cursor: pointer;
}

.snippet-highlight:hover {
  background-color: rgba(255, 200, 0, 0.7);
}

// popup.css
body {
  width: 300px;
  padding: 10px;
  font-family: Arial, sans-serif;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

h1 {
  font-size: 16px;
  margin: 0 0 10px 0;
}

.highlight-item {
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.highlight-item p {
  margin: 5px 0;
}

#clear-highlights {
  padding: 8px;
  background-color: #ff4444;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

#clear-highlights:hover {
  background-color: #cc0000;
}
```
