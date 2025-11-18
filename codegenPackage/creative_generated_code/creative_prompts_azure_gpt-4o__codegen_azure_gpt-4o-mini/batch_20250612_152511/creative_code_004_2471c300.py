"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-astrovault.pages.dev
Prompt: Develop a smart contract to facilitate cross-chain value capture for AstroVault ($AXV) tokens, ensuring compatibility with multi-chain networks.
Generated: DETERMINISTIC_2471c3006457c520
Batch ID: 20250612_152511
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

// Import necessary OpenZeppelin contracts for security and utility
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for supporting cross-chain functionality
interface ICrossChainBridge {
    function depositTokens(address token, uint256 amount, address recipient) external;
    function withdrawTokens(address token, uint256 amount, address recipient) external;
}

// AstroVault Smart Contract
contract AstroVault is Ownable {
    // Declare state variables
    IERC20 public axvToken; // ERC20 token being captured
    ICrossChainBridge public bridge; // Cross-chain bridge contract

    // Event for logging token deposits
    event TokensDeposited(address indexed user, uint256 amount);
    // Event for logging token withdrawals
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifier to check the amount of tokens to be deposited
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Constructor to initialize contract state
    constructor(IERC20 _axvToken, ICrossChainBridge _bridge) {
        axvToken = _axvToken;
        bridge = _bridge;
    }

    // Function to deposit AXV tokens to the smart contract
    function deposit(uint256 amount) external validAmount(amount) {
        // Transfer AXV tokens from user to this contract
        require(axvToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Log the deposit event
        emit TokensDeposited(msg.sender, amount);
    }

    // Function to withdraw AXV tokens to another chain
    function withdraw(uint256 amount, address recipient) external onlyOwner validAmount(amount) {
        // Ensure the contract has enough tokens to withdraw
        require(axvToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Initiate the withdrawal on the cross-chain bridge
        bridge.withdrawTokens(address(axvToken), amount, recipient);

        // Log the withdrawal event
        emit TokensWithdrawn(msg.sender, amount);
    }

    // Function to transfer AXV tokens to another chain
    function transferToAnotherChain(uint256 amount, address recipient) external onlyOwner validAmount(amount) {
        // Ensure the contract has enough tokens to transfer
        require(axvToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Deposit tokens to the bridge for cross-chain transfer
        bridge.depositTokens(address(axvToken), amount, recipient);

        // Log the transfer event (if needed, can be added)
    }

    // Function to retrieve the contract's AXV token balance
    function getTokenBalance() external view returns (uint256) {
        return axvToken.balanceOf(address(this));
    }
}
```
