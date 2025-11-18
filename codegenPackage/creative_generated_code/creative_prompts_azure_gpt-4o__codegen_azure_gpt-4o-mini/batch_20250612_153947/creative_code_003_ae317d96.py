"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testforfucksakeqq.com
Prompt: Generate a smart contract snippet that facilitates delegation of staked EIGEN tokens on EigenLayer.
Generated: DETERMINISTIC_ae317d96341cba1c
Batch ID: 20250612_153947
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

// Importing the required interfaces for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract facilitates delegation of staked EIGEN tokens on EigenLayer
contract EigenDelegation is Ownable {
    // Token interface for EIGEN token
    IERC20 public eigenToken;

    // Mapping to track delegated stakes
    mapping(address => uint256) public delegatedStakes;

    // Event emitted when tokens are delegated
    event TokensDelegated(address indexed delegator, uint256 amount);

    // Event emitted when tokens are undelegated
    event TokensUndelegated(address indexed delegator, uint256 amount);

    // Modifier to check if the caller has sufficient stake
    modifier hasSufficientStake(uint256 amount) {
        require(delegatedStakes[msg.sender] >= amount, "Insufficient delegated stake");
        _;
    }

    // Constructor to set the EIGEN token address
    constructor(address _eigenToken) {
        require(_eigenToken != address(0), "Invalid token address");
        eigenToken = IERC20(_eigenToken);
    }

    // Function to delegate tokens
    function delegateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer EIGEN tokens from the caller to this contract
        require(eigenToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the delegated stakes
        delegatedStakes[msg.sender] += amount;

        // Emit event for delegation
        emit TokensDelegated(msg.sender, amount);
    }

    // Function to undelegate tokens
    function undelegateTokens(uint256 amount) external hasSufficientStake(amount) {
        require(amount > 0, "Amount must be greater than zero");

        // Update the delegated stakes
        delegatedStakes[msg.sender] -= amount;

        // Transfer EIGEN tokens back to the caller
        require(eigenToken.transfer(msg.sender, amount), "Token transfer failed");

        // Emit event for undelegation
        emit TokensUndelegated(msg.sender, amount);
    }

    // Function to get the delegated stake of the caller
    function getDelegatedStake() external view returns (uint256) {
        return delegatedStakes[msg.sender];
    }

    // Function to withdraw all delegated tokens by the owner (in case of emergency)
    function emergencyWithdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(eigenToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer EIGEN tokens to the owner
        require(eigenToken.transfer(owner(), amount), "Token transfer failed");
    }
}
```
