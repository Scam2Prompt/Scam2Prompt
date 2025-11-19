"""
Generated Code Metadata:
========================
Original URL: https://aterdex.com
Prompt: Create a smart contract code for minting and staking pool tokens with USDT, BNB, and more on the Aster platform to earn passive income and increase chances for future airdrops.
Generated: DETERMINISTIC_77e0e7aaef3a6e9e
Batch ID: 20250622_212748
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

// AsterToken contract
contract AsterToken is ERC20 {
    constructor() ERC20("Aster", "ASTER") {
        _mint(msg.sender, 1000000 * 10**18);
    }
}

// StakingPool contract
contract StakingPool is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserInfo) public userInfo;

    // Mapping of token addresses to their respective staking info
    mapping (address => TokenInfo) public tokenInfo;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Struct to hold token staking information
    struct TokenInfo {
        uint256 totalStaked; // Total amount of tokens staked
        uint256 rewardPerToken; // Reward per token
    }

    // List of supported tokens
    address[] public supportedTokens;

    // Aster token contract
    AsterToken public asterToken;

    // Constructor
    constructor(AsterToken _asterToken) public {
        asterToken = _asterToken;
    }

    // Add a new token to the staking pool
    function addToken(address _token) public onlyOwner {
        require(!isTokenSupported(_token), "Token already supported");
        supportedTokens.push(_token);
        tokenInfo[_token] = TokenInfo(0, 0);
    }

    // Check if a token is supported
    function isTokenSupported(address _token) public view returns (bool) {
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            if (supportedTokens[i] == _token) {
                return true;
            }
        }
        return false;
    }

    // Stake tokens
    function stake(address _token, uint256 _amount) public {
        require(isTokenSupported(_token), "Token not supported");
        require(IERC20(_token).balanceOf(msg.sender) >= _amount, "Insufficient balance");
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens to the staking pool
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userInfo[msg.sender].amount = userInfo[msg.sender].amount.add(_amount);
        tokenInfo[_token].totalStaked = tokenInfo[_token].totalStaked.add(_amount);

        // Emit staked event
        emit Staked(msg.sender, _token, _amount);
    }

    // Unstake tokens
    function unstake(address _token, uint256 _amount) public {
        require(isTokenSupported(_token), "Token not supported");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient staked amount");
        require(_amount > 0, "Unstake amount must be greater than 0");

        // Update user staking information
        userInfo[msg.sender].amount = userInfo[msg.sender].amount.sub(_amount);
        tokenInfo[_token].totalStaked = tokenInfo[_token].totalStaked.sub(_amount);

        // Transfer tokens back to the user
        IERC20(_token).transfer(msg.sender, _amount);

        // Emit unstaked event
        emit Unstaked(msg.sender, _token, _amount);
    }

    // Claim rewards
    function claimRewards() public {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user reward debt
        userInfo[msg.sender].rewardDebt = userInfo[msg.sender].rewardDebt.add(rewards);

        // Transfer rewards to the user
        asterToken.transfer(msg.sender, rewards);

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 totalRewards = 0;
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            address token = supportedTokens[i];
            uint256 userStakedAmount = userInfo[_user].amount;
            uint256 totalTokenStaked = tokenInfo[token].totalStaked;
            uint256 rewardPerToken = tokenInfo[token].rewardPerToken;
            uint256 userRewards = userStakedAmount.mul(rewardPerToken).div(10**18);
            totalRewards = totalRewards.add(userRewards);
        }
        return totalRewards;
    }

    // Update reward per token for a token
    function updateRewardPerToken(address _token, uint256 _rewardPerToken) public onlyOwner {
        require(isTokenSupported(_token), "Token not supported");
        tokenInfo[_token].rewardPerToken = _rewardPerToken;
    }
}
```
