"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainrectification-dapp.web.app
Prompt: Develop a smart contract to handle staking balance management and provide real-time token value viewing, incorporating the features mentioned under "Staking Balance" and "View Value of Token."
Generated: DETERMINISTIC_e2c6b7f34af38712
Batch ID: 20250612_153916
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingContract {
    using SafeMath for uint256;

    // ERC20 token contract
    IERC20 public token;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Time of staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token contract
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens staked");

        // Reset user's stake information
        stakes[msg.sender].amount = 0;

        require(token.transfer(msg.sender, stakedAmount), "Transfer failed");
        emit Unstaked(msg.sender, stakedAmount);
    }

    // Function to view the staked balance of a user
    function viewStakedBalance(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to view the value of the staked tokens in terms of the token's current price
    function viewValueOfStakedTokens(address _user, uint256 currentTokenPrice) external view returns (uint256) {
        require(currentTokenPrice > 0, "Token price must be greater than 0");
        
        uint256 stakedAmount = stakes[_user].amount;
        return stakedAmount.mul(currentTokenPrice).div(1e18); // Assuming token price is in 18 decimals
    }
}
```
