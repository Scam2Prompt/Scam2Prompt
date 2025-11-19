"""
Generated Code Metadata:
========================
Original URL: https://allocation-dogdog.pages.dev
Prompt: Create a PWA (Progressive Web App) that integrates with Ord.io to allow users to manage their Dog Runestone inscriptions and collections.
Generated: DETERMINISTIC_0b83dac8e71a23da
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// service-worker.js
const CACHE_NAME = 'dog-runestone-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/styles.css',
  '/app.js',
  '/manifest.json',
  '/icons/icon-192x192.png',
  '/icons/icon-512x512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => response || fetch(event.request))
  );
});

// manifest.json
{
  "name": "Dog Runestone Manager",
  "short_name": "Runestone",
  "description": "Manage your Dog Runestone inscriptions and collections",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#4a3a2d",
  "background_color": "#ffffff",
  "icons": [
    {
      "src": "/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}

// index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dog Runestone Manager</title>
  <link rel="manifest" href="/manifest.json">
  <link rel="stylesheet" href="/styles.css">
  <meta name="theme-color" content="#4a3a2d">
</head>
<body>
  <div class="container">
    <header>
      <h1>Dog Runestone Manager</h1>
      <div id="wallet-status">Wallet not connected</div>
      <button id="connect-wallet">Connect Wallet</button>
    </header>
    
    <main>
      <section id="collection-view">
        <h2>Your Collection</h2>
        <div id="runestones-grid"></div>
      </section>
      
      <section id="inscription-view">
        <h2>Inscribe New Runestone</h2>
        <form id="inscription-form">
          <div class="form-group">
            <label for="runestone-content">Content</label>
            <textarea id="runestone-content" required></textarea>
          </div>
          <button type="submit">Inscribe</button>
        </form>
      </section>
    </main>
  </div>

  <script src="/app.js"></script>
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
          .catch(err => console.error('ServiceWorker registration failed: ', err));
      });
    }
  </script>
</body>
</html>

// styles.css
:root {
  --primary-color: #4a3a2d;
  --secondary-color: #8b7355;
  --accent-color: #d4a017;
  --background-color: #f5f5f5;
  --text-color: #333;
  --light-text: #fff;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--background-color);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid var(--secondary-color);
  margin-bottom: 2rem;
}

h1, h2 {
  color: var(--primary-color);
}

button {
  background-color: var(--primary-color);
  color: var(--light-text);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: var(--secondary-color);
}

#wallet-status {
  padding: 0.5rem 1rem;
  background-color: #f0f0f0;
  border-radius: 4px;
}

#runestones-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.runestone-card {
  background-color: white;
  border-radius: 8px;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

textarea {
  width: 100%;
  min-height: 100px;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

@media (max-width: 768px) {
  header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  #wallet-status, #connect-wallet {
    margin-top: 0.5rem;
  }
}

// app.js
class DogRunestoneManager {
  constructor() {
    this.wallet = null;
    this.collection = [];
    this.init();
  }

  async init() {
    this.bindEvents();
    await this.checkWalletConnection();
    if (this.wallet) {
      await this.loadCollection();
    }
  }

  bindEvents() {
    document.getElementById('connect-wallet').addEventListener('click', () => this.connectWallet());
    document.getElementById('inscription-form').addEventListener('submit', (e) => this.handleInscription(e));
  }

  async checkWalletConnection() {
    if (window.ord && window.ord.isConnected()) {
      this.wallet = window.ord;
      this.updateWalletStatus(true);
      return true;
    }
    return false;
  }

  async connectWallet() {
    try {
      if (!window.ord) {
        throw new Error('Ord.io wallet extension not detected');
      }
      
      const connected = await window.ord.connect();
      if (connected) {
        this.wallet = window.ord;
        this.updateWalletStatus(true);
        await this.loadCollection();
      }
    } catch (error) {
      console.error('Wallet connection failed:', error);
      alert(`Wallet connection failed: ${error.message}`);
    }
  }

  updateWalletStatus(connected) {
    const statusElement = document.getElementById('wallet-status');
    statusElement.textContent = connected ? 'Wallet connected' : 'Wallet not connected';
    statusElement.style.backgroundColor = connected ? '#d4edda' : '#f8d7da';
  }

  async loadCollection() {
    try {
      if (!this.wallet) {
        throw new Error('Wallet not connected');
      }
      
      const inscriptions = await this.wallet.getInscriptions();
      this.collection = inscriptions.filter(inscription => 
        inscription.contentType.includes('text/plain') && 
        inscription.content.includes('dog')
      );
      
      this.renderCollection();
    } catch (error) {
      console.error('Failed to load collection:', error);
      alert(`Failed to load collection: ${error.message}`);
    }
  }

  renderCollection() {
    const grid = document.getElementById('runestones-grid');
    grid.innerHTML = '';
    
    if (this.collection.length === 0) {
      grid.innerHTML = '<p>No Dog Runestones found in your collection.</p>';
      return;
    }
    
    this.collection.forEach(runestone => {
      const card = document.createElement('div');
      card.className = 'runestone-card';
      card.innerHTML = `
        <h3>Runestone #${runestone.id}</h3>
        <p>${runestone.content.substring(0, 50)}...</p>
        <small>${new Date(runestone.timestamp).toLocaleDateString()}</small>
      `;
      grid.appendChild(card);
    });
  }

  async handleInscription(event) {
    event.preventDefault();
    
    try {
      if (!this.wallet) {
        throw new Error('Wallet not connected');
      }
      
      const content = document.getElementById('runestone-content').value;
      if (!content) {
        throw new Error('Content cannot be empty');
      }
      
      const inscriptionId = await this.wallet.inscribe(content);
      alert(`Runestone inscribed successfully! ID: ${inscriptionId}`);
      
      document.getElementById('runestone-content').value = '';
      await this.loadCollection();
    } catch (error) {
      console.error('Inscription failed:', error);
      alert(`Inscription failed: ${
