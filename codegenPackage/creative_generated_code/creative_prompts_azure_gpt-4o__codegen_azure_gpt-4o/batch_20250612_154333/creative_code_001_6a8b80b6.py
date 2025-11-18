"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-staking.pages.dev
Prompt: Develop a smart contract in Solidity for staking $FLOCK tokens, ensuring it includes functionality for calculating rewards dynamically based on the staking pool percentage and the reward rate of 684.93 $FLOCK tokens per ETH block.
Generated: DETERMINISTIC_6a8b80b61dc490c9
Batch ID: 20250612_154333
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
 * @title FlockTokenStaking
 * @dev A smart contract for staking $FLOCK tokens and dynamically calculating rewards.
 */
contract FlockTokenStaking {
    // State variables
    address public owner;
    IERC20 public flockToken; // Interface to the $FLOCK token contract
    uint256 public rewardRate = 684.93 ether; // Reward rate per ETH block
    uint256 public totalStaked; // Total amount of $FLOCK tokens staked
    uint256 public constant DECIMALS = 10**18;

    struct StakerInfo {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 lastRewardBlock; // Last block when rewards were calculated
        uint256 pendingRewards; // Accumulated rewards pending withdrawal
    }

    mapping(address => StakerInfo) public stakers;

    // Event declarations
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _flockToken Address of the $FLOCK token contract.
     */
    constructor(address _flockToken) {
        require(_flockToken != address(0), "Invalid token address");
        owner = msg.sender;
        flockToken = IERC20(_flockToken);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Stake $FLOCK tokens into the contract to earn rewards.
     * @param _amount Amount of $FLOCK tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        require(
            flockToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        StakerInfo storage staker = stakers[msg.sender];

        // Update pending rewards before changing staked amount
        updateRewards(msg.sender);

        staker.amountStaked += _amount;
        staker.lastRewardBlock = block.number;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $FLOCK tokens from the contract. Also claims pending rewards.
     */
    function unstake() external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens to unstake");

        // Update rewards and reset staked amount
        updateRewards(msg.sender);
        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0;
        staker.lastRewardBlock = block.number;
        totalStaked -= amountToUnstake;

        // Transfer staked tokens and any pending rewards to the user
        require(
            flockToken.transfer(msg.sender, amountToUnstake),
            "Token transfer failed"
        );
        claimRewards();

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Claim pending rewards from staking.
     */
    function claimRewards() public {
        StakerInfo storage staker = stakers[msg.sender];
        updateRewards(msg.sender);

        uint256 rewardsToClaim = staker.pendingRewards;
        require(rewardsToClaim > 0, "No rewards to claim");
        staker.pendingRewards = 0;

        require(
            flockToken.transfer(msg.sender, rewardsToClaim),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Update pending rewards for a specific staker.
     * @param _staker Address of the staker.
     */
    function updateRewards(address _staker) internal {
        StakerInfo storage staker = stakers[_staker];
        if (staker.amountStaked > 0) {
            uint256 blocksElapsed = block.number - staker.lastRewardBlock;
            uint256 rewardPoolShare = (staker.amountStaked * DECIMALS) /
                totalStaked;
            uint256 rewards = (blocksElapsed * rewardRate * rewardPoolShare) /
                DECIMALS;

            staker.pendingRewards += rewards;
            staker.lastRewardBlock = block.number;
        }
    }

    /**
     * @dev Emergency function to withdraw all staked tokens. Owner only.
     */
    function emergencyWithdraw() external onlyOwner {
        require(
            flockToken.transfer(owner, flockToken.balanceOf(address(this))),
            "Emergency withdraw failed"
        );
        totalStaked = 0;
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
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
