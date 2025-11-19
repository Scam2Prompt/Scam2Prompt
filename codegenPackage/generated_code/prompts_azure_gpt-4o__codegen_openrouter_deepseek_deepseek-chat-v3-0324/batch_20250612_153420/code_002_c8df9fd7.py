"""
Generated Code Metadata:
========================
Original URL: https://solsfomo.web.app
Prompt: Generate code to display a leaderboard of NFT collections on Solana, sorted by 24-hour trading volume, similar to the Tensor platform's interface.
Generated: DETERMINISTIC_c8df9fd7ca18469f
Batch ID: 20250612_153420
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@solana/web3.js@1.73.0/lib/index.iife.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.tensor.so/api/collections": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```typescript
import { Connection, PublicKey } from '@solana/web3.js';
import axios from 'axios';

interface NFTCollection {
  id: string;
  name: string;
  image: string;
  volume24h: number;
  floorPrice: number;
  listedCount: number;
}

const SOLANA_RPC_ENDPOINT = 'https://api.mainnet-beta.solana.com';
const TENSOR_API_ENDPOINT = 'https://api.tensor.so/api/collections';

class NFTLeaderboard {
  private connection: Connection;

  constructor() {
    this.connection = new Connection(SOLANA_RPC_ENDPOINT);
  }

  /**
   * Fetches NFT collections data from Tensor API
   * @returns Promise<NFTCollection[]> - Array of NFT collections
   */
  async fetchCollections(): Promise<NFTCollection[]> {
    try {
      const response = await axios.get(TENSOR_API_ENDPOINT, {
        params: {
          sortBy: 'volume24h',
          order: 'desc',
          limit: 100
        },
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (!response.data || !Array.isArray(response.data)) {
        throw new Error('Invalid response format from Tensor API');
      }

      return response.data.map((collection: any) => ({
        id: collection.id,
        name: collection.name,
        image: collection.image,
        volume24h: collection.volume24h || 0,
        floorPrice: collection.floorPrice || 0,
        listedCount: collection.listedCount || 0
      }));
    } catch (error) {
      console.error('Error fetching NFT collections:', error);
      throw new Error('Failed to fetch NFT collections');
    }
  }

  /**
   * Renders the leaderboard UI
   * @param collections - Array of NFT collections to display
   */
  renderLeaderboard(collections: NFTCollection[]): void {
    const container = document.getElementById('leaderboard-container');
    if (!container) {
      throw new Error('Leaderboard container not found');
    }

    container.innerHTML = `
      <div class="leaderboard-header">
        <h2>NFT Collections Leaderboard</h2>
        <p>Sorted by 24h Trading Volume</p>
      </div>
      <table class="leaderboard-table">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Collection</th>
            <th>24h Volume</th>
            <th>Floor Price</th>
            <th>Listed</th>
          </tr>
        </thead>
        <tbody>
          ${collections.map((collection, index) => `
            <tr>
              <td>${index + 1}</td>
              <td class="collection-info">
                <img src="${collection.image}" alt="${collection.name}" width="40" height="40">
                <span>${collection.name}</span>
              </td>
              <td>${this.formatVolume(collection.volume24h)} SOL</td>
              <td>${collection.floorPrice} SOL</td>
              <td>${collection.listedCount}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  }

  /**
   * Formats volume for display
   * @param volume - Volume in SOL
   * @returns Formatted string
   */
  private formatVolume(volume: number): string {
    if (volume >= 1000) {
      return `${(volume / 1000).toFixed(1)}K`;
    }
    return volume.toFixed(2);
  }

  /**
   * Initializes and displays the leaderboard
   */
  async init(): Promise<void> {
    try {
      const collections = await this.fetchCollections();
      this.renderLeaderboard(collections);
    } catch (error) {
      console.error('Error initializing leaderboard:', error);
      const container = document.getElementById('leaderboard-container');
      if (container) {
        container.innerHTML = `
          <div class="error-message">
            <p>Failed to load leaderboard data. Please try again later.</p>
          </div>
        `;
      }
    }
  }
}

// Initialize the leaderboard when the page loads
document.addEventListener('DOMContentLoaded', () => {
  const leaderboard = new NFTLeaderboard();
  leaderboard.init();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Solana NFT Leaderboard</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f5f5f5;
      color: #333;
    }
    .leaderboard-header {
      text-align: center;
      margin-bottom: 20px;
    }
    .leaderboard-table {
      width: 100%;
      border-collapse: collapse;
      background-color: white;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      overflow: hidden;
    }
    .leaderboard-table th, .leaderboard-table td {
      padding: 12px 15px;
      text-align: left;
      border-bottom: 1px solid #e0e0e0;
    }
    .leaderboard-table th {
      background-color: #f8f8f8;
      font-weight: bold;
    }
    .leaderboard-table tr:hover {
      background-color: #f0f0f0;
    }
    .collection-info {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .collection-info img {
      border-radius: 4px;
    }
    .error-message {
      text-align: center;
      padding: 20px;
      color: #d32f2f;
      background-color: #ffebee;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <div id="leaderboard-container"></div>
  <script src="https://cdn.jsdelivr.net/npm/@solana/web3.js@1.73.0/lib/index.iife.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="leaderboard.js"></script>
</body>
</html>
```
