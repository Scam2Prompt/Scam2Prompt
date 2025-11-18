"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Develop a Solidity smart contract that automates the distribution of BTCMTX staking rewards based on the amount of tokens staked and the duration of staking.
Generated: DETERMINISTIC_f782d94cf5181f1c
Batch ID: 20250612_153420
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
 * @title BTCMTX Staking Rewards Smart Contract
 * @dev A contract for automating the distribution of BTCMTX staking rewards based on
 * the amount staked and the duration of staking.
 */
contract BTCMTXStakingRewards {
    // Address of the BTCMTX token contract
    IERC20 public btcmtxToken;

    // Reward rate per second (defined as tokens per second per staked token)
    uint256 public rewardRate;

    // Mapping of staker's address to their staking data
    mapping(address => StakingInfo) public stakingData;

    // Total amount of BTCMTX tokens staked in the contract
    uint256 public totalStaked;

    struct StakingInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt used for reward calculation
        uint256 lastUpdated; // Last time the staker's info was updated
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to ensure staking amount is greater than zero
    modifier nonZeroAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }

    constructor(IERC20 _btcmtxToken, uint256 _rewardRate) {
        btcmtxToken = _btcmtxToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake BTCMTX tokens in the contract.
     * @param _amount Amount of BTCMTX tokens to stake.
     */
    function stake(uint256 _amount) external nonZeroAmount(_amount) {
        StakingInfo storage userInfo = stakingData[msg.sender];

        // Update the user's rewards before modifying their stake
        _updateRewards(msg.sender);

        // Transfer BTCMTX tokens from the user to the contract
        require(
            btcmtxToken.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );

        // Update user's staking info and total staked
        userInfo.amount += _amount;
        userInfo.lastUpdated = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     * @param _amount Amount of BTCMTX tokens to withdraw.
     */
    function withdraw(uint256 _amount) external nonZeroAmount(_amount) {
        StakingInfo storage userInfo = stakingData[msg.sender];
        require(userInfo.amount >= _amount, "Insufficient staked balance");

        // Update the user's rewards before modifying their stake
        _updateRewards(msg.sender);

        // Transfer BTCMTX tokens back to the user
        require(btcmtxToken.transfer(msg.sender, _amount), "Transfer failed");

        // Update user's staking info and total staked
        userInfo.amount -= _amount;
        if (userInfo.amount == 0) {
            userInfo.lastUpdated = 0; // Reset lastUpdated if no tokens are staked
        }
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to claim their accumulated staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        StakingInfo storage userInfo = stakingData[msg.sender];
        uint256 pendingRewards = userInfo.rewardDebt;

        require(pendingRewards > 0, "No rewards available");

        // Reset reward debt after claiming
        userInfo.rewardDebt = 0;

        // Transfer reward tokens to the user
        require(
            btcmtxToken.transfer(msg.sender, pendingRewards),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) internal {
        StakingInfo storage userInfo = stakingData[_user];

        if (userInfo.amount == 0 || userInfo.lastUpdated == 0) {
            return;
        }

        // Calculate the rewards since the user's last update
        uint256 timeElapsed = block.timestamp - userInfo.lastUpdated;
        uint256 pendingRewards = (userInfo.amount * rewardRate * timeElapsed);

        userInfo.rewardDebt += pendingRewards;
        userInfo.lastUpdated = block.timestamp;
    }

    /**
     * @dev Allows the owner to set a new reward rate.
     * @param _newRewardRate The new reward rate (tokens per second per staked token).
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Restricts access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    /**
     * @dev Gets the contract owner (used for `onlyOwner` modifier).
     * @return The contract owner's address.
     */
    function owner() public view returns (address) {
        return address(this); // Example logic for owner; modify as necessary
    }
}

/**
 * @dev Interface for ERC20 functions used by the contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
