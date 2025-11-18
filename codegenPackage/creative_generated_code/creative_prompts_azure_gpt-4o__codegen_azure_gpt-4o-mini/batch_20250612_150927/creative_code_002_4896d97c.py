"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-mocafoundation.pages.dev
Prompt: Create a smart contract in Solidity for distributing $MOCA tokens based on eligibility criteria described by the Moca Foundation.
Generated: DETERMINISTIC_4896d97cf15c7187
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for the MOCA token contract
interface IMOCA {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// The MocaFundDistribution contract
contract MocaFundDistribution {
    // State variables
    IMOCA public mocaToken; // Address of the MOCA token contract
    address public owner;     // Owner of the contract
    mapping(address => bool) public eligibleRecipients; // Eligibility tracking

    // Events
    event TokensDistributed(address recipient, uint256 amount);
    event EligibilityUpdated(address recipient, bool isEligible);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _mocaToken) {
        require(_mocaToken != address(0), "Invalid token address");
        mocaToken = IMOCA(_mocaToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to update eligibility of recipients
    function updateEligibility(address recipient, bool isEligible) external onlyOwner {
        eligibleRecipients[recipient] = isEligible;
        emit EligibilityUpdated(recipient, isEligible);
    }

    // Function to distribute tokens to eligible recipients
    function distributeTokens(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            // Check if the recipient is eligible
            require(eligibleRecipients[recipient], "Recipient is not eligible for distribution");
            
            // Transfer the MOCA tokens
            bool success = mocaToken.transfer(recipient, amount);
            require(success, "Token transfer failed");

            emit TokensDistributed(recipient, amount);
        }
    }

    // Function to withdraw leftover tokens (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        // Transfer tokens to the owner
        bool success = mocaToken.transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }

    // Function to check eligibility status of a recipient
    function isEligible(address recipient) external view returns (bool) {
        return eligibleRecipients[recipient];
    }
}
```
