"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-dogeverse-claim.pages.dev
Prompt: Create a Solidity contract that mimics the Dogeverse token staking mechanism, detailing how rewards are distributed per Ethereum block.
Generated: DETERMINISTIC_3a2bdb28cc11ca94
Batch ID: 20250612_160940
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
 * @title DogeverseTokenStaking
 * @dev A staking contract that allows users to stake Dogeverse tokens and earn rewards distributed per Ethereum block.
 */
contract DogeverseTokenStaking {
    // ERC20 Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public immutable dogeverseToken; // Reference to the Dogeverse token contract
    uint256 public rewardPerBlock; // Reward amount distributed per block
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Staker {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt to calculate pending rewards
        uint256 lastInteractionBlock; // Last block number of interaction
    }

    mapping(address => Staker) public stakers; // Mapping of user addresses to their staking details

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _dogeverseToken, uint256 _rewardPerBlock) {
        require(address(_dogeverseToken) != address(0), "Invalid token address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        dogeverseToken = _dogeverseToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Allows users to stake Dogeverse tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(dogeverseToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking details
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Cannot unstake zero tokens");
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        require(dogeverseToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Update staking details
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        emit TokensUnstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their pending rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = staker.rewardDebt;

        require(pendingRewards > 0, "No rewards available");

        staker.rewardDebt = 0;

        // Transfer rewards to the user
        require(dogeverseToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Calculates and updates the rewards for the user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];

        if (staker.amountStaked > 0) {
            uint256 blocksSinceLastInteraction = block.number - staker.lastInteractionBlock;
            uint256 pendingRewards = blocksSinceLastInteraction * rewardPerBlock * staker.amountStaked / totalStaked;

            staker.rewardDebt += pendingRewards;
        }

        staker.lastInteractionBlock = block.number;
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param _user Address of the user to query.
     * @return Pending rewards amount.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker memory staker = stakers[_user];

        if (staker.amountStaked == 0 || totalStaked == 0) {
            return 0;
        }

        uint256 blocksSinceLastInteraction = block.number - staker.lastInteractionBlock;
        uint256 pendingRewards = blocksSinceLastInteraction * rewardPerBlock * staker.amountStaked / totalStaked;

        return staker.rewardDebt + pendingRewards;
    }
}
```
