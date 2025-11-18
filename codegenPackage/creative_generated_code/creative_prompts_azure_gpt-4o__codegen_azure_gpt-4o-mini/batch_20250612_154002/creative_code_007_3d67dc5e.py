"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defie.me
Prompt: Write code to enable staking functionality for an Ethereum-based DeFi platform.
Generated: DETERMINISTIC_3d67dc5e19a212eb
Batch ID: 20250612_154002
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

// Import the OpenZeppelin ERC20 and Ownable contracts for security and functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with the staking contract
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getStakedAmount(address user) external view returns (uint256);
}

// Main staking contract
contract Staking is IStaking, Ownable {
    // ERC20 token that will be staked
    IERC20 public stakingToken;

    // Mapping to track staked amounts of users
    mapping(address => uint256) private _stakedAmounts;

    // Event emitted on successful stake
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted on successful withdrawal
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Staking function allowing users to stake tokens
    function stake(uint256 amount) external override {
        require(amount > 0, "Cannot stake zero tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        _stakedAmounts[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Withdraw function allowing users to withdraw their staked tokens
    function withdraw(uint256 amount) external override {
        uint256 stakedAmount = _stakedAmounts[msg.sender];
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedAmount >= amount, "Insufficient staked amount");

        _stakedAmounts[msg.sender] -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view override returns (uint256) {
        return _stakedAmounts[user];
    }

    // Only owner can withdraw any tokens mistakenly sent to the contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
