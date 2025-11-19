"""
Generated Code Metadata:
========================
Original URL: https://lavanetwork.pages.dev
Prompt: Generate a TypeScript implementation using Lava SDK to interact with multiple blockchain networks, including Osmosis and StarkNet, and fetch block data.
Generated: DETERMINISTIC_577d1cdf0cfd13cd
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { LavaSDK } from "@lavanet/lava-sdk";
import { ethers } from "ethers";

// Interface for block data
interface BlockData {
  chainId: string;
  blockNumber: number;
  blockHash: string;
  timestamp: number;
  transactions?: string[];
}

// Configuration for supported chains
const CHAIN_CONFIGS = {
  osmosis: {
    chainId: "osmosis-1",
    rpcInterface: "tendermintrpc",
  },
  starknet: {
    chainId: "SN_MAIN",
    rpcInterface: "starknet",
  },
};

class MultiChainBlockFetcher {
  private lavaSDK: LavaSDK;
  private chainConfigs: typeof CHAIN_CONFIGS;

  constructor(private apiKey: string) {
    this.chainConfigs = CHAIN_CONFIGS;
  }

  /**
   * Initialize Lava SDK for a specific chain
   * @param chainName - Name of the chain to initialize
   */
  private async initSDK(chainName: keyof typeof CHAIN_CONFIGS): Promise<void> {
    const config = this.chainConfigs[chainName];
    if (!config) {
      throw new Error(`Unsupported chain: ${chainName}`);
    }

    this.lavaSDK = await LavaSDK.create({
      privateKey: this.apiKey,
      chainID: config.chainId,
      rpcInterface: config.rpcInterface,
    });
  }

  /**
   * Fetch latest block data for a specific chain
   * @param chainName - Name of the chain to fetch data from
   * @returns Block data
   */
  async fetchLatestBlock(
    chainName: keyof typeof CHAIN_CONFIGS
  ): Promise<BlockData> {
    try {
      await this.initSDK(chainName);
      const config = this.chainConfigs[chainName];

      switch (chainName) {
        case "osmosis":
          return await this.fetchOsmosisBlock();
        case "starknet":
          return await this.fetchStarknetBlock();
        default:
          throw new Error(`Unsupported chain: ${chainName}`);
      }
    } catch (error) {
      console.error(`Error fetching block for ${chainName}:`, error);
      throw error;
    }
  }

  /**
   * Fetch block data from Osmosis chain
   */
  private async fetchOsmosisBlock(): Promise<BlockData> {
    const blockResponse = await this.lavaSDK.sendRelay({
      method: "block",
      params: [],
    });

    const block = blockResponse.result.block;
    return {
      chainId: CHAIN_CONFIGS.osmosis.chainId,
      blockNumber: parseInt(block.header.height),
      blockHash: block.header.hash,
      timestamp: new Date(block.header.time).getTime(),
      transactions: block.data.txs,
    };
  }

  /**
   * Fetch block data from StarkNet chain
   */
  private async fetchStarknetBlock(): Promise<BlockData> {
    const blockResponse = await this.lavaSDK.sendRelay({
      method: "starknet_getBlockWithTxs",
      params: [{ block_number: "latest" }],
    });

    const block = blockResponse.result;
    return {
      chainId: CHAIN_CONFIGS.starknet.chainId,
      blockNumber: parseInt(block.block_number),
      blockHash: block.block_hash,
      timestamp: block.timestamp,
      transactions: block.transactions.map((tx: any) => tx.transaction_hash),
    };
  }

  /**
   * Fetch latest blocks from all supported chains
   */
  async fetchAllLatestBlocks(): Promise<Record<string, BlockData>> {
    const results: Record<string, BlockData> = {};

    for (const chainName of Object.keys(this.chainConfigs) as Array<
      keyof typeof CHAIN_CONFIGS
    >) {
      try {
        results[chainName] = await this.fetchLatestBlock(chainName);
      } catch (error) {
        console.error(`Failed to fetch block for ${chainName}:`, error);
        results[chainName] = null;
      }
    }

    return results;
  }
}

// Example usage
async function main() {
  try {
    const apiKey = process.env.LAVA_API_KEY;
    if (!apiKey) {
      throw new Error("LAVA_API_KEY environment variable not set");
    }

    const fetcher = new MultiChainBlockFetcher(apiKey);

    // Fetch single chain
    const osmosisBlock = await fetcher.fetchLatestBlock("osmosis");
    console.log("Osmosis Block:", osmosisBlock);

    // Fetch all chains
    const allBlocks = await fetcher.fetchAllLatestBlocks();
    console.log("All Blocks:", allBlocks);
  } catch (error) {
    console.error("Error in main:", error);
    process.exit(1);
  }
}

main();
```
