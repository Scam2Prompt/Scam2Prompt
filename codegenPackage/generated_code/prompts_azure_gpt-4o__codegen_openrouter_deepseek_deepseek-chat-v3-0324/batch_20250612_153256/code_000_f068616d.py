"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Write a smart contract using Solidity that implements a payment distribution mechanism for contributors in a product line, as described in the LookRev branch system.
Generated: DETERMINISTIC_f068616d511f6301
Batch ID: 20250612_153256
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
 * @title LookRevPaymentDistribution
 * @dev A smart contract for distributing payments among contributors in a product line
 * according to predefined percentages. Implements the LookRev branch system.
 */
contract LookRevPaymentDistribution {
    // Struct to store contributor information
    struct Contributor {
        address payable wallet;
        uint256 percentage; // Percentage points (e.g., 20 = 20%)
        string role;
    }

    // Owner of the contract
    address payable public owner;

    // List of contributors
    Contributor[] public contributors;

    // Total percentage allocated (must sum to 100)
    uint256 public totalPercentage;

    // Events
    event PaymentDistributed(address indexed receiver, uint256 amount, string role);
    event ContributorAdded(address indexed wallet, uint256 percentage, string role);
    event ContributorRemoved(address indexed wallet);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier validPercentage(uint256 _percentage) {
        require(_percentage > 0 && _percentage <= 100, "Percentage must be between 1 and 100");
        _;
    }

    modifier validTotalPercentage(uint256 _newPercentage) {
        require(totalPercentage + _newPercentage <= 100, "Total percentage cannot exceed 100");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the owner
     */
    constructor() {
        owner = payable(msg.sender);
    }

    /**
     * @dev Add a new contributor to the distribution list
     * @param _wallet The payable address of the contributor
     * @param _percentage The percentage of payments the contributor should receive
     * @param _role The role/description of the contributor
     */
    function addContributor(
        address payable _wallet,
        uint256 _percentage,
        string memory _role
    ) external onlyOwner validPercentage(_percentage) validTotalPercentage(_percentage) {
        require(_wallet != address(0), "Invalid wallet address");
        
        contributors.push(Contributor(_wallet, _percentage, _role));
        totalPercentage += _percentage;
        
        emit ContributorAdded(_wallet, _percentage, _role);
    }

    /**
     * @dev Remove a contributor from the distribution list
     * @param _index The index of the contributor to remove
     */
    function removeContributor(uint256 _index) external onlyOwner {
        require(_index < contributors.length, "Invalid contributor index");
        
        Contributor memory removedContributor = contributors[_index];
        totalPercentage -= removedContributor.percentage;
        
        // Move last element to the deleted spot
        if (_index < contributors.length - 1) {
            contributors[_index] = contributors[contributors.length - 1];
        }
        
        contributors.pop();
        
        emit ContributorRemoved(removedContributor.wallet);
    }

    /**
     * @dev Distribute the received payment among contributors
     */
    function distributePayment() external payable {
        require(msg.value > 0, "Payment amount must be greater than 0");
        require(contributors.length > 0, "No contributors to distribute to");
        require(totalPercentage == 100, "Total percentage must equal 100");
        
        uint256 remainingAmount = msg.value;
        
        // Distribute to all contributors except the last one
        for (uint256 i = 0; i < contributors.length - 1; i++) {
            Contributor memory contributor = contributors[i];
            uint256 amount = (msg.value * contributor.percentage) / 100;
            
            (bool success, ) = contributor.wallet.call{value: amount}("");
            require(success, "Transfer failed");
            
            remainingAmount -= amount;
            emit PaymentDistributed(contributor.wallet, amount, contributor.role);
        }
        
        // Send remaining amount to last contributor to avoid rounding errors
        Contributor memory lastContributor = contributors[contributors.length - 1];
        (bool lastSuccess, ) = lastContributor.wallet.call{value: remainingAmount}("");
        require(lastSuccess, "Transfer failed");
        
        emit PaymentDistributed(lastContributor.wallet, remainingAmount, lastContributor.role);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param _newOwner The address of the new owner
     */
    function transferOwnership(address payable _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Get the number of contributors
     * @return The number of contributors
     */
    function getContributorCount() external view returns (uint256) {
        return contributors.length;
    }

    /**
     * @dev Fallback function to receive payments
     */
    receive() external payable {
        distributePayment();
    }
}
```
