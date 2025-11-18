"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Generate code for implementing zkSwap Finance's Swap2Earn mechanism in a decentralized application, ensuring rewards are distributed to both traders and liquidity providers.
Generated: DETERMINISTIC_546192eca5af4d8e
Batch ID: 20250612_154728
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
 * @title zkSwapFinance Swap2Earn Mechanism
 * @dev This smart contract implements a Swap2Earn mechanism for rewarding traders and liquidity providers in a decentralized application.
 */
contract Swap2Earn {
    
    // Struct to store user rewards
    struct UserRewards {
        uint256 traderRewards;
        uint256 liquidityProviderRewards;
    }

    // Mapping to store rewards for each user address
    mapping(address => UserRewards) public userRewards;

    // Address of the contract owner
    address public owner;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 traderRewards, uint256 liquidityProviderRewards);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Swap2Earn: Caller is not the owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to calculate and distribute rewards to traders and liquidity providers.
     * @param _trader Address of the trader
     * @param _liquidityProvider Address of the liquidity provider
     * @param _tradeAmount Amount traded by the trader
     * @param _liquidityProvided Amount of liquidity provided
     */
    function distributeRewards(
        address _trader,
        address _liquidityProvider,
        uint256 _tradeAmount,
        uint256 _liquidityProvided
    ) external onlyOwner {
        require(_trader != address(0), "Swap2Earn: Trader address cannot be zero");
        require(_liquidityProvider != address(0), "Swap2Earn: Liquidity provider address cannot be zero");
        require(_tradeAmount > 0, "Swap2Earn: Trade amount must be greater than zero");
        require(_liquidityProvided > 0, "Swap2Earn: Liquidity provided must be greater than zero");

        // Calculate rewards (example logic: 1% of trade amount goes to trader, 0.5% of liquidity provided goes to provider)
        uint256 traderReward = (_tradeAmount * 1) / 100;
        uint256 liquidityProviderReward = (_liquidityProvided * 5) / 1000;

        // Update rewards in the mapping
        userRewards[_trader].traderRewards += traderReward;
        userRewards[_liquidityProvider].liquidityProviderRewards += liquidityProviderReward;

        // Emit an event for rewards distribution
        emit RewardsDistributed(_trader, traderReward, liquidityProviderReward);
    }

    /**
     * @dev Function for users to claim their rewards.
     * @param _isTrader True if the user is claiming trader rewards, false if claiming liquidity provider rewards
     */
    function claimRewards(bool _isTrader) external {
        uint256 rewardAmount;

        if (_isTrader) {
            rewardAmount = userRewards[msg.sender].traderRewards;
            require(rewardAmount > 0, "Swap2Earn: No trader rewards to claim");
            userRewards[msg.sender].traderRewards = 0;
        } else {
            rewardAmount = userRewards[msg.sender].liquidityProviderRewards;
            require(rewardAmount > 0, "Swap2Earn: No liquidity provider rewards to claim");
            userRewards[msg.sender].liquidityProviderRewards = 0;
        }

        // Transfer rewards to the user (assuming rewards are in ETH for simplicity)
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Swap2Earn: Reward transfer failed");
    }

    /**
     * @dev Fallback function to receive ETH for reward distribution.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw contract's ETH balance (owner-only).
     */
    function withdraw() external onlyOwner {
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Swap2Earn: Withdraw failed");
    }
}
```
