"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethrtc.com
Prompt: Write code to create an Ethereum smart contract for a pledge system, referencing real-time communication features.
Generated: DETERMINISTIC_7bb661d19df2b381
Batch ID: 20250612_152600
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; // Importing ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/access/Ownable.sol"; // Importing Ownable contract for access control

/**
 * @title PledgeSystem
 * @dev A smart contract to manage pledges for a project.
 */
contract PledgeSystem is Ownable {
    struct Pledge {
        address pledger;
        uint256 amount;
        bool withdrawn;
    }

    // Mapping to track pledges by contributor address
    mapping(address => Pledge) public pledges;
    // Total amount pledged
    uint256 public totalPledged;
    // Token used for pledging
    IERC20 public pledgeToken;

    // Event emitted when a new pledge is made
    event PledgeMade(address indexed pledger, uint256 amount);
    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(address indexed pledger, uint256 amount);

    /**
     * @dev Constructor to initialize the pledge token.
     * @param _pledgeToken Address of the ERC20 token to be used for pledging.
     */
    constructor(IERC20 _pledgeToken) {
        pledgeToken = _pledgeToken;
    }

    /**
     * @dev Function to make a pledge.
     * @param amount Amount of tokens to pledge.
     * Requirements:
     * - The caller must approve this contract to spend at least `amount` tokens.
     */
    function makePledge(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pledges[msg.sender].amount == 0, "Pledge already exists");

        // Transfer tokens from the pledger to the contract
        require(pledgeToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create a new pledge
        pledges[msg.sender] = Pledge(msg.sender, amount, false);
        totalPledged += amount;

        emit PledgeMade(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw a pledge.
     * Requirements:
     * - The caller must have a pledge that has not been withdrawn.
     */
    function withdrawPledge() external {
        Pledge storage pledge = pledges[msg.sender];
        require(pledge.amount > 0, "No pledge found");
        require(!pledge.withdrawn, "Pledge already withdrawn");

        // Mark the pledge as withdrawn
        pledge.withdrawn = true;

        // Transfer the token back to the pledger
        require(pledgeToken.transfer(msg.sender, pledge.amount), "Token transfer failed");

        emit PledgeWithdrawn(msg.sender, pledge.amount);
    }

    /**
     * @dev Function to get the details of a pledge.
     * @param pledger Address of the pledger.
     * @return Pledge details (amount and withdrawn status).
     */
    function getPledgeDetails(address pledger) external view returns (uint256 amount, bool withdrawn) {
        Pledge storage pledge = pledges[pledger];
        return (pledge.amount, pledge.withdrawn);
    }
}
```
