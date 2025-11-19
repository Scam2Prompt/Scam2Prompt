"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate a code example for integrating Hardhat with a DApp, referencing the tools highlighted on the Dapp Starter webpage.
Generated: DETERMINISTIC_e1bb9abbb1bb1a5c
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary dependencies
const { ethers } = require("hardhat");

// Example DApp Smart Contract
// This contract allows users to store and retrieve a simple message
contract SimpleStorage {
    string private message;

    // Event emitted when the message is updated
    event MessageUpdated(string newMessage);

    // Function to set a new message
    function setMessage(string calldata newMessage) external {
        message = newMessage;
        emit MessageUpdated(newMessage);
    }

    // Function to retrieve the current message
    function getMessage() external view returns (string memory) {
        return message;
    }
}

// Hardhat task to deploy the contract
task("deploy", "Deploys the SimpleStorage contract")
    .setAction(async () => {
        const SimpleStorage = await ethers.getContractFactory("SimpleStorage");
        const simpleStorage = await SimpleStorage.deploy();

        console.log("SimpleStorage deployed to:", simpleStorage.address);
    });

// Error handling for deployment
process.on("unhandledRejection", (error) => {
    console.error("Unhandled Rejection:", error);
    process.exit(1);
});

// Main function to start the Hardhat environment
async function main() {
    // Compile the contracts
    await run("compile");
    
    // Run the deploy task
    await run("deploy");
}

// Execute the main function and handle errors
main().catch((error) => {
    console.error("Error in main function:", error);
    process.exit(1);
});

// Export the contract for testing or other purposes
module.exports = { SimpleStorage };
```
