"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-nyanheroes.pages.dev
Prompt: Create a smart contract for distributing $NYAN tokens based on mission completion and referrals, inspired by the Nyan Heroes reward system.
Generated: DETERMINISTIC_bd7edb9227f60233
Batch ID: 20250612_152656
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
 * @title NYAN Token Distribution Contract
 * @dev Smart contract to distribute NYAN tokens based on mission completion and referrals.
 * Inspired by the Nyan Heroes reward system.
 */
contract NYANTokenDistributor {
    // Address of the NYAN token ERC20 contract
    IERC20 public immutable nyanToken;

    // Owner of the contract
    address public owner;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Mapping to track referrals
    mapping(address => address) public referrals;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed user, uint256 amount, string reason);

    // Event emitted when a referral is set
    event ReferralSet(address indexed user, address indexed referrer);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor initializes the NYAN token address and sets the contract owner
    constructor(IERC20 _nyanToken) {
        require(address(_nyanToken) != address(0), "Invalid token address");
        nyanToken = _nyanToken;
        owner = msg.sender;
    }

    /**
     * @dev Set a referral for a user.
     * @param referrer Address of the referrer
     */
    function setReferral(address referrer) external {
        require(referrer != msg.sender, "Cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Referral already set");
        referrals[msg.sender] = referrer;
        emit ReferralSet(msg.sender, referrer);
    }

    /**
     * @dev Distribute tokens based on mission completion.
     * @param user Address of the user to distribute tokens to
     * @param amount Amount of tokens to distribute
     */
    function distributeTokensForMission(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");
        require(nyanToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        balances[user] += amount;
        nyanToken.transfer(user, amount);
        emit TokensDistributed(user, amount, "Mission Completion");

        // Reward referrer if applicable
        address referrer = referrals[user];
        if (referrer != address(0)) {
            uint256 referralReward = amount / 10; // 10% referral reward
            balances[referrer] += referralReward;
            nyanToken.transfer(referrer, referralReward);
            emit TokensDistributed(referrer, referralReward, "Referral Reward");
        }
    }

    /**
     * @dev Owner can withdraw remaining tokens in contract.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(nyanToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        nyanToken.transfer(owner, amount);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
