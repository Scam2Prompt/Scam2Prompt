"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: "Generate a smart contract code for a liquidity mining-based bond with no Impermanent Loss for LP Farming, similar to iZiSwap's Farm iUSD."
Generated: DETERMINISTIC_6d398ae5a5897f94
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, a popular language for smart contracts on the Ethereum blockchain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityMiningBond
 * @author [Your Name]
 * @notice A smart contract for a liquidity mining-based bond with no Impermanent Loss for LP Farming.
 */
contract LiquidityMiningBond is Ownable {
    using SafeMath for uint256;

    // Struct to represent a user's stake
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Mapping of LP token addresses to their corresponding reward rates
    mapping(address => uint256) public rewardRates;

    // LP token address
    address public lpToken;

    // Reward token address
    address public rewardToken;

    // Total stakes
    uint256 public totalStakes;

    // Accrued rewards
    uint256 public accruedRewards;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are accrued
    event RewardsAccrued(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _lpToken LP token address
     * @param _rewardToken Reward token address
     */
    constructor(address _lpToken, address _rewardToken) public {
        lpToken = _lpToken;
        rewardToken = _rewardToken;
    }

    /**
     * @notice Stake LP tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");

        // Transfer LP tokens from user to contract
        IERC20(lpToken).transferFrom(msg.sender, address(this), _amount);

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].rewardDebt = getRewardDebt(msg.sender);

        // Update total stakes
        totalStakes = totalStakes.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake LP tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakes[msg.sender].amount >= _amount, "Insufficient stake");

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(_amount);
        stakes[msg.sender].rewardDebt = getRewardDebt(msg.sender);

        // Transfer LP tokens from contract to user
        IERC20(lpToken).transfer(msg.sender, _amount);

        // Update total stakes
        totalStakes = totalStakes.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Accrue rewards
     */
    function accrueRewards() public {
        // Calculate accrued rewards
        uint256 rewards = calculateRewards();

        // Update accrued rewards
        accruedRewards = accruedRewards.add(rewards);

        emit RewardsAccrued(msg.sender, rewards);
    }

    /**
     * @notice Get reward debt for a user
     * @param _user User address
     * @return Reward debt
     */
    function getRewardDebt(address _user) public view returns (uint256) {
        uint256 userStake = stakes[_user].amount;
        uint256 totalReward = calculateTotalReward();

        return userStake.mul(totalReward).div(totalStakes);
    }

    /**
     * @notice Calculate total reward
     * @return Total reward
     */
    function calculateTotalReward() public view returns (uint256) {
        uint256 totalReward = 0;

        for (address lpTokenAddress in rewardRates) {
            totalReward = totalReward.add(rewardRates[lpTokenAddress].mul(lpToken.balanceOf(address(this))));
        }

        return totalReward;
    }

    /**
     * @notice Calculate accrued rewards
     * @return Accrued rewards
     */
    function calculateRewards() public view returns (uint256) {
        uint256 rewards = 0;

        for (address user in stakes) {
            uint256 userStake = stakes[user].amount;
            uint256 rewardDebt = getRewardDebt(user);

            rewards = rewards.add(userStake.mul(rewardDebt).div(totalStakes));
        }

        return rewards;
    }

    /**
     * @notice Set reward rate for an LP token
     * @param _lpToken LP token address
     * @param _rewardRate Reward rate
     */
    function setRewardRate(address _lpToken, uint256 _rewardRate) public onlyOwner {
        rewardRates[_lpToken] = _rewardRate;
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        uint256 rewards = getRewardDebt(msg.sender);

        // Transfer rewards to user
        IERC20(rewardToken).transfer(msg.sender, rewards);

        // Update user's reward debt
        stakes[msg.sender].rewardDebt = 0;
    }
}
```

Please note that you need to install OpenZeppelin's contracts library to use this code. You can do this by running `npm install @openzeppelin/contracts` or `yarn add @openzeppelin/contracts` in your project directory.

Also, make sure to replace `[Your Name]` in the contract's author field with your actual name.

Before deploying this contract to the mainnet, make sure to thoroughly test it on a testnet. 

The usage of this contract would involve:

1. Deploying the contract with the LP token and reward token addresses.
2. Users staking their LP tokens.
3. Users unstaking their LP tokens.
4. The contract accruing rewards.
5. Users claiming their rewards.

The functions of this contract are:

- `stake(uint256 _amount)`: Stake LP tokens.
- `unstake(uint256 _amount)`: Unstake LP tokens.
- `accrueRewards()`: Accrue rewards.
- `getRewardDebt(address _user)`: Get reward debt for a user.
- `calculateTotalReward()`: Calculate total reward.
- `calculateRewards()`: Calculate accrued rewards.
- `setRewardRate(address _lpToken, uint256 _rewardRate)`: Set reward rate for an LP token.
- `claimRewards()`: Claim rewards. 

The events of this contract are:

- `Staked(address indexed user, uint256 amount)`: Emitted when a user stakes.
- `Unstaked(address indexed user, uint256 amount)`: Emitted when a user unstakes.
- `RewardsAccrued(address indexed user, uint256 amount)`: Emitted when rewards are accrued. 

The modifiers of this contract are:

- `onlyOwner()`: Only the contract owner can call a function with this modifier. 

The require statements ensure that:

- The stake/unstake amount is greater than zero.
- The user has sufficient stake to unstake.

Please adapt the provided code according to your needs. This code serves as a basic template. Consider adding more functionality and error checking depending on your use case. Always do your own research and testing before deploying any smart contract to the mainnet. 

Hope this helps! Let me know if you have any questions.
