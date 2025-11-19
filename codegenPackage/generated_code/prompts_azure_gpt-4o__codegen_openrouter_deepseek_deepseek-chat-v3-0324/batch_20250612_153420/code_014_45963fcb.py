"""
Generated Code Metadata:
========================
Original URL: https://elephantrewards.pages.dev
Prompt: Write a Solidity contract for implementing a discounted bond system that pays out daily rewards, similar to Elephant Money Farms' 30-day bond feature.
Generated: DETERMINISTIC_45963fcbdc11dabe
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DiscountedBond is Ownable, ReentrancyGuard {
    // Bond details
    struct Bond {
        uint256 amount;
        uint256 startTime;
        uint256 endTime;
        uint256 claimedAmount;
        bool isActive;
    }

    // Token used for bonding
    IERC20 public bondToken;
    // Reward token
    IERC20 public rewardToken;
    // Bond duration in seconds (30 days)
    uint256 public constant BOND_DURATION = 30 days;
    // Discount percentage (e.g., 1000 = 10%)
    uint256 public discountPercentage;
    // Total bonds created
    uint256 public totalBonds;
    // Mapping from bond ID to Bond struct
    mapping(uint256 => Bond) public bonds;
    // Mapping from user address to their bond IDs
    mapping(address => uint256[]) public userBonds;

    // Events
    event BondCreated(address indexed user, uint256 bondId, uint256 amount, uint256 discountedAmount);
    event RewardClaimed(address indexed user, uint256 bondId, uint256 amount);
    event BondClosed(address indexed user, uint256 bondId);

    constructor(
        address _bondToken,
        address _rewardToken,
        uint256 _discountPercentage
    ) {
        require(_bondToken != address(0), "Invalid bond token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_discountPercentage > 0 && _discountPercentage <= 10000, "Invalid discount percentage");

        bondToken = IERC20(_bondToken);
        rewardToken = IERC20(_rewardToken);
        discountPercentage = _discountPercentage;
    }

    /**
     * @notice Create a new bond
     * @param amount Amount of bond tokens to deposit
     */
    function createBond(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Calculate discounted amount
        uint256 discountedAmount = amount - (amount * discountPercentage / 10000);
        
        // Transfer bond tokens from user to contract
        require(
            bondToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Create new bond
        uint256 bondId = totalBonds++;
        bonds[bondId] = Bond({
            amount: discountedAmount,
            startTime: block.timestamp,
            endTime: block.timestamp + BOND_DURATION,
            claimedAmount: 0,
            isActive: true
        });

        userBonds[msg.sender].push(bondId);

        emit BondCreated(msg.sender, bondId, amount, discountedAmount);
    }

    /**
     * @notice Claim available rewards for a bond
     * @param bondId ID of the bond to claim rewards from
     */
    function claimRewards(uint256 bondId) external nonReentrant {
        require(bonds[bondId].isActive, "Bond is not active");
        require(bonds[bondId].startTime <= block.timestamp, "Bond not started yet");

        Bond storage bond = bonds[bondId];
        uint256 claimable = calculateClaimable(bondId);
        require(claimable > 0, "No rewards to claim");

        bond.claimedAmount += claimable;
        
        // Transfer rewards to user
        require(
            rewardToken.transfer(msg.sender, claimable),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, bondId, claimable);
    }

    /**
     * @notice Close a bond and claim remaining rewards
     * @param bondId ID of the bond to close
     */
    function closeBond(uint256 bondId) external nonReentrant {
        require(bonds[bondId].isActive, "Bond is not active");
        require(block.timestamp >= bonds[bondId].endTime, "Bond not matured yet");

        Bond storage bond = bonds[bondId];
        bond.isActive = false;

        // Claim any remaining rewards
        uint256 claimable = calculateClaimable(bondId);
        if (claimable > 0) {
            bond.claimedAmount += claimable;
            require(
                rewardToken.transfer(msg.sender, claimable),
                "Reward transfer failed"
            );
        }

        // Return principal to user
        require(
            bondToken.transfer(msg.sender, bond.amount),
            "Principal transfer failed"
        );

        emit BondClosed(msg.sender, bondId);
    }

    /**
     * @notice Calculate claimable rewards for a bond
     * @param bondId ID of the bond to calculate rewards for
     * @return claimableAmount Amount of rewards that can be claimed
     */
    function calculateClaimable(uint256 bondId) public view returns (uint256) {
        Bond memory bond = bonds[bondId];
        if (!bond.isActive || bond.startTime > block.timestamp) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp - bond.startTime;
        if (elapsedTime > BOND_DURATION) {
            elapsedTime = BOND_DURATION;
        }

        uint256 totalRewards = bond.amount;
        uint256 earnedAmount = (totalRewards * elapsedTime) / BOND_DURATION;
        return earnedAmount - bond.claimedAmount;
    }

    /**
     * @notice Get all bond IDs for a user
     * @param user Address of the user
     * @return Array of bond IDs
     */
    function getUserBonds(address user) external view returns (uint256[] memory) {
        return userBonds[user];
    }

    /**
     * @notice Update discount percentage (owner only)
     * @param newDiscount New discount percentage (1000 = 10%)
     */
    function setDiscountPercentage(uint256 newDiscount) external onlyOwner {
        require(newDiscount > 0 && newDiscount <= 10000, "Invalid discount percentage");
        discountPercentage = newDiscount;
    }

    /**
     * @notice Withdraw excess tokens (owner only)
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawExcessTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(bondToken), "Cannot withdraw bond tokens");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
