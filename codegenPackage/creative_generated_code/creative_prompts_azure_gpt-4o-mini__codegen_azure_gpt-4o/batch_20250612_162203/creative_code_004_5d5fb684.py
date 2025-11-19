"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Write a Solidity contract snippet that checks if the presale cap of 3,000,000 FTM has been reached during the DRE presale.
Generated: DETERMINISTIC_5d5fb684169240fb
Batch ID: 20250612_162203
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

/**
 * @title DREPresale
 * @dev Contract for managing the presale of DRE tokens. Ensures presale cap is enforced.
 */
contract DREPresale {
    // State variable to track the total amount of FTM sent during presale
    uint256 public totalFTMContributed;

    // Presale cap in FTM (3,000,000 FTM)
    uint256 public constant PRESALE_CAP = 3_000_000 * 10**18; // Assuming FTM has 18 decimals

    // Address of the presale owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Event emitted when a contribution is made
    event Contribution(address indexed contributor, uint256 amount);

    // Event emitted when the presale cap is reached
    event PresaleCapReached();

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to contribute FTM to the presale. Checks if the cap is reached before accepting contributions.
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than zero");
        require(
            totalFTMContributed + msg.value <= PRESALE_CAP,
            "Presale cap exceeded"
        );

        // Update the total contributions
        totalFTMContributed += msg.value;

        // Emit the contribution event
        emit Contribution(msg.sender, msg.value);

        // Check if the presale cap has been reached
        if (totalFTMContributed == PRESALE_CAP) {
            emit PresaleCapReached();
        }
    }

    /**
     * @dev Function to withdraw collected FTM. Restricted to the contract owner.
     */
    function withdrawFTM() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No FTM to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to reject direct FTM transfers.
     */
    receive() external payable {
        revert("Direct FTM transfers not allowed");
    }
}
```
