"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Generate a smart contract in Solidity that mimics Loud's fee split mechanism for distributing rewards to contributors.
Generated: DETERMINISTIC_62aa1654465f2509
Batch ID: 20250612_163224
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
 * @title FeeSplitContract
 * @dev A smart contract to split fees among contributors based on predefined shares.
 */
contract FeeSplitContract {
    // Address of the contract owner
    address public owner;

    // Mapping to store contributors and their respective shares
    mapping(address => uint256) public shares;

    // Array to keep track of all contributors
    address[] public contributors;

    // Total shares allocated
    uint256 public totalShares;

    // Event emitted when fees are distributed
    event FeesDistributed(uint256 totalAmount);

    // Event emitted when a contributor is added or updated
    event ContributorUpdated(address indexed contributor, uint256 share);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add or update a contributor's share.
     * @param contributor Address of the contributor.
     * @param share Share percentage (in basis points, e.g., 1000 = 10%).
     */
    function setContributor(address contributor, uint256 share) external onlyOwner {
        require(contributor != address(0), "Invalid contributor address");
        require(share > 0, "Share must be greater than zero");

        // If the contributor is new, add them to the contributors array
        if (shares[contributor] == 0) {
            contributors.push(contributor);
        }

        // Update the total shares
        totalShares = totalShares - shares[contributor] + share;

        // Update the contributor's share
        shares[contributor] = share;

        emit ContributorUpdated(contributor, share);
    }

    /**
     * @dev Function to distribute fees among contributors based on their shares.
     * The contract must have sufficient balance to distribute the fees.
     */
    function distributeFees() external {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No fees available for distribution");
        require(totalShares > 0, "No shares allocated");

        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            uint256 contributorShare = (contractBalance * shares[contributor]) / totalShares;

            // Transfer the calculated share to the contributor
            (bool success, ) = contributor.call{value: contributorShare}("");
            require(success, "Fee transfer failed");
        }

        emit FeesDistributed(contractBalance);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw any remaining Ether in the contract.
     * @param to Address to send the remaining Ether.
     */
    function withdrawRemainingFunds(address payable to) external onlyOwner {
        require(to != address(0), "Invalid address");
        uint256 remainingBalance = address(this).balance;
        require(remainingBalance > 0, "No funds to withdraw");

        (bool success, ) = to.call{value: remainingBalance}("");
        require(success, "Withdrawal failed");
    }
}
```
