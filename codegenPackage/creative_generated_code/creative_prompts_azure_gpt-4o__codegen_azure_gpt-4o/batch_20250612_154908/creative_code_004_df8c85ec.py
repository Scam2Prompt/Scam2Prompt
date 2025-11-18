"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: Create a smart contract in Solidity to interact with Gitcoin's Round Manager for distributing funds to multiple recipients based on predefined criteria.
Generated: DETERMINISTIC_df8c85ecca9fd55a
Batch ID: 20250612_154908
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
 * @title GitcoinFundsDistributor
 * @dev A smart contract to interact with Gitcoin Round Manager to distribute funds to multiple recipients
 * based on predefined criteria.
 */
contract GitcoinFundsDistributor {
    address public owner;

    // Struct to define recipient information
    struct Recipient {
        address payable recipientAddress;
        uint256 allocationPercentage; // Allocation percentage (0-100)
    }

    Recipient[] public recipients;
    uint256 public totalPercentage;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Event emitted after successful fund distribution
    event FundsDistributed(uint256 totalAmount, uint256 timestamp);

    /**
     * @dev Constructor sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds a recipient to the distribution list. 
     * @param _recipientAddress The recipient's payable address.
     * @param _allocationPercentage The percentage of funds to allocate to this recipient.
     */
    function addRecipient(address payable _recipientAddress, uint256 _allocationPercentage) external onlyOwner {
        require(_recipientAddress != address(0), "Recipient address cannot be zero address");
        require(_allocationPercentage > 0 && _allocationPercentage <= 100, "Allocation percentage must be between 1 and 100");
        require(totalPercentage + _allocationPercentage <= 100, "Total allocation exceeds 100%");

        recipients.push(Recipient(_recipientAddress, _allocationPercentage));
        totalPercentage += _allocationPercentage;
    }

    /**
     * @dev Removes all recipients and resets allocations.
     */
    function resetRecipients() external onlyOwner {
        delete recipients;
        totalPercentage = 0;
    }

    /**
     * @dev Distributes funds to recipients based on their allocation percentage.
     * Contract must have a balance to distribute funds.
     */
    function distributeFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for distribution");
        require(recipients.length > 0, "No recipients to distribute funds to");

        for (uint256 i = 0; i < recipients.length; i++) {
            Recipient memory recipient = recipients[i];
            uint256 amount = (contractBalance * recipient.allocationPercentage) / 100;
            recipient.recipientAddress.transfer(amount);
        }

        emit FundsDistributed(contractBalance, block.timestamp);
    }

    /**
     * @dev Allows the contract to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw any remaining funds in the contract.
     * @param _to The address to send the remaining funds to.
     */
    function withdrawRemainingFunds(address payable _to) external onlyOwner {
        require(_to != address(0), "Recipient address cannot be zero address");
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");

        _to.transfer(contractBalance);
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract to a new owner.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be zero address");
        owner = _newOwner;
    }
}
```
