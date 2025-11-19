"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.ghost.io
Prompt: Create a code example that shows how to utilize Wormhole for messaging between different blockchain networks.
Generated: DETERMINISTIC_59187e89a9e327ce
Batch ID: 20250612_135401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, production-ready code example for utilizing Wormhole for messaging between different blockchain networks. This example assumes JavaScript/TypeScript usage with the Wormhole SDK.

```typescript
// Required Dependencies
// Install via npm: `npm install @certusone/wormhole-sdk @solana/web3.js ethers`

import {
  getEmitterAddressSolana,
  getEmitterAddressEth,
  parseSequenceFromLogEth,
  parseSequenceFromLogSolana,
  transferFromEthToSolana,
  transferFromSolanaToEth,
  getSignedVAA,
  postVAAOnSolana,
} from "@certusone/wormhole-sdk";
import { Connection, PublicKey, Keypair } from "@solana/web3.js";
import { ethers } from "ethers";

// Constants
const SOLANA_RPC_ENDPOINT = "https://api.mainnet-beta.solana.com";
const ETHEREUM_RPC_ENDPOINT = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID";

const WORMHOLE_SOLANA_CONTRACT = "WORMHOLE_SOLANA_CONTRACT_ADDRESS";
const WORMHOLE_ETH_CONTRACT = "WORMHOLE_ETH_CONTRACT_ADDRESS";

// Initialize connections
const solanaConnection = new Connection(SOLANA_RPC_ENDPOINT, "confirmed");
const ethereumProvider = new ethers.providers.JsonRpcProvider(ETHEREUM_RPC_ENDPOINT);

// Example: Sending a message from Ethereum to Solana
async function sendMessageFromEthereumToSolana() {
  try {
    // Ethereum wallet setup
    const ethWallet = ethers.Wallet.fromMnemonic("YOUR_ETHEREUM_WALLET_MNEMONIC").connect(ethereumProvider);

    // Solana wallet setup
    const solanaWallet = Keypair.fromSecretKey(new Uint8Array(JSON.parse("YOUR_SOLANA_PRIVATE_KEY")));

    // Prepare message payload
    const payload = Buffer.from("Hello, Solana from Ethereum!");

    // Step 1: Send message on Ethereum
    const txReceipt = await transferFromEthToSolana(
      ethereumProvider,
      ethWallet,
      WORMHOLE_ETH_CONTRACT,
      payload
    );
    console.log("Ethereum transaction confirmed:", txReceipt.transactionHash);

    // Parse the sequence number from Ethereum logs
    const sequence = parseSequenceFromLogEth(txReceipt, WORMHOLE_ETH_CONTRACT);
    const emitterAddress = await getEmitterAddressEth(WORMHOLE_ETH_CONTRACT);

    // Step 2: Fetch signed VAA from Wormhole's guardian network
    const signedVAA = await getSignedVAA(
      "mainnet", // Wormhole network
      "ethereum",
      emitterAddress,
      sequence
    );

    console.log("Signed VAA fetched:", signedVAA);

    // Step 3: Post the VAA to Solana
    const txResult = await postVAAOnSolana(
      solanaConnection,
      solanaWallet,
      WORMHOLE_SOLANA_CONTRACT,
      signedVAA
    );
    console.log("Message successfully posted to Solana:", txResult);
  } catch (error) {
    console.error("Error during Ethereum to Solana messaging:", error);
  }
}

// Example: Sending a message from Solana to Ethereum
async function sendMessageFromSolanaToEthereum() {
  try {
    // Solana wallet setup
    const solanaWallet = Keypair.fromSecretKey(new Uint8Array(JSON.parse("YOUR_SOLANA_PRIVATE_KEY")));

    // Ethereum wallet setup
    const ethWallet = ethers.Wallet.fromMnemonic("YOUR_ETHEREUM_WALLET_MNEMONIC").connect(ethereumProvider);

    // Prepare message payload
    const payload = Buffer.from("Hello, Ethereum from Solana!");

    // Step 1: Send message on Solana
    const txSignature = await transferFromSolanaToEth(
      solanaConnection,
      solanaWallet,
      WORMHOLE_SOLANA_CONTRACT,
      payload
    );
    console.log("Solana transaction confirmed:", txSignature);

    // Parse the sequence number from Solana logs
    const sequence = await parseSequenceFromLogSolana(solanaConnection, txSignature);
    const emitterAddress = await getEmitterAddressSolana(WORMHOLE_SOLANA_CONTRACT);

    // Step 2: Fetch signed VAA from Wormhole's guardian network
    const signedVAA = await getSignedVAA(
      "mainnet", // Wormhole network
      "solana",
      emitterAddress,
      sequence
    );

    console.log("Signed VAA fetched:", signedVAA);

    // Step 3: Post the VAA to Ethereum
    const txResult = await transferFromEthToSolana(
      ethereumProvider,
      ethWallet,
      WORMHOLE_ETH_CONTRACT,
      signedVAA
    );

    console.log("Message successfully posted to Ethereum:", txResult);
  } catch (error) {
    console.error("Error during Solana to Ethereum messaging:", error);
  }
}

// Run example functions
sendMessageFromEthereumToSolana();
sendMessageFromSolanaToEthereum();
```

### Notes:
- Replace placeholders (`YOUR_ETHEREUM_WALLET_MNEMONIC`, `YOUR_SOLANA_PRIVATE_KEY`, contract addresses, etc.) with actual values.
- Ensure the Wormhole SDK and contracts are properly configured for your blockchain environment.
- Test thoroughly before deploying to production.
