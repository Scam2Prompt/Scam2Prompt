"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonedge-finance-io.web.app
Prompt: Write a Solidity contract for a tier-based staking mechanism that unlocks exclusive VC rounds for top-tier stakers, as described in MoonEdge's Evermoon VC round.
Generated: DETERMINISTIC_8dbd90ee1c488df9
Batch ID: 20250612_152710
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
 * @title TierBasedStaking
 * @dev A staking contract where users stake tokens to reach tiers.
 * Top-tier stakers unlock exclusive VC rounds.
 */
contract TierBasedStaking {
    // Struct to store information about individual stakers
    struct Staker {
        uint256 amountStaked; // Total tokens staked by the user
        uint256 stakingTimestamp; // Timestamp when staking started
        uint8 tier; // Current tier of the staker
    }

    // Tier levels and their corresponding staking thresholds
    uint256 public constant TIER1_THRESHOLD = 1000 ether; // Top-tier threshold
    uint256 public constant TIER2_THRESHOLD = 500 ether;
    uint256 public constant TIER3_THRESHOLD = 100 ether;

    // Mapping of user address to their staking information
    mapping(address => Staker) public stakers;

    // Token used for staking (ERC20 interface)
    IERC20 public stakingToken;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Event declarations
    event Staked(address indexed user, uint256 amount, uint8 tier);
    event Unstaked(address indexed user, uint256 amount);
    event TierChanged(address indexed user, uint8 newTier);

    /**
     * @dev Constructor to initialize the staking token.
     * @param _stakingToken Address of the ERC20 token used for staking.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens to participate in the tier-based mechanism.
     * @param _amount Number of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        Staker storage staker = stakers[msg.sender];

        // Update staking details
        staker.amountStaked += _amount;
        staker.stakingTimestamp = block.timestamp;
        totalStaked += _amount;

        // Update the user's tier
        uint8 newTier = calculateTier(staker.amountStaked);
        if (newTier != staker.tier) {
            staker.tier = newTier;
            emit TierChanged(msg.sender, newTier);
        }

        emit Staked(msg.sender, _amount, newTier);
    }

    /**
     * @dev Unstake tokens and exit the tier-based mechanism.
     * @param _amount Number of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(
            staker.amountStaked >= _amount,
            "Insufficient staked amount to unstake"
        );

        // Update staking details
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        // Update the user's tier
        uint8 newTier = calculateTier(staker.amountStaked);
        if (newTier != staker.tier) {
            staker.tier = newTier;
            emit TierChanged(msg.sender, newTier);
        }

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Determine the tier based on the staked amount.
     * @param _amountStaked Amount of tokens staked by the user.
     * @return tier The tier corresponding to the staked amount.
     */
    function calculateTier(uint256 _amountStaked) public pure returns (uint8 tier) {
        if (_amountStaked >= TIER1_THRESHOLD) {
            return 1; // Top tier
        } else if (_amountStaked >= TIER2_THRESHOLD) {
            return 2;
        } else if (_amountStaked >= TIER3_THRESHOLD) {
            return 3;
        } else {
            return 0; // No tier
        }
    }

    /**
     * @dev Get the staker's current tier.
     * @param _user Address of the user.
     * @return tier The tier of the user.
     */
    function getTier(address _user) external view returns (uint8) {
        return stakers[_user].tier;
    }
}

// Minimal ERC20 interface for token interactions
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
