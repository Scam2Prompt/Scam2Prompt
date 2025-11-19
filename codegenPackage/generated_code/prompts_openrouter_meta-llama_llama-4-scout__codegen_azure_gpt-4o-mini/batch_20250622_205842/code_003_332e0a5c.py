"""
Generated Code Metadata:
========================
Original URL: https://fight2maga-claimreward.pages.dev
Prompt: "Generate a simple smart contract in Solidity that allows users to donate ETH and receive $FIGHT tokens in return, based on the token's contract address and the team's donation initiative."
Generated: DETERMINISTIC_332e0a5c3d9e804e
Batch ID: 20250622_205842
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

// Interface for the ERC20 token contract
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for donation and token distribution
contract DonationContract {
    // Address of the $FIGHT token contract
    address public fightTokenAddress;
    // Mapping to track donations
    mapping(address => uint256) public donations;

    // Event to log donations
    event Donated(address indexed donor, uint256 amount, uint256 tokensReceived);

    // Constructor to set the $FIGHT token address
    constructor(address _fightTokenAddress) {
        require(_fightTokenAddress != address(0), "Invalid token address");
        fightTokenAddress = _fightTokenAddress;
    }

    // Function to donate ETH and receive $FIGHT tokens
    function donate() external payable {
        require(msg.value > 0, "Donation must be greater than 0");

        // Calculate the amount of $FIGHT tokens to send (1 ETH = 100 $FIGHT for example)
        uint256 tokensToSend = msg.value * 100; // Adjust the rate as needed

        // Transfer $FIGHT tokens to the donor
        IERC20 fightToken = IERC20(fightTokenAddress);
        require(fightToken.balanceOf(address(this)) >= tokensToSend, "Insufficient tokens in contract");

        // Update the donation mapping
        donations[msg.sender] += msg.value;

        // Transfer tokens to the donor
        require(fightToken.transfer(msg.sender, tokensToSend), "Token transfer failed");

        // Emit donation event
        emit Donated(msg.sender, msg.value, tokensToSend);
    }

    // Function to withdraw ETH from the contract (only owner can call this)
    function withdrawETH() external {
        // Only the contract owner should be able to withdraw
        // Implement ownership check here (e.g., using Ownable pattern)

        // Transfer all ETH to the owner
        payable(msg.sender).transfer(address(this).balance);
    }

    // Function to withdraw $FIGHT tokens from the contract (only owner can call this)
    function withdrawTokens(uint256 amount) external {
        // Only the contract owner should be able to withdraw
        // Implement ownership check here (e.g., using Ownable pattern)

        IERC20 fightToken = IERC20(fightTokenAddress);
        require(fightToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Transfer tokens to the owner
        require(fightToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Fallback function to accept ETH donations
    receive() external payable {
        donate();
    }
}
```
