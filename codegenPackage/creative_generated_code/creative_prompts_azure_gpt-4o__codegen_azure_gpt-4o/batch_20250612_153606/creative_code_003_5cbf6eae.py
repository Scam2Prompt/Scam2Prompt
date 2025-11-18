"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xuirin-com.pages.dev
Prompt: Write a Solidity smart contract for handling cashback rewards based on the tiered structure (Silver, Gold, Diamond) described in xuirin Finance's DeFi Debit Card program.
Generated: DETERMINISTIC_5cbf6eae5db442f8
Batch ID: 20250612_153606
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
 * @title Cashback Rewards Contract
 * @dev A smart contract for handling cashback rewards based on tiered structure:
 *      Silver, Gold, Diamond tiers.
 */
contract CashbackRewards {
    // Owner of the contract
    address public owner;

    // Enum representing reward tiers
    enum Tier { Silver, Gold, Diamond }

    // Struct to represent user information
    struct User {
        Tier tier;        // User's reward tier
        uint256 cashback; // Accumulated cashback balance
    }

    // Mapping to store user information based on their address
    mapping(address => User) public users;

    // Event emitted when cashback is updated for a user
    event CashbackUpdated(address indexed user, uint256 amount);

    // Event emitted when a user's tier is updated
    event TierUpdated(address indexed user, Tier newTier);

    // Modifier to restrict function access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this operation");
        _;
    }

    // Modifier to ensure a user exists in the users mapping
    modifier userExists(address _user) {
        require(users[_user].tier != Tier(uint256(-1)), "User does not exist");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new user to the system
     * @param _user Address of the user
     * @param _tier Initial tier of the user (Silver, Gold, Diamond)
     */
    function addUser(address _user, Tier _tier) external onlyOwner {
        require(users[_user].tier == Tier(uint256(-1)), "User already exists");
        users[_user] = User(_tier, 0);
    }

    /**
     * @dev Update user's tier
     * @param _user Address of the user
     * @param _newTier New tier to be assigned
     */
    function updateTier(address _user, Tier _newTier) external onlyOwner userExists(_user) {
        users[_user].tier = _newTier;
        emit TierUpdated(_user, _newTier);
    }

    /**
     * @dev Calculate and add cashback based on the user's tier
     * @param _user Address of the user
     * @param _spendAmount Amount spent by the user
     */
    function addCashback(address _user, uint256 _spendAmount) external userExists(_user) {
        uint256 cashbackPercentage = getCashbackPercentage(users[_user].tier);
        uint256 cashbackAmount = (_spendAmount * cashbackPercentage) / 100;

        // Update user's cashback balance
        users[_user].cashback += cashbackAmount;

        emit CashbackUpdated(_user, cashbackAmount);
    }

    /**
     * @dev Withdraw accumulated cashback for a user
     * @param _user Address of the user
     */
    function withdrawCashback(address _user) external userExists(_user) {
        require(users[_user].cashback > 0, "No cashback available to withdraw");
        
        uint256 cashbackToWithdraw = users[_user].cashback;
        users[_user].cashback = 0;

        // Transfer cashback to user
        (bool sent, ) = _user.call{value: cashbackToWithdraw}("");
        require(sent, "Cashback withdrawal failed");

        emit CashbackUpdated(_user, 0);
    }

    /**
     * @dev Get the cashback percentage based on the user's tier
     * @param _tier Tier of the user
     * @return Cashback percentage (e.g., 1 for 1%)
     */
    function getCashbackPercentage(Tier _tier) public pure returns (uint256) {
        if (_tier == Tier.Silver) {
            return 1; // 1% cashback
        } else if (_tier == Tier.Gold) {
            return 2; // 2% cashback
        } else if (_tier == Tier.Diamond) {
            return 3; // 3% cashback
        } else {
            revert("Invalid tier");
        }
    }

    /**
     * @dev Receive Ether to fund cashback withdrawals
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unexpected Ether transfers
     */
    fallback() external payable {}
}
```
