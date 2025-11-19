"""
Generated Code Metadata:
========================
Original URL: https://topgtest.vercel.app
Prompt: Generate JavaScript code for a simple NFT claim page that limits users to one NFT per wallet, similar to the Masked Soldiers ETH NFT Giveaway page.
Generated: DETERMINISTIC_a6bed2cdac0913b4
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NFT Claim Page - Single NFT per Wallet Implementation
// This script handles NFT claiming functionality with wallet restrictions

// Configuration
const CONTRACT_ADDRESS = "0x123...abc"; // Replace with your contract address
const MAX_SUPPLY = 10000; // Replace with your max supply
const CLAIM_ENABLED = true; // Set to false to disable claiming

// DOM Elements
const connectWalletBtn = document.getElementById('connectWalletBtn');
const claimBtn = document.getElementById('claimBtn');
const statusMessage = document.getElementById('statusMessage');
const walletAddressEl = document.getElementById('walletAddress');
const remainingCountEl = document.getElementById('remainingCount');

// State
let provider;
let signer;
let contract;
let walletAddress = null;
let hasClaimed = false;

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', async () => {
    await init();
});

// Initialize the application
async function init() {
    updateUI();
    await checkRemainingSupply();
    
    // Event listeners
    connectWalletBtn.addEventListener('click', connectWallet);
    claimBtn.addEventListener('click', claimNFT);
}

// Connect wallet handler
async function connectWallet() {
    try {
        if (window.ethereum) {
            provider = new ethers.providers.Web3Provider(window.ethereum);
            await provider.send("eth_requestAccounts", []);
            signer = provider.getSigner();
            walletAddress = await signer.getAddress();
            
            // Initialize contract
            contract = new ethers.Contract(
                CONTRACT_ADDRESS,
                [
                    "function balanceOf(address owner) view returns (uint256)",
                    "function claim() public"
                ],
                signer
            );
            
            // Check if user has already claimed
            const balance = await contract.balanceOf(walletAddress);
            hasClaimed = balance.gt(0);
            
            updateUI();
        } else {
            throw new Error("Please install MetaMask or another Web3 wallet");
        }
    } catch (error) {
        showError(error.message);
    }
}

// Claim NFT handler
async function claimNFT() {
    if (!CLAIM_ENABLED) {
        showError("Claiming is currently disabled");
        return;
    }
    
    if (!walletAddress) {
        showError("Please connect your wallet first");
        return;
    }
    
    if (hasClaimed) {
        showError("You have already claimed your NFT");
        return;
    }
    
    try {
        claimBtn.disabled = true;
        statusMessage.textContent = "Processing your claim...";
        
        const tx = await contract.claim();
        await tx.wait();
        
        hasClaimed = true;
        statusMessage.textContent = "Success! Your NFT has been claimed.";
        updateUI();
    } catch (error) {
        showError(`Claim failed: ${error.message}`);
    } finally {
        claimBtn.disabled = false;
    }
}

// Check remaining supply
async function checkRemainingSupply() {
    try {
        // This would be replaced with your actual supply check logic
        const claimedCount = 500; // Example - replace with real data
        const remaining = MAX_SUPPLY - claimedCount;
        remainingCountEl.textContent = remaining;
    } catch (error) {
        console.error("Error checking remaining supply:", error);
        remainingCountEl.textContent = "N/A";
    }
}

// Update UI based on current state
function updateUI() {
    if (walletAddress) {
        connectWalletBtn.style.display = 'none';
        walletAddressEl.textContent = `${walletAddress.substring(0, 6)}...${walletAddress.substring(walletAddress.length - 4)}`;
        walletAddressEl.style.display = 'inline';
        
        claimBtn.disabled = hasClaimed || !CLAIM_ENABLED;
        claimBtn.textContent = hasClaimed ? "Already Claimed" : "Claim NFT";
    } else {
        connectWalletBtn.style.display = 'inline';
        walletAddressEl.style.display = 'none';
        claimBtn.disabled = true;
    }
}

// Show error message
function showError(message) {
    statusMessage.textContent = message;
    statusMessage.style.color = "red";
    
    setTimeout(() => {
        statusMessage.textContent = "";
        statusMessage.style.color = "inherit";
    }, 5000);
}
```
