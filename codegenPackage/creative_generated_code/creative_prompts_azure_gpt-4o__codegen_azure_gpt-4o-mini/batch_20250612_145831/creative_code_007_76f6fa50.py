"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skimasky56.pages.dev
Prompt: Develop a smart contract for managing $SKI reward claims, ensuring alignment with the SKI MASK DOG platform's terms and conditions.
Generated: DETERMINISTIC_76f6fa5071c2f455
Batch ID: 20250612_145831
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

// Importing OpenZeppelin's ERC20 contract for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SKIRewardManager
 * @dev A smart contract for managing $SKI reward claims
 */
contract SKIRewardManager is Ownable {
    IERC20 public skiToken; // The SKI token contract
    mapping(address => uint256) public rewardClaims; // Records the amount claimed by each address
    uint256 public totalRewards; // Total rewards available for distribution
    bool public rewardsPaused; // Flag to pause claim operations

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed claimant, uint256 amount);

    // Modifier to check if rewards are paused
    modifier whenNotPaused() {
        require(!rewardsPaused, "Claims are currently paused");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _skiToken Address of the SKI token contract
     */
    constructor(address _skiToken) {
        require(_skiToken != address(0), "Invalid token address");
        skiToken = IERC20(_skiToken);
    }

    /**
     * @dev Allows the owner to set the total rewards available
     * @param _totalRewards Amount of rewards to set
     */
    function setTotalRewards(uint256 _totalRewards) external onlyOwner {
        totalRewards = _totalRewards;
    }

    /**
     * @dev Allows the owner to pause or resume reward claims
     * @param _paused Boolean indicating pause state
     */
    function setRewardsPaused(bool _paused) external onlyOwner {
        rewardsPaused = _paused;
    }

    /**
     * @dev Allows users to claim their rewards
     * @param amount Amount of rewards to claim
     */
    function claimRewards(uint256 amount) external whenNotPaused {
        require(amount > 0, "Claim amount must be greater than zero");
        require(rewardClaims[msg.sender] + amount <= totalRewards, "Insufficient rewards available");

        rewardClaims[msg.sender] += amount;
        totalRewards -= amount;

        // Transfer SKI tokens to the claimant
        bool success = skiToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw remaining tokens in case of emergency
     * @param to Address to withdraw tokens to
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= skiToken.balanceOf(address(this)), "Insufficient contract balance");

        bool success = skiToken.transfer(to, amount);
        require(success, "Token transfer failed");
    }
}
```
