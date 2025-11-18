"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://broccoliclaim.web.app
Prompt: Create a smart contract for managing token rewards distribution, inspired by the Broccoli platform's single-transaction claim functionality.
Generated: DETERMINISTIC_6cf040b545fec229
Batch ID: 20250612_154542
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

/**
 * @title TokenRewardsDistributor
 * @dev A smart contract for managing token rewards distribution with single-transaction claim functionality.
 */
contract TokenRewardsDistributor {
    // Using SafeMath for arithmetic operations (Optional: Solidity 0.8.x has built-in overflow/underflow protections)
    using SafeMath for uint256;

    // Token interface
    IERC20 public immutable rewardToken;

    // Owner of the contract
    address public owner;

    // Mapping to store reward balances for users
    mapping(address => uint256) public rewards;

    // Events
    event RewardsDistributed(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    /**
     * @dev Modifier to check if the caller is the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the reward token and owner.
     * @param _rewardToken Address of the ERC20 reward token.
     */
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be a zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param _user Address of the user to receive rewards.
     * @param _amount Amount of rewards to distribute.
     */
    function distributeRewards(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Reward amount must be greater than zero");

        rewards[_user] = rewards[_user].add(_amount);
        emit RewardsDistributed(_user, _amount);
    }

    /**
     * @dev Function for users to claim their rewards in a single transaction.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Clear the user's rewards balance
        rewards[msg.sender] = 0;

        // Transfer tokens from contract to user
        require(rewardToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract. Only owner can execute this.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        require(rewardToken.transfer(owner, _amount), "Token withdrawal failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// SafeMath library for arithmetic operations (optional for Solidity 0.8.x)
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "Addition overflow");
        return c;
    }
}
```
