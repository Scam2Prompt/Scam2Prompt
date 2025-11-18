"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethermail.pages.dev
Prompt: Develop a smart contract that interacts with EtherMail's PayWall feature, allowing users to define content preferences and earn EMC rewards for promotional emails.
Generated: DETERMINISTIC_f2e4ea00aa08fe3b
Batch ID: 20250612_152249
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
 * @title EtherMailPayWallInteraction
 * @dev A smart contract to interact with EtherMail's PayWall feature, enabling users to define
 *      content preferences and earn EMC rewards for receiving promotional emails.
 */
contract EtherMailPayWallInteraction {

    // Structure to store user content preferences
    struct UserPreferences {
        bool acceptPromotionalEmails;
        string[] preferredTopics;
    }

    // Mapping to store user preferences
    mapping(address => UserPreferences) private userPreferences;

    // Event emitted when a user updates their preferences
    event PreferencesUpdated(
        address indexed user,
        bool acceptPromotionalEmails,
        string[] preferredTopics
    );

    // Event emitted when EMC rewards are distributed to the user
    event EMCRewardDistributed(
        address indexed user,
        uint256 amount
    );

    // ERC20 token interface for EMC rewards
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    // Address of the EMC token contract
    IERC20 private emcToken;

    // Constructor to initialize the EMC token contract address
    constructor(address _emcTokenAddress) {
        require(_emcTokenAddress != address(0), "Invalid token address");
        emcToken = IERC20(_emcTokenAddress);
    }

    /**
     * @notice Update user's content preferences.
     * @param _acceptPromotionalEmails Whether the user accepts promotional emails.
     * @param _preferredTopics List of topics the user is interested in.
     */
    function updatePreferences(
        bool _acceptPromotionalEmails,
        string[] memory _preferredTopics
    ) external {
        userPreferences[msg.sender] = UserPreferences({
            acceptPromotionalEmails: _acceptPromotionalEmails,
            preferredTopics: _preferredTopics
        });

        emit PreferencesUpdated(msg.sender, _acceptPromotionalEmails, _preferredTopics);
    }

    /**
     * @notice Distribute EMC rewards to the user for accepting promotional emails.
     * @param _amount Amount of EMC tokens to distribute.
     */
    function distributeRewards(uint256 _amount) external {
        require(
            userPreferences[msg.sender].acceptPromotionalEmails,
            "User has not opted in for promotional emails"
        );
        require(_amount > 0, "Reward amount must be greater than zero");

        // Transfer EMC tokens to the user
        bool success = emcToken.transfer(msg.sender, _amount);
        require(success, "EMC token transfer failed");

        emit EMCRewardDistributed(msg.sender, _amount);
    }

    /**
     * @notice Retrieve the content preferences of a user.
     * @param _user Address of the user.
     * @return acceptPromotionalEmails Whether the user accepts promotional emails.
     * @return preferredTopics List of topics the user is interested in.
     */
    function getPreferences(address _user)
        external
        view
        returns (bool acceptPromotionalEmails, string[] memory preferredTopics)
    {
        UserPreferences memory preferences = userPreferences[_user];
        return (preferences.acceptPromotionalEmails, preferences.preferredTopics);
    }
}
```
