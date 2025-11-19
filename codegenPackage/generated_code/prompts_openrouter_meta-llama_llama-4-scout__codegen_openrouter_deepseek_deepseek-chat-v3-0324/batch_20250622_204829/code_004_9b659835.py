"""
Generated Code Metadata:
========================
Original URL: https://ethhix.com
Prompt: "Design a basic Ethereum pledge smart contract using Solidity."
Generated: DETERMINISTIC_9b65983583bfe713
Batch ID: 20250622_204829
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

/**
 * @title PledgeContract
 * @dev A smart contract for managing pledges (donations) in Ether
 */
contract PledgeContract {
    // Struct to store pledge information
    struct Pledge {
        address donor;
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track pledges by donor address
    mapping(address => Pledge) public pledges;

    // Event emitted when a new pledge is made
    event Pledged(address indexed donor, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed recipient, uint256 amount);

    // Address of the contract owner
    address public owner;

    // Total amount pledged
    uint256 public totalPledged;

    // Modifier to restrict function access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to make a pledge
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        pledges[msg.sender] = Pledge({
            donor: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp
        });

        totalPledged += msg.value;
        emit Pledged(msg.sender, msg.value);
    }

    /**
     * @dev Allows the owner to withdraw the pledged funds
     * @param amount The amount to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        require(amount > 0, "Withdrawal amount must be greater than 0");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawn(owner, amount);
    }

    /**
     * @dev Returns the contract's current balance
     * @return The contract balance in wei
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Returns pledge information for a given donor
     * @param donor Address of the donor
     * @return The pledge details
     */
    function getPledge(address donor) external view returns (Pledge memory) {
        return pledges[donor];
    }
}
```
