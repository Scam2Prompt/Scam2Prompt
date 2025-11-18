"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy.pages.dev
Prompt: Generate code to interact with Beefy Finance smart contracts and automate the process of depositing funds into a specific vault.
Generated: DETERMINISTIC_4b449fb11c9d1e2d
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const ethers = require('ethers'); // Ethereum library for interacting with smart contracts
require('dotenv').config(); // For managing sensitive data securely

// Constants for the application
const RPC_URL = process.env.RPC_URL; // Ethereum node URL (e.g., Infura or Alchemy)
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Your wallet's private key (ensure this is stored securely)
const BEEFY_VAULT_ADDRESS = process.env.BEEFY_VAULT_ADDRESS; // Address of the Beefy Finance vault
const TOKEN_ADDRESS = process.env.TOKEN_ADDRESS; // Address of the token to deposit
const AMOUNT_TO_DEPOSIT = process.env.AMOUNT_TO_DEPOSIT; // Amount to deposit (as a string for precision)

// Beefy Finance Vault ABI (simplified example)
const BEEFY_VAULT_ABI = [
  "function deposit(uint256 amount) external",
  "function want() external view returns (address)",
];

// ERC20 Token ABI (simplified example)
const ERC20_ABI = [
  "function approve(address spender, uint256 amount) external returns (bool)",
  "function allowance(address owner, address spender) external view returns (uint256)",
  "function balanceOf(address account) external view returns (uint256)",
];

// Initialize the Ethereum provider and wallet
const provider = new ethers.JsonRpcProvider(RPC_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

async function main() {
  try {
    // Beefy Vault Contract
    const vaultContract = new ethers.Contract(BEEFY_VAULT_ADDRESS, BEEFY_VAULT_ABI, wallet);

    // Get the token to deposit from the vault
    const tokenAddress = await vaultContract.want();
    if (tokenAddress.toLowerCase() !== TOKEN_ADDRESS.toLowerCase()) {
      throw new Error("Configured token address does not match the vault's required token.");
    }

    // ERC20 Token Contract
    const tokenContract = new ethers.Contract(TOKEN_ADDRESS, ERC20_ABI, wallet);

    // Check the allowance of the vault to spend tokens
    const allowance = await tokenContract.allowance(wallet.address, BEEFY_VAULT_ADDRESS);
    const amountToDeposit = ethers.parseUnits(AMOUNT_TO_DEPOSIT, 18); // Adjust decimals as necessary

    if (allowance.lt(amountToDeposit)) {
      console.log("Allowance insufficient, approving the vault to spend tokens...");
      // Approve the vault to spend the tokens
      const approveTx = await tokenContract.approve(BEEFY_VAULT_ADDRESS, amountToDeposit);
      await approveTx.wait();
      console.log("Approval transaction confirmed.");
    }

    // Check wallet balance
    const walletBalance = await tokenContract.balanceOf(wallet.address);
    if (walletBalance.lt(amountToDeposit)) {
      throw new Error("Insufficient token balance for the deposit.");
    }

    // Deposit tokens into the Beefy vault
    console.log("Depositing tokens into the Beefy vault...");
    const depositTx = await vaultContract.deposit(amountToDeposit);
    await depositTx.wait();
    console.log("Deposit successful!");

  } catch (error) {
    console.error("An error occurred:", error.message);
    console.error(error);
  }
}

// Execute the script
main();
```

### **Environment Variables Required:**
- `RPC_URL`: Ethereum node provider URL (e.g., Infura URL).
- `PRIVATE_KEY`: Your wallet's private key.
- `BEEFY_VAULT_ADDRESS`: The vault address for Beefy Finance.
- `TOKEN_ADDRESS`: The address of the token you are depositing.
- `AMOUNT_TO_DEPOSIT`: Amount of tokens to deposit (e.g., `"1.5"` for 1.5 tokens).

### **How to Run:**
1. Save the file as `deposit-to-beefy.js`.
2. Run `npm install ethers dotenv` to install dependencies.
3. Create a `.env` file with the required environment variables.
4. Execute the script with `node deposit-to-beefy.js`.
