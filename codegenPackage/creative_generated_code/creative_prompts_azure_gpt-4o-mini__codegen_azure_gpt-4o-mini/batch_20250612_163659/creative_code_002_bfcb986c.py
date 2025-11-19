"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-app.pages.dev
Prompt: Create a Solidity contract that implements the unique SocialFi model described on the Kangamoon website for earning additional tokens.
Generated: DETERMINISTIC_bfcb986cfcc49c37
Batch ID: 20250612_163659
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title KangamoonSocialFi
 * @dev Implements a SocialFi model for earning additional tokens
 */
contract KangamoonSocialFi is Ownable {
    // Mapping to track user balances
    mapping(address => uint256) public userBalances;
    // Total tokens distributed
    uint256 public totalDistributed;
    // The token to be distributed
    IERC20 public rewardToken;

    // Event emitted when tokens are earned
    event TokensEarned(address indexed user, uint256 amount);

    // Constructor to initialize the reward token
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to earn tokens based on user activity.
     * @param _amount The amount of tokens to reward the user.
     */
    function earnTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Update user balance
        userBalances[msg.sender] += _amount;
        totalDistributed += _amount;

        // Emit event for earning tokens
        emit TokensEarned(msg.sender, _amount);
    }

    /**
     * @dev Function for the owner to distribute tokens to users.
     * @param _user The address of the user to receive tokens.
     * @param _amount The amount of tokens to distribute.
     */
    function distributeTokens(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Transfer tokens to user
        rewardToken.transfer(_user, _amount);
    }

    /**
     * @dev Function to check the user's balance.
     * @return The balance of the user.
     */
    function checkUserBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }

    /**
     * @dev Function for the owner to withdraw tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Transfer tokens to owner
        rewardToken.transfer(owner(), _amount);
    }
}
```
