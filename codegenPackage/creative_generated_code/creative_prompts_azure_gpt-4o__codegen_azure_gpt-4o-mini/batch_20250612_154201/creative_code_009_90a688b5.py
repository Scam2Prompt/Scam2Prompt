"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrade-fegs.pages.dev
Prompt: Write a Solidity function for a Smart Contract that integrates with the FEG Token ecosystem to enable presale participation, ensuring compliance with slippage and tax settings.
Generated: DETERMINISTIC_90a688b599c15dbc
Batch ID: 20250612_154201
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

// Importing the necessary interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PresaleParticipation is Ownable {
    // Address of the FEG token
    address public fegTokenAddress;

    // Event to be emitted when a user participates in the presale
    event PresaleParticipated(address indexed participant, uint256 amount);

    // Setting up the token address in the constructor
    constructor(address _fegTokenAddress) {
        require(_fegTokenAddress != address(0), "Invalid FEG token address");
        fegTokenAddress = _fegTokenAddress;
    }

    // Function to participate in the presale
    function participateInPresale(uint256 amount, uint256 minAmountOut, uint256 taxRate) external {
        // Validate the input parameters
        require(amount > 0, "Amount must be greater than zero");
        require(taxRate <= 100, "Tax rate must be between 0 and 100");

        // Transfer FEG tokens from participant to this contract
        IERC20 fegToken = IERC20(fegTokenAddress);
        uint256 initialBalance = fegToken.balanceOf(address(this));

        // Transfer tokens from the participant to the contract
        require(fegToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        uint256 newBalance = fegToken.balanceOf(address(this));
        uint256 receivedAmount = newBalance - initialBalance;

        // Calculate the effective amount after tax
        uint256 effectiveAmount = receivedAmount * (100 - taxRate) / 100;

        // Check for slippage compliance
        require(effectiveAmount >= minAmountOut, "Received amount too low");

        // Emit an event for successful participation
        emit PresaleParticipated(msg.sender, effectiveAmount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        IERC20 fegToken = IERC20(fegTokenAddress);
        uint256 contractBalance = fegToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");

        // Transfer tokens to the owner
        require(fegToken.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
