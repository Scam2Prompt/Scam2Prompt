"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Explain the differences between the three redemption phases for $BASED tokens and how the token allocation varies depending on the phase.
Generated: DETERMINISTIC_ce65deada9478b40
Batch ID: 20250622_211350
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
 * @title BasedTokenRedemption
 * @dev Manages the three redemption phases for $BASED tokens with varying allocations.
 */
contract BasedTokenRedemption {
    // Redemption phases
    enum RedemptionPhase {
        EarlyBird,
        Standard,
        Final
    }

    // Current redemption phase
    RedemptionPhase public currentPhase;

    // Token allocations for each phase (in basis points, where 10000 = 100%)
    uint256 private constant EARLY_BIRD_ALLOCATION = 5000; // 50%
    uint256 private constant STANDARD_ALLOCATION = 3000;  // 30%
    uint256 private constant FINAL_ALLOCATION = 2000;     // 20%

    // Total supply of $BASED tokens
    uint256 public totalSupply;

    // Mapping to track redeemed tokens per phase
    mapping(RedemptionPhase => uint256) public redeemedPerPhase;

    // Event emitted when tokens are redeemed
    event TokensRedeemed(address indexed user, RedemptionPhase phase, uint256 amount);

    /**
     * @dev Constructor initializes the total supply and sets the initial phase.
     * @param _totalSupply Total supply of $BASED tokens.
     */
    constructor(uint256 _totalSupply) {
        totalSupply = _totalSupply;
        currentPhase = RedemptionPhase.EarlyBird;
    }

    /**
     * @dev Advances the redemption phase to the next one.
     * Only callable by the contract owner (not implemented here for simplicity).
     */
    function advancePhase() external {
        require(
            currentPhase != RedemptionPhase.Final,
            "BasedTokenRedemption: Already in final phase"
        );

        if (currentPhase == RedemptionPhase.EarlyBird) {
            currentPhase = RedemptionPhase.Standard;
        } else if (currentPhase == RedemptionPhase.Standard) {
            currentPhase = RedemptionPhase.Final;
        }
    }

    /**
     * @dev Redeems tokens based on the current phase.
     * @param amount The amount of tokens to redeem.
     */
    function redeemTokens(uint256 amount) external {
        require(amount > 0, "BasedTokenRedemption: Amount must be greater than 0");

        uint256 allocation;
        if (currentPhase == RedemptionPhase.EarlyBird) {
            allocation = EARLY_BIRD_ALLOCATION;
        } else if (currentPhase == RedemptionPhase.Standard) {
            allocation = STANDARD_ALLOCATION;
        } else {
            allocation = FINAL_ALLOCATION;
        }

        uint256 maxRedeemable = (totalSupply * allocation) / 10000;
        require(
            redeemedPerPhase[currentPhase] + amount <= maxRedeemable,
            "BasedTokenRedemption: Exceeds phase allocation"
        );

        redeemedPerPhase[currentPhase] += amount;
        
        // In a real implementation, you would transfer tokens here
        // _transfer(msg.sender, amount);

        emit TokensRedeemed(msg.sender, currentPhase, amount);
    }

    /**
     * @dev Returns the remaining tokens available for redemption in the current phase.
     */
    function getRemainingPhaseAllocation() external view returns (uint256) {
        uint256 allocation;
        if (currentPhase == RedemptionPhase.EarlyBird) {
            allocation = EARLY_BIRD_ALLOCATION;
        } else if (currentPhase == RedemptionPhase.Standard) {
            allocation = STANDARD_ALLOCATION;
        } else {
            allocation = FINAL_ALLOCATION;
        }

        uint256 maxRedeemable = (totalSupply * allocation) / 10000;
        return maxRedeemable - redeemedPerPhase[currentPhase];
    }
}
```
