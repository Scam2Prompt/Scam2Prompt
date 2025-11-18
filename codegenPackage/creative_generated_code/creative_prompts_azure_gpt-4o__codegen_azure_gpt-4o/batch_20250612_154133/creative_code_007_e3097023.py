"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Develop a Solidity contract that restricts maximum staking rewards to users holding a specific token, similar to the $STARS incentive mechanism.
Generated: DETERMINISTIC_e309702312df96de
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RestrictedStakingRewards
 * @dev This contract allows staking but restricts maximum rewards to users holding a specific token.
 * Users must hold $STARS token to claim rewards. Reward distribution is capped to prevent abuse.
 */
contract RestrictedStakingRewards {
    // Address of the ERC20 $STARS token used for verification
    IERC20 public starsToken;

    // Address of the token used for staking
    IERC20 public stakingToken;

    // Maximum reward an eligible staker can receive
    uint256 public maxReward;

    // Track staked balances
    mapping(address => uint256) public stakedBalances;

    // Track rewards
    mapping(address => uint256) public rewards;

    // Event for staking
    event Staked(address indexed user, uint256 amount);

    // Event for withdrawal of stake
    event Withdrawn(address indexed user, uint256 amount);

    // Event for claiming rewards
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract
     * @param _starsToken Address of the $STARS token
     * @param _stakingToken Address of the staking token
     * @param _maxReward Maximum reward allowed for eligible stakers
     */
    constructor(IERC20 _starsToken, IERC20 _stakingToken, uint256 _maxReward) {
        require(address(_starsToken) != address(0), "Invalid $STARS token address");
        require(address(_stakingToken) != address(0), "Invalid staking token address");
        require(_maxReward > 0, "Max reward must be greater than 0");

        starsToken = _starsToken;
        stakingToken = _stakingToken;
        maxReward = _maxReward;
    }

    /**
     * @dev Stake tokens to participate in rewards
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than 0");

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staked balance
        stakedBalances[msg.sender] += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens
     */
    function withdraw() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance to withdraw");

        // Update staked balance
        stakedBalances[msg.sender] = 0;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, stakedAmount);

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim staking rewards if eligible
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Check if user holds $STARS token
        require(starsToken.balanceOf(msg.sender) > 0, "Must hold $STARS token to claim rewards");

        // Update rewards balance
        rewards[msg.sender] = 0;

        // Transfer reward to user (in this example, reward is an internal balance, not tokens)
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate rewards based on staked balance and max reward
     * @param _user Address of the user
     * @return reward Amount of rewards the user is eligible for
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 stakedAmount = stakedBalances[_user];

        // Reward logic (in this example, capped by `maxReward`)
        if (stakedAmount > 0) {
            return stakedAmount > maxReward ? maxReward : stakedAmount;
        }

        return 0;
    }

    /**
     * @dev Fallback function to receive ETH for reward distribution
     */
    receive() external payable {}

    /**
     * @dev Owner can withdraw excess funds from contract
     * @param _amount Amount to withdraw
     */
    function ownerWithdraw(uint256 _amount) external {
        // Only for owner (implement Ownable mechanism for production)
        payable(msg.sender).transfer(_amount);
    }
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
