"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-store-en.pages.dev
Prompt: Describe how to implement a rewards program in a decentralized application (dApp) using Pushd tokens to incentivize user engagement.
Generated: DETERMINISTIC_84ee17a711f48c58
Batch ID: 20250612_161617
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
 * @title RewardsProgram
 * @dev A decentralized application (dApp) rewards program using Pushd tokens to incentivize user engagement.
 * Users earn Pushd tokens for completing tasks/interactions, and balances can be withdrawn.
 */
contract RewardsProgram {
    // Token contract interface
    IERC20 public pushdToken;

    // Mapping to store user balances of Pushd tokens
    mapping(address => uint256) public userBalances;

    // Owner of the contract
    address public owner;

    // Events for logging
    event TokensAwarded(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifier for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    /**
     * @dev Constructor to initialize the Pushd token address and set contract owner.
     * @param _pushdToken The address of the Pushd token contract.
     */
    constructor(address _pushdToken) {
        require(_pushdToken != address(0), "Invalid token address");
        pushdToken = IERC20(_pushdToken);
        owner = msg.sender;
    }

    /**
     * @dev Award Pushd tokens to a user for completing a task or interaction.
     * @param _user The address of the user to reward.
     * @param _amount The amount of Pushd tokens to award.
     */
    function awardTokens(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than zero");
        
        // Update user balance
        userBalances[_user] += _amount;

        emit TokensAwarded(_user, _amount);
    }

    /**
     * @dev Withdraw accumulated Pushd tokens by the user.
     */
    function withdrawTokens() external {
        uint256 balance = userBalances[msg.sender];
        require(balance > 0, "No tokens to withdraw");

        // Update user balance before transferring to prevent reentrancy attacks
        userBalances[msg.sender] = 0;

        // Transfer Pushd tokens to the user
        require(pushdToken.transfer(msg.sender, balance), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Emergency function to recover tokens accidentally sent to the contract.
     * @param _token The address of the token to recover.
     * @param _to The address where the recovered tokens will be sent.
     * @param _amount The amount of tokens to recover.
     */
    function recoverTokens(address _token, address _to, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");

        IERC20(_token).transfer(_to, _amount);
    }
}

/**
 * @dev ERC20 Token Interface to interact with Pushd token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
