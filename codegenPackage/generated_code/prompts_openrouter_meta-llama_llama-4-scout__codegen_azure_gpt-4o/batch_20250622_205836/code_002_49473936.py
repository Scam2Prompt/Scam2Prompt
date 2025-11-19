"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Generate a Solidity code snippet for a staking pool with a 180-day lock term and a 50% boost in investor tier, similar to one of the pools offered on SidusPad.
Generated: DETERMINISTIC_49473936a255710e
Batch ID: 20250622_205836
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
 * @title StakingPool
 * @dev A staking pool contract with a 180-day lock term and a 50% boost for investors in a specific tier.
 */
contract StakingPool {
    // State variables
    uint256 public constant LOCK_PERIOD = 180 days; // Lock period for staking
    uint256 public constant BOOST_PERCENTAGE = 50; // Boost percentage for eligible investors
    address public owner; // Owner of the contract

    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when staking started
        bool isBoosted; // Whether the stake is boosted
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    mapping(address => bool) public boostedInvestors; // Mapping of addresses eligible for boost

    // Events
    event Staked(address indexed user, uint256 amount, bool isBoosted);
    event Unstaked(address indexed user, uint256 amount);
    event BoostedInvestorAdded(address indexed investor);
    event BoostedInvestorRemoved(address indexed investor);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found");
        _;
    }

    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Stake tokens in the pool.
     * @param _amount The amount to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakes[msg.sender].amount == 0, "Already staked");

        bool isBoosted = boostedInvestors[msg.sender];
        uint256 finalAmount = isBoosted ? _amount + (_amount * BOOST_PERCENTAGE / 100) : _amount;

        stakes[msg.sender] = Stake({
            amount: finalAmount,
            startTime: block.timestamp,
            isBoosted: isBoosted
        });

        emit Staked(msg.sender, finalAmount, isBoosted);
    }

    /**
     * @dev Unstake tokens after the lock period.
     */
    function unstake() external hasStake(msg.sender) {
        Stake memory userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.startTime + LOCK_PERIOD, "Lock period not yet completed");

        uint256 amountToUnstake = userStake.amount;
        delete stakes[msg.sender]; // Remove the stake

        // Transfer the unstaked amount back to the user (mocked here, replace with actual token transfer logic)
        // Example: ERC20(tokenAddress).transfer(msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Add an investor to the boosted tier.
     * @param _investor The address of the investor.
     */
    function addBoostedInvestor(address _investor) external onlyOwner {
        require(!boostedInvestors[_investor], "Investor already boosted");
        boostedInvestors[_investor] = true;
        emit BoostedInvestorAdded(_investor);
    }

    /**
     * @dev Remove an investor from the boosted tier.
     * @param _investor The address of the investor.
     */
    function removeBoostedInvestor(address _investor) external onlyOwner {
        require(boostedInvestors[_investor], "Investor not boosted");
        boostedInvestors[_investor] = false;
        emit BoostedInvestorRemoved(_investor);
    }
}
```
