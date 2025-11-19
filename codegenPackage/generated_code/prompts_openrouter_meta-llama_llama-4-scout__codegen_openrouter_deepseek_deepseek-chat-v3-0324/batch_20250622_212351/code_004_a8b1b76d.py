"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Create a Chrome extension that generates QR codes for web pages, similar to Quick QR, including customization options for colors and sizes.
Generated: DETERMINISTIC_a8b1b76dd5d73e4f
Batch ID: 20250622_212351
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
  "name": "Quick QR Generator",
  "version": "1.0",
  "description": "Generate QR codes for web pages with customization options",
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "permissions": ["activeTab", "storage"],
  "background": {
    "service_worker": "background.js"
  }
}

// popup.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quick QR Generator</title>
  <link rel="stylesheet" href="popup.css">
  <script src="qrcode.min.js"></script>
  <script src="popup.js" defer></script>
</head>
<body>
  <div class="container">
    <h1>Quick QR Generator</h1>
    <div id="qr-code"></div>
    <div class="controls">
      <div class="control-group">
        <label for="size">Size:</label>
        <input type="range" id="size" min="100" max="500" value="200">
        <span id="size-value">200</span>
      </div>
      <div class="control-group">
        <label for="fg-color">Foreground:</label>
        <input type="color" id="fg-color" value="#000000">
      </div>
      <div class="control-group">
        <label for="bg-color">Background:</label>
        <input type="color" id="bg-color" value="#ffffff">
      </div>
      <div class="control-group">
        <button id="download-btn">Download QR Code</button>
      </div>
    </div>
  </div>
</body>
</html>

// popup.css
body {
  width: 300px;
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}

.container {
  padding: 15px;
}

h1 {
  font-size: 18px;
  margin-top: 0;
  text-align: center;
}

#qr-code {
  display: flex;
  justify-content: center;
  margin: 15px 0;
}

.controls {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.control-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.control-group label {
  font-size: 14px;
  min-width: 80px;
}

input[type="range"] {
  flex-grow: 1;
}

input[type="color"] {
  width: 30px;
  height: 30px;
  padding: 0;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 8px;
  background-color: #4285f4;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

button:hover {
  background-color: #3367d6;
}

// popup.js
document.addEventListener('DOMContentLoaded', async () => {
  const qrCodeElement = document.getElementById('qr-code');
  const sizeSlider = document.getElementById('size');
  const sizeValue = document.getElementById('size-value');
  const fgColorPicker = document.getElementById('fg-color');
  const bgColorPicker = document.getElementById('bg-color');
  const downloadBtn = document.getElementById('download-btn');
  
  let currentTabUrl = '';
  let qrCode = null;

  // Load saved preferences
  chrome.storage.sync.get(['size', 'fgColor', 'bgColor'], (data) => {
    if (data.size) {
      sizeSlider.value = data.size;
      sizeValue.textContent = data.size;
    }
    if (data.fgColor) fgColorPicker.value = data.fgColor;
    if (data.bgColor) bgColorPicker.value = data.bgColor;
  });

  // Get current tab URL
  try {
    const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
    currentTabUrl = tabs[0].url;
    generateQRCode();
  } catch (error) {
    console.error('Error getting current tab:', error);
    qrCodeElement.innerHTML = '<p>Error: Could not get current page URL</p>';
  }

  // Generate QR code
  function generateQRCode() {
    if (!currentTabUrl) return;

    const size = parseInt(sizeSlider.value);
    const fgColor = fgColorPicker.value;
    const bgColor = bgColorPicker.value;

    qrCodeElement.innerHTML = '';
    qrCode = new QRCode(qrCodeElement, {
      text: currentTabUrl,
      width: size,
      height: size,
      colorDark: fgColor,
      colorLight: bgColor,
      correctLevel: QRCode.CorrectLevel.H
    });
  }

  // Update QR code when settings change
  sizeSlider.addEventListener('input', () => {
    sizeValue.textContent = sizeSlider.value;
    generateQRCode();
  });

  fgColorPicker.addEventListener('input', generateQRCode);
  bgColorPicker.addEventListener('input', generateQRCode);

  // Save preferences when changed
  sizeSlider.addEventListener('change', savePreferences);
  fgColorPicker.addEventListener('change', savePreferences);
  bgColorPicker.addEventListener('change', savePreferences);

  function savePreferences() {
    chrome.storage.sync.set({
      size: sizeSlider.value,
      fgColor: fgColorPicker.value,
      bgColor: bgColorPicker.value
    });
  }

  // Download QR code
  downloadBtn.addEventListener('click', () => {
    if (!qrCode) return;

    try {
      const canvas = qrCodeElement.querySelector('canvas');
      if (!canvas) throw new Error('QR code canvas not found');

      const link = document.createElement('a');
      link.download = `qr-code-${new Date().getTime()}.png`;
      link.href = canvas.toDataURL('image/png');
      link.click();
    } catch (error) {
      console.error('Error downloading QR code:', error);
      alert('Error downloading QR code. Please try again.');
    }
  });
});

// background.js
// No background functionality needed for this extension
```
