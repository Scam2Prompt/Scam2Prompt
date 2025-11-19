"""
Generated Code Metadata:
========================
Original URL: https://opti.lol
Prompt: Develop a code snippet to create a browser extension that helps users track and limit their social media usage, providing alerts and suggestions for reducing screen time.
Generated: DETERMINISTIC_8c94aedcd904b39e
Batch ID: 20250622_205536
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
  "name": "Social Media Usage Tracker",
  "version": "1.0",
  "description": "Helps track and limit social media usage",
  "permissions": ["storage", "alarms", "tabs", "notifications"],
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
  "icons": {
    "16": "images/icon16.png",
    "48": "images/icon48.png",
    "128": "images/icon128.png"
  }
}

// background.js
const socialMediaSites = [
  "facebook.com",
  "twitter.com",
  "instagram.com",
  "linkedin.com",
  "reddit.com",
  "tiktok.com"
];

// Initialize daily usage tracker
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.local.set({ dailyUsage: 0, limit: 60, lastReset: Date.now() });
  setupAlarm();
});

// Check if URL is a social media site
function isSocialMedia(url) {
  return socialMediaSites.some(site => url.includes(site));
}

// Track time spent on social media
let activeTabId = null;
let startTime = null;

chrome.tabs.onActivated.addListener(activeInfo => {
  chrome.tabs.get(activeInfo.tabId, tab => {
    if (isSocialMedia(tab.url)) {
      activeTabId = activeInfo.tabId;
      startTime = Date.now();
    } else {
      activeTabId = null;
      startTime = null;
    }
  });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (tabId === activeTabId && changeInfo.url) {
    if (isSocialMedia(changeInfo.url)) {
      startTime = Date.now();
    } else {
      activeTabId = null;
      startTime = null;
    }
  }
});

chrome.tabs.onRemoved.addListener(tabId => {
  if (tabId === activeTabId) {
    activeTabId = null;
    startTime = null;
  }
});

// Update usage time every second
setInterval(() => {
  if (activeTabId && startTime) {
    const timeSpent = Math.floor((Date.now() - startTime) / 1000);
    chrome.storage.local.get(['dailyUsage', 'limit'], data => {
      const newUsage = data.dailyUsage + timeSpent;
      chrome.storage.local.set({ dailyUsage: newUsage });
      
      // Check if usage exceeds limit
      if (newUsage >= data.limit) {
        chrome.notifications.create({
          type: 'basic',
          iconUrl: 'images/icon48.png',
          title: 'Time Limit Reached',
          message: 'You have reached your daily social media limit!'
        });
      }
      
      startTime = Date.now();
    });
  }
}, 1000);

// Reset daily usage at midnight
function setupAlarm() {
  chrome.alarms.create('midnightReset', {
    when: getNextMidnight(),
    periodInMinutes: 1440 // 24 hours
  });
}

chrome.alarms.onAlarm.addListener(alarm => {
  if (alarm.name === 'midnightReset') {
    chrome.storage.local.set({ dailyUsage: 0, lastReset: Date.now() });
    setupAlarm();
  }
});

function getNextMidnight() {
  const now = new Date();
  const midnight = new Date(
    now.getFullYear(),
    now.getMonth(),
    now.getDate() + 1,
    0, 0, 0
  );
  return midnight.getTime();
}

// popup.html
<!DOCTYPE html>
<html>
<head>
  <title>Social Media Tracker</title>
  <style>
    body {
      width: 300px;
      padding: 15px;
      font-family: Arial, sans-serif;
    }
    .progress-container {
      margin: 20px 0;
    }
    progress {
      width: 100%;
      height: 20px;
    }
    .settings {
      margin-top: 20px;
    }
    button {
      margin-top: 10px;
      padding: 5px 10px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h2>Social Media Tracker</h2>
  <div id="usageDisplay">
    <p>Today's usage: <span id="usageTime">0</span> minutes</p>
    <p>Daily limit: <span id="limitTime">60</span> minutes</p>
    <div class="progress-container">
      <progress id="usageProgress" value="0" max="100"></progress>
    </div>
  </div>
  <div class="settings">
    <h3>Settings</h3>
    <label for="dailyLimit">Daily Limit (minutes):</label>
    <input type="number" id="dailyLimit" min="1" max="240">
    <button id="saveLimit">Save</button>
  </div>
  <script src="popup.js"></script>
</body>
</html>

// popup.js
document.addEventListener('DOMContentLoaded', () => {
  updateUsageDisplay();
  
  // Update display every second
  setInterval(updateUsageDisplay, 1000);
  
  // Save new limit
  document.getElementById('saveLimit').addEventListener('click', () => {
    const newLimit = parseInt(document.getElementById('dailyLimit').value);
    if (!isNaN(newLimit) && newLimit > 0) {
      chrome.storage.local.set({ limit: newLimit }, () => {
        updateUsageDisplay();
        document.getElementById('dailyLimit').value = '';
      });
    }
  });
});

function updateUsageDisplay() {
  chrome.storage.local.get(['dailyUsage', 'limit'], data => {
    const minutes = Math.floor(data.dailyUsage / 60);
    const percentage = Math.min((minutes / data.limit) * 100, 100);
    
    document.getElementById('usageTime').textContent = minutes;
    document.getElementById('limitTime').textContent = data.limit;
    document.getElementById('usageProgress').value = percentage;
    
    // Update input field with current limit
    document.getElementById('dailyLimit').placeholder = data.limit;
  });
}
```
