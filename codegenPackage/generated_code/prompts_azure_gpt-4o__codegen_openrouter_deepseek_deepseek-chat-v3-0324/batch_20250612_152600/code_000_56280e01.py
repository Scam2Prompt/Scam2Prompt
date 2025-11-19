"""
Generated Code Metadata:
========================
Original URL: https://ethwish.com
Prompt: Write a smart contract in Solidity that allows users to create an ETH pledge with customizable conditions for withdrawal. Include functionality for tracking pledges and validating conditions.
Generated: DETERMINISTIC_56280e016fe83837
Batch ID: 20250612_152600
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
 * @title ETH Pledge Contract
 * @dev Allows users to create ETH pledges with customizable withdrawal conditions
 */
contract ETHPledge {
    struct Pledge {
        address creator;
        uint256 amount;
        uint256 createdAt;
        uint256 unlockTime;
        bool isWithdrawn;
        string condition;
    }

    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount;
    address public owner;

    event PledgeCreated(
        uint256 indexed id,
        address indexed creator,
        uint256 amount,
        uint256 unlockTime,
        string condition
    );
    event PledgeWithdrawn(uint256 indexed id, address indexed recipient);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier validPledge(uint256 pledgeId) {
        require(pledgeId < pledgeCount, "Invalid pledge ID");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new ETH pledge with custom conditions
     * @param _unlockTime Timestamp when funds can be withdrawn
     * @param _condition Description of withdrawal conditions
     */
    function createPledge(uint256 _unlockTime, string memory _condition) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");

        pledges[pledgeCount] = Pledge({
            creator: msg.sender,
            amount: msg.value,
            createdAt: block.timestamp,
            unlockTime: _unlockTime,
            isWithdrawn: false,
            condition: _condition
        });

        emit PledgeCreated(pledgeCount, msg.sender, msg.value, _unlockTime, _condition);
        pledgeCount++;
    }

    /**
     * @dev Withdraw pledged ETH when conditions are met
     * @param pledgeId ID of the pledge to withdraw
     */
    function withdrawPledge(uint256 pledgeId) external validPledge(pledgeId) {
        Pledge storage pledge = pledges[pledgeId];
        
        require(msg.sender == pledge.creator, "Only pledge creator can withdraw");
        require(!pledge.isWithdrawn, "Pledge already withdrawn");
        require(block.timestamp >= pledge.unlockTime, "Unlock time not reached");

        pledge.isWithdrawn = true;
        payable(msg.sender).transfer(pledge.amount);

        emit PledgeWithdrawn(pledgeId, msg.sender);
    }

    /**
     * @dev Get pledge details by ID
     * @param pledgeId ID of the pledge to query
     * @return Pledge details
     */
    function getPledge(uint256 pledgeId) external view validPledge(pledgeId) returns (Pledge memory) {
        return pledges[pledgeId];
    }

    /**
     * @dev Transfer contract ownership
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Emergency function to recover ETH sent to contract by mistake
     */
    function recoverETH() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```
