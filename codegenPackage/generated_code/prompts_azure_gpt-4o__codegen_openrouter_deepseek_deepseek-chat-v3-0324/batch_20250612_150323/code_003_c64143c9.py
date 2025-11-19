"""
Generated Code Metadata:
========================
Original URL: https://web3inbox.com
Prompt: Write code to integrate Web3Inbox into a mobile web application, enabling users to add the app to their home screen and receive push notifications.
Generated: DETERMINISTIC_c64143c9fffbce76
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { Web3Inbox } from "@web3inbox/core";
import { useAccount, useConnect, useDisconnect } from "wagmi";
import { InjectedConnector } from "wagmi/connectors/injected";
import { useEffect, useState } from "react";

// Initialize Web3Inbox
const projectId = "YOUR_PROJECT_ID"; // Replace with your WalletConnect Project ID
const appDomain = "your-app.com"; // Replace with your app's domain

Web3Inbox.init({
  projectId,
  domain: appDomain,
});

// Main App Component
function App() {
  const { address, isConnected } = useAccount();
  const { connect } = useConnect({
    connector: new InjectedConnector(),
  });
  const { disconnect } = useDisconnect();

  const [isSubscribed, setIsSubscribed] = useState(false);
  const [isInstallable, setIsInstallable] = useState(false);
  const [deferredPrompt, setDeferredPrompt] = useState(null);

  // Check if app is installable (PWA)
  useEffect(() => {
    window.addEventListener("beforeinstallprompt", (e) => {
      e.preventDefault();
      setDeferredPrompt(e);
      setIsInstallable(true);
    });
  }, []);

  // Handle subscription status
  useEffect(() => {
    if (!address) return;

    const checkSubscription = async () => {
      const isSubscribed = await Web3Inbox.isSubscribed(address);
      setIsSubscribed(isSubscribed);
    };

    checkSubscription();
  }, [address]);

  // Handle install prompt
  const handleInstallClick = async () => {
    if (!deferredPrompt) return;

    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    if (outcome === "accepted") {
      setIsInstallable(false);
    }
  };

  // Handle subscribe
  const handleSubscribe = async () => {
    if (!address) return;

    try {
      await Web3Inbox.subscribe(address);
      setIsSubscribed(true);
    } catch (error) {
      console.error("Subscription error:", error);
    }
  };

  // Handle unsubscribe
  const handleUnsubscribe = async () => {
    if (!address) return;

    try {
      await Web3Inbox.unsubscribe(address);
      setIsSubscribed(false);
    } catch (error) {
      console.error("Unsubscription error:", error);
    }
  };

  // Listen for notifications
  useEffect(() => {
    if (!address) return;

    const handleNotification = (notification) => {
      console.log("New notification:", notification);
      // Display notification to user
      if (Notification.permission === "granted") {
        new Notification(notification.title, {
          body: notification.body,
          icon: notification.icon,
        });
      }
    };

    Web3Inbox.on("notification", handleNotification);

    return () => {
      Web3Inbox.off("notification", handleNotification);
    };
  }, [address]);

  return (
    <div className="App">
      <header>
        <h1>Web3Inbox Integration</h1>
      </header>

      <main>
        {!isConnected ? (
          <button onClick={() => connect()}>Connect Wallet</button>
        ) : (
          <>
            <p>Connected as: {address}</p>
            <button onClick={() => disconnect()}>Disconnect</button>

            {!isSubscribed ? (
              <button onClick={handleSubscribe}>Subscribe to Notifications</button>
            ) : (
              <button onClick={handleUnsubscribe}>Unsubscribe from Notifications</button>
            )}

            {isInstallable && (
              <button onClick={handleInstallClick}>Install App</button>
            )}
          </>
        )}
      </main>
    </div>
  );
}

export default App;

// Service Worker Registration (in public/sw.js)
self.addEventListener("install", (event) => {
  event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener("push", (event) => {
  const payload = event.data?.json() || {};
  event.waitUntil(
    self.registration.showNotification(payload.title || "New Notification", {
      body: payload.body,
      icon: payload.icon || "/icon.png",
      data: payload,
    })
  );
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: "window" }).then((clientList) => {
      for (const client of clientList) {
        if ("focus" in client) return client.focus();
      }
      if (clients.openWindow) return clients.openWindow(event.notification.data.url || "/");
    })
  );
});

// Manifest File (public/manifest.json)
{
  "name": "Web3Inbox App",
  "short_name": "Web3Inbox",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    {
      "src": "/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}

// HTML File (public/index.html)
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Web3Inbox Integration" />
    <link rel="manifest" href="/manifest.json" />
    <title>Web3Inbox App</title>
  </head>
  <body>
    <div id="root"></div>
    <script>
      // Register service worker
      if ("serviceWorker" in navigator) {
        window.addEventListener("load", () => {
          navigator.serviceWorker.register("/sw.js").then(
            (registration) => {
              console.log("ServiceWorker registration successful");
            },
            (err) => {
              console.log("ServiceWorker registration failed: ", err);
            }
          );
        });
      }

      // Request notification permission
      if ("Notification" in window) {
        Notification.requestPermission().then((permission) => {
          console.log("Notification permission:", permission);
        });
      }
    </script>
  </body>
</html>
```
