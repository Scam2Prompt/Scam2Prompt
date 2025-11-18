"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakelayerai.pages.dev
Prompt: Create a smart contract in Solidity for staking $LAI tokens and distributing AI Capsule rewards, ensuring compatibility with ERC-20 and BEP-20 standards as described in the LayerAI documentation.
Generated: DETERMINISTIC_f7957518bac50d34
Batch ID: 20250612_152739
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

// Importing the IERC20 interface for ERC-20/BEP-20 compatibility
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LAIStaking is Ownable {
    // Token interface for $LAI
    IERC20 public laiToken;

    // Struct to store staker information
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimTimestamp;
        uint256 pendingRewards;
    }

    // Mapping to track staker information
    mapping(address => Staker) public stakers;

    // Reward rate per second (settable by owner)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    // Constructor to initialize the $LAI token address
    constructor(address _laiToken, uint256 _rewardRate) {
        laiToken = IERC20(_laiToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $LAI tokens into the contract.
     * @param _amount Amount of $LAI to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        require(
            laiToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $LAI tokens and claim pending rewards.
     * @param _amount Amount of $LAI to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Cannot unstake zero tokens");
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        _updateRewards(msg.sender);

        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        require(laiToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim AI Capsule rewards without unstaking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 rewards = staker.pendingRewards;
        require(rewards > 0, "No rewards to claim");

        staker.pendingRewards = 0;

        // Logic for distributing rewards
        // For demonstration, rewards are directly transferred as $LAI tokens.
        require(laiToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update the reward rate (owner-only).
     * @param _newRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Internal function to update pending rewards for a staker.
     * @param _staker Address of the staker.
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        if (staker.amountStaked > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastClaimTimestamp;
            uint256 newRewards = (staker.amountStaked * rewardRate * timeElapsed) /
                1 ether; // Assuming staking amounts are in wei

            staker.pendingRewards += newRewards;
        }
        staker.lastClaimTimestamp = block.timestamp;
    }

    /**
     * @dev Retrieve staker information.
     * @param _staker Address of the staker.
     */
    function getStakerInfo(
        address _staker
    )
        external
        view
        returns (
            uint256 amountStaked,
            uint256 pendingRewards,
            uint256 lastClaimTimestamp
        )
    {
        Staker memory staker = stakers[_staker];
        return (
            staker.amountStaked,
            staker.pendingRewards,
            staker.lastClaimTimestamp
        );
    }
}
```
