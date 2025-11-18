"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimesa.pages.dev
Prompt: Write a smart contract function for verifying token claim eligibility, inspired by the functionality described on the Masa Airdrop Portal.
Generated: DETERMINISTIC_b4a4ca16e899a130
Batch ID: 20250612_151159
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
 * @title TokenAirdrop
 * @dev Implements airdrop functionality with token claim eligibility verification.
 */
contract TokenAirdrop {
    // Address of the token contract
    address public tokenContract;

    // Mapping to track claimed tokens by eligible users
    mapping(address => bool) public hasClaimed;

    // List of eligible addresses for the airdrop
    mapping(address => bool) public eligibleAddresses;

    // Event emitted when a claim is successful
    event TokenClaimed(address indexed user);

    /**
     * @dev Constructor to initialize the token contract address.
     * @param _tokenContract Address of the token contract.
     */
    constructor(address _tokenContract) {
        require(_tokenContract != address(0), "Token contract address cannot be zero");
        tokenContract = _tokenContract;
    }

    /**
     * @dev Function to verify token claim eligibility and mark as claimed.
     * @notice Only eligible addresses can claim, and only once.
     */
    function claimTokens() external {
        // Check if the caller is eligible for the airdrop
        require(eligibleAddresses[msg.sender], "Caller is not eligible for the airdrop");

        // Check if the caller has already claimed the tokens
        require(!hasClaimed[msg.sender], "Caller has already claimed tokens");

        // Logic for transferring tokens can be added here
        // For example, ERC20(tokenContract).transfer(msg.sender, tokenAmount);
        // Ensure token transfer success in production-ready code

        // Mark the caller as having claimed their tokens
        hasClaimed[msg.sender] = true;

        // Emit an event for successful claim
        emit TokenClaimed(msg.sender);
    }

    /**
     * @dev Function to add eligible addresses (can only be called by contract owner).
     * @param _users Array of addresses to mark as eligible.
     */
    function addEligibleAddresses(address[] calldata _users) external {
        // In production, this function should be restricted to the contract owner or admin
        for (uint256 i = 0; i < _users.length; i++) {
            eligibleAddresses[_users[i]] = true;
        }
    }

    /**
     * @dev Function to remove eligible addresses (can only be called by contract owner).
     * @param _users Array of addresses to remove eligibility.
     */
    function removeEligibleAddresses(address[] calldata _users) external {
        // In production, this function should be restricted to the contract owner or admin
        for (uint256 i = 0; i < _users.length; i++) {
            eligibleAddresses[_users[i]] = false;
        }
    }
}
```
