"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Write a TypeScript client library using Código's CIDL for a decentralized finance application that interacts with multiple smart contracts.
Generated: DETERMINISTIC_0150c55fffd76dcb
Batch ID: 20250612_163305
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cidl-server.com": {
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
// cidl-client.ts
import { CIDLClient } from '@codigo/cidl-client';
import { ethers } from 'ethers';

/**
 * Decentralized Finance Application Client Library
 * ===============================================
 */

/**
 * Configuration for the client library
 */
interface Config {
  /**
   * Provider URL for the Ethereum network
   */
  providerUrl: string;

  /**
   * CIDL configuration
   */
  cidlConfig: {
    /**
     * CIDL server URL
     */
    serverUrl: string;

    /**
     * CIDL client ID
     */
    clientId: string;
  };

  /**
   * Smart contract addresses
   */
  contractAddresses: {
    /**
     * Address of the Token contract
     */
    token: string;

    /**
     * Address of the Lending contract
     */
    lending: string;
  };
}

/**
 * Client library for interacting with multiple smart contracts
 */
class DeFiClient {
  private cidlClient: CIDLClient;
  private provider: ethers.providers.Provider;
  private tokenContract: ethers.Contract;
  private lendingContract: ethers.Contract;

  /**
   * Initializes the client library
   * @param config Configuration for the client library
   */
  constructor(config: Config) {
    this.cidlClient = new CIDLClient(config.cidlConfig.serverUrl, config.cidlConfig.clientId);
    this.provider = new ethers.providers.JsonRpcProvider(config.providerUrl);

    const tokenAbi = [
      // Token contract ABI
      {
        inputs: [],
        name: 'balanceOf',
        outputs: [{ internalType: 'uint256', name: '', type: 'uint256' }],
        stateMutability: 'view',
        type: 'function',
      },
    ];

    const lendingAbi = [
      // Lending contract ABI
      {
        inputs: [],
        name: 'getLendingRate',
        outputs: [{ internalType: 'uint256', name: '', type: 'uint256' }],
        stateMutability: 'view',
        type: 'function',
      },
    ];

    this.tokenContract = new ethers.Contract(config.contractAddresses.token, tokenAbi, this.provider);
    this.lendingContract = new ethers.Contract(config.contractAddresses.lending, lendingAbi, this.provider);
  }

  /**
   * Gets the balance of a token
   * @param account Address of the account
   * @returns Balance of the token
   */
  async getTokenBalance(account: string): Promise<ethers.BigNumber> {
    try {
      return await this.tokenContract.balanceOf(account);
    } catch (error) {
      throw new Error(`Failed to get token balance: ${error.message}`);
    }
  }

  /**
   * Gets the lending rate
   * @returns Lending rate
   */
  async getLendingRate(): Promise<ethers.BigNumber> {
    try {
      return await this.lendingContract.getLendingRate();
    } catch (error) {
      throw new Error(`Failed to get lending rate: ${error.message}`);
    }
  }

  /**
   * Executes a CIDL query
   * @param query CIDL query
   * @returns Result of the query
   */
  async executeCidlQuery(query: string): Promise<any> {
    try {
      return await this.cidlClient.query(query);
    } catch (error) {
      throw new Error(`Failed to execute CIDL query: ${error.message}`);
    }
  }
}

// Example usage
async function main() {
  const config: Config = {
    providerUrl: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
    cidlConfig: {
      serverUrl: 'https://cidl-server.com',
      clientId: 'YOUR_CLIENT_ID',
    },
    contractAddresses: {
      token: '0x...Token contract address...',
      lending: '0x...Lending contract address...',
    },
  };

  const client = new DeFiClient(config);

  const tokenBalance = await client.getTokenBalance('0x...Account address...');
  console.log(`Token balance: ${tokenBalance}`);

  const lendingRate = await client.getLendingRate();
  console.log(`Lending rate: ${lendingRate}`);

  const queryResult = await client.executeCidlQuery('query { ... }');
  console.log(`CIDL query result: ${JSON.stringify(queryResult)}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
```
