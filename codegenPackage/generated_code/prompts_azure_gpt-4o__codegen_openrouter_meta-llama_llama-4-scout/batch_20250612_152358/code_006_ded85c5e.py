"""
Generated Code Metadata:
========================
Original URL: https://bafybeicc34wxgmwfldpiehsmb6azuurx52lonvbu63phtv6fto7rbacmja.ipfs.dweb.link
Prompt: Create a script to deploy Hyperlane on a blockchain and configure it to relay messages across multiple virtual machines (VMs). Include details on how to support 5+ VMs as described in the Hyperlane documentation.
Generated: DETERMINISTIC_ded85c5e26e77dcc
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID_${chainId}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { ethers } = require('ethers');
const { Hyperlane } = require('@hyperlane-xyz/sdk');

// Define constants for deployment
const CHAIN_IDS = [1, 5, 10, 42, 42161]; // Example chain IDs for 5+ VMs
const RELAYER_PRIVATE_KEY = '0x...'; // Replace with relayer private key
const MAILBOX_CONTRACT_ADDRESS = '0x...'; // Replace with mailbox contract address

// Define Hyperlane deployment function
async function deployHyperlane() {
  try {
    // Initialize Hyperlane instance
    const hyperlane = new Hyperlane({
      // Specify chain IDs and provider URLs for each chain
      chains: CHAIN_IDS.map((chainId) => ({
        chainId,
        providerUrl: `https://mainnet.infura.io/v3/YOUR_PROJECT_ID_${chainId}`,
      })),
    });

    // Deploy Mailbox contracts on each chain
    const mailboxes = await Promise.all(
      CHAIN_IDS.map(async (chainId) => {
        const mailbox = await hyperlane.mailbox.deploy(chainId);
        return mailbox.address;
      })
    );

    // Deploy Relayer contract
    const relayer = await hyperlane.relayer.deploy(MAILER_CONTRACT_ADDRESS);

    // Configure Relayer to relay messages across VMs
    await relayer.configureRelayer({
      // Specify Mailbox contract addresses for each chain
      mailboxes,
      // Specify relayer private key
      relayerPrivateKey: RELAYER_PRIVATE_KEY,
    });

    // Verify Mailbox and Relayer contracts on each chain
    await Promise.all(
      CHAIN_IDS.map(async (chainId) => {
        const mailboxAddress = mailboxes.find(
          (address) => address.chainId === chainId
        );
        await hyperlane.mailbox.verify(chainId, mailboxAddress);
        await hyperlane.relayer.verify(chainId, relayer.address);
      })
    );

    console.log('Hyperlane deployment successful!');
  } catch (error) {
    console.error('Error deploying Hyperlane:', error);
  }
}

// Run deployment function
deployHyperlane();
```

```typescript
// hyperlane.ts
import { ethers } from 'ethers';
import { Hyperlane } from '@hyperlane-xyz/sdk';

/**
 * Deploy Hyperlane on a blockchain and configure it to relay messages across multiple virtual machines (VMs).
 */
export class HyperlaneDeployment {
  private readonly chainIds: number[];
  private readonly relayerPrivateKey: string;
  private readonly mailboxContractAddress: string;

  constructor(chainIds: number[], relayerPrivateKey: string, mailboxContractAddress: string) {
    this.chainIds = chainIds;
    this.relayerPrivateKey = relayerPrivateKey;
    this.mailboxContractAddress = mailboxContractAddress;
  }

  /**
   * Initialize Hyperlane instance.
   */
  private async initHyperlane(): Promise<Hyperlane> {
    const providers = this.chainIds.map((chainId) => ({
      chainId,
      providerUrl: `https://mainnet.infura.io/v3/YOUR_PROJECT_ID_${chainId}`,
    }));

    return new Hyperlane({ chains: providers });
  }

  /**
   * Deploy Mailbox contracts on each chain.
   */
  private async deployMailboxes(hyperlane: Hyperlane): Promise<string[]> {
    return Promise.all(
      this.chainIds.map(async (chainId) => {
        const mailbox = await hyperlane.mailbox.deploy(chainId);
        return mailbox.address;
      })
    );
  }

  /**
   * Deploy Relayer contract.
   */
  private async deployRelayer(hyperlane: Hyperlane): Promise<ethers.Contract> {
    return hyperlane.relayer.deploy(this.mailboxContractAddress);
  }

  /**
   * Configure Relayer to relay messages across VMs.
   */
  private async configureRelayer(relayer: ethers.Contract, mailboxes: string[]): Promise<void> {
    await relayer.configureRelayer({
      mailboxes,
      relayerPrivateKey: this.relayerPrivateKey,
    });
  }

  /**
   * Verify Mailbox and Relayer contracts on each chain.
   */
  private async verifyContracts(hyperlane: Hyperlane, mailboxes: string[], relayer: ethers.Contract): Promise<void> {
    await Promise.all(
      this.chainIds.map(async (chainId) => {
        const mailboxAddress = mailboxes.find((address) => address.chainId === chainId);
        await hyperlane.mailbox.verify(chainId, mailboxAddress);
        await hyperlane.relayer.verify(chainId, relayer.address);
      })
    );
  }

  /**
   * Deploy and configure Hyperlane.
   */
  public async deploy(): Promise<void> {
    try {
      const hyperlane = await this.initHyperlane();
      const mailboxes = await this.deployMailboxes(hyperlane);
      const relayer = await this.deployRelayer(hyperlane);
      await this.configureRelayer(relayer, mailboxes);
      await this.verifyContracts(hyperlane, mailboxes, relayer);

      console.log('Hyperlane deployment successful!');
    } catch (error) {
      console.error('Error deploying Hyperlane:', error);
    }
  }
}

// Usage
const chainIds = [1, 5, 10, 42, 42161];
const relayerPrivateKey = '0x...';
const mailboxContractAddress = '0x...';

const deployment = new HyperlaneDeployment(chainIds, relayerPrivateKey, mailboxContractAddress);
deployment.deploy();
```
