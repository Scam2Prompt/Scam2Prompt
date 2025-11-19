"""
Generated Code Metadata:
========================
Original URL: https://ethermail.pages.dev
Prompt: Develop a smart contract that interacts with EtherMail's PayWall feature, allowing users to define content preferences and earn EMC rewards for promotional emails.
Generated: DETERMINISTIC_f2e4ea00aa08fe3b
Batch ID: 20250612_152249
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract EtherMailPayWall is Ownable, ReentrancyGuard {
    // EMC token interface
    IERC20 public emcToken;

    // Content category structure
    struct Category {
        string name;
        uint256 rewardRate; // EMC per email
        bool active;
    }

    // User preferences structure
    struct UserPreferences {
        uint256[] selectedCategories;
        uint256 totalEarned;
        uint256 lastInteraction;
    }

    // Mapping of category IDs to Category struct
    mapping(uint256 => Category) public categories;

    // Mapping of user addresses to their preferences
    mapping(address => UserPreferences) public userPreferences;

    // Total categories count
    uint256 public categoryCount;

    // Events
    event CategoryAdded(uint256 indexed categoryId, string name, uint256 rewardRate);
    event CategoryUpdated(uint256 indexed categoryId, string name, uint256 rewardRate, bool active);
    event PreferencesUpdated(address indexed user, uint256[] categories);
    event RewardsClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    constructor(address _emcTokenAddress) {
        require(_emcTokenAddress != address(0), "Invalid EMC token address");
        emcToken = IERC20(_emcTokenAddress);
    }

    /**
     * @dev Add a new content category
     * @param _name Name of the category
     * @param _rewardRate EMC reward rate per email
     */
    function addCategory(string memory _name, uint256 _rewardRate) external onlyOwner {
        uint256 categoryId = categoryCount;
        categories[categoryId] = Category({
            name: _name,
            rewardRate: _rewardRate,
            active: true
        });
        categoryCount++;
        emit CategoryAdded(categoryId, _name, _rewardRate);
    }

    /**
     * @dev Update an existing category
     * @param _categoryId ID of the category to update
     * @param _name New name for the category
     * @param _rewardRate New reward rate for the category
     * @param _active Whether the category is active
     */
    function updateCategory(
        uint256 _categoryId,
        string memory _name,
        uint256 _rewardRate,
        bool _active
    ) external onlyOwner {
        require(_categoryId < categoryCount, "Invalid category ID");
        categories[_categoryId] = Category({
            name: _name,
            rewardRate: _rewardRate,
            active: _active
        });
        emit CategoryUpdated(_categoryId, _name, _rewardRate, _active);
    }

    /**
     * @dev Set user preferences for content categories
     * @param _categoryIds Array of category IDs the user wants to receive
     */
    function setPreferences(uint256[] memory _categoryIds) external {
        require(_categoryIds.length <= categoryCount, "Too many categories");

        // Validate all categories exist and are active
        for (uint256 i = 0; i < _categoryIds.length; i++) {
            require(_categoryIds[i] < categoryCount, "Invalid category ID");
            require(categories[_categoryIds[i]].active, "Category not active");
        }

        userPreferences[msg.sender].selectedCategories = _categoryIds;
        userPreferences[msg.sender].lastInteraction = block.timestamp;
        
        emit PreferencesUpdated(msg.sender, _categoryIds);
    }

    /**
     * @dev Record email view and calculate rewards
     * @param _user User address
     * @param _categoryId Category of the email viewed
     */
    function recordEmailView(address _user, uint256 _categoryId) external onlyOwner {
        require(_categoryId < categoryCount, "Invalid category ID");
        require(categories[_categoryId].active, "Category not active");

        UserPreferences storage pref = userPreferences[_user];
        
        // Check if user has this category selected
        bool hasCategory = false;
        for (uint256 i = 0; i < pref.selectedCategories.length; i++) {
            if (pref.selectedCategories[i] == _categoryId) {
                hasCategory = true;
                break;
            }
        }
        
        if (hasCategory) {
            pref.totalEarned += categories[_categoryId].rewardRate;
            pref.lastInteraction = block.timestamp;
        }
    }

    /**
     * @dev Claim accumulated EMC rewards
     */
    function claimRewards() external nonReentrant {
        UserPreferences storage pref = userPreferences[msg.sender];
        require(pref.totalEarned > 0, "No rewards to claim");

        uint256 amount = pref.totalEarned;
        pref.totalEarned = 0;

        require(
            emcToken.transfer(msg.sender, amount),
            "EMC transfer failed"
        );

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Withdraw EMC tokens from contract (owner only)
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner nonReentrant {
        require(
            emcToken.transfer(owner(), _amount),
            "EMC transfer failed"
        );
        emit TokensWithdrawn(owner(), _amount);
    }

    /**
     * @dev Get user's selected categories
     * @param _user User address
     * @return Array of category IDs
     */
    function getUserCategories(address _user) external view returns (uint256[] memory) {
        return userPreferences[_user].selectedCategories;
    }

    /**
     * @dev Get user's total earned EMC
     * @param _user User address
     * @return Total earned EMC
     */
    function getUserTotalEarned(address _user) external view returns (uint256) {
        return userPreferences[_user].totalEarned;
    }
}
```
