"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiener-dog.pages.dev
Prompt: Write a Solidity function to distribute community rewards (20% of token supply) to $WAI token holders based on their staking contributions.
Generated: DETERMINISTIC_0c78458c78062666
Batch ID: 20250612_150226
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

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @title CommunityRewards
 * @dev This contract handles the distribution of community rewards to $WAI token holders
 */
contract CommunityRewards {
    IERC20 public waiToken; // $WAI token contract
    uint256 public totalRewards; // Total rewards to distribute
    address public owner; // Contract owner

    // Mapping to track staking contributions of each address
    mapping(address => uint256) public stakingContributions;

    // Events for logging purposes
    event RewardsDistributed(uint256 totalReward, uint256 timestamp);
    
    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(address _waiToken) {
        waiToken = IERC20(_waiToken);
        totalRewards = (waiToken.totalSupply() * 20) / 100; // Calculate 20% of the total supply
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Allows the owner to update staking contributions
     * @param staker The address of the staker
     * @param amount The amount of tokens staked
     */
    function updateStakingContribution(address staker, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        stakingContributions[staker] += amount; // Update the staking contribution
    }

    /**
     * @dev Distributes rewards to all $WAI token holders based on their staking contributions
     */
    function distributeRewards() external onlyOwner {
        uint256 totalContributions = getTotalContributions();
        require(totalContributions > 0, "No contributions to distribute rewards");

        // Distributing rewards proportionally based on contributions
        for (uint256 i = 0; i < totalContributions; i++) {
            address staker = getStakerAtIndex(i); // Assume this function exists
            uint256 reward = (stakingContributions[staker] * totalRewards) / totalContributions;
            if (reward > 0) {
                require(waiToken.transfer(staker, reward), "Transfer failed");
            }
        }
        
        emit RewardsDistributed(totalRewards, block.timestamp); // Emit event
    }

    /**
     * @dev Calculates the total contributions from all stakers
     * @return The total contributions
     */
    function getTotalContributions() internal view returns (uint256) {
        uint256 total = 0;
        // Logic to iterate through all stakers and sum their contributions (assume list of stakers is maintained)
        // For simplicity, not implemented here
        return total;
    }

    /**
     * @dev Gets the staker at a specific index (placeholder for actual implementation)
     * @param index The index of the staker
     * @return The address of the staker
     */
    function getStakerAtIndex(uint256 index) internal view returns (address) {
        // Implementation to retrieve a staker by index would go here
        // This is a placeholder function
        return address(0);
    }
}
```
