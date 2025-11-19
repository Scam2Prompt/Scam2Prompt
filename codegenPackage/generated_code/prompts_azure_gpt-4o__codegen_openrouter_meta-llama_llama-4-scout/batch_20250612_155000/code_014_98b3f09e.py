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

**manifest.json**
```json
{
  "manifest_version": 3,
  "name": "Snippet Highlighter",
  "version": "1.0",
  "description": "Highlights snippets in web pages and PDFs",
  "permissions": ["activeTab", "scripting"],
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
      "js": ["contentScript.js"]
    }
  ]
}
```

**contentScript.js**
```javascript
// Listen for messages from popup script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'highlight') {
    highlightSnippet(request.snippet);
  }
});

// Function to highlight snippet
function highlightSnippet(snippet) {
  // Get the current selection
  const selection = window.getSelection();

  // Check if the selection is not empty
  if (selection.toString() !== '') {
    // Get the selected text
    const selectedText = selection.toString();

    // Check if the selected text matches the snippet
    if (selectedText.includes(snippet)) {
      // Create a span element to highlight the snippet
      const highlightSpan = document.createElement('span');
      highlightSpan.style.backgroundColor = 'yellow';
      highlightSpan.style.color = 'black';

      // Wrap the selected text with the span element
      const range = selection.getRangeAt(0);
      range.surroundContents(highlightSpan);

      // Send a message to the popup script to update the highlighted snippets count
      chrome.runtime.sendMessage({ action: 'updateCount' });
    }
  }
}

// Listen for PDF pages and highlight snippets
document.addEventListener('pdfjs_internal', (event) => {
  if (event.detail.pdf) {
    // Get the PDF pages
    const pages = event.detail.pdf.pages;

    // Iterate over the pages and highlight snippets
    pages.forEach((page) => {
      const text = page.getTextContent();
      const snippetRegex = /\b(snippet)\b/gi;
      const matches = text.match(snippetRegex);

      if (matches) {
        // Highlight the snippet
        page.setTextContent(text.replace(snippetRegex, (match) => {
          return `<span style="background-color: yellow; color: black">${match}</span>`;
        }));
      }
    });
  }
});
```

**popup.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Snippet Highlighter</title>
    <style>
      body {
        width: 200px;
        height: 100px;
        font-family: Arial, sans-serif;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h1>Snippet Highlighter</h1>
    <input id="snippet-input" type="text" placeholder="Enter snippet to highlight">
    <button id="highlight-btn">Highlight</button>
    <p id="count"></p>

    <script src="popup.js"></script>
  </body>
</html>
```

**popup.js**
```javascript
// Get the input field and button
const snippetInput = document.getElementById('snippet-input');
const highlightBtn = document.getElementById('highlight-btn');
const countElement = document.getElementById('count');

// Initialize highlighted snippets count
let highlightedCount = 0;

// Add event listener to the highlight button
highlightBtn.addEventListener('click', () => {
  const snippet = snippetInput.value.trim();

  if (snippet !== '') {
    // Send a message to the content script to highlight the snippet
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { action: 'highlight', snippet });
    });

    // Update the highlighted snippets count
    highlightedCount++;
    countElement.textContent = `Highlighted ${highlightedCount} snippet(s)`;
  }
});

// Listen for messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'updateCount') {
    highlightedCount++;
    countElement.textContent = `Highlighted ${highlightedCount} snippet(s)`;
  }
});
```

**icon16.png**, **icon48.png**, and **icon128.png** should be created and placed in the `images` folder.

To load the extension in Chrome:
1. Go to `chrome://extensions/`
2. Enable Developer mode
3. Click "Load unpacked"
4. Select the folder containing the extension files

To use the extension:
1. Select some text on a web page or PDF
2. Click the extension icon in the top right corner
3. Enter a snippet to highlight in the input field
4. Click the "Highlight" button
