"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-fix-scw-signers-offchain-labs.vercel.app
Prompt: What are the key features of the Arbitrum token bridge, and how can I integrate it into my dApp?
Generated: DETERMINISTIC_db8af61c07b86aff
Batch ID: 20250612_135401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ethers } = require("ethers");
const { Bridge } = require("@arbitrum/sdk"); // Arbitrum SDK for interacting with the token bridge

// Key configuration variables
const L1_RPC_URL = "<Your-L1-RPC-Provider-URL>"; // Ethereum RPC URL (e.g., Infura, Alchemy)
const L2_RPC_URL = "<Your-L2-RPC-Provider-URL>"; // Arbitrum RPC URL (e.g., Infura, Alchemy)
const PRIVATE_KEY = "<Your-Private-Key>"; // Your wallet's private key
const TOKEN_ADDRESS_L1 = "<ERC20-Token-Contract-Address-On-L1>"; // Address of the ERC20 token on Ethereum (L1)
const RECEIVER_ADDRESS_L2 = "<Receiver-Wallet-Address-On-L2>"; // Wallet address to receive tokens on Arbitrum (L2)
const AMOUNT_TO_BRIDGE = ethers.utils.parseUnits("100", 18); // Amount of tokens to bridge (e.g., 100 tokens)

// Initialize providers for L1 and L2
const l1Provider = new ethers.providers.JsonRpcProvider(L1_RPC_URL);
const l2Provider = new ethers.providers.JsonRpcProvider(L2_RPC_URL);

// Create wallet instances for L1 and L2
const l1Wallet = new ethers.Wallet(PRIVATE_KEY, l1Provider);
const l2Wallet = new ethers.Wallet(PRIVATE_KEY, l2Provider);

// Main function to bridge tokens
async function bridgeTokens() {
  try {
    console.log("Initializing Arbitrum Bridge...");

    // Instantiate the Arbitrum Bridge object
    const bridge = await Bridge.init(l1Wallet, l2Wallet);

    // Get token contract instance on L1
    const l1TokenContract = new ethers.Contract(
      TOKEN_ADDRESS_L1,
      [
        "function approve(address spender, uint256 amount) public returns (bool)",
        "function balanceOf(address owner) public view returns (uint256)",
      ],
      l1Wallet
    );

    // Check token balance on L1
    const balance = await l1TokenContract.balanceOf(l1Wallet.address);
    console.log(`L1 Token Balance: ${ethers.utils.formatUnits(balance, 18)} tokens`);

    if (balance.lt(AMOUNT_TO_BRIDGE)) {
      throw new Error("Insufficient token balance on L1.");
    }

    // Approve the token bridge to spend tokens on L1
    console.log("Approving tokens for the bridge...");
    const txApprove = await l1TokenContract.approve(bridge.getL1GatewayAddress(TOKEN_ADDRESS_L1), AMOUNT_TO_BRIDGE);
    await txApprove.wait();
    console.log("Approval transaction confirmed");

    // Deposit tokens from L1 to L2
    console.log(`Depositing ${ethers.utils.formatUnits(AMOUNT_TO_BRIDGE, 18)} tokens to Arbitrum L2...`);
    const depositTx = await bridge.depositToken(TOKEN_ADDRESS_L1, AMOUNT_TO_BRIDGE, RECEIVER_ADDRESS_L2);
    console.log("Deposit transaction submitted:", depositTx.hash);

    // Wait for the deposit transaction to be confirmed
    await depositTx.wait();
    console.log("Deposit transaction confirmed");

    // Confirm receipt of tokens on L2
    console.log("Confirming token deposit on Arbitrum L2...");
    const receipt = await bridge.waitForL2Deposit(depositTx);
    console.log("Tokens successfully bridged to L2:", receipt);

  } catch (error) {
    console.error("An error occurred while bridging tokens:", error.message);
  }
}

// Execute the bridge function
bridgeTokens();
```
