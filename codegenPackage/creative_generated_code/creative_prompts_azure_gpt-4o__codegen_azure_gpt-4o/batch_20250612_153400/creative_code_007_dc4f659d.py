"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visit-magamemecoin.pages.dev
Prompt: Develop a smart contract function to ensure the 0.33% donation allocation for U.S. Veterans and Child Rescue charities when MAGA Memecoin transactions occur.
Generated: DETERMINISTIC_dc4f659d5ff3ec24
Batch ID: 20250612_153400
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
 * @title MAGAMemecoinDonation
 * @dev Smart contract to ensure 0.33% of every transaction is allocated to U.S. Veterans
 * and Child Rescue charities when MAGA Memecoin transactions occur.
 */
contract MAGAMemecoinDonation {
    address public owner;
    address public veteransCharityAddress;
    address public childRescueCharityAddress;
    uint256 public donationPercentage = 33; // Represents 0.33% (0.33 * 100)

    event DonationDistributed(uint256 amountToVeterans, uint256 amountToChildRescue);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    constructor(address _veteransCharityAddress, address _childRescueCharityAddress) {
        require(_veteransCharityAddress != address(0), "Veterans charity address cannot be zero.");
        require(_childRescueCharityAddress != address(0), "Child rescue charity address cannot be zero.");
        owner = msg.sender;
        veteransCharityAddress = _veteransCharityAddress;
        childRescueCharityAddress = _childRescueCharityAddress;
    }

    /**
     * @dev Handles donation allocation during MAGA Memecoin transactions.
     * @param transactionAmount The total amount of the transaction.
     */
    function handleDonation(uint256 transactionAmount) external payable {
        require(msg.value == transactionAmount, "Transaction amount mismatch with sent value.");
        require(transactionAmount > 0, "Transaction amount must be greater than zero.");

        // Calculate donation amount (0.33% of transaction)
        uint256 donationAmount = (transactionAmount * donationPercentage) / 10000;

        // Split donation amount equally between charities
        uint256 amountToVeterans = donationAmount / 2;
        uint256 amountToChildRescue = donationAmount - amountToVeterans;

        // Transfer donations to charity addresses
        (bool successVeterans, ) = veteransCharityAddress.call{value: amountToVeterans}("");
        require(successVeterans, "Transfer to Veterans charity failed.");

        (bool successChildRescue, ) = childRescueCharityAddress.call{value: amountToChildRescue}("");
        require(successChildRescue, "Transfer to Child Rescue charity failed.");

        emit DonationDistributed(amountToVeterans, amountToChildRescue);
    }

    /**
     * @dev Updates the charity addresses. Only callable by the owner.
     * @param _veteransCharityAddress The new address for the Veterans charity.
     * @param _childRescueCharityAddress The new address for the Child Rescue charity.
     */
    function updateCharityAddresses(
        address _veteransCharityAddress,
        address _childRescueCharityAddress
    ) external onlyOwner {
        require(_veteransCharityAddress != address(0), "Veterans charity address cannot be zero.");
        require(_childRescueCharityAddress != address(0), "Child rescue charity address cannot be zero.");

        veteransCharityAddress = _veteransCharityAddress;
        childRescueCharityAddress = _childRescueCharityAddress;
    }

    /**
     * @dev Withdraws any remaining funds accidentally sent to the contract.
     * Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Fallback function to accept ETH sent directly to the contract.
     */
    receive() external payable {}
}
```
