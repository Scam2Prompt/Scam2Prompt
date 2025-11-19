"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-resolver.web.app
Prompt: Develop a referral program in a smart contract that rewards users with a percentage of token purchases, similar to the community referral system of Pepe Ascension.
Generated: DETERMINISTIC_d6ca7509caf1b692
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, production-ready smart contract written in Solidity that fulfills your request:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ReferralProgram
 * @dev A referral program smart contract that rewards users with a percentage of token purchases.
 */
contract ReferralProgram {
    // State variables
    address public owner; // Owner of the contract
    uint256 public referralRewardPercentage; // Reward percentage for referrals (e.g., 5 for 5%)
    mapping(address => uint256) public balances; // Tracks balances of users
    mapping(address => address) public referrer; // Tracks the referrer of each user

    // Events
    event Purchase(address indexed purchaser, uint256 amount, address indexed referrer);
    event ReferralReward(address indexed referrer, uint256 rewardAmount);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _referralRewardPercentage) {
        require(_referralRewardPercentage > 0 && _referralRewardPercentage <= 100, "Percentage must be between 1 and 100");
        owner = msg.sender;
        referralRewardPercentage = _referralRewardPercentage;
    }

    /**
     * @dev Allows the owner to update the referral reward percentage.
     * @param _newPercentage The new reward percentage.
     */
    function updateReferralRewardPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage > 0 && _newPercentage <= 100, "Percentage must be between 1 and 100");
        referralRewardPercentage = _newPercentage;
    }

    /**
     * @dev Purchases tokens and assigns referral rewards if applicable.
     * @param referrerAddress The address of the referrer.
     */
    function purchaseTokens(address referrerAddress) external payable {
        require(msg.value > 0, "Purchase amount must be greater than zero");

        // Track the purchase
        balances[msg.sender] += msg.value;

        // Emit the purchase event
        emit Purchase(msg.sender, msg.value, referrerAddress);

        // If referrer is valid, reward them
        if (referrerAddress != address(0) && referrerAddress != msg.sender) {
            referrer[msg.sender] = referrerAddress;
            uint256 reward = (msg.value * referralRewardPercentage) / 100;
            balances[referrerAddress] += reward;

            // Emit the referral reward event
            emit ReferralReward(referrerAddress, reward);
        }
    }

    /**
     * @dev Withdraw ether from the contract (only owner can withdraw).
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");
        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {}
}
```

This smart contract handles token purchases, rewards referrers with a percentage of the purchase, and includes proper error handling, documentation, and adherence to best practices in Solidity.
