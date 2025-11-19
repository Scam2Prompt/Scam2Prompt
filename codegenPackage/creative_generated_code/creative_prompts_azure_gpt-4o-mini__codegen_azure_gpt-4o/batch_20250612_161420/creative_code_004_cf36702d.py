"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipepetrader-c9j0k84jr-edrive.vercel.app
Prompt: Create an example of a referral reward system in a smart contract that aligns with the Ai Pepe Trader's airdrop strategy.
Generated: DETERMINISTIC_cf36702d92c05980
Batch ID: 20250612_161420
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
 * @title ReferralRewardSystem
 * @dev A smart contract to implement a referral-based reward system for Ai Pepe Trader's airdrop strategy.
 */
contract ReferralRewardSystem {
    // Address of the contract owner
    address public owner;

    // Airdrop reward amount (in wei)
    uint256 public airdropReward;

    // Referral reward amount (in wei)
    uint256 public referralReward;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Mapping to track referrals
    mapping(address => address) public referrer;

    // Event emitted when a user claims their airdrop
    event AirdropClaimed(address indexed user, uint256 amount);

    // Event emitted when a referral reward is distributed
    event ReferralRewardDistributed(address indexed referrer, address indexed referee, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with reward amounts.
     * @param _airdropReward The amount to distribute for airdrops.
     * @param _referralReward The amount to reward referrers.
     */
    constructor(uint256 _airdropReward, uint256 _referralReward) {
        require(_airdropReward > 0, "Airdrop reward must be greater than zero.");
        require(_referralReward > 0, "Referral reward must be greater than zero.");

        owner = msg.sender;
        airdropReward = _airdropReward;
        referralReward = _referralReward;
    }

    /**
     * @dev Function to claim an airdrop. If referred, the referrer gets a reward.
     * @param _referrer Address of the referrer. Pass address(0) if no referrer.
     */
    function claimAirdrop(address _referrer) external {
        require(balances[msg.sender] == 0, "Airdrop already claimed.");

        // Update user's balance with airdrop reward
        balances[msg.sender] += airdropReward;
        emit AirdropClaimed(msg.sender, airdropReward);

        // Handle referral logic
        if (_referrer != address(0) && _referrer != msg.sender && balances[_referrer] > 0) {
            referrer[msg.sender] = _referrer;
            balances[_referrer] += referralReward;
            emit ReferralRewardDistributed(_referrer, msg.sender, referralReward);
        }
    }

    /**
     * @dev Function to withdraw funds from the contract (owner only).
     */
    function withdraw() external {
        require(msg.sender == owner, "Only the owner can withdraw funds.");
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal.");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Fallback function to allow the contract to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Function to get the balance of the contract.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
