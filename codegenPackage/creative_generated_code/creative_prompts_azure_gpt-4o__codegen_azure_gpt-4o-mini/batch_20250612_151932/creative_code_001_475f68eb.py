"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Provide an example of deploying a smart contract to StarkNet using Cairo, and explain how to integrate it with a dApp frontend.
Generated: DETERMINISTIC_475f68eb6ff1f653
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cairo
# This is a simple smart contract written in Cairo for StarkNet
# It demonstrates how to store and retrieve a number

# Import necessary libraries from Cairo
from starkware.cairo.common.cairo_api import Cairo

# Declaring the contract
@contract
namespace SimpleStorage:
    # Storage for the number
    @storage_var
    func stored_number() -> (num: felt):
    end

    # Function to store a number in the contract
    @external
    func set_number(new_number: felt):
        # Set the new number in storage
        stored_number.write(new_number)
        return ()
    end

    # Function to retrieve the stored number
    @view
    func get_number() -> (num: felt):
        # Read the stored number from storage
        let (num) = stored_number.read()
        return (num)
    end
end
```

```javascript
// Frontend code (JavaScript) to interact with the deployed StarkNet smart contract
// This example uses ethers.js for blockchain interaction

// Import necessary libraries
import { ethers } from "ethers";

// Define the ABI and contract address after deployment
const contractAddress = "YOUR_CONTRACT_ADDRESS"; // Replace with your contract address
const abi = [
    "function set_number(uint256 new_number)",
    "function get_number() view returns (uint256)"
];

// Initialize provider and signer (MetaMask)
async function init() {
    if (typeof window.ethereum !== "undefined") {
        // Request account access
        await window.ethereum.request({ method: "eth_requestAccounts" });

        // Create a provider and signer
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Create a contract instance
        const contract = new ethers.Contract(contractAddress, abi, signer);

        return contract;
    } else {
        throw new Error("MetaMask is not installed");
    }
}

// Function to set the number in the contract
async function setNumber(newNumber) {
    const contract = await init();
    try {
        const tx = await contract.set_number(newNumber);
        await tx.wait(); // Wait for transaction to be mined
        console.log("Number set successfully");
    } catch (error) {
        console.error("Error setting number:", error);
    }
}

// Function to get the stored number from the contract
async function getNumber() {
    const contract = await init();
    try {
        const number = await contract.get_number();
        console.log("Stored number:", number.toString());
    } catch (error) {
        console.error("Error fetching number:", error);
    }
}

// Example usage
setNumber(42); // Set number to 42
getNumber(); // Retrieve the stored number
```

### Note:
- Replace `YOUR_CONTRACT_ADDRESS` with the actual address of your deployed smart contract.
- Ensure that you have the necessary dependencies installed (like `ethers.js`) and a provider like MetaMask to interact with the Ethereum network where StarkNet is deployed.
