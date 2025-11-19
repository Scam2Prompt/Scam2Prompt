"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememogulsclaim.pages.dev
Prompt: Write a code snippet for staking and unstaking Meme Moguls tokens in a decentralized application.
Generated: DETERMINISTIC_84abb91a8a5d6de3
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for staking and unstaking Meme Moguls tokens
contract MemeMogulsStaking {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public mogulToken;

    // User staking details
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping from user address to user information
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _mogulToken) {
        mogulToken = _mogulToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        
        // Transfer tokens from user to this contract
        mogulToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.rewardDebt; // Placeholder for reward logic

        // Update total staked
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update user info
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt; // Placeholder for reward logic

        // Transfer tokens back to user
        mogulToken.transfer(msg.sender, _amount);

        // Update total staked
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return userInfo[_user].amount;
    }
}
```
