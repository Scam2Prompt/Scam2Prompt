"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.pw
Prompt: Generate a code snippet using Wormhole Connect to allow users to bridge wrapped or native assets between blockchains with only 3 lines of code.
Generated: DETERMINISTIC_fbbbc4a05d569aa7
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Wormhole Connect library
import { WormholeConnect } from '@wormhole-foundation/wormhole-connect';

// Initialize the Wormhole Connect SDK with configuration
const wormhole = new WormholeConnect({ apiKey: 'YOUR_API_KEY' });  // Replace 'YOUR_API_KEY' with your actual API key

// Function to bridge assets between blockchains
async function bridgeAssets(asset, fromChain, toChain, amount) {
  try {
    // Bridge the specified asset
    const transaction = await wormhole.bridge({ 
      asset,         // Asset to bridge (e.g., 'ETH', 'USDC')
      fromChain,     // Source blockchain (e.g., 'ethereum')
      toChain,       // Target blockchain (e.g., 'solana')
      amount         // Amount of the asset to bridge
    });
    console.log('Transaction successful:', transaction);
  } catch (error) {
    console.error('Error during asset bridging:', error); // Handle any errors gracefully
  }
}

// Example usage: Bridge 0.1 ETH from Ethereum to Solana
bridgeAssets('ETH', 'ethereum', 'solana', 0.1);
```
