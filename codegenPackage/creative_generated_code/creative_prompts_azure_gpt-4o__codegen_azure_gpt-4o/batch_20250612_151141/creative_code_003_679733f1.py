"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Write a Solidity smart contract for the Crudo Protocol's loyalty program that rewards users with CRUDO tokens for frequent gas purchases and referrals, as outlined in the webpage content.
Generated: DETERMINISTIC_679733f113d368af
Batch ID: 20250612_151141
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
 * @title CrudoLoyaltyProgram
 * @dev This contract implements a loyalty program for the Crudo Protocol where users can earn CRUDO tokens
 *      through gas purchases and referrals.
 */
contract CrudoLoyaltyProgram {
    // Address of the CRUDO token contract
    address public crudoToken;

    // Owner of the contract
    address public owner;

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Mapping to track referrals
    mapping(address => address) public referrals;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when a referral is added
    event ReferralAdded(address indexed referrer, address indexed referred);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize contract with CRUDO token address and set the contract owner.
     * @param _crudoToken Address of the CRUDO token contract.
     */
    constructor(address _crudoToken) {
        require(_crudoToken != address(0), "Invalid CRUDO token address");
        crudoToken = _crudoToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to add a referral. Allows users to refer others.
     * @param referrer Address of the referrer.
     */
    function addReferral(address referrer) external {
        require(referrer != msg.sender, "Cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Referral already exists");

        referrals[msg.sender] = referrer;

        emit ReferralAdded(referrer, msg.sender);
    }

    /**
     * @dev Function to distribute rewards to users.
     *      Rewards are distributed based on gas purchases and referrals.
     * @param user Address of the user to reward.
     * @param amount Amount of CRUDO tokens to reward.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Invalid reward amount");

        rewards[user] += amount;

        emit RewardsDistributed(user, amount);

        // Transfer CRUDO tokens to the user
        require(
            IERC20(crudoToken).transfer(user, amount),
            "Token transfer failed"
        );
    }

    /**
     * @dev Function to view rewards for a user.
     * @param user Address of the user.
     * @return The total reward balance of the user.
     */
    function viewRewards(address user) external view returns (uint256) {
        return rewards[user];
    }

    /**
     * @dev Interface for ERC20 token interactions.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount)
            external
            returns (bool);
    }
}
```
