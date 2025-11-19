"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Generate a tutorial for setting up a Polkadot account and using Ledger Live for staking, referencing the specific features mentioned on Polkadot India.
Generated: DETERMINISTIC_be207b15f3789190
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-documented JavaScript/TypeScript tutorial code that demonstrates Polkadot account setup and staking via Ledger Live. This uses the `@polkadot/api` library and includes proper error handling:

```typescript
/**
 * Polkadot Account Setup and Staking Tutorial
 * Demonstrates how to:
 * 1. Create a Polkadot account
 * 2. Connect to Ledger Live
 * 3. Perform staking operations
 * 
 * References Polkadot India features:
 * - Nomination pools
 * - Ledger hardware wallet integration
 * - Staking dashboard functionality
 */

import { ApiPromise, WsProvider } from '@polkadot/api';
import { Keyring } from '@polkadot/keyring';
import { cryptoWaitReady } from '@polkadot/util-crypto';
import { formatBalance } from '@polkadot/util';

// Configuration constants
const POLKADOT_ENDPOINT = 'wss://rpc.polkadot.io';
const LEDGER_LIVE_DERIVATION_PATH = "m/44'/354'/0'/0/0";

interface StakingInfo {
  totalStaked: string;
  activeEra: number;
  rewards: string;
}

class PolkadotStakingTutorial {
  private api: ApiPromise | null = null;

  /**
   * Initialize Polkadot API connection
   */
  async initialize(): Promise<void> {
    try {
      await cryptoWaitReady();
      
      const provider = new WsProvider(POLKADOT_ENDPOINT);
      this.api = await ApiPromise.create({ provider });
      
      console.log('Connected to Polkadot network');
    } catch (error) {
      console.error('Initialization failed:', error);
      throw error;
    }
  }

  /**
   * Create a new Polkadot account (software-based)
   */
  createSoftwareAccount(): { address: string; mnemonic: string } {
    try {
      const keyring = new Keyring({ type: 'sr25519' });
      const pair = keyring.addFromUri(undefined, { name: 'polkadot-tutorial' }, 'sr25519');
      
      return {
        address: pair.address,
        mnemonic: pair.mnemonic || '' // Will be undefined if created from seed
      };
    } catch (error) {
      console.error('Account creation failed:', error);
      throw error;
    }
  }

  /**
   * Simulate connecting to Ledger Live (in a real app, you'd use ledgerhq/hw-app-polkadot)
   */
  async connectLedgerAccount(): Promise<string> {
    try {
      // In a real implementation, you would use:
      // const transport = await TransportWebUSB.create();
      // const polkadot = new Polkadot(transport);
      // const { address } = await polkadot.getAddress(LEDGER_LIVE_DERIVATION_PATH);
      
      // For tutorial purposes, we'll simulate this
      const keyring = new Keyring({ type: 'sr25519' });
      const pair = keyring.addFromUri(`//Ledger${Math.floor(Math.random() * 1000)}`, {}, 'sr25519');
      
      console.log('Simulated Ledger connection - in a real app, use hw-app-polkadot');
      return pair.address;
    } catch (error) {
      console.error('Ledger connection failed:', error);
      throw error;
    }
  }

  /**
   * Get staking information for an account
   */
  async getStakingInfo(accountAddress: string): Promise<StakingInfo> {
    if (!this.api) throw new Error('API not initialized');
    
    try {
      const [activeEra, stakingInfo, rewards] = await Promise.all([
        this.api.query.staking.activeEra(),
        this.api.query.staking.nominators(accountAddress),
        this.api.derive.staking.account(accountAddress)
      ]);

      return {
        totalStaked: formatBalance(stakingInfo.unwrapOrDefault().total.toBn()),
        activeEra: activeEra.unwrapOrDefault().index.toNumber(),
        rewards: formatBalance(rewards.claimedRewards)
      };
    } catch (error) {
      console.error('Failed to get staking info:', error);
      throw error;
    }
  }

  /**
   * Join a nomination pool (simplified example)
   */
  async joinNominationPool(accountAddress: string, poolId: number, amount: string): Promise<void> {
    if (!this.api) throw new Error('API not initialized');
    
    try {
      // In a real implementation, you would sign with Ledger
      const tx = this.api.tx.nominationPools.join(poolId, amount);
      
      console.log(`Transaction created to join pool ${poolId} with ${amount} DOT`);
      // await tx.signAndSend(accountAddress, { signer: ledgerSigner });
      
      console.log('Simulated transaction - in a real app, this would be signed by Ledger');
    } catch (error) {
      console.error('Failed to join nomination pool:', error);
      throw error;
    }
  }

  /**
   * Clean up resources
   */
  async disconnect(): Promise<void> {
    try {
      if (this.api) {
        await this.api.disconnect();
        console.log('Disconnected from Polkadot network');
      }
    } catch (error) {
      console.error('Disconnection failed:', error);
    }
  }
}

// Example usage
(async () => {
  const tutorial = new PolkadotStakingTutorial();
  
  try {
    // 1. Initialize connection
    await tutorial.initialize();
    
    // 2. Create software account (alternative to Ledger)
    const softwareAccount = tutorial.createSoftwareAccount();
    console.log('Software account created:', softwareAccount.address);
    
    // 3. Connect Ledger account
    const ledgerAccount = await tutorial.connectLedgerAccount();
    console.log('Ledger account address:', ledgerAccount);
    
    // 4. Get staking info
    const stakingInfo = await tutorial.getStakingInfo(ledgerAccount);
    console.log('Staking information:', stakingInfo);
    
    // 5. Join nomination pool (simulated)
    await tutorial.joinNominationPool(ledgerAccount, 1, '1000000000000'); // 1 DOT
    
  } catch (error) {
    console.error('Tutorial failed:', error);
  } finally {
    await tutorial.disconnect();
  }
})();
```

Note: This is a simulation tutorial. For actual Ledger integration, you would need to:
1. Install `@ledgerhq/hw-app-polkadot`
2. Use WebUSB or HID transport
3. Implement proper transaction signing with the hardware wallet

The code follows Polkadot India's recommended practices by:
- Using nomination pools
- Demonstrating hardware wallet integration path
- Including staking information retrieval
- Following Polkadot.js best practices
