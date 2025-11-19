"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Write a Solidity contract that manages the staking rewards for BTCBSC holders, ensuring daily payouts in line with the Bitcoin block schedule.
Generated: DETERMINISTIC_458e54d2b97e260b
Batch ID: 20250612_163305
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
 * @title StakingRewards
 * @dev A smart contract to manage staking rewards for BTCBSC holders, with daily payouts
 *      aligned to the Bitcoin block schedule (~10-minute intervals).
 */
contract StakingRewards {

    // Address of the token (BTCBSC) being staked
    IERC20 public btcBscToken;

    // Reward rate per block (aligned to ~10 minutes, assuming 144 blocks per day)
    uint256 public rewardRatePerBlock;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Mapping to track last claimed block for rewards
    mapping(address => uint256) public lastClaimedBlock;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the token address and reward rate per block.
     * @param _btcBscToken Address of the BTCBSC token.
     * @param _rewardRatePerBlock Reward rate per block in tokens.
     */
    constructor(IERC20 _btcBscToken, uint256 _rewardRatePerBlock) {
        btcBscToken = _btcBscToken;
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @dev Stake BTCBSC tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer BTCBSC tokens from user to contract
        require(btcBscToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user stake and total staked amount
        userStakes[msg.sender] += _amount;
        totalStaked += _amount;

        // Update last claimed block for user
        lastClaimedBlock[msg.sender] = block.number;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked BTCBSC tokens and claim rewards.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than 0");
        require(userStakes[msg.sender] >= _amount, "Insufficient staked balance");

        // Claim rewards before withdrawal
        claimRewards();

        // Update user stake and total staked amount
        userStakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer BTCBSC tokens back to user
        require(btcBscToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() public {
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        // Update last claimed block for user
        lastClaimedBlock[msg.sender] = block.number;

        // Update user rewards
        userRewards[msg.sender] = 0;

        // Transfer rewards to user
        require(btcBscToken.transfer(msg.sender, pendingRewards), "Token transfer failed");

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakedAmount = userStakes[_user];
        uint256 blocksElapsed = block.number - lastClaimedBlock[_user];

        // Calculate rewards based on staked amount, blocks elapsed, and reward rate
        return (stakedAmount * blocksElapsed * rewardRatePerBlock) / 1e18;
    }

    /**
     * @dev Get the current staking balance of a user.
     * @param _user Address of the user.
     * @return Staking balance of the user.
     */
    function getStakingBalance(address _user) external view returns (uint256) {
        return userStakes[_user];
    }

    /**
     * @dev Get the total rewards accrued by a user.
     * @param _user Address of the user.
     * @return Total rewards accrued.
     */
    function getPendingRewards(address _user) external view returns (uint256) {
        return calculateRewards(_user);
    }
}

/**
 * @dev Interface for ERC20 token functions used in the contract.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
