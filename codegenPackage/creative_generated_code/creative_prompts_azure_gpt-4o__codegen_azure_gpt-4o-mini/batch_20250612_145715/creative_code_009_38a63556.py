"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-claimv2.pages.dev
Prompt: Develop a smart contract that integrates a VIP membership tier system for token holders, inspired by Everlodge's private members club functionality.
Generated: DETERMINISTIC_38a63556bf8bb7ef
Batch ID: 20250612_145715
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VIPMembership
 * @dev This smart contract manages a VIP membership tier system for token holders.
 */
contract VIPMembership is Ownable {
    
    // Struct to represent a member
    struct Member {
        bool isActive; // Indicates if the member is active
        uint256 tier;  // Represents the membership tier
    }

    // Mapping to store members' data
    mapping(address => Member) public members;

    // The ERC20 token used for membership
    IERC20 public membershipToken;

    // Events for logging membership changes
    event MembershipToggled(address indexed member, bool isActive);
    event TierUpdated(address indexed member, uint256 newTier);

    // Modifier to check if the caller is a member
    modifier onlyMember() {
        require(members[msg.sender].isActive, "You are not a VIP member.");
        _;
    }

    /**
     * @dev Constructor to set the ERC20 token address.
     * @param _tokenAddress The address of the ERC20 token.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero.");
        membershipToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Allows a user to become a VIP member by depositing tokens.
     * @param _amount The amount of tokens to deposit.
     */
    function becomeMember(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero.");
        require(membershipToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed.");

        members[msg.sender] = Member({
            isActive: true,
            tier: 1 // Default tier for new members
        });

        emit MembershipToggled(msg.sender, true);
    }

    /**
     * @dev Allows a member to upgrade their membership tier.
     * @param _newTier The new tier to set for the member.
     */
    function upgradeTier(uint256 _newTier) external onlyMember {
        require(_newTier > members[msg.sender].tier, "New tier must be higher than current tier.");

        members[msg.sender].tier = _newTier;

        emit TierUpdated(msg.sender, _newTier);
    }

    /**
     * @dev Allows a member to cancel their membership.
     */
    function cancelMembership() external onlyMember {
        members[msg.sender].isActive = false;

        emit MembershipToggled(msg.sender, false);
    }

    /**
     * @dev Allows the owner to withdraw any tokens accidentally sent to this contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero.");
        require(membershipToken.balanceOf(address(this)) >= _amount, "Insufficient balance.");
        
        membershipToken.transfer(owner(), _amount);
    }
}
```
