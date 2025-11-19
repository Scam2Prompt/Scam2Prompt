"""
Generated Code Metadata:
========================
Original URL: https://pacmoon-8ko.pages.dev
Prompt: Write a smart contract in Solidity for an airdrop event similar to Pacmoon's Airdrop Season 3 on the Blast network.
Generated: DETERMINISTIC_f94489213edd50c6
Batch ID: 20250622_211442
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

/**
 * @title AirdropContract
 * @dev Implements an airdrop mechanism similar to Pacmoon's Airdrop Season 3
 * Supports ERC20 token distribution with eligibility checks and claim functionality
 */
contract AirdropContract is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public airdropAmount;
    uint256 public claimPeriodEnd;
    bool public airdropPaused;

    // Mapping to track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Mapping to store eligible addresses and their allocated amounts
    mapping(address => uint256) public eligibleAmounts;

    // Events
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event AirdropPaused(bool paused);
    event EligibilitySet(address[] recipients, uint256[] amounts);

    /**
     * @dev Constructor
     * @param _token Address of the ERC20 token to be airdropped
     * @param _airdropAmount Default amount each eligible address can claim
     * @param _claimPeriodEnd Timestamp when claiming period ends
     */
    constructor(
        address _token,
        uint256 _airdropAmount,
        uint256 _claimPeriodEnd
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_claimPeriodEnd > block.timestamp, "Claim period must be in the future");

        token = IERC20(_token);
        airdropAmount = _airdropAmount;
        claimPeriodEnd = _claimPeriodEnd;
    }

    /**
     * @dev Set eligibility for multiple addresses with custom amounts
     * @param recipients Array of eligible addresses
     * @param amounts Array of amounts each address can claim
     */
    function setEligibility(
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid address");
            eligibleAmounts[recipients[i]] = amounts[i];
        }

        emit EligibilitySet(recipients, amounts);
    }

    /**
     * @dev Claim airdrop tokens
     */
    function claim() external nonReentrant {
        require(!airdropPaused, "Airdrop is paused");
        require(block.timestamp <= claimPeriodEnd, "Claim period has ended");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(eligibleAmounts[msg.sender] > 0, "Not eligible");

        uint256 amount = eligibleAmounts[msg.sender];
        hasClaimed[msg.sender] = true;

        require(
            token.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit AirdropClaimed(msg.sender, amount);
    }

    /**
     * @dev Pause or unpause the airdrop
     * @param _paused Boolean indicating whether to pause or unpause
     */
    function setPaused(bool _paused) external onlyOwner {
        airdropPaused = _paused;
        emit AirdropPaused(_paused);
    }

    /**
     * @dev Extend the claim period
     * @param _newEnd New end timestamp for claim period
     */
    function extendClaimPeriod(uint256 _newEnd) external onlyOwner {
        require(_newEnd > claimPeriodEnd, "New end must be after current end");
        claimPeriodEnd = _newEnd;
    }

    /**
     * @dev Withdraw remaining tokens after claim period ends
     * @param _to Address to send remaining tokens to
     */
    function withdrawRemaining(address _to) external onlyOwner {
        require(block.timestamp > claimPeriodEnd, "Claim period not ended");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(_to, balance), "Token transfer failed");
    }

    /**
     * @dev Check claimable amount for an address
     * @param _address Address to check
     * @return Amount claimable by the address
     */
    function getClaimableAmount(address _address) external view returns (uint256) {
        if (hasClaimed[_address] || block.timestamp > claimPeriodEnd || airdropPaused) {
            return 0;
        }
        return eligibleAmounts[_address];
    }
}
```
