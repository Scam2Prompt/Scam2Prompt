"""
Generated Code Metadata:
========================
Original URL: https://polkadot.org
Prompt: Can you explain how to use Polkadot's bridges to connect with other blockchains?
Generated: DETERMINISTIC_9ab159469efddbbc
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a TypeScript code example demonstrating how to interact with Polkadot's bridges using the `@polkadot/api` library:

```typescript
import { ApiPromise, WsProvider } from '@polkadot/api';

// Example configuration
const BRIDGE_CHAIN_WS = 'wss://bridge-chain.example.com';
const PARACHAIN_WS = 'wss://parachain.example.com';

// Initialize bridge chain connection
async function initBridgeConnection() {
  try {
    const provider = new WsProvider(BRIDGE_CHAIN_WS);
    const api = await ApiPromise.create({ provider });

    console.log(`Connected to bridge chain at ${BRIDGE_CHAIN_WS}`);
    console.log(`Chain: ${await api.rpc.system.chain()}`);
    console.log(`Genesis hash: ${api.genesisHash.toHex()}`);

    return api;
  } catch (error) {
    console.error('Failed to connect to bridge chain:', error);
    throw error;
  }
}

// Initialize parachain connection
async function initParachainConnection() {
  try {
    const provider = new WsProvider(PARACHAIN_WS);
    const api = await ApiPromise.create({ provider });

    console.log(`Connected to parachain at ${PARACHAIN_WS}`);
    console.log(`Chain: ${await api.rpc.system.chain()}`);

    return api;
  } catch (error) {
    console.error('Failed to connect to parachain:', error);
    throw error;
  }
}

// Example of sending a cross-chain message via bridge
async function sendCrossChainMessage(
  bridgeApi: ApiPromise,
  parachainApi: ApiPromise,
  senderAddress: string,
  recipientAddress: string,
  amount: number
) {
  try {
    // Construct the transfer extrinsic
    const transferExtrinsic = bridgeApi.tx.bridgeTransfer.send(
      parachainApi.genesisHash,
      recipientAddress,
      amount
    );

    // Sign and send the transaction
    const hash = await transferExtrinsic.signAndSend(senderAddress);

    console.log(`Transaction sent with hash: ${hash.toHex()}`);
    return hash;
  } catch (error) {
    console.error('Failed to send cross-chain message:', error);
    throw error;
  }
}

// Main execution flow
async function main() {
  try {
    const bridgeApi = await initBridgeConnection();
    const parachainApi = await initParachainConnection();

    // Example addresses - replace with actual addresses
    const sender = '5Fbpc5Wj4vX2Qr5Jic5VZ7JLQGFNfZ6Q2q1J3YJ5RZvq1jK';
    const recipient = '5Efpc5Wj4vX2Qr5Jic5VZ7JLQGFNfZ6Q2q1J3YJ5RZvq1jK';
    const amount = 1000000000000; // 1 DOT (in Planck)

    await sendCrossChainMessage(bridgeApi, parachainApi, sender, recipient, amount);
  } catch (error) {
    console.error('Application error:', error);
    process.exit(1);
  }
}

main().catch(console.error);
```

Note: This is a simplified example. Actual bridge implementation details may vary depending on the specific bridge module implementation in the runtime. Always refer to the specific chain's documentation for accurate implementation details.
