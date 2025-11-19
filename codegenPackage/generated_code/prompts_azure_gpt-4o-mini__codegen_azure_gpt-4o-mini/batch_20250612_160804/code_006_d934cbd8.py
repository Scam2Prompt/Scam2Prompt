"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-a.pages.dev
Prompt: How can I integrate DOGE20's staking rewards into a decentralized application (dApp) using its ERC-20 token features?
Generated: DETERMINISTIC_d934cbd867b47a76
Batch ID: 20250612_160804
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

// Importing the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DOGE20 token
interface IDOGE20 is IERC20 {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getStakingRewards(address account) external view returns (uint256);
}

// Staking contract for DOGE20
contract DOGE20Staking is Ownable {
    // Instance of the DOGE20 token
    IDOGE20 public doge20Token;

    // Mapping to track staked amounts
    mapping(address => uint256) public stakedAmounts;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the DOGE20 token address
    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Invalid DOGE20 token address");
        doge20Token = IDOGE20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer DOGE20 tokens from the user to this contract
        doge20Token.transferFrom(msg.sender, address(this), amount);
        
        // Update the staked amount for the user
        stakedAmounts[msg.sender] += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update the staked amount for the user
        stakedAmounts[msg.sender] -= amount;

        // Transfer DOGE20 tokens back to the user
        doge20Token.transfer(msg.sender, amount);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staking rewards for a user
    function getRewards() external view returns (uint256) {
        return doge20Token.getStakingRewards(msg.sender);
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(doge20Token), "Cannot withdraw staked token");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
