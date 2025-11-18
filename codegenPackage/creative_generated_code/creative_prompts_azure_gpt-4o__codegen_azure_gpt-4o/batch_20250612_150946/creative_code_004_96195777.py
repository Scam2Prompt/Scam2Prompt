"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogeverse-com.pages.dev
Prompt: Write JavaScript code using ethers.js to allow users to connect their wallets, select a blockchain network, and participate in the $DOGEVERSE presale by swapping ETH or other supported tokens.
Generated: DETERMINISTIC_96195777a9e735b3
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js
import { ethers } from "ethers";

// Constants
const PRESALE_CONTRACT_ADDRESS = "0xYourPresaleContractAddress"; // Replace with your presale contract address
const PRESALE_ABI = [
  // Add the ABI of your presale contract here
];
const SUPPORTED_NETWORKS = {
  1: "Ethereum Mainnet",
  5: "Goerli Testnet",
  137: "Polygon Mainnet",
  80001: "Mumbai Testnet",
  // Add more supported networks as needed
};
const SUPPORTED_TOKENS = ["ETH", "USDT", "USDC"]; // Replace with your supported tokens

// Variables
let provider, signer, presaleContract;

// Utility function to display messages (errors, user notifications)
const displayMessage = (message) => {
  console.log(message); // Replace with custom UI logic for notifications
};

// Function to connect the wallet
async function connectWallet() {
  if (!window.ethereum) {
    displayMessage("MetaMask is not installed. Please install it to connect your wallet.");
    return;
  }

  try {
    // Request wallet connection
    await window.ethereum.request({ method: "eth_requestAccounts" });
    provider = new ethers.providers.Web3Provider(window.ethereum);
    signer = provider.getSigner();
    const userAddress = await signer.getAddress();

    displayMessage(`Wallet connected: ${userAddress}`);
  } catch (error) {
    displayMessage(`Failed to connect wallet: ${error.message}`);
  }
}

// Function to switch network
async function switchNetwork(networkId) {
  if (!SUPPORTED_NETWORKS[networkId]) {
    displayMessage("Selected network is not supported.");
    return;
  }

  try {
    await window.ethereum.request({
      method: "wallet_switchEthereumChain",
      params: [{ chainId: ethers.utils.hexValue(networkId) }],
    });
    displayMessage(`Switched to ${SUPPORTED_NETWORKS[networkId]}`);
  } catch (error) {
    if (error.code === 4902) {
      displayMessage("Network is not available in MetaMask. Please add it manually.");
    } else {
      displayMessage(`Failed to switch network: ${error.message}`);
    }
  }
}

// Function to participate in the $DOGEVERSE presale
async function participateInPresale(tokenSymbol, amount) {
  if (!provider || !signer) {
    displayMessage("Please connect your wallet first.");
    return;
  }

  if (!SUPPORTED_TOKENS.includes(tokenSymbol)) {
    displayMessage(`${tokenSymbol} is not supported for the presale.`);
    return;
  }

  try {
    // Instantiate the presale contract
    presaleContract = new ethers.Contract(PRESALE_CONTRACT_ADDRESS, PRESALE_ABI, signer);

    let tx;
    if (tokenSymbol === "ETH") {
      // Sending ETH to the presale contract
      tx = await presaleContract.buyWithETH({ value: ethers.utils.parseEther(amount) });
    } else {
      // Sending ERC20 tokens to the presale contract
      const tokenContractAddress = await presaleContract.getTokenAddress(tokenSymbol); // Assuming the presale contract has this function
      const tokenContract = new ethers.Contract(tokenContractAddress, [
        "function approve(address spender, uint256 amount) public returns (bool)",
      ], signer);

      // Approve the presale contract to spend the tokens
      const tokenDecimals = await tokenContract.decimals(); // Assuming the token contract has decimals function
      const parsedAmount = ethers.utils.parseUnits(amount, tokenDecimals);
      await tokenContract.approve(PRESALE_CONTRACT_ADDRESS, parsedAmount);

      // Participate in the presale with the specified token
      tx = await presaleContract.buyWithToken(tokenContractAddress, parsedAmount);
    }

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    displayMessage(`Transaction successful: ${receipt.transactionHash}`);
  } catch (error) {
    displayMessage(`Failed to participate in the presale: ${error.message}`);
  }
}

// Event listener for account and network changes
window.ethereum?.on("accountsChanged", (accounts) => {
  if (accounts.length === 0) {
    displayMessage("Wallet disconnected.");
  } else {
    displayMessage(`Wallet changed: ${accounts[0]}`);
  }
});

window.ethereum?.on("chainChanged", (chainId) => {
  displayMessage(`Network changed: ${SUPPORTED_NETWORKS[parseInt(chainId, 16)] || "Unknown Network"}`);
});

// Exporting functions if needed in a modular environment
export { connectWallet, switchNetwork, participateInPresale };

```
