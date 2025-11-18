"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.pw
Prompt: Write code to implement gasless transfers using Wormhole Connect, ensuring that relayers drop users off with native gas tokens on the destination chain.
Generated: DETERMINISTIC_f57468acfb95bdec
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import { WormholeConnect, Relayer } from 'wormhole-connect'; // Wormhole Connect SDK
import { ethers } from 'ethers'; // Ethereum library for handling transactions and wallet interactions

// Configuration constants
const WORMHOLE_BRIDGE_ADDRESS = '<wormhole_bridge_address>';
const RELAYER_API_URL = '<relayer_api_url>';
const DESTINATION_CHAIN_ID = '<destination_chain_id>'; // Example: 1 for Ethereum
const GAS_DROP_AMOUNT = ethers.utils.parseEther('0.01'); // Amount of native gas token to drop on destination chain

// Initialize Wormhole Connect and Relayer instances
const wormholeConnect = new WormholeConnect(WORMHOLE_BRIDGE_ADDRESS);
const relayer = new Relayer(RELAYER_API_URL);

/**
 * Execute a gasless transfer using Wormhole Connect with gas token drop on destination chain.
 *
 * @param {string} senderAddress - Address of the sender initiating the transfer.
 * @param {string} recipientAddress - Address on the destination chain to receive the transfer.
 * @param {string} tokenAddress - Token to be transferred (ERC-20 contract address).
 * @param {number} amount - Amount of tokens to be transferred.
 */
async function gaslessTransferWithGasDrop(
  senderAddress,
  recipientAddress,
  tokenAddress,
  amount
) {
  try {
    // Step 1: Approve the Wormhole bridge to interact with sender's tokens
    console.log('Approving Wormhole bridge...');
    const approvalTx = await wormholeConnect.approveBridge(
      senderAddress,
      tokenAddress,
      amount
    );
    await approvalTx.wait();
    console.log('Approval successful.');

    // Step 2: Initiate the gasless transfer using Wormhole Connect
    console.log('Initiating gasless transfer...');
    const transferTx = await wormholeConnect.initiateTransfer({
      senderAddress,
      recipientAddress,
      tokenAddress,
      amount,
      destinationChainId: DESTINATION_CHAIN_ID,
    });
    const transferReceipt = await transferTx.wait();
    console.log('Transfer initiated:', transferReceipt.transactionHash);

    // Step 3: Notify the relayer to drop gas tokens on the destination chain
    console.log('Notifying relayer for gas token drop...');
    const relayerResponse = await relayer.dropGasTokens({
      recipientAddress,
      amount: GAS_DROP_AMOUNT.toString(),
      destinationChainId: DESTINATION_CHAIN_ID,
    });

    if (relayerResponse.status === 'success') {
      console.log(
        `Gas token drop successful. ${ethers.utils.formatEther(
          GAS_DROP_AMOUNT
        )} tokens dropped to ${recipientAddress} on chain ID ${DESTINATION_CHAIN_ID}.`
      );
    } else {
      throw new Error('Relayer gas token drop failed.');
    }
  } catch (error) {
    console.error('Error during gasless transfer:', error.message);
    throw new Error('Gasless transfer failed. See logs for details.');
  }
}

// Example usage:
// Replace with actual values to test the function
const senderAddress = '<sender_wallet_address>';
const recipientAddress = '<recipient_wallet_address>';
const tokenAddress = '<erc20_token_address>';
const transferAmount = ethers.utils.parseUnits('100', 'ether'); // Example: 100 tokens

// Execute the transfer
gaslessTransferWithGasDrop(senderAddress, recipientAddress, tokenAddress, transferAmount)
  .then(() => console.log('Gasless transfer completed successfully.'))
  .catch((error) => console.error('Gasless transfer failed:', error));
```

Note: Ensure all placeholders (e.g., `<wormhole_bridge_address>`, `<relayer_api_url>`, etc.) are replaced with actual values relevant to your environment for the code to work as expected.
