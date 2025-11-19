"""
Generated Code Metadata:
========================
Original URL: https://synthr.pages.dev
Prompt: "Design a staking mechanism for SYNTHR's veSYNTH token, including the distribution of syUSD and SYNTH rewards, and write a Solidity code snippet for it."
Generated: DETERMINISTIC_c3608b587364090d
Batch ID: 20250622_210027
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
 * @title Staking Contract for veSYNTH Token
 * @dev This contract allows users to stake veSYNTH tokens and earn rewards in syUSD and SYNTH tokens.
 */
contract veSYNTHStaking {
    // State variables
    IERC20 public veSYNTH; // veSYNTH token contract
    IERC20 public syUSD;   // syUSD token contract
    IERC20 public SYNTH;   // SYNTH token contract

    uint256 public totalStaked; // Total amount of veSYNTH staked
    uint256 public rewardRateSyUSD; // Reward rate for syUSD (per second)
    uint256 public rewardRateSYNTH; // Reward rate for SYNTH (per second)

    struct StakeInfo {
        uint256 amount; // Amount of veSYNTH staked
        uint256 lastUpdated; // Last time rewards were calculated
        uint256 pendingSyUSDRewards; // Pending syUSD rewards
        uint256 pendingSYNTHRewards; // Pending SYNTH rewards
    }

    mapping(address => StakeInfo) public stakes; // Mapping of user address to their stake info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 syUSDRewards, uint256 SYNTHRewards);

    // Constructor
    constructor(
        address _veSYNTH,
        address _syUSD,
        address _SYNTH,
        uint256 _rewardRateSyUSD,
        uint256 _rewardRateSYNTH
    ) {
        veSYNTH = IERC20(_veSYNTH);
        syUSD = IERC20(_syUSD);
        SYNTH = IERC20(_SYNTH);
        rewardRateSyUSD = _rewardRateSyUSD;
        rewardRateSYNTH = _rewardRateSYNTH;
    }

    /**
     * @dev Stake veSYNTH tokens to earn rewards.
     * @param _amount Amount of veSYNTH tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer veSYNTH tokens from the user to the contract
        require(veSYNTH.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking info
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake veSYNTH tokens and claim rewards.
     * @param _amount Amount of veSYNTH tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer veSYNTH tokens back to the user
        require(veSYNTH.transfer(msg.sender, _amount), "Token transfer failed");

        // Update staking info
        stakes[msg.sender].amount -= _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards (syUSD and SYNTH tokens).
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Get pending rewards
        uint256 syUSDRewards = stakes[msg.sender].pendingSyUSDRewards;
        uint256 SYNTHRewards = stakes[msg.sender].pendingSYNTHRewards;

        require(syUSDRewards > 0 || SYNTHRewards > 0, "No rewards to claim");

        // Reset pending rewards
        stakes[msg.sender].pendingSyUSDRewards = 0;
        stakes[msg.sender].pendingSYNTHRewards = 0;

        // Transfer rewards to the user
        if (syUSDRewards > 0) {
            require(syUSD.transfer(msg.sender, syUSDRewards), "syUSD transfer failed");
        }
        if (SYNTHRewards > 0) {
            require(SYNTH.transfer(msg.sender, SYNTHRewards), "SYNTH transfer failed");
        }

        emit RewardsClaimed(msg.sender, syUSDRewards, SYNTHRewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        StakeInfo storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp - stake.lastUpdated;

            // Calculate rewards
            stake.pendingSyUSDRewards += (stake.amount * rewardRateSyUSD * timeElapsed) / 1e18;
            stake.pendingSYNTHRewards += (stake.amount * rewardRateSYNTH * timeElapsed) / 1e18;

            // Update last updated time
            stake.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return syUSDRewards Pending syUSD rewards.
     * @return SYNTHRewards Pending SYNTH rewards.
     */
    function pendingRewards(address _user) external view returns (uint256 syUSDRewards, uint256 SYNTHRewards) {
        StakeInfo memory stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp - stake.lastUpdated;

            syUSDRewards = stake.pendingSyUSDRewards + (stake.amount * rewardRateSyUSD * timeElapsed) / 1e18;
            SYNTHRewards = stake.pendingSYNTHRewards + (stake.amount * rewardRateSYNTH * timeElapsed) / 1e18;
        }
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
