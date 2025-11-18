"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9eth.eu
Prompt: Write a smart contract in Solidity to check wallet eligibility for an ETH airdrop, similar to the functionality described on the "Lido Stake Wrap Airdrop Governance" portal.
Generated: DETERMINISTIC_c7221b27e2f769a0
Batch ID: 20250612_154829
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

contract AirdropEligibility {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => bool) public eligibleWallets; // Mapping to track eligible wallets
    mapping(address => bool) public claimed; // Mapping to track claimed airdrops

    // Events
    event WalletAdded(address indexed wallet);
    event AirdropClaimed(address indexed wallet);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender; // Set deployer as the owner
    }

    // Function to add eligible wallets for the airdrop
    function addEligibleWallets(address[] calldata wallets) external onlyOwner {
        for (uint i = 0; i < wallets.length; i++) {
            require(wallets[i] != address(0), "Invalid wallet address");
            eligibleWallets[wallets[i]] = true; // Mark wallet as eligible
            emit WalletAdded(wallets[i]); // Emit event
        }
    }

    // Function to check if a wallet is eligible
    function isEligible(address wallet) external view returns (bool) {
        return eligibleWallets[wallet]; // Return eligibility status
    }

    // Function to claim the airdrop
    function claimAirdrop() external {
        require(eligibleWallets[msg.sender], "Not eligible for airdrop");
        require(!claimed[msg.sender], "Airdrop already claimed");

        // Mark airdrop as claimed
        claimed[msg.sender] = true;

        // Logic to transfer airdrop tokens can be added here
        // For example: transferTokens(msg.sender, airdropAmount);

        emit AirdropClaimed(msg.sender); // Emit event
    }

    // Function to withdraw accidental ETH sent to the contract
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance); // Transfer balance to owner
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
