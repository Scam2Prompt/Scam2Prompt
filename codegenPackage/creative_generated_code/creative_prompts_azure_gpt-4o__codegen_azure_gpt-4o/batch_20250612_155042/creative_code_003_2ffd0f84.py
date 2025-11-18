"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://30eth.vip
Prompt: Create a function in Solidity to verify NFT airdrop receipt and calculate potential rewards based on the 30eth.vip eligibility rules.
Generated: DETERMINISTIC_2ffd0f84d7a5dc1f
Batch ID: 20250612_155042
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
 * @title NFTAirdropVerifier
 * @dev A smart contract to verify NFT airdrop receipts and calculate potential rewards
 * based on predefined eligibility rules.
 */
contract NFTAirdropVerifier {
    // Event emitted when rewards are calculated
    event RewardsCalculated(address indexed user, uint256 rewardAmount);

    // Mapping to track NFT airdrop receipts
    mapping(address => bool) public airdropReceipts;

    // Mapping to store reward multipliers for eligible users
    mapping(address => uint256) public rewardMultipliers;

    // Constant for the base reward amount (in wei)
    uint256 public constant BASE_REWARD = 0.1 ether;

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Verifies if a user is eligible for airdrop based on their receipt status.
     * @param user The address of the user.
     * @return True if the user has received the airdrop, false otherwise.
     */
    function isAirdropReceived(address user) public view returns (bool) {
        return airdropReceipts[user];
    }

    /**
     * @dev Marks a user as having received the airdrop. Can only be called by the owner.
     * @param user The address of the user.
     */
    function markAirdropReceived(address user) external onlyOwner {
        require(!airdropReceipts[user], "Airdrop already received for this user");
        airdropReceipts[user] = true;
    }

    /**
     * @dev Sets the reward multiplier for a user. Can only be called by the owner.
     * @param user The address of the user.
     * @param multiplier The reward multiplier to set.
     */
    function setRewardMultiplier(address user, uint256 multiplier) external onlyOwner {
        require(multiplier > 0, "Multiplier must be greater than 0");
        rewardMultipliers[user] = multiplier;
    }

    /**
     * @dev Calculates the user's potential rewards based on eligibility rules.
     * @param user The address of the user.
     * @return The potential reward amount in wei.
     */
    function calculateRewards(address user) external view returns (uint256) {
        require(isAirdropReceived(user), "User has not received the airdrop");
        uint256 multiplier = rewardMultipliers[user];
        require(multiplier > 0, "No reward multiplier set for this user");
        return BASE_REWARD * multiplier;
    }

    /**
     * @dev Public function to verify receipt and calculate rewards for a user.
     * Emits a `RewardsCalculated` event.
     * @param user The address of the user.
     * @return rewardAmount The calculated reward amount.
     */
    function verifyAndCalculateRewards(address user) external returns (uint256 rewardAmount) {
        require(isAirdropReceived(user), "User has not received the airdrop");
        uint256 multiplier = rewardMultipliers[user];
        require(multiplier > 0, "No reward multiplier set for this user");

        rewardAmount = BASE_REWARD * multiplier;
        emit RewardsCalculated(user, rewardAmount);
    }

    /**
     * @dev Allows the owner to withdraw the contract's balance.
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     */
    receive() external payable {}
}
```
