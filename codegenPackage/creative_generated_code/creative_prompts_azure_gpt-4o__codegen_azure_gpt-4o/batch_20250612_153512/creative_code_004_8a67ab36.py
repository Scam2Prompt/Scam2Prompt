"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yologames-io.pages.dev
Prompt: Write code in Solidity to implement a reward system for players supplying liquidity to single-player games, as outlined in YOLO Games' "Be the House" feature.
Generated: DETERMINISTIC_8a67ab36754efb7b
Batch ID: 20250612_153512
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
 * @title YOLOGamesLiquidityRewards
 * @dev A contract to reward players who supply liquidity to single-player games.
 * Players receive rewards based on their contribution and the game's success.
 */
contract YOLOGamesLiquidityRewards {
    // Struct to track liquidity providers
    struct LiquidityProvider {
        uint256 amountProvided; // Amount of liquidity provided by the player
        uint256 rewardsEarned;  // Rewards earned by the player
    }

    // Mapping of player addresses to their liquidity provider details
    mapping(address => LiquidityProvider) public liquidityProviders;

    // Total liquidity supplied to the games
    uint256 public totalLiquidity;

    // Reward rate per unit of liquidity (settable by the owner)
    uint256 public rewardRate;

    // Address of the contract owner
    address public owner;

    // Events
    event LiquidityProvided(address indexed provider, uint256 amount);
    event RewardsClaimed(address indexed provider, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    constructor(uint256 _initialRewardRate) {
        require(_initialRewardRate > 0, "Reward rate must be greater than zero");
        owner = msg.sender;
        rewardRate = _initialRewardRate;
    }

    /**
     * @dev Allows a player to provide liquidity to the contract.
     * @param _amount The amount of liquidity to provide.
     */
    function provideLiquidity(uint256 _amount) external payable {
        require(_amount > 0, "Liquidity amount must be greater than zero");
        require(msg.value == _amount, "Ether amount must match the liquidity amount");

        LiquidityProvider storage provider = liquidityProviders[msg.sender];
        provider.amountProvided += _amount;
        totalLiquidity += _amount;

        emit LiquidityProvided(msg.sender, _amount);
    }

    /**
     * @dev Calculates the rewards for a given player based on their liquidity contribution.
     * @param _provider The address of the liquidity provider.
     * @return The reward amount.
     */
    function calculateRewards(address _provider) public view returns (uint256) {
        LiquidityProvider memory provider = liquidityProviders[_provider];
        return (provider.amountProvided * rewardRate) / 1 ether; // Normalized reward calculation
    }

    /**
     * @dev Allows a player to claim their accumulated rewards.
     */
    function claimRewards() external {
        LiquidityProvider storage provider = liquidityProviders[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update internal state
        provider.rewardsEarned += rewards;

        // Transfer rewards to the player
        payable(msg.sender).transfer(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Allows the contract owner to update the reward rate.
     * @param _newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Fallback function to handle accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed. Use provideLiquidity()");
    }

    /**
     * @dev Allows the contract owner to withdraw contract funds (emergency use).
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(_amount);
    }
}
```
