"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Write a Solidity smart contract to manage TG.Casino's High Roller NFT rewards, including rakeback and staking bonuses.
Generated: DETERMINISTIC_f5aa9e86c6262e93
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/// @title TG.Casino High Roller NFT Rewards Contract
/// @notice This contract manages rakeback and staking bonuses for TG.Casino NFT holders.
contract HighRollerNFTRewards {
    // Events
    event RakebackClaimed(address indexed user, uint256 amount);
    event StakingBonusClaimed(address indexed user, uint256 amount);
    event RakebackUpdated(address indexed user, uint256 amount);
    event StakingBonusUpdated(address indexed user, uint256 amount);

    // Struct to store user rewards
    struct Rewards {
        uint256 rakeback; // Amount of rakeback available
        uint256 stakingBonus; // Amount of staking bonus available
    }

    // State variables
    address public owner; // Owner of the contract
    mapping(address => Rewards) public userRewards; // Mapping of user addresses to their rewards

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    modifier hasRewards(address _user) {
        require(
            userRewards[_user].rakeback > 0 || userRewards[_user].stakingBonus > 0,
            "No rewards available"
        );
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to update rakeback for a user
    /// @notice Updates the rakeback rewards for the specified user
    /// @param _user Address of the user
    /// @param _amount Amount of rakeback to add
    function updateRakeback(address _user, uint256 _amount)
        external
        onlyOwner
        validAddress(_user)
    {
        userRewards[_user].rakeback += _amount;
        emit RakebackUpdated(_user, _amount);
    }

    // Function to update staking bonus for a user
    /// @notice Updates the staking bonus rewards for the specified user
    /// @param _user Address of the user
    /// @param _amount Amount of staking bonus to add
    function updateStakingBonus(address _user, uint256 _amount)
        external
        onlyOwner
        validAddress(_user)
    {
        userRewards[_user].stakingBonus += _amount;
        emit StakingBonusUpdated(_user, _amount);
    }

    // Function for users to claim their rakeback
    /// @notice Allows a user to claim their available rakeback rewards
    function claimRakeback() external hasRewards(msg.sender) {
        uint256 rakeback = userRewards[msg.sender].rakeback;
        require(rakeback > 0, "No rakeback rewards available");

        userRewards[msg.sender].rakeback = 0; // Reset rakeback to zero
        payable(msg.sender).transfer(rakeback); // Transfer funds to user

        emit RakebackClaimed(msg.sender, rakeback);
    }

    // Function for users to claim their staking bonus
    /// @notice Allows a user to claim their available staking bonus rewards
    function claimStakingBonus() external hasRewards(msg.sender) {
        uint256 stakingBonus = userRewards[msg.sender].stakingBonus;
        require(stakingBonus > 0, "No staking bonus rewards available");

        userRewards[msg.sender].stakingBonus = 0; // Reset staking bonus to zero
        payable(msg.sender).transfer(stakingBonus); // Transfer funds to user

        emit StakingBonusClaimed(msg.sender, stakingBonus);
    }

    // Function to withdraw contract funds (owner only)
    /// @notice Allows the owner to withdraw all contract funds
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");

        payable(owner).transfer(balance);
    }

    // Receive function to accept Ether
    receive() external payable {}

    // Fallback function
    fallback() external payable {}
}
```
