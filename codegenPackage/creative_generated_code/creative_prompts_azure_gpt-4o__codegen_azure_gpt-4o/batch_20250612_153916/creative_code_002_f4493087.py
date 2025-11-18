"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Develop a smart contract in Solidity that tracks referral fees for Unichain-Rooster NFT mints and automatically distributes rewards to the specified wallet address.
Generated: DETERMINISTIC_f4493087debe3ca9
Batch ID: 20250612_153916
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
 * @title ReferralFeeDistributor
 * @dev This smart contract manages referral fees for Unichain-Rooster NFT mints
 * and automatically distributes rewards to a designated wallet address.
 */
contract ReferralFeeDistributor {
    // Address of the contract owner
    address public owner;

    // Maps referrers to their accumulated referral fees
    mapping(address => uint256) public referralFees;

    // Event emitted when referral fees are distributed
    event ReferralFeeDistributed(address indexed referrer, uint256 amount);

    // Event emitted when the owner updates the referral fee percentage
    event FeePercentageUpdated(uint256 oldPercentage, uint256 newPercentage);

    // Fee percentage (e.g., 5% is represented as 500, with 10000 = 100%)
    uint256 public feePercentage;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(uint256 _feePercentage) {
        require(_feePercentage > 0 && _feePercentage <= 10000, "Invalid fee percentage");
        owner = msg.sender;
        feePercentage = _feePercentage;
    }

    /**
     * @dev Updates the referral fee percentage.
     * @param _newFeePercentage The new referral fee percentage (e.g., 500 for 5%).
     */
    function updateFeePercentage(uint256 _newFeePercentage) external onlyOwner {
        require(_newFeePercentage > 0 && _newFeePercentage <= 10000, "Invalid fee percentage");
        uint256 oldPercentage = feePercentage;
        feePercentage = _newFeePercentage;

        emit FeePercentageUpdated(oldPercentage, _newFeePercentage);
    }

    /**
     * @dev Calculates and distributes referral fees.
     * @param referrer The address of the referrer.
     * @param mintPrice The price of the NFT mint.
     */
    function distributeReferralFee(address referrer, uint256 mintPrice) external payable {
        require(referrer != address(0), "Invalid referrer address");
        require(mintPrice > 0, "Mint price must be greater than zero");

        // Calculate the referral fee
        uint256 referralFee = (mintPrice * feePercentage) / 10000;

        // Ensure the msg.sender sends enough Ether to cover the referral fee
        require(msg.value >= referralFee, "Insufficient Ether sent for referral fee");

        // Update the referrer's accumulated fees
        referralFees[referrer] += referralFee;

        // Transfer the referral fee to the referrer
        (bool success, ) = referrer.call{value: referralFee}("");
        require(success, "Referral fee transfer failed");

        emit ReferralFeeDistributed(referrer, referralFee);
    }

    /**
     * @dev Withdraws contract balance (for emergency purposes or owner profits).
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to accept Ether (used for testing or unexpected transfers).
     */
    receive() external payable {}

    /**
     * @dev Fallback function for non-Ether calls (to prevent accidental loss of funds).
     */
    fallback() external payable {}
}
```
