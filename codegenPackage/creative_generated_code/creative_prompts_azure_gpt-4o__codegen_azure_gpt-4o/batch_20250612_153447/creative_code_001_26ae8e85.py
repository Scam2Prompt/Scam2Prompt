"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeu.pages.dev
Prompt: Generate Solidity code for a smart contract that facilitates double staking rewards for $PEPU tokens on Pepe Unchained.
Generated: DETERMINISTIC_26ae8e8553ed9edb
Batch ID: 20250612_153447
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
 * @title DoubleStakingRewards
 * @dev Smart contract that facilitates double staking rewards for $PEPU tokens.
 */
contract DoubleStakingRewards {
    // Address of the $PEPU token contract
    IERC20 public pepuToken;

    // Total rewards pool
    uint256 public rewardPool;

    // Struct to store staking information
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakedTime;
        uint256 rewardsEarned;
    }

    // Mapping to track staker information by address
    mapping(address => Staker) public stakers;

    // Reward rate in tokens per second (double rewards applied)
    uint256 public rewardRate;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _pepuToken Address of the $PEPU token contract.
     * @param _rewardRate Reward rate in tokens per second.
     */
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        pepuToken = _pepuToken;
        rewardRate = _rewardRate * 2; // Double reward rate
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake $PEPU tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the staker to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);
        staker.amountStaked += _amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their $PEPU tokens.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0;

        // Transfer tokens from the contract back to the staker
        require(pepuToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);
        uint256 rewardsToClaim = staker.rewardsEarned;

        require(rewardsToClaim > 0, "No rewards to claim");
        require(rewardPool >= rewardsToClaim, "Insufficient reward pool");

        // Reduce rewards pool and reset staker rewards
        rewardPool -= rewardsToClaim;
        staker.rewardsEarned = 0;

        // Transfer rewards to the staker
        require(pepuToken.transfer(msg.sender, rewardsToClaim), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Updates the rewards for a specific staker.
     * @param _staker Address of the staker.
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        if (staker.amountStaked > 0) {
            uint256 timeStaked = block.timestamp - staker.lastStakedTime;
            uint256 newRewards = timeStaked * rewardRate * staker.amountStaked / (10 ** 18);
            staker.rewardsEarned += newRewards;
            staker.lastStakedTime = block.timestamp;
        }
    }

    /**
     * @dev Allows the owner to add rewards to the reward pool.
     * @param _amount Amount of $PEPU tokens to add to the reward pool.
     */
    function addRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Cannot add zero rewards");

        // Transfer tokens to the contract for the rewards pool
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        rewardPool += _amount;
    }

    /**
     * @dev Allows the owner to withdraw remaining rewards from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawRewards(uint256 _amount) external onlyOwner {
        require(_amount <= rewardPool, "Insufficient reward pool");

        // Transfer tokens from the contract back to the owner
        require(pepuToken.transfer(owner, _amount), "Token transfer failed");

        rewardPool -= _amount;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
