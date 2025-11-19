"""
Generated Code Metadata:
========================
Original URL: https://runetech0.github.io
Prompt: Provide a step-by-step guide to integrate a "new content available" notification feature in a Jekyll blog, inspired by Rune Tech's implementation.
Generated: DETERMINISTIC_b076e15615c7d3e6
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// service-worker.js
const CACHE_NAME = 'my-jekyll-blog-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/assets/css/main.css',
  '/assets/js/main.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});

self.addEventListener('message', event => {
  if (event.data.action === 'skipWaiting') {
    self.skipWaiting();
  }
});
```

```javascript
// assets/js/update-notifier.js
class UpdateNotifier {
  constructor() {
    this.registration = null;
    this.updateAvailable = false;
    this.notificationElement = this.createNotificationElement();
    this.registerServiceWorker();
    this.setupEventListeners();
  }

  createNotificationElement() {
    const element = document.createElement('div');
    element.id = 'update-notification';
    element.className = 'update-notification hidden';
    element.innerHTML = `
      <p>New content is available!</p>
      <button id="update-button">Refresh</button>
    `;
    document.body.appendChild(element);
    return element;
  }

  registerServiceWorker() {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/service-worker.js')
        .then(reg => {
          this.registration = reg;
          this.checkForUpdates();
          reg.addEventListener('updatefound', () => this.trackInstallingWorker(reg.installing));
        })
        .catch(err => console.error('ServiceWorker registration failed:', err));
    }
  }

  trackInstallingWorker(worker) {
    worker.addEventListener('statechange', () => {
      if (worker.state === 'installed' && navigator.serviceWorker.controller) {
        this.showUpdateNotification();
      }
    });
  }

  checkForUpdates() {
    if (this.registration) {
      this.registration.update().catch(err => console.error('Update check failed:', err));
    }
  }

  showUpdateNotification() {
    this.updateAvailable = true;
    this.notificationElement.classList.remove('hidden');
  }

  hideUpdateNotification() {
    this.updateAvailable = false;
    this.notificationElement.classList.add('hidden');
  }

  setupEventListeners() {
    document.getElementById('update-button').addEventListener('click', () => {
      if (this.updateAvailable && this.registration && this.registration.waiting) {
        this.registration.waiting.postMessage({ action: 'skipWaiting' });
      }
      window.location.reload();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.updateAvailable) {
        this.hideUpdateNotification();
      }
    });
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new UpdateNotifier();
});
```

```css
/* assets/css/update-notifier.css */
.update-notification {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 15px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 15px;
}

.update-notification.hidden {
  display: none;
}

.update-notification p {
  margin: 0;
  color: #333;
}

#update-button {
  background: #0078d7;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 3px;
  cursor: pointer;
}

#update-button:hover {
  background: #0066c0;
}
```

```html
<!-- _includes/head.html -->
<head>
  <!-- Existing head content -->
  <link rel="stylesheet" href="/assets/css/update-notifier.css">
  <script src="/assets/js/update-notifier.js" defer></script>
</head>
```

```yaml
# _config.yml
# Add these to your existing config
service_worker:
  enabled: true
  cache_name: "my-jekyll-blog-cache-v1"
```

```javascript
// _plugins/service_worker_generator.rb
Jekyll::Hooks.register :site, :post_write do |site|
  if site.config['service_worker'] && site.config['service_worker']['enabled']
    File.open(File.join(site.dest, 'service-worker.js'), 'w') do |f|
      f.write(<<~JS)
        const CACHE_NAME = '#{site.config['service_worker']['cache_name']}';
        const urlsToCache = [
          '/',
          '/index.html',
          '/assets/css/main.css',
          '/assets/js/main.js'
        ];

        self.addEventListener('install', event => {
          event.waitUntil(
            caches.open(CACHE_NAME)
              .then(cache => cache.addAll(urlsToCache))
          );
        });

        self.addEventListener('fetch', event => {
          event.respondWith(
            caches.match(event.request)
              .then(response => response || fetch(event.request))
          );
        });

        self.addEventListener('message', event => {
          if (event.data.action === 'skipWaiting') {
            self.skipWaiting();
          }
        });
      JS
    end
  end
end
```
