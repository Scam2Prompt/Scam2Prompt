"""
Generated Code Metadata:
========================
Original URL: https://focalize-app.pages.dev
Prompt: "Implement an open-source, decentralized, and censorship-resistant social DApp on Lens Protocol using a browser extension architecture like Focalize."
Generated: DETERMINISTIC_0d8104576dd22cca
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Lens Social DApp Browser Extension
// Main extension script

import { ethers } from 'ethers';
import { LensClient, development } from '@lens-protocol/client';
import { Storage } from '@plasmohq/storage';

// Initialize storage
const storage = new Storage();

// Lens client configuration
const lensClient = new LensClient({
  environment: development
});

// Extension background service
class LensSocialExtension {
  private provider: ethers.providers.Web3Provider;
  private signer: ethers.Signer;
  private isConnected: boolean = false;

  constructor() {
    this.initialize();
  }

  private async initialize() {
    try {
      // Check for existing wallet connection
      const connected = await storage.get('walletConnected');
      if (connected) {
        await this.connectWallet();
      }

      // Set up listeners
      this.setupListeners();
    } catch (error) {
      console.error('Initialization error:', error);
    }
  }

  private setupListeners() {
    chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
      (async () => {
        try {
          switch (request.type) {
            case 'connectWallet':
              await this.connectWallet();
              sendResponse({ success: true });
              break;
            case 'disconnectWallet':
              await this.disconnectWallet();
              sendResponse({ success: true });
              break;
            case 'createPost':
              const postResult = await this.createPost(request.content);
              sendResponse(postResult);
              break;
            case 'getProfile':
              const profile = await this.getProfile();
              sendResponse(profile);
              break;
            case 'getFeed':
              const feed = await this.getFeed();
              sendResponse(feed);
              break;
            default:
              sendResponse({ error: 'Unknown request type' });
          }
        } catch (error) {
          console.error('Message handler error:', error);
          sendResponse({ error: error.message });
        }
      })();
      return true; // Keep message channel open for async response
    });
  }

  private async connectWallet() {
    try {
      if (!window.ethereum) {
        throw new Error('No Ethereum provider found');
      }

      this.provider = new ethers.providers.Web3Provider(window.ethereum);
      await this.provider.send('eth_requestAccounts', []);
      this.signer = this.provider.getSigner();
      this.isConnected = true;

      await storage.set('walletConnected', true);

      // Authenticate with Lens
      const address = await this.signer.getAddress();
      const challenge = await lensClient.authentication.generateChallenge(address);
      const signature = await this.signer.signMessage(challenge);
      await lensClient.authentication.authenticate(address, signature);

      return { success: true };
    } catch (error) {
      console.error('Wallet connection error:', error);
      return { error: error.message };
    }
  }

  private async disconnectWallet() {
    try {
      this.isConnected = false;
      this.provider = null;
      this.signer = null;
      await storage.set('walletConnected', false);
      await lensClient.authentication.logout();
      return { success: true };
    } catch (error) {
      console.error('Wallet disconnection error:', error);
      return { error: error.message };
    }
  }

  private async createPost(content: string) {
    try {
      if (!this.isConnected) {
        throw new Error('Wallet not connected');
      }

      const profileId = await storage.get('defaultProfileId');
      if (!profileId) {
        throw new Error('No default profile selected');
      }

      const result = await lensClient.publication.postOnchain({
        profileId,
        content,
        contentURI: `ipfs://${content}` // Simplified for example
      });

      return { success: true, txHash: result.txHash };
    } catch (error) {
      console.error('Post creation error:', error);
      return { error: error.message };
    }
  }

  private async getProfile() {
    try {
      if (!this.isConnected) {
        throw new Error('Wallet not connected');
      }

      const address = await this.signer.getAddress();
      const ownedProfiles = await lensClient.profile.fetchAll({
        ownedBy: [address]
      });

      if (ownedProfiles.items.length === 0) {
        return { error: 'No profiles found for this address' };
      }

      const defaultProfileId = await storage.get('defaultProfileId');
      const defaultProfile = defaultProfileId 
        ? ownedProfiles.items.find(p => p.id === defaultProfileId)
        : ownedProfiles.items[0];

      return { success: true, profile: defaultProfile };
    } catch (error) {
      console.error('Profile fetch error:', error);
      return { error: error.message };
    }
  }

  private async getFeed() {
    try {
      if (!this.isConnected) {
        throw new Error('Wallet not connected');
      }

      const profileId = await storage.get('defaultProfileId');
      if (!profileId) {
        throw new Error('No default profile selected');
      }

      const feed = await lensClient.feed.fetch({
        profileId,
        limit: 20
      });

      return { success: true, feed: feed.items };
    } catch (error) {
      console.error('Feed fetch error:', error);
      return { error: error.message };
    }
  }
}

// Initialize extension
new LensSocialExtension();
```

```typescript
// Content script for injection into web pages
// content-script.ts

import { Storage } from '@plasmohq/storage';

const storage = new Storage();

// Inject UI elements into the page
function injectUI() {
  const container = document.createElement('div');
  container.id = 'lens-social-container';
  container.style.position = 'fixed';
  container.style.bottom = '20px';
  container.style.right = '20px';
  container.style.zIndex = '10000';

  document.body.appendChild(container);

  // Listen for updates from background
  chrome.runtime.onMessage.addListener((message) => {
    updateUI(message);
  });

  // Initial UI state
  renderInitialUI();
}

function renderInitialUI() {
  const container = document.getElementById('lens-social-container');
  if (!container) return;

  container.innerHTML = `
    <div style="background: white; padding: 10px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
      <button id="lens-connect-btn" style="padding: 8px 16px; background: #8f5fe8; color: white; border: none; border-radius: 4px; cursor: pointer;">
        Connect Wallet
      </button>
      <div id="lens-status" style="margin-top: 8px; font-size: 12px;">Not connected</div>
    </div>
  `;

  document.getElementById('lens-connect-btn').addEventListener('click', () => {
    chrome.runtime.sendMessage({ type: 'connectWallet' });
  });
}

function updateUI(message) {
  const statusElement = document.getElementById('lens-status');
  if (!statusElement) return;

  if (message.success) {
    statusElement.textContent = 'Connected';
    statusElement.style.color = 'green';
  } else if (message.error) {
    statusElement.textContent = `Error: ${message.error}`;
    statusElement.style.color = 'red';
  }
}

// Initialize content script
injectUI();
```

```json
// Manifest file
// manifest.json

{
  "manifest_version": 3,
  "name": "Lens Social DApp",
  "version": "1.0.0",
  "description": "A decentralized social media extension for Lens Protocol",
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content-script.js"],
      "css": ["styles.css"]
    }
  ],
  "permissions": [
    "storage",
    "activeTab",
    "scripting"
  ],
  "host_permissions": [
    "<all_urls>"
  ],
  "web_accessible_resources": [{
    "resources": ["*.js", "*.css"],
    "matches": ["<all_urls>"]
  }]
}
```

```typescript
// Type definitions for Lens Protocol
// types.d.ts

declare module '@lens-protocol/client' {
  export interface LensClient {
    authentication: {
      generateChallenge(address: string): Promise<string>;
      authenticate(address: string, signature: string): Promise<void>;
      logout(): Promise<void>;
    };
    profile: {
      fetchAll(params: { ownedBy: string[] }): Promise<{
        items: Profile[];
      }>;
    };
    publication: {
      postOnchain(params: {
        profileId: string;
        content: string;
        contentURI: string;
      }): Promise<{ txHash
