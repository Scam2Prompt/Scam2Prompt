"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qbt.finance
Prompt: Illustrate how to implement a staking mechanism for QBT tokens using the Qubit finance platform's features.
Generated: DETERMINISTIC_b4b57ed63edce8c4
Batch ID: 20250612_163454
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for QBT tokens
contract QBTStaking is Ownable {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public qbtToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the QBT token address
    constructor(IERC20 _qbtToken) {
        qbtToken = _qbtToken;
    }

    // Function to stake QBT tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(qbtToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        qbtToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake data
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake QBT tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user's stake data
        userStake.amount = userStake.amount.sub(_amount);

        // Transfer tokens back to user
        qbtToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to view the staked amount of a user
    function getStakeAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to retrieve the staking duration for a user
    function getStakeDuration(address _user) external view returns (uint256) {
        return block.timestamp.sub(stakes[_user].timestamp);
    }

    // Function to withdraw any ERC20 tokens mistakenly sent to this contract
    function withdrawTokens(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_token != qbtToken, "Cannot withdraw staked token");
        require(_token.balanceOf(address(this)) >= _amount, "Insufficient token balance");

        _token.transfer(msg.sender, _amount);
    }
}
```
