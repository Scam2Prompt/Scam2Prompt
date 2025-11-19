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

contract PaymentDistribution {
    // Struct to represent a contributor
    struct Contributor {
        address payable wallet; // Wallet address of the contributor
        uint256 share;          // Share percentage of the total payment
    }

    // Mapping to store contributors by their address
    mapping(address => Contributor) public contributors;
    // Total shares of all contributors
    uint256 public totalShares;
    // Owner of the contract
    address public owner;

    // Event to log payment distribution
    event PaymentDistributed(uint256 totalAmount, uint256 totalShares);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to add a contributor
    function addContributor(address payable _wallet, uint256 _share) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        require(_share > 0, "Share must be greater than zero");
        require(contributors[_wallet].share == 0, "Contributor already exists");

        contributors[_wallet] = Contributor(_wallet, _share);
        totalShares += _share;
    }

    // Function to remove a contributor
    function removeContributor(address _wallet) external onlyOwner {
        require(contributors[_wallet].share > 0, "Contributor does not exist");

        totalShares -= contributors[_wallet].share;
        delete contributors[_wallet];
    }

    // Function to distribute payments to contributors
    function distributePayment() external payable {
        require(msg.value > 0, "No payment sent");
        require(totalShares > 0, "No contributors to distribute payment");

        // Distributing payment to each contributor based on their share
        for (address contributorAddress in contributors) {
            Contributor memory contributor = contributors[contributorAddress];
            uint256 payment = (msg.value * contributor.share) / totalShares;
            contributor.wallet.transfer(payment);
        }

        emit PaymentDistributed(msg.value, totalShares);
    }

    // Fallback function to accept Ether
    receive() external payable {
        // Accept Ether sent directly to the contract
    }

    // Function to withdraw any remaining balance in the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance);
    }
}
```
