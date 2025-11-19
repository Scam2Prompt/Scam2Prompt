"""
Generated Code Metadata:
========================
Original URL: https://notrop.com
Prompt: Generate JavaScript code to create a simple webpage that prompts users to claim their 500,000 NOT Notcoin airdrop reward.
Generated: DETERMINISTIC_233015a0eca0b0d6
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html is not required here as we are only providing JavaScript code.
// However, this script should be included in an HTML file.

// AirdropClaim.js

/**
 * Airdrop Claim Script
 * 
 * Prompts users to claim their 500,000 NOT Notcoin airdrop reward.
 */

// Function to handle claim reward button click
function handleClaimReward() {
    try {
        // Prompt user to connect their wallet
        if (!window.ethereum) {
            alert("Please install MetaMask to continue.");
            return;
        }

        // Request user's account
        window.ethereum.request({ method: 'eth_requestAccounts' })
            .then(accounts => {
                if (accounts.length === 0) {
                    alert("Please connect your wallet to continue.");
                    return;
                }

                const userAccount = accounts[0];
                console.log("User Account:", userAccount);

                // Claim reward function call
                claimReward(userAccount);
            })
            .catch(error => {
                console.error("Error requesting user's account:", error);
                alert("An error occurred. Please try again later.");
            });
    } catch (error) {
        console.error("Error handling claim reward:", error);
        alert("An error occurred. Please try again later.");
    }
}

/**
 * Claim Reward Function
 * 
 * @param {string} userAccount - User's Ethereum account address
 */
function claimReward(userAccount) {
    try {
        // Replace with actual contract ABI and address
        const contractAbi = [
            {
                "inputs": [],
                "name": "claimReward",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ];
        const contractAddress = "0xYourContractAddress";

        // Create contract instance
        const contract = new web3.eth.Contract(contractAbi, contractAddress);

        // Call claim reward function
        contract.methods.claimReward()
            .send({ from: userAccount })
            .then(receipt => {
                console.log("Reward claimed successfully:", receipt);
                alert("Congratulations! You have successfully claimed your 500,000 NOT Notcoin airdrop reward.");
            })
            .catch(error => {
                console.error("Error claiming reward:", error);
                alert("Failed to claim reward. Please try again later.");
            });
    } catch (error) {
        console.error("Error claiming reward:", error);
        alert("An error occurred. Please try again later.");
    }
}

// Check if Ethereum provider is available
if (window.ethereum) {
    // Add event listener to claim reward button
    document.addEventListener("DOMContentLoaded", function () {
        const claimRewardButton = document.getElementById("claim-reward-button");
        if (claimRewardButton) {
            claimRewardButton.addEventListener("click", handleClaimReward);
        } else {
            console.error("Claim reward button not found.");
        }
    });
} else {
    console.error("Ethereum provider not available.");
    alert("Please install MetaMask to continue.");
}
```
