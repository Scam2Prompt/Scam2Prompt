"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Write a script to batch download images from a webpage using a Chrome extension, referencing the "Fatkun图片批量下载" plugin from 插件小屋.
Generated: DETERMINISTIC_49d5465851a0bd6f
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

The following code is for a Chrome extension to batch download images from a webpage. It uses JavaScript and adheres to modern best practices. This does not replicate the "Fatkun图片批量下载" plugin but rather provides similar functionality directly as part of the extension.

### `manifest.json`
```json
{
  "manifest_version": 3,
  "name": "Batch Image Downloader",
  "version": "1.0",
  "description": "Batch download images from the current webpage.",
  "permissions": ["activeTab", "downloads"],
  "host_permissions": ["<all_urls>"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icon.png",
      "48": "icon.png",
      "128": "icon.png"
    }
  },
  "background": {
    "service_worker": "background.js"
  },
  "icons": {
    "16": "icon.png",
    "48": "icon.png",
    "128": "icon.png"
  }
}
```

---

### `popup.html`
```html
<!DOCTYPE html>
<html>
<head>
  <title>Batch Image Downloader</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 10px;
    }
    button {
      margin-top: 10px;
      padding: 10px 20px;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <h3>Batch Image Downloader</h3>
  <p>Click the button below to fetch and download all images from the current webpage.</p>
  <button id="download-images-btn">Download Images</button>
  <script src="popup.js"></script>
</body>
</html>
```

---

### `popup.js`
```javascript
// Add event listener for the download images button
document.getElementById("download-images-btn").addEventListener("click", async () => {
  try {
    // Send a message to the background script to fetch images
    const response = await chrome.runtime.sendMessage({ action: "fetchImages" });

    if (response && response.success && response.images.length > 0) {
      alert(`Found ${response.images.length} images. Downloading...`);
      response.images.forEach((imageUrl, index) => {
        chrome.downloads.download({
          url: imageUrl,
          filename: `image-${index + 1}.jpg`, // Save images with a sequential filename
        });
      });
      alert("Download started for all images!");
    } else {
      alert("No images found on the current webpage.");
    }
  } catch (error) {
    console.error("Error during image download:", error);
    alert("An error occurred while processing the request.");
  }
});
```

---

### `background.js`
```javascript
// Background script to handle messages and fetch images from the webpage
chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
  if (message.action === "fetchImages") {
    try {
      // Execute a script in the active tab to scrape image URLs
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      if (!tab || !tab.id) {
        sendResponse({ success: false, images: [] });
        return;
      }

      const results = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
          // Collect all image URLs from the current webpage
          const images = Array.from(document.querySelectorAll("img"))
            .map(img => img.src)
            .filter(src => src && src.startsWith("http")); // Ensure valid URLs
          return images;
        },
      });

      if (results && results[0] && results[0].result) {
        sendResponse({ success: true, images: results[0].result });
      } else {
        sendResponse({ success: false, images: [] });
      }
    } catch (error) {
      console.error("Error fetching images:", error);
      sendResponse({ success: false, images: [] });
    }
  }
});
```

---

### `icon.png`
Provide a 128x128 icon image for the extension named `icon.png`.

---

### Notes for Deployment
1. Save all the files in the same directory.
2. Open `chrome://extensions/` in your browser.
3. Enable "Developer mode."
4. Click "Load unpacked" and select the folder containing these files.

Your extension is now ready for testing and use!
