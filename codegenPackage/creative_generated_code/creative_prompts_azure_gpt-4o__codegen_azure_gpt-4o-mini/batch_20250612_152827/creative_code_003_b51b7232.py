"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riftscalingzea.pages.dev
Prompt: Create a smart contract for distributing $RIFT airdrops, including functionality for eligibility verification and time-based claiming windows.
Generated: DETERMINISTIC_b51b7232ffd57d29
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RIFT Airdrop Contract
 * @dev This contract manages the airdrop of $RIFT tokens to eligible users
 * with time-based claiming windows and eligibility verification.
 */
contract RIFT Airdrop is Ownable {
    // ERC20 token to be distributed
    IERC20 public riftToken;

    // Struct to hold airdrop details
    struct Airdrop {
        uint256 amount;           // Amount of tokens allocated for the airdrop
        uint256 startTime;       // Start time for claiming
        uint256 endTime;         // End time for claiming
        bool claimed;            // Status of claim for the address
    }

    // Mapping of addresses to their airdrop details
    mapping(address => Airdrop) public airdrops;

    // Event emitted when airdrop is created
    event AirdropCreated(address indexed recipient, uint256 amount, uint256 startTime, uint256 endTime);
    
    // Event emitted when airdrop is claimed
    event AirdropClaimed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the token contract address.
     * @param _riftToken Address of the $RIFT token contract.
     */
    constructor(IERC20 _riftToken) {
        riftToken = _riftToken;
    }

    /**
     * @dev Function to create an airdrop for a specific address.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to distribute.
     * @param duration Duration in seconds for which the airdrop is valid.
     */
    function createAirdrop(address recipient, uint256 amount, uint256 duration) external onlyOwner {
        require(recipient != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than 0");
        require(airdrops[recipient].amount == 0, "Airdrop already exists for this address");

        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + duration;

        airdrops[recipient] = Airdrop(amount, startTime, endTime, false);
        
        emit AirdropCreated(recipient, amount, startTime, endTime);
    }

    /**
     * @dev Function for eligible users to claim their airdrop.
     */
    function claimAirdrop() external {
        Airdrop storage airdrop = airdrops[msg.sender];

        // Check if airdrop is valid
        require(airdrop.amount > 0, "No airdrop available for this address");
        require(block.timestamp >= airdrop.startTime, "Claiming window has not started");
        require(block.timestamp <= airdrop.endTime, "Claiming window has ended");
        require(!airdrop.claimed, "Airdrop already claimed");

        // Mark airdrop as claimed
        airdrop.claimed = true;

        // Transfer tokens to the caller
        require(riftToken.transfer(msg.sender, airdrop.amount), "Token transfer failed");

        emit AirdropClaimed(msg.sender, airdrop.amount);
    }

    /**
     * @dev Function to withdraw unclaimed tokens by the owner after the airdrop period.
     */
    function withdrawUnclaimedTokens() external onlyOwner {
        uint256 totalUnclaimed = riftToken.balanceOf(address(this));
        uint256 claimedAmount = 0;

        // Calculate total claimed amount
        for (uint256 i = 0; i < totalClaimedAddresses(); i++) {
            claimedAmount += airdrops[claimedAddress(i)].amount;
        }

        uint256 withdrawableAmount = totalUnclaimed - claimedAmount;

        require(withdrawableAmount > 0, "No unclaimed tokens to withdraw");
        require(riftToken.transfer(msg.sender, withdrawableAmount), "Token transfer failed");
    }

    // Helper functions to manage claimed addresses (not shown).
    // In a complete implementation, you would manage an array of claimed addresses.

    function totalClaimedAddresses() internal view returns (uint256) {
        // Logic to return total claimed addresses
    }

    function claimedAddress(uint256 index) internal view returns (address) {
        // Logic to return claimed address at a given index
    }
}
```
