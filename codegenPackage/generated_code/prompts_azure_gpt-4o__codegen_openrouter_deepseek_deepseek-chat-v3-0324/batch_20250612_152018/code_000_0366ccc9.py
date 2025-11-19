"""
Generated Code Metadata:
========================
Original URL: https://analogone.pages.dev
Prompt: Write code using Analog's Watch SDK to build a scalable cross-chain DApp that retrieves Web3 data securely and efficiently. Include examples of General Message Passing (GMP) for cross-chain communication.
Generated: DETERMINISTIC_0366ccc90574cc15
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries and SDKs
import { AnalogWatchSDK, Chain, GMPClient, QueryOptions } from '@analog-labs/watch-sdk';
import { ethers } from 'ethers';
import axios from 'axios';

// Initialize Analog Watch SDK
const analogWatch = new AnalogWatchSDK({
  apiKey: process.env.ANALOG_API_KEY,
  network: Chain.ETHEREUM, // Default chain
});

// Initialize GMP client for cross-chain communication
const gmpClient = new GMPClient({
  analogWatch,
  supportedChains: [Chain.ETHEREUM, Chain.POLYGON, Chain.ARBITRUM],
});

// Interface for Web3 data response
interface Web3Data {
  chainId: number;
  blockNumber: number;
  gasPrice: string;
  contractData?: any;
}

// Main DApp class
class CrossChainDApp {
  private provider: ethers.providers.JsonRpcProvider;

  constructor(rpcUrl: string) {
    this.provider = new ethers.providers.JsonRpcProvider(rpcUrl);
  }

  /**
   * Fetch Web3 data from a specific chain
   * @param chain - Chain identifier
   * @param contractAddress - Optional contract address to query
   * @returns Promise<Web3Data>
   */
  async fetchWeb3Data(chain: Chain, contractAddress?: string): Promise<Web3Data> {
    try {
      // Switch chain in SDK
      analogWatch.switchChain(chain);

      // Get basic chain data
      const [blockNumber, gasPrice] = await Promise.all([
        this.provider.getBlockNumber(),
        this.provider.getGasPrice(),
      ]);

      const result: Web3Data = {
        chainId: chain,
        blockNumber,
        gasPrice: ethers.utils.formatUnits(gasPrice, 'gwei'),
      };

      // If contract address provided, fetch contract data
      if (contractAddress) {
        const contractData = await analogWatch.queryContract({
          address: contractAddress,
          abi: ['function totalSupply() view returns (uint256)'],
          functionName: 'totalSupply',
          args: [],
        } as QueryOptions);
        result.contractData = contractData;
      }

      return result;
    } catch (error) {
      console.error(`Error fetching Web3 data for chain ${chain}:`, error);
      throw new Error(`Failed to fetch Web3 data: ${error.message}`);
    }
  }

  /**
   * Send cross-chain message using GMP
   * @param fromChain - Source chain
   * @param toChain - Destination chain
   * @param message - Message payload
   * @returns Promise<string> - Transaction hash
   */
  async sendCrossChainMessage(
    fromChain: Chain,
    toChain: Chain,
    message: any
  ): Promise<string> {
    try {
      const txHash = await gmpClient.sendMessage({
        fromChain,
        toChain,
        payload: JSON.stringify(message),
      });

      return txHash;
    } catch (error) {
      console.error('Error in cross-chain message:', error);
      throw new Error(`GMP failed: ${error.message}`);
    }
  }

  /**
   * Listen for cross-chain messages
   * @param chain - Chain to listen on
   * @param callback - Callback function when message arrives
   */
  listenForCrossChainMessages(chain: Chain, callback: (message: any) => void) {
    gmpClient.subscribeToMessages(chain, (message) => {
      try {
        const parsedMessage = JSON.parse(message.payload);
        callback(parsedMessage);
      } catch (error) {
        console.error('Error parsing incoming message:', error);
      }
    });
  }
}

// Example usage
(async () => {
  try {
    const dapp = new CrossChainDApp(process.env.RPC_URL!);

    // Fetch Web3 data from Ethereum
    const ethData = await dapp.fetchWeb3Data(Chain.ETHEREUM);
    console.log('Ethereum data:', ethData);

    // Example GMP message
    const message = {
      action: 'transfer',
      amount: '100',
      token: 'USDC',
    };

    // Send cross-chain message
    const txHash = await dapp.sendCrossChainMessage(
      Chain.ETHEREUM,
      Chain.POLYGON,
      message
    );
    console.log('Cross-chain message sent. TX hash:', txHash);

    // Listen for incoming messages
    dapp.listenForCrossChainMessages(Chain.POLYGON, (msg) => {
      console.log('Received cross-chain message:', msg);
    });
  } catch (error) {
    console.error('DApp error:', error);
  }
})();
```
