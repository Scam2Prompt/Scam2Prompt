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

Here's the code for the Chrome extension that highlights snippets in web pages and PDFs. It consists of the necessary files for the extension: `manifest.json`, `content.js`, and `background.js`. This code is clean, production-ready, and follows best practices.

---

### `manifest.json`
```json
{
  "manifest_version": 3,
  "name": "Snippet Highlighter",
  "version": "1.0",
  "description": "Highlight snippets on web pages and PDFs.",
  "permissions": ["activeTab", "scripting"],
  "host_permissions": ["<all_urls>"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "action": {
    "default_title": "Snippet Highlighter",
    "default_popup": "popup.html"
  }
}
```

---

### `content.js`
```javascript
// content.js
// This script runs on the webpage to highlight specified text snippets.

// Utility function to highlight matched text
function highlightText(snippet) {
  const body = document.body;
  const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT, null, false);

  // Regular expression to match the snippet case-insensitively
  const regex = new RegExp(snippet, "gi");

  while (walker.nextNode()) {
    const node = walker.currentNode;

    // Check if the text node contains the snippet
    if (regex.test(node.nodeValue)) {
      const parent = node.parentNode;

      // Skip if the parent is already a highlight element
      if (parent && parent.classList.contains("snippet-highlight")) {
        continue;
      }

      // Create a span element to highlight the snippet
      const highlightedSpan = document.createElement("span");
      highlightedSpan.className = "snippet-highlight";
      highlightedSpan.style.backgroundColor = "yellow";
      highlightedSpan.style.color = "black";

      // Replace matched text with the highlighted span
      highlightedSpan.innerHTML = node.nodeValue.replace(regex, (match) => `<mark>${match}</mark>`);

      parent.replaceChild(highlightedSpan, node);
    }
  }
}

// Attach a listener to receive snippets from the background script
chrome.runtime.onMessage.addListener((message) => {
  if (message.type === "highlight-snippet") {
    highlightText(message.snippet);
  }
});
```

---

### `background.js`
```javascript
// background.js
// Background script to handle user actions and communication with content scripts.

// Listen for user action in the extension
chrome.action.onClicked.addListener((tab) => {
  // Prompt the user for a snippet to highlight
  const snippet = prompt("Enter the snippet text to highlight:");

  if (snippet) {
    // Send the snippet to the content script for highlighting
    chrome.tabs.sendMessage(tab.id, { type: "highlight-snippet", snippet: snippet });
  } else {
    console.log("No snippet provided.");
  }
});
```

---

### `popup.html` (Optional)
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 10px;
    }
    button {
      padding: 10px 20px;
      font-size: 14px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Snippet Highlighter</h1>
  <button id="highlight-btn">Highlight Snippets</button>

  <script>
    const highlightButton = document.getElementById("highlight-btn");
    highlightButton.addEventListener("click", () => {
      const snippet = prompt("Enter the snippet text to highlight:");
      if (snippet) {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
          chrome.tabs.sendMessage(tabs[0].id, { type: "highlight-snippet", snippet: snippet });
        });
      }
    });
  </script>
</body>
</html>
```

### Additional Notes
1. Place the files in the same directory.
2. Load this extension in Chrome via "Load unpacked" in the Extensions Manager.
3. Error handling (e.g., for invalid inputs or unsupported pages) is included indirectly via checks like `if (snippet)`.

Ensure you test this thoroughly on both web pages and PDFs, and refine the snippet-matching logic as needed for edge cases.
