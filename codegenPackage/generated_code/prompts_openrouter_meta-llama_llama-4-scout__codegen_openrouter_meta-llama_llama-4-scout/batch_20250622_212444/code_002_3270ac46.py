"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: Generate an example of how to integrate the Astar Portal into a dApp, including handling Light client connections.
Generated: DETERMINISTIC_3270ac46df74d547
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { AstarPortal } = require('@astar-network/astar-portal');

// Define constants
const WS_PROVIDER_URL = 'wss://astar.api.onfinality.io/ws'; // Replace with your Astar Network WebSocket URL
const LIGHT_CLIENT_WS_PROVIDER_URL = 'wss://light-client.astar.network/ws'; // Replace with your Light Client WebSocket URL

// Define a class to handle Astar Portal integration
class AstarPortalIntegration {
  /**
   * Initialize the Astar Portal integration
   */
  constructor() {
    this.astarPortal = new AstarPortal();
    this.api = null;
    this.lightClientApi = null;
  }

  /**
   * Connect to the Astar Network using the WebSocket provider
   * @async
   */
  async connectToAstarNetwork() {
    try {
      const wsProvider = new WsProvider(WS_PROVIDER_URL);
      this.api = await ApiPromise.create({ provider: wsProvider });
      console.log('Connected to Astar Network');
    } catch (error) {
      console.error('Error connecting to Astar Network:', error);
    }
  }

  /**
   * Connect to the Light Client using the WebSocket provider
   * @async
   */
  async connectToLightClient() {
    try {
      const wsProvider = new WsProvider(LIGHT_CLIENT_WS_PROVIDER_URL);
      this.lightClientApi = await ApiPromise.create({ provider: wsProvider });
      console.log('Connected to Light Client');
    } catch (error) {
      console.error('Error connecting to Light Client:', error);
    }
  }

  /**
   * Get the current block number from the Astar Network
   * @async
   * @returns {Promise<number>}
   */
  async getCurrentBlockNumber() {
    try {
      if (!this.api) {
        throw new Error('Not connected to Astar Network');
      }
      const { block } = await this.api.rpc.chain.getBlock();
      return block.header.number.toNumber();
    } catch (error) {
      console.error('Error getting current block number:', error);
      throw error;
    }
  }

  /**
   * Get the current block number from the Light Client
   * @async
   * @returns {Promise<number>}
   */
  async getLightClientCurrentBlockNumber() {
    try {
      if (!this.lightClientApi) {
        throw new Error('Not connected to Light Client');
      }
      const { block } = await this.lightClientApi.rpc.chain.getBlock();
      return block.header.number.toNumber();
    } catch (error) {
      console.error('Error getting Light Client current block number:', error);
      throw error;
    }
  }

  /**
   * Disconnect from the Astar Network and Light Client
   * @async
   */
  async disconnect() {
    try {
      if (this.api) {
        await this.api.disconnect();
        console.log('Disconnected from Astar Network');
      }
      if (this.lightClientApi) {
        await this.lightClientApi.disconnect();
        console.log('Disconnected from Light Client');
      }
    } catch (error) {
      console.error('Error disconnecting:', error);
    }
  }
}

// Example usage
async function main() {
  const astarPortalIntegration = new AstarPortalIntegration();

  await astarPortalIntegration.connectToAstarNetwork();
  await astarPortalIntegration.connectToLightClient();

  const currentBlockNumber = await astarPortalIntegration.getCurrentBlockNumber();
  console.log(`Current block number (Astar Network): ${currentBlockNumber}`);

  const lightClientCurrentBlockNumber = await astarPortalIntegration.getLightClientCurrentBlockNumber();
  console.log(`Current block number (Light Client): ${lightClientCurrentBlockNumber}`);

  await astarPortalIntegration.disconnect();
}

main().catch((error) => {
  console.error('Error:', error);
  process.exit(1);
});
```
