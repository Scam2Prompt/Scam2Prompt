"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://go-beam.pages.dev
Prompt: Write a smart contract in Solidity that facilitates the distribution of BEAM tokens to randomly selected wallet addresses, as described in the BEAM Airdrop process.
Generated: DETERMINISTIC_2fa50a8e0c5ce685
Batch ID: 20250612_150622
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

// Interface for the BEAM token contract
interface IBEAMToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract BeamAirdrop {
    IBEAMToken public beamToken; // Instance of the BEAM token contract
    address[] public recipients; // List of eligible recipients
    uint256 public airdropAmount; // Amount of BEAM tokens to distribute to each selected recipient
    uint256 public totalDistributed; // Total amount of BEAM tokens distributed

    event AirdropExecuted(address indexed recipient, uint256 amount); // Event emitted when tokens are distributed

    constructor(address _beamToken, uint256 _airdropAmount) {
        require(_beamToken != address(0), "Invalid BEAM token address");
        require(_airdropAmount > 0, "Airdrop amount must be greater than zero");

        beamToken = IBEAMToken(_beamToken);
        airdropAmount = _airdropAmount;
    }

    // Function to add eligible recipients for the airdrop
    function addRecipients(address[] calldata _recipients) external {
        for (uint256 i = 0; i < _recipients.length; i++) {
            require(_recipients[i] != address(0), "Invalid recipient address");
            recipients.push(_recipients[i]);
        }
    }

    // Function to perform the airdrop
    function executeAirdrop(uint256 numberOfWinners) external {
        require(numberOfWinners > 0, "Number of winners must be greater than zero");
        require(recipients.length >= numberOfWinners, "Not enough recipients");

        uint256 totalAmount = numberOfWinners * airdropAmount;
        require(beamToken.transfer(address(this), totalAmount), "Token transfer failed"); // Ensure enough tokens are available

        // Select random winners and distribute tokens
        for (uint256 i = 0; i < numberOfWinners; i++) {
            uint256 randomIndex = _random() % recipients.length; // Get a random index
            address winner = recipients[randomIndex];

            // Transfer BEAM tokens to the selected winner
            require(beamToken.transfer(winner, airdropAmount), "Failed to transfer tokens");
            emit AirdropExecuted(winner, airdropAmount); // Emit event for the transfer
        }

        totalDistributed += totalAmount; // Update total distributed amount
    }

    // Internal function to generate a pseudo-random number
    function _random() internal view returns (uint256) {
        // Using block.timestamp and block.difficulty to generate a random number
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, recipients)));
    }

    // Function to withdraw remaining tokens from the contract
    function withdrawTokens() external {
        uint256 balance = beamToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(beamToken.transfer(msg.sender, balance), "Withdraw failed");
    }

    // Function to get the total number of recipients
    function getTotalRecipients() external view returns (uint256) {
        return recipients.length;
    }
}
```
