"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vetterplatform.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates the staking of VSL tokens, calculates preons, and applies tier multipliers for bonus preons based on the Vetter platform's rules.
Generated: DETERMINISTIC_4f1c98d54b2309e3
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
 * @title VSL Token Staking Smart Contract
 * @author Vetter Platform
 * @notice Facilitates staking of VSL tokens, calculates preons, and applies tier multipliers for bonus preons.
 * @dev Production-ready contract following Solidity best practices.
 */

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract VSLStaking {
    // State variables
    IERC20 public vslToken; // VSL Token contract instance
    address public owner; // Contract owner address

    struct Stake {
        uint256 amount; // Amount of staked tokens
        uint256 stakeTime; // Timestamp of staking
    }

    mapping(address => Stake) public stakes; // Maps user addresses to their stakes
    mapping(address => uint256) public preons; // Maps user addresses to calculated preons

    // Tier multipliers for bonus preons
    uint256 public constant TIER_1_MULTIPLIER = 10; // Bronze Tier multiplier
    uint256 public constant TIER_2_MULTIPLIER = 20; // Silver Tier multiplier
    uint256 public constant TIER_3_MULTIPLIER = 30; // Gold Tier multiplier

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event PreonsCalculated(address indexed user, uint256 preons);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(IERC20 _vslToken) {
        vslToken = _vslToken;
        owner = msg.sender;
    }

    /**
     * @notice Stake VSL tokens
     * @param _amount Amount of VSL tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(vslToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].stakeTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake VSL tokens
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens staked");

        // Transfer tokens back to the user
        require(vslToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].stakeTime = 0;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Calculate preons for the user based on staking amount and tier multiplier
     * @dev This function can be customized based on the Vetter platform's specific rules
     */
    function calculatePreons(address _user) external {
        uint256 stakedAmount = stakes[_user].amount;
        require(stakedAmount > 0, "No tokens staked");

        uint256 multiplier = getTierMultiplier(stakedAmount);
        uint256 calculatedPreons = stakedAmount * multiplier;

        preons[_user] = calculatedPreons;

        emit PreonsCalculated(_user, calculatedPreons);
    }

    /**
     * @notice Get tier multiplier based on staked amount
     * @param _amount Staked amount
     * @return Multiplier value
     */
    function getTierMultiplier(uint256 _amount) public pure returns (uint256) {
        if (_amount >= 1000 ether) {
            return TIER_3_MULTIPLIER; // Gold Tier
        } else if (_amount >= 500 ether) {
            return TIER_2_MULTIPLIER; // Silver Tier
        } else {
            return TIER_1_MULTIPLIER; // Bronze Tier
        }
    }

    /**
     * @notice Withdraw all contract funds (only owner)
     * @dev This should only be used for emergency or contract maintenance
     * @param _to Address to send the withdrawn funds
     */
    function emergencyWithdraw(address _to) external onlyOwner {
        uint256 balance = vslToken.balanceOf(address(this));
        require(vslToken.transfer(_to, balance), "Withdraw failed");
    }
}
```
