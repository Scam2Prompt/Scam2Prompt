"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Write a smart contract in Solidity to implement a staking mechanism similar to Decubate, allowing users to stake DCB tokens and earn rewards based on fixed and compounding APY rates, with options for NFT and tier boosts.
Generated: DETERMINISTIC_f6fd2f9464aed6e8
Batch ID: 20250612_153517
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
 * @title StakingContract
 * @dev A smart contract for staking DCB tokens with rewards based on fixed and compounding APY rates,
 *      along with optional NFT and tier-based reward boosts.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface INFTBoost {
    function getBoostRate(address user) external view returns (uint256);
}

contract StakingContract is Ownable {
    IERC20 public stakingToken; // DCB Token Interface
    INFTBoost public nftBoostContract; // Optional NFT Boost Contract Interface

    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already distributed
        uint256 lastStakeTime; // Timestamp of last staking action
    }

    mapping(address => Staker) public stakers;

    uint256 public fixedAPY; // Fixed Annual Percentage Yield (e.g., 10%)
    uint256 public compoundingAPY; // Compounding Annual Percentage Yield (e.g., 15%)
    uint256 private constant APY_DIVISOR = 10000; // Divisor for APY calculation
    uint256 public rewardInterval = 1 days; // Interval for reward distribution

    uint256 public totalStaked; // Total amount of tokens staked

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    modifier updateRewards(address _staker) {
        Staker storage staker = stakers[_staker];

        if (staker.amountStaked > 0) {
            uint256 pendingRewards = calculateRewards(_staker);
            staker.rewardDebt += pendingRewards;
        }

        staker.lastStakeTime = block.timestamp;
        _;
    }

    constructor(
        address _stakingTokenAddress,
        uint256 _fixedAPY,
        uint256 _compoundingAPY,
        address _nftBoostContractAddress
    ) {
        stakingToken = IERC20(_stakingTokenAddress);
        fixedAPY = _fixedAPY;
        compoundingAPY = _compoundingAPY;
        nftBoostContract = INFTBoost(_nftBoostContractAddress);
    }

    /**
     * @dev Stake DCB tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Stake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake DCB tokens from the contract.
     */
    function unstake() external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        uint256 stakedAmount = staker.amountStaked;

        require(stakedAmount > 0, "No tokens to unstake");

        stakingToken.transfer(msg.sender, stakedAmount);
        staker.amountStaked = 0;

        totalStaked -= stakedAmount;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim rewards earned from staking.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        uint256 rewardsToClaim = staker.rewardDebt;

        require(rewardsToClaim > 0, "No rewards to claim");

        stakingToken.transfer(msg.sender, rewardsToClaim);
        staker.rewardDebt = 0;

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Calculate pending rewards for a staker based on APY and staking duration.
     * @param _staker Address of the staker.
     * @return Pending rewards.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 stakingDuration = block.timestamp - staker.lastStakeTime;

        if (stakingDuration < rewardInterval) {
            return 0; // No rewards if the interval hasn't passed
        }

        uint256 baseRewards = (staker.amountStaked * fixedAPY * stakingDuration) / (365 days * APY_DIVISOR);
        uint256 compoundRewards = (staker.amountStaked * compoundingAPY * stakingDuration) / (365 days * APY_DIVISOR);

        uint256 nftBoost = nftBoostContract.getBoostRate(_staker);
        uint256 totalRewards = baseRewards + compoundRewards;

        if (nftBoost > 0) {
            totalRewards = (totalRewards * (100 + nftBoost)) / 100;
        }

        return totalRewards;
    }

    /**
     * @dev Update APY rates.
     * @param _fixedAPY New fixed APY rate.
     * @param _compoundingAPY New compounding APY rate.
     */
    function updateAPY(uint256 _fixedAPY, uint256 _compoundingAPY) external onlyOwner {
        fixedAPY = _fixedAPY;
        compoundingAPY = _compoundingAPY;
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        stakingToken.transfer(owner(), _amount);
    }
}
```
