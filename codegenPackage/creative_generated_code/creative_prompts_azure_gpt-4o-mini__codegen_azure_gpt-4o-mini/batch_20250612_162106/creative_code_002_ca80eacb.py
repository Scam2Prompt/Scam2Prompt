"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockketpool.github.io
Prompt: Explain how to create and manage a Rocket Pool node operator using smart contracts.
Generated: DETERMINISTIC_ca80eacb39e9dc55
Batch ID: 20250612_162106
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

// Importing required contracts and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// RocketPoolNodeOperator: A contract to manage a Rocket Pool node operator
contract RocketPoolNodeOperator {
    // State variables
    address public owner; // The owner of the node operator
    uint256 public totalStaked; // Total amount staked by the operator
    IERC20 public rETH; // Reference to the Rocket Pool ETH token contract

    // Events
    event NodeOperatorCreated(address indexed operator, uint256 initialStake);
    event EtherStaked(address indexed operator, uint256 amount);
    event EtherUnstaked(address indexed operator, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _rETH) {
        require(_rETH != address(0), "Invalid rETH address");
        owner = msg.sender; // Set contract creator as owner
        rETH = IERC20(_rETH); // Initialize the rETH token interface
    }

    // Function to stake ETH in the Rocket Pool
    function stake(uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid staking amount");
        
        // Transfer rETH tokens to this contract
        rETH.transferFrom(msg.sender, address(this), amount);
        
        // Update total staked amount
        totalStaked += amount;

        emit EtherStaked(msg.sender, amount);
    }

    // Function to unstake ETH from the Rocket Pool
    function unstake(uint256 amount) external onlyOwner {
        require(amount > 0 && amount <= totalStaked, "Invalid unstaking amount");
        
        // Update total staked amount
        totalStaked -= amount;

        // Transfer rETH tokens back to the operator
        rETH.transfer(msg.sender, amount);

        emit EtherUnstaked(msg.sender, amount);
    }

    // Function to retrieve the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to withdraw any ERC20 tokens mistakenly sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(rETH), "Cannot withdraw rETH");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to destroy the contract and send remaining funds to the owner
    function destroy() external onlyOwner {
        selfdestruct(payable(owner));
    }
}
```
