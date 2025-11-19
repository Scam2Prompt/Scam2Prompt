"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: Write a function to manage Light client connections in the Astar Portal for the Astar & Shiden Network.
Generated: DETERMINISTIC_bd19a49e012fd5e9
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary libraries and types
import { ApiPromise, WsProvider } from '@polkadot/api';
import { typesBundleForPolkadot } from '@astar-network/astar-sdk-core';

// Define network types
type Network = 'astar' | 'shiden';
type ConnectionStatus = 'connected' | 'disconnected' | 'connecting' | 'error';

// Interface for connection manager
interface LightClientConnection {
  api: ApiPromise | null;
  status: ConnectionStatus;
  network: Network;
  endpoint: string;
}

// Default endpoints for each network
const DEFAULT_ENDPOINTS: Record<Network, string> = {
  astar: 'wss://rpc.astar.network',
  shiden: 'wss://rpc.shiden.astar.network'
};

class LightClientConnectionManager {
  private connection: LightClientConnection;

  constructor(network: Network, customEndpoint?: string) {
    this.connection = {
      api: null,
      status: 'disconnected',
      network,
      endpoint: customEndpoint || DEFAULT_ENDPOINTS[network]
    };
  }

  /**
   * Connects to the network using light client
   * @returns Promise<ApiPromise> The connected API instance
   */
  public async connect(): Promise<ApiPromise> {
    if (this.connection.status === 'connected' && this.connection.api) {
      return this.connection.api;
    }

    this.connection.status = 'connecting';

    try {
      const provider = new WsProvider(this.connection.endpoint);
      const api = await ApiPromise.create({
        provider,
        typesBundle: typesBundleForPolkadot
      });

      await api.isReady;

      this.connection.api = api;
      this.connection.status = 'connected';

      return api;
    } catch (error) {
      this.connection.status = 'error';
      throw new Error(`Failed to connect to ${this.connection.network}: ${error instanceof Error ? error.message : String(error)}`);
    }
  }

  /**
   * Disconnects from the network
   */
  public async disconnect(): Promise<void> {
    if (this.connection.status === 'disconnected' || !this.connection.api) {
      return;
    }

    try {
      await this.connection.api.disconnect();
      this.connection.api = null;
      this.connection.status = 'disconnected';
    } catch (error) {
      this.connection.status = 'error';
      throw new Error(`Failed to disconnect from ${this.connection.network}: ${error instanceof Error ? error.message : String(error)}`);
    }
  }

  /**
   * Gets the current connection status
   * @returns ConnectionStatus The current connection status
   */
  public getStatus(): ConnectionStatus {
    return this.connection.status;
  }

  /**
   * Gets the connected API instance
   * @returns ApiPromise | null The connected API instance or null if not connected
   */
  public getApi(): ApiPromise | null {
    return this.connection.api;
  }

  /**
   * Gets the network name
   * @returns Network The network name
   */
  public getNetwork(): Network {
    return this.connection.network;
  }

  /**
   * Gets the current endpoint
   * @returns string The current endpoint
   */
  public getEndpoint(): string {
    return this.connection.endpoint;
  }

  /**
   * Changes the network endpoint
   * @param endpoint The new endpoint to connect to
   */
  public async changeEndpoint(endpoint: string): Promise<void> {
    if (this.connection.endpoint === endpoint) {
      return;
    }

    const wasConnected = this.connection.status === 'connected';
    
    if (wasConnected) {
      await this.disconnect();
    }

    this.connection.endpoint = endpoint;

    if (wasConnected) {
      await this.connect();
    }
  }
}

export { LightClientConnectionManager, Network, ConnectionStatus };
```
