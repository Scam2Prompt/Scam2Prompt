"""
Generated Code Metadata:
========================
Original URL: https://pablo-defis.web.app
Prompt: Create a Solidity smart contract that implements the staking protocol described in the Pablo ecosystem, ensuring revenue sharing in both $PABLO tokens and USDT.
Generated: DETERMINISTIC_811667d2a87196b4
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PabloStakingContract
 * @author [Your Name]
 * @notice This contract implements the staking protocol for the Pablo ecosystem.
 *         It allows users to stake their $PABLO tokens and USDT, and earns rewards
 *         in both $PABLO tokens and USDT.
 */
contract PabloStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token addresses
    address public pabloTokenAddress;
    address public usdtTokenAddress;

    // Staking pools
    mapping(address => StakingPool) public stakingPools;

    // Reward rates
    uint256 public pabloRewardRate;
    uint256 public usdtRewardRate;

    // Reward distribution intervals
    uint256 public rewardDistributionInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardDistributionTimestamp;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 pabloRewards, uint256 usdtRewards);

    /**
     * @param _pabloTokenAddress Address of the $PABLO token
     * @param _usdtTokenAddress Address of the USDT token
     * @param _pabloRewardRate Reward rate for $PABLO tokens
     * @param _usdtRewardRate Reward rate for USDT
     * @param _rewardDistributionInterval Reward distribution interval in seconds
     */
    constructor(
        address _pabloTokenAddress,
        address _usdtTokenAddress,
        uint256 _pabloRewardRate,
        uint256 _usdtRewardRate,
        uint256 _rewardDistributionInterval
    ) public {
        require(_pabloTokenAddress != address(0), "PABLO token address cannot be zero");
        require(_usdtTokenAddress != address(0), "USDT token address cannot be zero");
        require(_pabloRewardRate > 0, "PABLO reward rate must be greater than zero");
        require(_usdtRewardRate > 0, "USDT reward rate must be greater than zero");
        require(_rewardDistributionInterval > 0, "Reward distribution interval must be greater than zero");

        pabloTokenAddress = _pabloTokenAddress;
        usdtTokenAddress = _usdtTokenAddress;
        pabloRewardRate = _pabloRewardRate;
        usdtRewardRate = _usdtRewardRate;
        rewardDistributionInterval = _rewardDistributionInterval;

        lastRewardDistributionTimestamp = block.timestamp;
    }

    /**
     * @dev Stakes $PABLO tokens and USDT
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from user to contract
        IERC20(pabloTokenAddress).safeTransferFrom(msg.sender, address(this), _amount);

        // Update staking pool
        if (stakingPools[msg.sender].pabloStaked == 0) {
            stakingPools[msg.sender] = StakingPool(0, 0, 0);
        }
        stakingPools[msg.sender].pabloStaked = stakingPools[msg.sender].pabloStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes $PABLO tokens and USDT
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(stakingPools[msg.sender].pabloStaked >= _amount, "Insufficient staked tokens");

        // Update staking pool
        stakingPools[msg.sender].pabloStaked = stakingPools[msg.sender].pabloStaked.sub(_amount);

        // Transfer tokens from contract to user
        IERC20(pabloTokenAddress).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distributes rewards to stakers
     */
    function distributeRewards() public {
        require(block.timestamp.sub(lastRewardDistributionTimestamp) >= rewardDistributionInterval, "Reward distribution interval has not passed");

        // Calculate rewards
        uint256 pabloRewards = calculateRewards(pabloTokenAddress, pabloRewardRate);
        uint256 usdtRewards = calculateRewards(usdtTokenAddress, usdtRewardRate);

        // Update last reward distribution timestamp
        lastRewardDistributionTimestamp = block.timestamp;

        // Distribute rewards to stakers
        for (address user in stakingPools) {
            if (stakingPools[user].pabloStaked > 0) {
                uint256 userPabloRewards = pabloRewards.mul(stakingPools[user].pabloStaked).div(getTotalStaked(pabloTokenAddress));
                uint256 userUsdtRewards = usdtRewards.mul(stakingPools[user].usdtStaked).div(getTotalStaked(usdtTokenAddress));

                // Transfer rewards to user
                IERC20(pabloTokenAddress).safeTransfer(user, userPabloRewards);
                IERC20(usdtTokenAddress).safeTransfer(user, userUsdtRewards);

                emit RewardsDistributed(user, userPabloRewards, userUsdtRewards);
            }
        }
    }

    /**
     * @dev Calculates rewards for a given token
     * @param _tokenAddress Address of the token
     * @param _rewardRate Reward rate for the token
     * @return Rewards for the token
     */
    function calculateRewards(address _tokenAddress, uint256 _rewardRate) internal view returns (uint256) {
        // Calculate rewards based on the reward rate and total staked tokens
        uint256 totalStaked = getTotalStaked(_tokenAddress);
        return totalStaked.mul(_rewardRate).div(10000);
    }

    /**
     * @dev Gets the total staked tokens for a given token
     * @param _tokenAddress Address of the token
     * @return Total staked tokens
     */
    function getTotalStaked(address _tokenAddress) internal view returns (uint256) {
        uint256 totalStaked = 0;
        for (address user in stakingPools) {
            if (_tokenAddress == pabloTokenAddress) {
                totalStaked = totalStaked.add(stakingPools[user].pabloStaked);
            } else if (_tokenAddress == usdtTokenAddress) {
                totalStaked = totalStaked.add(stakingPools[user].usdtStaked);
            }
        }
        return totalStaked;
    }

    struct StakingPool {
        uint256 pabloStaked;
        uint256 usdtStaked;
        uint256 rewardsEarned;
    }
}
```
