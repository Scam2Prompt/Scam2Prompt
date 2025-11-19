"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Generate a code snippet for a smart contract that manages a presale with a cap of 1000 BASE for the $JESSE token.
Generated: DETERMINISTIC_9804bdf54911001c
Batch ID: 20250612_161520
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

/*
 * @title Presale Contract for JESSE Token
 * @dev This contract handles a capped presale for the JESSE token, allowing
 * participants to buy up to a total cap of 1000 BASE tokens.
 */
contract JESSEPresale {
    // Address of the token owner
    address public owner;

    // Total amount of BASE tokens raised during the presale
    uint256 public totalRaised;

    // Maximum cap for the presale (1000 BASE tokens)
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Token price in BASE (e.g., 1 JESSE = 0.01 BASE)
    uint256 public constant TOKEN_PRICE = 0.01 ether;

    // Mapping to track individual contributions
    mapping(address => uint256) public contributions;

    // Event emitted when a contribution is made
    event ContributionReceived(address indexed contributor, uint256 amount);

    // Event emitted when the presale is finalized
    event PresaleFinalized(uint256 totalRaised);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /*
     * @notice Function to contribute to the presale
     * @dev Accepts BASE tokens and updates the contribution record
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than zero");
        require(totalRaised + msg.value <= PRESALE_CAP, "Exceeds presale cap");

        // Update the total raised amount
        totalRaised += msg.value;

        // Update the individual contribution
        contributions[msg.sender] += msg.value;

        // Emit an event for the contribution
        emit ContributionReceived(msg.sender, msg.value);
    }

    /*
     * @notice Function to finalize the presale
     * @dev Can only be called by the owner after the presale cap is reached
     */
    function finalizePresale() external onlyOwner {
        require(totalRaised >= PRESALE_CAP, "Presale cap not reached");

        // Transfer all funds raised to the owner
        payable(owner).transfer(address(this).balance);

        // Emit an event for presale finalization
        emit PresaleFinalized(totalRaised);
    }

    /*
     * @notice Fallback function to prevent accidental transfers
     * @dev Ensures all transfers go through the contribute() function
     */
    receive() external payable {
        revert("Use contribute() to participate in presale");
    }
}
```
