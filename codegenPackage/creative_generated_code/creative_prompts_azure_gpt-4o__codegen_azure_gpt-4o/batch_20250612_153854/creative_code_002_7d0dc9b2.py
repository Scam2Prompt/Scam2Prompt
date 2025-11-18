"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-air-spring.nfts2.me
Prompt: Implement a function in Solidity that calculates referral fees based on the number of NFT mints completed through a referral link, as outlined in the Zora Air Spring system.
Generated: DETERMINISTIC_7d0dc9b29d287847
Batch ID: 20250612_153854
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
 * @title ReferralFeeCalculator
 * @dev A contract to calculate referral fees based on NFT mints via referral links.
 */
contract ReferralFeeCalculator {
    // State variables
    address public owner; // Contract owner
    uint256 public feePerMint; // Fee amount per NFT mint (in wei)
    mapping(address => uint256) public referralMintCount; // Tracks the number of mints for each referrer
    mapping(address => uint256) public referralFeesEarned; // Tracks fees earned by each referrer

    // Events
    event MintRecorded(address indexed referrer, uint256 mintCount);
    event ReferralFeePaid(address indexed referrer, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _feePerMint Fee per NFT mint (in wei).
     */
    constructor(uint256 _feePerMint) {
        require(_feePerMint > 0, "Fee per mint must be greater than zero");
        owner = msg.sender;
        feePerMint = _feePerMint;
    }

    /**
     * @dev Records a mint for a referrer and updates the referral fees earned.
     * @param referrer The address of the referrer.
     */
    function recordMint(address referrer) external payable {
        require(referrer != address(0), "Invalid referrer address");
        require(msg.value == feePerMint, "Incorrect fee amount sent");

        // Increment mint count for the referrer
        referralMintCount[referrer]++;

        // Update total fees earned by the referrer
        referralFeesEarned[referrer] += msg.value;

        // Emit event for mint recorded
        emit MintRecorded(referrer, referralMintCount[referrer]);
    }

    /**
     * @dev Allows referrers to withdraw their earned referral fees.
     */
    function withdrawReferralFees() external {
        uint256 feesEarned = referralFeesEarned[msg.sender];
        require(feesEarned > 0, "No fees available for withdrawal");

        // Reset the referrer's fees before transferring to prevent reentrancy attacks
        referralFeesEarned[msg.sender] = 0;

        // Transfer the fees to the referrer
        (bool success, ) = msg.sender.call{value: feesEarned}("");
        require(success, "Fee transfer failed");

        // Emit event for referral fee paid
        emit ReferralFeePaid(msg.sender, feesEarned);
    }

    /**
     * @dev Updates the fee per NFT mint (only callable by the owner).
     * @param _newFeePerMint New fee per NFT mint (in wei).
     */
    function updateFeePerMint(uint256 _newFeePerMint) external onlyOwner {
        require(_newFeePerMint > 0, "Fee per mint must be greater than zero");
        feePerMint = _newFeePerMint;
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("Direct ETH deposits are not allowed");
    }

    /**
     * @dev Withdraw all funds from the contract (only callable by the owner).
     */
    function withdrawAllFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Funds transfer failed");
    }
}
```
