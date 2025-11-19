"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Generate TypeScript client library code for interacting with a blockchain smart contract using Código's code generation feature.
Generated: DETERMINISTIC_7a4965310586cb76
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// blockchain-client.ts
// TypeScript client library for interacting with a blockchain smart contract
// Generated using Código's code generation feature

import { ethers, Contract, providers, Signer } from 'ethers';
import { TransactionResponse } from '@ethersproject/abstract-provider';

/**
 * Configuration interface for the blockchain client
 */
interface BlockchainClientConfig {
  contractAddress: string;
  providerOrSigner: providers.Provider | Signer;
  abi: any[];
}

/**
 * Represents a blockchain client for interacting with smart contracts
 */
export class BlockchainClient {
  private contract: Contract;
  private readonly config: BlockchainClientConfig;

  /**
   * Creates an instance of BlockchainClient
   * @param config Configuration object containing contract details
   */
  constructor(config: BlockchainClientConfig) {
    if (!config.contractAddress || !config.providerOrSigner || !config.abi) {
      throw new Error('Invalid configuration: Missing required parameters');
    }

    this.config = config;
    this.contract = new ethers.Contract(
      config.contractAddress,
      config.abi,
      config.providerOrSigner
    );
  }

  /**
   * Calls a read-only function on the smart contract
   * @param functionName Name of the function to call
   * @param args Arguments to pass to the function
   * @returns Promise containing the function result
   */
  public async callViewFunction<T>(
    functionName: string,
    ...args: any[]
  ): Promise<T> {
    try {
      if (!this.contract[functionName]) {
        throw new Error(`Function ${functionName} not found in contract ABI`);
      }

      return await this.contract[functionName](...args);
    } catch (error) {
      throw new Error(
        `Error calling view function ${functionName}: ${error instanceof Error ? error.message : String(error)}`
      );
    }
  }

  /**
   * Sends a transaction to execute a contract function
   * @param functionName Name of the function to call
   * @param args Arguments to pass to the function
   * @returns Promise containing the transaction response
   */
  public async sendTransaction(
    functionName: string,
    ...args: any[]
  ): Promise<TransactionResponse> {
    try {
      if (!this.contract[functionName]) {
        throw new Error(`Function ${functionName} not found in contract ABI`);
      }

      if (!('sendTransaction' in this.config.providerOrSigner)) {
        throw new Error('Current provider is not a signer');
      }

      return await this.contract[functionName](...args);
    } catch (error) {
      throw new Error(
        `Error sending transaction for function ${functionName}: ${error instanceof Error ? error.message : String(error)}`
      );
    }
  }

  /**
   * Gets the current contract address
   * @returns The contract address
   */
  public getContractAddress(): string {
    return this.config.contractAddress;
  }

  /**
   * Gets the current contract ABI
   * @returns The contract ABI
   */
  public getContractABI(): any[] {
    return this.config.abi;
  }

  /**
   * Gets the contract instance
   * @returns The ethers.js Contract instance
   */
  public getContractInstance(): Contract {
    return this.contract;
  }
}

/**
 * Factory function to create a BlockchainClient instance
 * @param config Configuration for the client
 * @returns Initialized BlockchainClient instance
 */
export function createBlockchainClient(
  config: BlockchainClientConfig
): BlockchainClient {
  return new BlockchainClient(config);
}
```
