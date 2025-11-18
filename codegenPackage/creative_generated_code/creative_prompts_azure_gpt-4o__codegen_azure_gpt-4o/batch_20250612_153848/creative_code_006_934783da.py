"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchrameextansun.gitbook.io
Prompt: Write code to retrieve the balance of Ethereum and ERC-20 tokens stored in a user's MetaMask wallet. Include error handling for cases where the wallet is not connected.
Generated: DETERMINISTIC_934783dae6383f0d
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers.js library
const { ethers } = require("ethers");

// Function to retrieve Ethereum and ERC-20 token balances
async function getWalletBalances(tokenAddress = null) {
  try {
    // Ensure MetaMask is installed in the browser
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install it to continue.");
    }

    // Request user to connect their MetaMask wallet
    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Create a provider connected to MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (connected wallet)
    const signer = provider.getSigner();

    // Retrieve the connected wallet address
    const walletAddress = await signer.getAddress();

    // Fetch Ethereum balance
    const ethBalance = await provider.getBalance(walletAddress);

    // Convert balance from Wei to Ether
    const formattedEthBalance = ethers.utils.formatEther(ethBalance);

    // If no token address is provided, return only the Ethereum balance
    if (!tokenAddress) {
      return {
        walletAddress,
        ethBalance: formattedEthBalance,
        tokenBalance: null,
      };
    }

    // Define ERC-20 token contract ABI
    const erc20Abi = [
      "function balanceOf(address owner) view returns (uint256)",
      "function decimals() view returns (uint8)",
    ];

    // Create a contract instance for the ERC-20 token
    const tokenContract = new ethers.Contract(tokenAddress, erc20Abi, provider);

    // Fetch the token balance of the wallet
    const tokenBalanceRaw = await tokenContract.balanceOf(walletAddress);

    // Fetch the token's decimals for proper formatting
    const tokenDecimals = await tokenContract.decimals();

    // Format the token balance based on its decimals
    const formattedTokenBalance = ethers.utils.formatUnits(tokenBalanceRaw, tokenDecimals);

    // Return the wallet address, Ethereum balance, and token balance
    return {
      walletAddress,
      ethBalance: formattedEthBalance,
      tokenBalance: formattedTokenBalance,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("Error retrieving wallet balances:", error.message);
    return {
      error: error.message,
    };
  }
}

// Example usage: Retrieve Ethereum and USDT (ERC-20 token) balances
(async () => {
  const tokenAddress = "0xdAC17F958D2ee523a2206206994597C13D831ec7"; // Example: USDT token address
  const balances = await getWalletBalances(tokenAddress);
  console.log("Wallet Balances:", balances);
})();
```
