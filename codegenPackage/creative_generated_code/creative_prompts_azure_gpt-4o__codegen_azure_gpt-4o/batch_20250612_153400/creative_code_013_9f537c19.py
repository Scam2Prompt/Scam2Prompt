"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-ai.pages.dev
Prompt: Write a Solidity smart contract for distributing monthly rewards from the `$ETFS` sell tax pool to token holders automatically.
Generated: DETERMINISTIC_9f537c197a7664b0
Batch ID: 20250612_153400
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
 * @title ETFSRewardDistributor
 * @dev A smart contract for distributing monthly rewards from the $ETFS sell tax pool to token holders automatically.
 */
contract ETFSRewardDistributor {
    // Address of the token contract (assumes ERC20-compatible tokens)
    address public tokenAddress;

    // Mapping of token holders and their reward amounts
    mapping(address => uint256) public rewards;

    // Total reward pool collected from sell taxes
    uint256 public rewardPool;

    // Last distribution timestamp
    uint256 public lastDistributionTime;

    // Reward distribution interval (monthly)
    uint256 public constant DISTRIBUTION_INTERVAL = 30 days;

    // Event emitted for successful distributions
    event RewardsDistributed(uint256 amount, uint256 timestamp);

    // Event emitted when a user claims their reward
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to ensure only the token contract can call certain functions (e.g., adding to reward pool)
    modifier onlyTokenContract() {
        require(msg.sender == tokenAddress, "Caller is not the token contract");
        _;
    }

    // Constructor to initialize the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        lastDistributionTime = block.timestamp; // Set initial distribution time
    }

    /**
     * @dev Add funds to the reward pool (typically called by the token contract).
     * @param amount The amount to add to the reward pool.
     */
    function addToRewardPool(uint256 amount) external onlyTokenContract {
        require(amount > 0, "Amount must be greater than 0");
        rewardPool += amount;
    }

    /**
     * @dev Distribute rewards to token holders based on their balances.
     * This function can only be called after the distribution interval has passed.
     */
    function distributeRewards() external {
        require(
            block.timestamp >= lastDistributionTime + DISTRIBUTION_INTERVAL,
            "Distribution interval has not passed"
        );

        // Get total supply of the token
        uint256 totalSupply = IERC20(tokenAddress).totalSupply();
        require(totalSupply > 0, "Token total supply is zero");

        // Iterate through token holders (simplified for demonstration purposes)
        // In production, you may need off-chain scripts or additional mechanisms to track holders efficiently.
        address[] memory holders = getTokenHolders();
        uint256 totalDistributed = 0;

        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            uint256 holderBalance = IERC20(tokenAddress).balanceOf(holder);

            // Calculate reward based on holder's token balance
            uint256 reward = (holderBalance * rewardPool) / totalSupply;
            rewards[holder] += reward;
            totalDistributed += reward;
        }

        // Update reward pool after distribution
        rewardPool -= totalDistributed;

        // Update last distribution time
        lastDistributionTime = block.timestamp;

        emit RewardsDistributed(totalDistributed, block.timestamp);
    }

    /**
     * @dev Allow token holders to claim their rewards.
     */
    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for the caller
        rewards[msg.sender] = 0;

        // Transfer rewards to the caller
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev A placeholder function to simulate getting token holders.
     * In production, implement a robust solution for tracking holders.
     */
    function getTokenHolders() internal view returns (address[] memory) {
        // Placeholder logic
        address[] memory holders = new address[](0);
        return holders;
    }

    // Fallback function to allow the contract to receive ETH
    receive() external payable {}

    /**
     * @dev Interface for ERC20 tokens.
     */
    interface IERC20 {
        function totalSupply() external view returns (uint256);

        function balanceOf(address account) external view returns (uint256);
    }
}
```
