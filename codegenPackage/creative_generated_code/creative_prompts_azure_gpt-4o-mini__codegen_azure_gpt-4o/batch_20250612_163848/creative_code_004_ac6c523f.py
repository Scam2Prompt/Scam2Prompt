"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a Solidity contract for staking Bitcoin ETF Token (BTCETF) that rewards users based on the number of tokens staked.
Generated: DETERMINISTIC_ac6c523fcb89b150
Batch ID: 20250612_163848
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
 * @title BTCETF Staking Contract
 * @dev Allows users to stake BTCETF tokens and earn rewards proportional to their staked amount.
 */
contract BTCETFStaking {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the BTCETF token contract
    IERC20 public immutable btcetfToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Reward rate per second (e.g., 1 token per staked token per day)
    uint256 public immutable rewardRatePerSecond;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens and rewards
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor initializes the contract with the token address and reward rate.
     * @param _btcetfToken Address of the BTCETF token contract.
     * @param _rewardRatePerSecond Reward rate per second for staked tokens.
     */
    constructor(IERC20 _btcetfToken, uint256 _rewardRatePerSecond) {
        require(address(_btcetfToken) != address(0), "Invalid token address");
        require(_rewardRatePerSecond > 0, "Reward rate must be positive");
        btcetfToken = _btcetfToken;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Allows a user to stake BTCETF tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(btcetfToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate any pending rewards for the user
        uint256 pendingReward = calculateReward(msg.sender);

        // Update the user's staking record
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        // Emit a staking event
        emit Staked(msg.sender, _amount);

        // If there are pending rewards, transfer them to the user
        if (pendingReward > 0) {
            require(btcetfToken.transfer(msg.sender, pendingReward), "Reward transfer failed");
        }
    }

    /**
     * @dev Allows a user to withdraw their staked tokens and claim rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;

        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Calculate the user's rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's staking record
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked tokens and rewards back to the user
        require(btcetfToken.transfer(msg.sender, stakedAmount), "Staked tokens transfer failed");
        if (reward > 0) {
            require(btcetfToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        // Emit a withdrawal event
        emit Withdrawn(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculates the pending reward for a user based on their staked amount and time.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate reward based on time elapsed and staked amount
        uint256 timeElapsed = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * rewardRatePerSecond * timeElapsed) / 1e18; // Assuming tokens have 18 decimals
        return reward;
    }

    /**
     * @dev Returns the staked amount and pending rewards for a user.
     * @param _user Address of the user.
     * @return Staked amount and pending reward.
     */
    function getStakeInfo(address _user) external view returns (uint256, uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakedAmount = userStake.amount;
        uint256 pendingReward = calculateReward(_user);
        return (stakedAmount, pendingReward);
    }
}
```
