"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-xai-games.pages.dev
Prompt: Create a smart contract that implements staking tiers and reward multipliers for esXAI tokens, ensuring compatibility with self-custody wallets and Ledger hardware wallets, as outlined on the Xai Staking webpage.
Generated: DETERMINISTIC_5e2653b02c5db674
Batch ID: 20250612_152527
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// Importing the Ownable contract to manage contract ownership
import "@openzeppelin/contracts/access/Ownable.sol";

// A contract for staking esXAI tokens with tiers and reward multipliers
contract XaiStaking is Ownable {
    // Define the esXAI token interface
    IERC20 public esXAI;

    // Struct to represent a staking tier
    struct StakingTier {
        uint256 minDeposit;    // Minimum deposit for the tier
        uint256 multiplier;     // Reward multiplier for the tier
    }

    // Mapping of staking tiers
    mapping(uint256 => StakingTier) public tiers;
    uint256 public tierCount;

    // Struct to hold user staking information
    struct UserStake {
        uint256 amount;         // Amount staked
        uint256 tierId;        // Staking tier ID
        uint256 startTime;      // Timestamp when staking started
    }

    // Mapping of user addresses to their staking info
    mapping(address => UserStake) public userStakes;

    // Event for staking actions
    event Staked(address indexed user, uint256 amount, uint256 tierId);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the esXAI token address
    constructor(address _esXAI) {
        require(_esXAI != address(0), "Invalid token address");
        esXAI = IERC20(_esXAI);
    }

    // Function to add a new staking tier
    function addTier(uint256 _minDeposit, uint256 _multiplier) external onlyOwner {
        require(_multiplier > 0, "Multiplier must be greater than 0");
        
        tiers[tierCount] = StakingTier({
            minDeposit: _minDeposit,
            multiplier: _multiplier
        });
        tierCount++;
    }

    // Function to stake esXAI tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(esXAI.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Determine which tier the user falls into
        uint256 tierId = getTierId(_amount);
        require(tierId < tierCount, "Amount does not meet any tier requirements");

        // Transfer tokens to the contract
        esXAI.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake
        userStakes[msg.sender] = UserStake({
            amount: _amount,
            tierId: tierId,
            startTime: block.timestamp
        });

        emit Staked(msg.sender, _amount, tierId);
    }

    // Function to calculate the tier ID based on the amount staked
    function getTierId(uint256 _amount) internal view returns (uint256) {
        for (uint256 i = 0; i < tierCount; i++) {
            if (_amount >= tiers[i].minDeposit) {
                return i;
            }
        }
        revert("No valid tier found");
    }

    // Function to unstake tokens
    function unstake() external {
        UserStake storage stake = userStakes[msg.sender];
        require(stake.amount > 0, "No tokens staked");

        // Transfer tokens back to the user
        esXAI.transfer(msg.sender, stake.amount);

        emit Unstaked(msg.sender, stake.amount);
        delete userStakes[msg.sender]; // Clear user stake info
    }

    // Function to claim rewards based on staking
    function claimRewards() external {
        UserStake storage stake = userStakes[msg.sender];
        require(stake.amount > 0, "No tokens staked");

        uint256 reward = calculateRewards(stake.amount, stake.tierId);
        require(reward > 0, "No rewards available");

        // Transfer rewards to user
        esXAI.transfer(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate rewards based on amount and tier
    function calculateRewards(uint256 _amount, uint256 _tierId) internal view returns (uint256) {
        StakingTier memory tier = tiers[_tierId];
        uint256 duration = block.timestamp - userStakes[msg.sender].startTime;

        // Example reward calculation: amount * multiplier * duration (in seconds)
        return (_amount * tier.multiplier * duration) / 1e18; // Assuming a scaling factor
    }
}
```
