"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethhix.com
Prompt: Write code to handle JavaScript errors when interacting with ETH pledge smart contracts on mobile devices without JavaScript enabled.
Generated: DETERMINISTIC_71441509b14d5804
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// EthereumPledgeHandler.js
class EthereumPledgeHandler {
    constructor() {
        // Initialize the Ethereum provider and contract
        this.provider = null;
        this.contract = null;
        this.contractAddress = "0xYourSmartContractAddress"; // Replace with your contract address
        this.abi = []; // Replace with your contract ABI

        this.init();
    }

    // Initialize the Ethereum provider and contract
    async init() {
        if (typeof window.ethereum !== 'undefined') {
            this.provider = new ethers.providers.Web3Provider(window.ethereum);
            this.contract = new ethers.Contract(this.contractAddress, this.abi, this.provider.getSigner());
        } else {
            console.error("Ethereum provider not found. Please install MetaMask.");
            alert("Ethereum provider not found. Please install MetaMask.");
        }
    }

    // Method to pledge ETH to the smart contract
    async pledge(amount) {
        try {
            if (!this.contract) {
                throw new Error("Contract is not initialized.");
            }
            
            const tx = await this.contract.pledge({ value: ethers.utils.parseEther(amount) });
            await tx.wait(); // Wait for the transaction to be mined

            console.log("Pledge successful:", tx);
            alert("Pledge successful!");
        } catch (error) {
            this.handleError(error);
        }
    }

    // Method to handle errors
    handleError(error) {
        // Log error to the console
        console.error("An error occurred:", error);

        // Display user-friendly error message
        if (error.code === 'INSUFFICIENT_FUNDS') {
            alert("You have insufficient funds for this transaction.");
        } else if (error.code === 'USER_REJECTED_TRANSACTION') {
            alert("Transaction was rejected by the user.");
        } else {
            alert("An unexpected error occurred. Please try again.");
        }
    }

    // Method to check if the user is connected to MetaMask
    async checkConnection() {
        try {
            const accounts = await this.provider.listAccounts();
            if (accounts.length > 0) {
                console.log("User is connected:", accounts[0]);
            } else {
                console.warn("User is not connected to MetaMask.");
                alert("Please connect to MetaMask to interact with the contract.");
            }
        } catch (error) {
            this.handleError(error);
        }
    }
}

// Usage example:
document.addEventListener("DOMContentLoaded", () => {
    const pledgeHandler = new EthereumPledgeHandler();

    document.getElementById("pledgeButton").addEventListener("click", async () => {
        const amount = document.getElementById("amountInput").value;
        await pledgeHandler.checkConnection();
        await pledgeHandler.pledge(amount);
    });
});
```

**Note**: Ensure you replace `0xYourSmartContractAddress` and `[]` with your actual smart contract address and ABI.
