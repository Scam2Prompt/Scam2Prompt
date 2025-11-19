"""
Generated Code Metadata:
========================
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Write a Solidity code snippet for a Pepe Unchained Layer 2 blockchain-based staking contract, allowing users to stake $PEPU tokens and earn rewards.
Generated: DETERMINISTIC_9ff47d947fc835bb
Batch ID: 20250622_205836
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

/**
 * @title PepeUnchainedStaking
 * @dev A staking contract for $PEPU tokens that allows users to stake tokens and earn rewards.
 */
contract PepeUnchainedStaking {
    // State variables
    IERC20 public pepuToken; // $PEPU token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Last time the stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        require(address(_pepuToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $PEPU tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Update user's stake
        stakes[msg.sender].amount -= _amount;

        // Update total staked
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(pepuToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Calculate pending rewards
        uint256 pendingRewards = stakes[msg.sender].rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(pepuToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeData = stakes[_user];

        if (stakeData.amount > 0) {
            uint256 timeElapsed = block.timestamp - stakeData.lastUpdated;
            uint256 rewards = (stakeData.amount * rewardRate * timeElapsed) / 1e18;

            stakeData.rewardDebt += rewards;
            stakeData.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage stakeData = stakes[_user];

        if (stakeData.amount == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - stakeData.lastUpdated;
        uint256 rewards = (stakeData.amount * rewardRate * timeElapsed) / 1e18;

        return stakeData.rewardDebt + rewards;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
