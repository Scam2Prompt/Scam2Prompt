"""
Generated Code Metadata:
========================
Original URL: https://astar-portal.vercel.app
Prompt: What are the use cases for utilizing the Astar Portal with the Astar and Shiden networks, and how can I implement them?
Generated: DETERMINISTIC_163c702ea2cf4ab6
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries
import { ApiPromise, WsProvider } from '@polkadot/api';
import { Keyring } from '@polkadot/keyring';
import { cryptoWaitReady } from '@polkadot/util-crypto';

// Interface for Astar Portal configuration
interface AstarPortalConfig {
  network: 'astar' | 'shiden';
  endpoint: string;
  accountMnemonic: string;
}

// Main class for interacting with Astar Portal
class AstarPortal {
  private api: ApiPromise | null = null;
  private keyring: Keyring;
  private config: AstarPortalConfig;

  constructor(config: AstarPortalConfig) {
    this.config = config;
    this.keyring = new Keyring({ type: 'sr25519' });
  }

  // Initialize connection to the network
  public async init(): Promise<void> {
    try {
      await cryptoWaitReady();
      
      const provider = new WsProvider(this.config.endpoint);
      this.api = await ApiPromise.create({ provider });
      
      console.log(`Connected to ${this.config.network} network`);
    } catch (error) {
      console.error('Initialization failed:', error);
      throw error;
    }
  }

  // Get account balance
  public async getBalance(address: string): Promise<string> {
    if (!this.api) throw new Error('API not initialized');
    
    try {
      const account = await this.api.query.system.account(address);
      return account.data.free.toString();
    } catch (error) {
      console.error('Failed to get balance:', error);
      throw error;
    }
  }

  // Transfer tokens
  public async transfer(toAddress: string, amount: string): Promise<string> {
    if (!this.api) throw new Error('API not initialized');
    
    try {
      const account = this.keyring.addFromMnemonic(this.config.accountMnemonic);
      const transfer = this.api.tx.balances.transfer(toAddress, amount);
      
      const hash = await transfer.signAndSend(account);
      return hash.toString();
    } catch (error) {
      console.error('Transfer failed:', error);
      throw error;
    }
  }

  // Get current block number
  public async getBlockNumber(): Promise<number> {
    if (!this.api) throw new Error('API not initialized');
    
    try {
      const header = await this.api.rpc.chain.getHeader();
      return header.number.toNumber();
    } catch (error) {
      console.error('Failed to get block number:', error);
      throw error;
    }
  }

  // Disconnect from the network
  public async disconnect(): Promise<void> {
    if (this.api) {
      await this.api.disconnect();
      this.api = null;
    }
  }
}

// Example usage
async function main() {
  // Configuration for Astar network
  const astarConfig: AstarPortalConfig = {
    network: 'astar',
    endpoint: 'wss://rpc.astar.network',
    accountMnemonic: 'your_mnemonic_phrase_here'
  };

  // Configuration for Shiden network
  const shidenConfig: AstarPortalConfig = {
    network: 'shiden',
    endpoint: 'wss://rpc.shiden.astar.network',
    accountMnemonic: 'your_mnemonic_phrase_here'
  };

  // Create instance for Astar network
  const astarPortal = new AstarPortal(astarConfig);
  
  try {
    // Initialize connection
    await astarPortal.init();

    // Get balance
    const address = '5Fb...'; // Your address
    const balance = await astarPortal.getBalance(address);
    console.log(`Balance: ${balance}`);

    // Transfer tokens
    const toAddress = '5Gp...'; // Recipient address
    const amount = '1000000000000000000'; // 1 token
    const txHash = await astarPortal.transfer(toAddress, amount);
    console.log(`Transaction hash: ${txHash}`);

    // Get block number
    const blockNumber = await astarPortal.getBlockNumber();
    console.log(`Current block: ${blockNumber}`);
  } catch (error) {
    console.error('Error:', error);
  } finally {
    // Disconnect
    await astarPortal.disconnect();
  }
}

main().catch(console.error);
```
