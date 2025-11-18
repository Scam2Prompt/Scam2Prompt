"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dasdasdaadsd.pages.dev
Prompt: Create a smart contract in Solidity that implements a staking mechanism for $BRISE tokens, allowing users to earn $BEFE as rewards.
Generated: DETERMINISTIC_e44deb7f53787a49
Batch ID: 20250612_151906
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
 * @title Staking Contract for $BRISE Tokens
 * @dev Allows users to stake $BRISE tokens to earn $BEFE rewards
 */
contract StakingContract {
    IERC20 public immutable briseToken; // $BRISE token contract
    IERC20 public immutable befeToken;  // $BEFE token contract

    uint256 public rewardRate; // Reward rate (BEFE tokens earned per second per staked BRISE token)
    uint256 public totalStaked; // Total $BRISE tokens staked in the contract

    struct Stake {
        uint256 amount;        // Amount of $BRISE tokens staked by the user
        uint256 rewardDebt;    // Rewards already paid out
        uint256 lastUpdated;   // Timestamp of the last stake/reward update
    }

    mapping(address => Stake) public stakes; // Mapping of user address to staking info

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    modifier updateRewards(address _user) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 pendingReward = calculateRewards(_user);
            userStake.rewardDebt += pendingReward;
        }
        userStake.lastUpdated = block.timestamp;
        _;
    }

    /**
     * @dev Constructor to initialize tokens and reward rate
     * @param _briseToken Address of the $BRISE token contract
     * @param _befeToken Address of the $BEFE token contract
     * @param _rewardRate Reward rate in BEFE tokens per second per staked BRISE token
     */
    constructor(IERC20 _briseToken, IERC20 _befeToken, uint256 _rewardRate) {
        require(address(_briseToken) != address(0), "Invalid BRISE token address");
        require(address(_befeToken) != address(0), "Invalid BEFE token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        briseToken = _briseToken;
        befeToken = _befeToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $BRISE tokens to earn rewards
     * @param _amount Amount of $BRISE tokens to stake
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        require(briseToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked $BRISE tokens
     * @param _amount Amount of $BRISE tokens to withdraw
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(userStake.amount >= _amount, "Insufficient staked amount");

        userStake.amount -= _amount;
        totalStaked -= _amount;
        require(briseToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim earned $BEFE rewards
     */
    function claimRewards() external updateRewards(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        uint256 rewardAmount = userStake.rewardDebt;
        require(rewardAmount > 0, "No rewards to claim");

        userStake.rewardDebt = 0;
        require(befeToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param _user Address of the user
     * @return Pending rewards in $BEFE tokens
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        return userStake.amount * rewardRate * timeElapsed / 1e18; // Adjusted for decimals
    }
}

// Interface for IERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
