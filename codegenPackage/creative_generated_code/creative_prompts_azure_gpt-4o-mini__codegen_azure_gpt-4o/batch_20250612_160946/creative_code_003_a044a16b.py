"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertrumpcoin-io.pages.dev
Prompt: Develop a Solidity contract that allows users to stake Super Trump Coin and earn rewards based on the tokenomics outlined on the website.
Generated: DETERMINISTIC_a044a16bc3057823
Batch ID: 20250612_160946
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
 * @dev A contract that allows users to stake Super Trump Coin (STC) and earn rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {

    // Address of the Super Trump Coin (STC) token contract
    IERC20 public immutable stcToken;

    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;      // Amount of STC tokens staked
        uint256 rewardDebt;  // Rewards already withdrawn
        uint256 lastUpdated; // Timestamp of the last stake/reward update
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Reward rate per second (set according to tokenomics)
    uint256 public immutable rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token contract and reward rate.
     * @param _stcToken Address of the STC token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stcToken, uint256 _rewardRate) {
        require(address(_stcToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stcToken = _stcToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake STC tokens.
     * @param _amount Amount of STC tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update user's rewards before modifying their stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(stcToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake their STC tokens.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Update user's rewards before modifying their stake
        _updateRewards(msg.sender);

        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;

        // Transfer tokens back to the user
        require(stcToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Allows a user to claim their rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = userStake.rewardDebt;
        require(pendingRewards > 0, "No rewards available");

        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        require(stcToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to calculate and update pending rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;

        if (timeElapsed > 0 && userStake.amount > 0) {
            uint256 rewards = (userStake.amount * rewardRate * timeElapsed) / 1e18; // Assuming rewardRate is scaled
            userStake.rewardDebt += rewards;
        }

        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Returns the pending rewards for a user (view function).
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;

        if (timeElapsed > 0 && userStake.amount > 0) {
            uint256 rewards = (userStake.amount * rewardRate * timeElapsed) / 1e18;
            return userStake.rewardDebt + rewards;
        }

        return userStake.rewardDebt;
    }
}
```
