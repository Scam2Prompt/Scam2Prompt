"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iensooa.pages.dev
Prompt: Write a script to enable push notifications for Web3Inbox on a mobile browser, including steps to add the app to the home screen.
Generated: DETERMINISTIC_5c8834a0fbf6f54d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Web3Inbox Push Notification and Add to Home Screen Script
// This script enables push notifications for Web3Inbox on a mobile browser and guides users to add the app to the home screen.

// Check if the browser supports service workers and notifications
if ('serviceWorker' in navigator && 'PushManager' in window) {
  // Register the service worker
  navigator.serviceWorker.register('/service-worker.js').then((registration) => {
    console.log('Service Worker registered with scope:', registration.scope);

    // Request permission for push notifications
    Notification.requestPermission().then((permission) => {
      if (permission === 'granted') {
        // Subscribe the user to push notifications
        registration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey: urlBase64ToUint8Array('<Your-VAPID-Public-Key>')
        }).then((subscription) => {
          console.log('Push subscription successful:', subscription);

          // Send subscription details to your server to enable notifications
          sendSubscriptionToServer(subscription);
        }).catch((error) => {
          console.error('Failed to subscribe to push notifications:', error);
        });
      } else {
        console.warn('Push notification permission denied.');
      }
    }).catch((error) => {
      console.error('Failed to request notification permission:', error);
    });
  }).catch((error) => {
    console.error('Service Worker registration failed:', error);
  });
} else {
  console.warn('Push notifications are not supported on this browser.');
}

// Function to convert VAPID public key from base64 to Uint8Array
function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);
  for (let i = 0; i < rawData.length; i++) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

// Function to send subscription details to the server
function sendSubscriptionToServer(subscription) {
  fetch('/api/save-subscription', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(subscription)
  }).then((response) => {
    if (response.ok) {
      console.log('Subscription saved successfully.');
    } else {
      console.error('Failed to save subscription:', response.statusText);
    }
  }).catch((error) => {
    console.error('Error sending subscription to server:', error);
  });
}

// Prompt user to add the app to the home screen
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (event) => {
  // Prevent the default prompt
  event.preventDefault();
  deferredPrompt = event;

  // Show a custom UI prompt to the user to add the app to the home screen
  const addButton = document.createElement('button');
  addButton.textContent = 'Add Web3Inbox to Home Screen';
  addButton.style.position = 'fixed';
  addButton.style.bottom = '20px';
  addButton.style.right = '20px';
  addButton.style.zIndex = '1000';
  addButton.style.padding = '10px 20px';
  addButton.style.backgroundColor = '#4CAF50';
  addButton.style.color = '#fff';
  addButton.style.border = 'none';
  addButton.style.borderRadius = '5px';
  addButton.style.cursor = 'pointer';
  document.body.appendChild(addButton);

  addButton.addEventListener('click', () => {
    // Trigger the installation prompt
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then((choiceResult) => {
      if (choiceResult.outcome === 'accepted') {
        console.log('User accepted the installation prompt.');
      } else {
        console.log('User dismissed the installation prompt.');
      }
      deferredPrompt = null;
      document.body.removeChild(addButton);
    });
  });
});

// Inform the user if the app is already installed
window.addEventListener('appinstalled', () => {
  console.log('Web3Inbox has been installed.');
});
```
