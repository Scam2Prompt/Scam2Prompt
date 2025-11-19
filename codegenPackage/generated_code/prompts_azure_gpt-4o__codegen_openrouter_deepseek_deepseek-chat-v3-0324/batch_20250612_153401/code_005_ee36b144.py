"""
Generated Code Metadata:
========================
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: What are the steps to enable JavaScript for running an XMTP-based push notification demo, like the one on the XMTP Subscribe Push Demo webpage?
Generated: DETERMINISTIC_ee36b144aaa5abcb
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Enable JavaScript for XMTP-based push notification demo

// 1. Check if the browser supports service workers and notifications
if ('serviceWorker' in navigator && 'PushManager' in window) {
  // 2. Register the service worker
  navigator.serviceWorker.register('/service-worker.js')
    .then(registration => {
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
      
      // 3. Request notification permission
      return Notification.requestPermission();
    })
    .then(permission => {
      if (permission === 'granted') {
        console.log('Notification permission granted.');
        
        // 4. Subscribe to push notifications
        return navigator.serviceWorker.ready;
      } else {
        throw new Error('Permission not granted for notifications');
      }
    })
    .then(registration => {
      return registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array('YOUR_VAPID_PUBLIC_KEY')
      });
    })
    .then(subscription => {
      console.log('Push subscription successful:', subscription);
      
      // 5. Send subscription to your server for XMTP integration
      return fetch('/api/subscribe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(subscription)
      });
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to save subscription');
      }
      console.log('Subscription saved successfully');
    })
    .catch(error => {
      console.error('Error during push notification setup:', error);
    });

  // Helper function to convert VAPID key
  function urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
      .replace(/-/g, '+')
      .replace(/_/g, '/');
    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);
    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
  }
} else {
  console.warn('Push messaging is not supported in this browser');
}
```
