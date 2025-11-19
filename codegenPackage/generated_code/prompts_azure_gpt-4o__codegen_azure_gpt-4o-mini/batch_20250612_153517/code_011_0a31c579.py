"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Generate a Solidity contract for the $HEHE airdrop, ensuring that 666 recipients are randomly selected and rewarded with tokens.
Generated: DETERMINISTIC_0a31c5792fbce780
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HeheAirdrop is Context, Ownable {
    // The ERC20 token to be airdropped
    IERC20 public token;

    // Total number of recipients
    uint256 public constant TOTAL_RECIPIENTS = 666;

    // Mapping to track if an address has already received tokens
    mapping(address => bool) public hasReceived;

    // Array to store eligible recipients
    address[] public eligibleRecipients;

    // Event to log the airdrop
    event AirdropExecuted(address indexed recipient, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to add eligible recipients
    function addEligibleRecipients(address[] calldata recipients) external onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            require(!hasReceived[recipients[i]], "Recipient already added");
            eligibleRecipients.push(recipients[i]);
            hasReceived[recipients[i]] = false; // Initialize as not received
        }
    }

    // Function to execute the airdrop
    function executeAirdrop(uint256 amount) external onlyOwner {
        require(eligibleRecipients.length >= TOTAL_RECIPIENTS, "Not enough eligible recipients");
        
        // Randomly select recipients
        uint256[] memory selectedIndices = _selectRandomRecipients();
        
        for (uint256 i = 0; i < selectedIndices.length; i++) {
            address recipient = eligibleRecipients[selectedIndices[i]];
            require(!hasReceived[recipient], "Recipient has already received tokens");
            
            // Transfer tokens to the recipient
            token.transfer(recipient, amount);
            hasReceived[recipient] = true; // Mark as received
            
            emit AirdropExecuted(recipient, amount);
        }
    }

    // Internal function to select random recipients
    function _selectRandomRecipients() internal view returns (uint256[] memory) {
        uint256[] memory indices = new uint256[](TOTAL_RECIPIENTS);
        uint256 totalEligible = eligibleRecipients.length;

        for (uint256 i = 0; i < TOTAL_RECIPIENTS; i++) {
            uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))) % totalEligible;
            indices[i] = randomIndex;
        }

        return indices;
    }

    // Function to withdraw any remaining tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        token.transfer(owner(), amount);
    }
}
```
