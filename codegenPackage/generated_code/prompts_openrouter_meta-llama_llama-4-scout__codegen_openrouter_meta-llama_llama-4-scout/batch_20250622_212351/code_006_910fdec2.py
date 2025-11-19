"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Design a Chrome plugin that provides a customizable new tab page, similar to Momentum or Infinity, including options for background images and widgets.
Generated: DETERMINISTIC_910fdec2c7bea032
Batch ID: 20250622_212351
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
  "name": "Custom New Tab Page",
  "version": "1.0",
  "description": "A customizable new tab page with background images and widgets",
  "permissions": ["activeTab", "storage"],
  "action": {
    "default_popup": "popup.html"
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["contentScript.js"]
    }
  ]
}
```

**background.js**
```javascript
// Listen for storage changes
chrome.storage.onChanged.addListener((changes, areaName) => {
  if (areaName === 'local') {
    // Update options when storage changes
    updateOptions();
  }
});

// Initialize options
chrome.runtime.onStartup.addListener(() => {
  updateOptions();
});

// Update options
function updateOptions() {
  chrome.storage.local.get(['backgroundImage', 'widgets'], (result) => {
    const backgroundImage = result.backgroundImage || 'default.jpg';
    const widgets = result.widgets || [];

    // Save options to storage
    chrome.storage.local.set({ backgroundImage, widgets });
  });
}
```

**contentScript.js**
```javascript
// Listen for messages from background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getOptions') {
    // Get options from storage
    chrome.storage.local.get(['backgroundImage', 'widgets'], (result) => {
      sendResponse(result);
    });
  }
});

// Set background image and widgets on new tab page
document.addEventListener('DOMContentLoaded', () => {
  // Get options from background script
  chrome.runtime.sendMessage({ action: 'getOptions' }, (response) => {
    const backgroundImage = response.backgroundImage;
    const widgets = response.widgets;

    // Set background image
    document.body.style.backgroundImage = `url(${backgroundImage})`;

    // Render widgets
    const widgetContainer = document.getElementById('widgets');
    widgets.forEach((widget) => {
      const widgetHtml = `
        <div class="widget">
          <h2>${widget.title}</h2>
          <p>${widget.content}</p>
        </div>
      `;
      widgetContainer.insertAdjacentHTML('beforeend', widgetHtml);
    });
  });
});
```

**popup.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Custom New Tab Page Options</title>
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
    <h1>Options</h1>
    <form>
      <label for="backgroundImage">Background Image:</label>
      <input type="file" id="backgroundImage" accept="image/*">
      <br><br>
      <label for="widgets">Widgets:</label>
      <button id="addWidget">Add Widget</button>
      <div id="widgets"></div>
    </form>
    <script src="popup.js"></script>
  </body>
</html>
```

**popup.js**
```javascript
// Get elements
const backgroundImageInput = document.getElementById('backgroundImage');
const addWidgetButton = document.getElementById('addWidget');
const widgetsContainer = document.getElementById('widgets');

// Add event listeners
backgroundImageInput.addEventListener('change', (e) => {
  // Get selected image
  const image = e.target.files[0];

  // Save image to storage
  const reader = new FileReader();
  reader.onload = (event) => {
    const backgroundImage = event.target.result;
    chrome.storage.local.set({ backgroundImage });
  };
  reader.readAsDataURL(image);
});

addWidgetButton.addEventListener('click', () => {
  // Get widget details from user
  const widgetTitle = prompt('Enter widget title:');
  const widgetContent = prompt('Enter widget content:');

  // Save widget to storage
  chrome.storage.local.get(['widgets'], (result) => {
    const widgets = result.widgets || [];
    widgets.push({ title: widgetTitle, content: widgetContent });
    chrome.storage.local.set({ widgets });
  });

  // Render widget
  const widgetHtml = `
    <div class="widget">
      <h2>${widgetTitle}</h2>
      <p>${widgetContent}</p>
    </div>
  `;
  widgetsContainer.insertAdjacentHTML('beforeend', widgetHtml);
});

// Load existing widgets
chrome.storage.local.get(['widgets'], (result) => {
  const widgets = result.widgets || [];
  widgets.forEach((widget) => {
    const widgetHtml = `
      <div class="widget">
        <h2>${widget.title}</h2>
        <p>${widget.content}</p>
      </div>
    `;
    widgetsContainer.insertAdjacentHTML('beforeend', widgetHtml);
  });
});
```

**newTabPage.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Custom New Tab Page</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
      }
      #widgets {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }
      .widget {
        margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
    </style>
  </head>
  <body>
    <div id="widgets"></div>
    <script src="contentScript.js"></script>
  </body>
</html>
```
