"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-particle.pages.dev
Prompt: Create a smart contract that interacts with the Particle Pioneer Testnet to distribute exclusive on-chain rewards to early registrants.
Generated: DETERMINISTIC_a4b8aaba5f328de5
Batch ID: 20250612_150946
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

// Import OpenZeppelin's Ownable contract for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";
// Import OpenZeppelin's SafeERC20 for safe token transfers 
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

// Interface for the ERC20 token contract
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Smart contract to distribute exclusive rewards to early registrants
contract EarlyRegistrantReward is Ownable {
    using SafeERC20 for IERC20;

    // Token to be distributed as a reward
    IERC20 public rewardToken;
    // Mapping to track early registrants' rewards
    mapping(address => uint256) public rewards;
    // Flag to allow distribution of rewards
    bool public distributionActive;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);
    
    // Modifier to check if distribution is active
    modifier isActive() {
        require(distributionActive, "Distribution is not active");
        _;
    }

    // Constructor to initialize the contract with the reward token
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
        distributionActive = false; // Start with distribution inactive
    }

    // Function to activate or deactivate the reward distribution
    function setDistributionActive(bool _active) external onlyOwner {
        distributionActive = _active;
    }

    // Function for the owner to distribute rewards to early registrants
    function distributeRewards(address[] calldata registrants, uint256[] calldata amounts) external onlyOwner isActive {
        require(registrants.length == amounts.length, "Mismatched arrays");

        for (uint256 i = 0; i < registrants.length; i++) {
            // Check for zero addresses
            require(registrants[i] != address(0), "Invalid recipient address");
            // Update the rewards mapping
            rewards[registrants[i]] += amounts[i];
            // Transfer the reward tokens to the registrant
            rewardToken.safeTransfer(registrants[i], amounts[i]);
            // Emit an event for each distribution
            emit RewardsDistributed(registrants[i], amounts[i]);
        }
    }

    // Function to withdraw unclaimed rewards (if any) by the owner
    function withdrawUnclaimedRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        rewardToken.safeTransfer(owner(), amount);
    }

    // Function to check the total rewards of a registrant
    function checkRewards(address registrant) external view returns (uint256) {
        return rewards[registrant];
    }
}
```
