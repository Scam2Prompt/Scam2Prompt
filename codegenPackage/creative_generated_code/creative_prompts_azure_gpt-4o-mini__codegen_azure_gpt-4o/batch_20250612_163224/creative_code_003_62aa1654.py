"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayloud.io
Prompt: Generate a smart contract in Solidity that mimics Loud's fee split mechanism for distributing rewards to contributors.
Generated: DETERMINISTIC_62aa1654465f2509
Batch ID: 20250612_163224
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
 * @title FeeSplitContract
 * @dev A smart contract to distribute rewards to contributors based on predefined shares
 */
contract FeeSplitContract {
    // Address of the contract owner (administrator)
    address public owner;

    // Mapping to store contributors and their respective shares
    mapping(address => uint256) public shares;

    // Array to keep track of all contributors
    address[] public contributors;

    // Event emitted when funds are distributed
    event FundsDistributed(uint256 totalAmount);
    
    // Event emitted when a contributor's share is updated
    event ShareUpdated(address contributor, uint256 newShare);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Constructor to set the initial contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update or add a contributor's share
     * @param contributor Address of the contributor
     * @param share The share percentage (must be greater than 0)
     */
    function setShare(address contributor, uint256 share) external onlyOwner {
        require(contributor != address(0), "Invalid contributor address");
        require(share > 0, "Share must be greater than 0");
        
        if (shares[contributor] == 0) {
            // If contributor is new, add them to the contributor list
            contributors.push(contributor);
        }
        shares[contributor] = share;

        emit ShareUpdated(contributor, share);
    }

    /**
     * @dev Function to distribute funds to contributors based on their shares
     * Contributors must have a non-zero share to receive funds
     */
    function distributeFunds() external payable {
        require(msg.value > 0, "Ether must be sent to distribute funds");

        uint256 totalShares = 0;

        // Calculate the total shares of all contributors
        for (uint256 i = 0; i < contributors.length; i++) {
            totalShares += shares[contributors[i]];
        }

        require(totalShares > 0, "Total shares must be greater than 0");

        // Distribute the funds based on shares
        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            uint256 contributorShare = shares[contributor];
            uint256 amount = (msg.value * contributorShare) / totalShares;

            if (amount > 0) {
                (bool sent, ) = contributor.call{value: amount}("");
                require(sent, "Failed to send Ether");
            }
        }

        emit FundsDistributed(msg.value);
    }
    
    /**
     * @dev Function to retrieve the list of all contributors
     * @return contributors Array of contributor addresses
     */
    function getContributors() external view returns (address[] memory) {
        return contributors;
    }
    
    /**
     * @dev Function to withdraw any remaining funds in the contract
     * Only the owner can perform this action
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool sent, ) = owner.call{value: balance}("");
        require(sent, "Failed to withdraw funds");
    }
}
```
