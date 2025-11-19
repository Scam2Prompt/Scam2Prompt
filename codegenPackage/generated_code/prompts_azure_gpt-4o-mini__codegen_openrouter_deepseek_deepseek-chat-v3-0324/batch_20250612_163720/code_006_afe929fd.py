"""
Generated Code Metadata:
========================
Original URL: https://multichaingreenbitcoinapp.pages.dev
Prompt: Develop a smart contract that allows users to stake their $GBTC tokens and earn rewards based on their predictions of Bitcoin prices.
Generated: DETERMINISTIC_afe929fd48ac437e
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract for staking $GBTC tokens with Bitcoin price prediction rewards:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract GBTCStaking is Ownable {
    IERC20 public gbtcToken;
    AggregatorV3Interface public priceFeed;

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 predictedPrice; // Predicted BTC price in USD (with 8 decimals)
        bool rewardClaimed;
    }

    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public constant REWARD_PERCENTAGE = 10; // 10% reward for correct prediction
    uint256 public totalStaked;
    
    mapping(address => Stake[]) public userStakes;

    event Staked(address indexed user, uint256 amount, uint256 predictedPrice);
    event RewardClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    constructor(address _gbtcToken, address _priceFeed) {
        require(_gbtcToken != address(0), "Invalid token address");
        require(_priceFeed != address(0), "Invalid price feed address");
        
        gbtcToken = IERC20(_gbtcToken);
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    function stake(uint256 _amount, uint256 _predictedPrice) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(gbtcToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        require(gbtcToken.allowance(msg.sender, address(this)) >= _amount, "Not enough allowance");

        bool transferSuccess = gbtcToken.transferFrom(msg.sender, address(this), _amount);
        require(transferSuccess, "Token transfer failed");

        userStakes[msg.sender].push(Stake({
            amount: _amount,
            startTime: block.timestamp,
            predictedPrice: _predictedPrice,
            rewardClaimed: false
        }));

        totalStaked += _amount;
        emit Staked(msg.sender, _amount, _predictedPrice);
    }

    function claimReward(uint256 _stakeIndex) external {
        require(_stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][_stakeIndex];
        
        require(block.timestamp >= userStake.startTime + MIN_STAKE_DURATION, "Staking period not ended");
        require(!userStake.rewardClaimed, "Reward already claimed");

        (, int256 currentPrice, , , ) = priceFeed.latestRoundData();
        uint256 actualPrice = uint256(currentPrice);

        if (actualPrice == userStake.predictedPrice) {
            uint256 rewardAmount = (userStake.amount * REWARD_PERCENTAGE) / 100;
            
            require(gbtcToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
            bool rewardSuccess = gbtcToken.transfer(msg.sender, rewardAmount);
            require(rewardSuccess, "Reward transfer failed");
            
            emit RewardClaimed(msg.sender, rewardAmount);
        }

        userStake.rewardClaimed = true;
    }

    function unstake(uint256 _stakeIndex) external {
        require(_stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][_stakeIndex];
        
        require(block.timestamp >= userStake.startTime + MIN_STAKE_DURATION, "Staking period not ended");

        uint256 amountToUnstake = userStake.amount;
        totalStaked -= amountToUnstake;

        // Remove the stake from the array
        if (_stakeIndex < userStakes[msg.sender].length - 1) {
            userStakes[msg.sender][_stakeIndex] = userStakes[msg.sender][userStakes[msg.sender].length - 1];
        }
        userStakes[msg.sender].pop();

        bool transferSuccess = gbtcToken.transfer(msg.sender, amountToUnstake);
        require(transferSuccess, "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    function getUserStakes(address _user) external view returns (Stake[] memory) {
        return userStakes[_user];
    }

    function getCurrentBTCPrice() external view returns (uint256) {
        (, int256 currentPrice, , , ) = priceFeed.latestRoundData();
        return uint256(currentPrice);
    }

    // Emergency function to recover ERC20 tokens (only owner)
    function recoverERC20(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).transfer(owner(), _amount);
    }
}
```
