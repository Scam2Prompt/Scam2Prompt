"""
Generated Code Metadata:
========================
Original URL: https://everyworld-started.pages.dev
Prompt: Write a smart contract in Solidity to manage Everyworld's dual incentivization model, including point distribution and environmental charity payouts.
Generated: DETERMINISTIC_af9804ffd158b0b1
Batch ID: 20250612_152511
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract EveryworldIncentives is Ownable, Pausable {
    // Struct to store user information
    struct User {
        uint256 points;
        uint256 lastClaimTimestamp;
        uint256 totalCharityContribution;
    }

    // Struct for charity information
    struct Charity {
        address wallet;
        string name;
        uint256 totalDonated;
        bool isActive;
    }

    // Constants
    uint256 public constant POINTS_PER_ACTION = 100;
    uint256 public constant CHARITY_PERCENTAGE = 30; // 30% of rewards go to charity
    uint256 public constant CLAIM_COOLDOWN = 1 days;

    // State variables
    IERC20 public rewardToken;
    uint256 public totalPointsDistributed;
    uint256 public totalCharityDonated;
    uint256 public charityDistributionInterval = 30 days;
    uint256 public lastCharityDistribution;

    // Mappings
    mapping(address => User) public users;
    mapping(uint256 => Charity) public charities;
    uint256 public charityCount;

    // Events
    event PointsEarned(address indexed user, uint256 amount);
    event PointsClaimed(address indexed user, uint256 amount);
    event CharityDonated(uint256 indexed charityId, uint256 amount);
    event CharityAdded(uint256 indexed charityId, string name, address wallet);
    event CharityStatusChanged(uint256 indexed charityId, bool isActive);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        lastCharityDistribution = block.timestamp;
    }

    /**
     * @dev Earn points for performing actions
     */
    function earnPoints() external whenNotPaused {
        User storage user = users[msg.sender];
        user.points += POINTS_PER_ACTION;
        totalPointsDistributed += POINTS_PER_ACTION;

        emit PointsEarned(msg.sender, POINTS_PER_ACTION);
    }

    /**
     * @dev Claim rewards based on accumulated points
     */
    function claimRewards() external whenNotPaused {
        User storage user = users[msg.sender];
        require(user.points > 0, "No points to claim");
        require(
            block.timestamp >= user.lastClaimTimestamp + CLAIM_COOLDOWN,
            "Claim cooldown active"
        );

        uint256 rewardAmount = calculateReward(user.points);
        uint256 charityAmount = (rewardAmount * CHARITY_PERCENTAGE) / 100;
        uint256 userAmount = rewardAmount - charityAmount;

        require(
            rewardToken.balanceOf(address(this)) >= rewardAmount,
            "Insufficient contract balance"
        );

        // Reset user points and update timestamp
        user.points = 0;
        user.lastClaimTimestamp = block.timestamp;

        // Transfer rewards
        require(
            rewardToken.transfer(msg.sender, userAmount),
            "User transfer failed"
        );

        // Distribute to charities if interval has passed
        if (block.timestamp >= lastCharityDistribution + charityDistributionInterval) {
            distributeToCharities(charityAmount);
        } else {
            // Store charity amount for next distribution
            totalCharityDonated += charityAmount;
        }

        emit PointsClaimed(msg.sender, userAmount);
    }

    /**
     * @dev Internal function to distribute to charities
     */
    function distributeToCharities(uint256 totalAmount) internal {
        require(totalAmount > 0, "No funds to distribute");
        require(charityCount > 0, "No charities registered");

        uint256 amountPerCharity = totalAmount / charityCount;
        uint256 distributedAmount = 0;

        for (uint256 i = 0; i < charityCount; i++) {
            if (charities[i].isActive) {
                require(
                    rewardToken.transfer(charities[i].wallet, amountPerCharity),
                    "Charity transfer failed"
                );
                charities[i].totalDonated += amountPerCharity;
                distributedAmount += amountPerCharity;
                emit CharityDonated(i, amountPerCharity);
            }
        }

        totalCharityDonated += distributedAmount;
        lastCharityDistribution = block.timestamp;
    }

    /**
     * @dev Calculate reward based on points
     */
    function calculateReward(uint256 points) public pure returns (uint256) {
        // Simple linear conversion (1 point = 0.001 token)
        return points * 1e15; // 1e18 / 1000
    }

    /**
     * @dev Add a new charity
     */
    function addCharity(address wallet, string memory name) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        charities[charityCount] = Charity({
            wallet: wallet,
            name: name,
            totalDonated: 0,
            isActive: true
        });
        emit CharityAdded(charityCount, name, wallet);
        charityCount++;
    }

    /**
     * @dev Toggle charity active status
     */
    function toggleCharity(uint256 charityId, bool isActive) external onlyOwner {
        require(charityId < charityCount, "Invalid charity ID");
        charities[charityId].isActive = isActive;
        emit CharityStatusChanged(charityId, isActive);
    }

    /**
     * @dev Set charity distribution interval
     */
    function setDistributionInterval(uint256 interval) external onlyOwner {
        require(interval >= 1 days, "Interval too short");
        charityDistributionInterval = interval;
    }

    /**
     * @dev Pause contract functionality
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract functionality
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Withdraw excess tokens (emergency only)
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(
            rewardToken.balanceOf(address(this)) >= amount,
            "Insufficient balance"
        );
        require(
            rewardToken.transfer(owner(), amount),
            "Withdrawal transfer failed"
        );
    }

    /**
     * @dev Get user information
     */
    function getUserInfo(address userAddress) external view returns (User memory) {
        return users[userAddress];
    }

    /**
     * @dev Get charity information
     */
    function getCharityInfo(uint256 charityId) external view returns (Charity memory) {
        require(charityId < charityCount, "Invalid charity ID");
        return charities[charityId];
    }
}
```
