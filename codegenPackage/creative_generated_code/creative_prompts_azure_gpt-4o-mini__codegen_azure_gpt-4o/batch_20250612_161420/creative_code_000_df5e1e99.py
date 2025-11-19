"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miner-pepebnb2.vercel.app
Prompt: Generate a smart contract for an investment platform based on the Binance Smart Chain that includes features like referral bonuses and anti-whale controls.
Generated: DETERMINISTIC_df5e1e999e2de91f
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
 * @title InvestmentPlatform
 * @dev A smart contract for an investment platform on Binance Smart Chain
 *      featuring referral bonuses and anti-whale controls.
 */
contract InvestmentPlatform {
    // State variables
    address public owner; // Contract owner
    uint256 public constant MAX_INVESTMENT = 1000 ether; // Maximum investment limit (anti-whale control)
    uint256 public constant REFERRAL_BONUS = 5; // Referral bonus percentage (5%)
    uint256 public constant MINIMUM_INVESTMENT = 0.1 ether; // Minimum investment amount

    struct Investor {
        uint256 totalInvested; // Total amount invested
        uint256 totalReferralBonus; // Total referral bonuses earned
    }

    mapping(address => Investor) public investors; // Mapping of investor addresses to their data
    mapping(address => address) public referrals; // Mapping of investor addresses to their referrers

    event InvestmentMade(address indexed investor, uint256 amount, address indexed referrer);
    event ReferralBonusPaid(address indexed referrer, address indexed referee, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier isValidInvestment(uint256 amount) {
        require(amount >= MINIMUM_INVESTMENT, "Investment amount is below the minimum limit");
        require(
            investors[msg.sender].totalInvested + amount <= MAX_INVESTMENT,
            "Investment exceeds the maximum limit"
        );
        _;
    }

    constructor() {
        owner = msg.sender; // Set contract deployer as owner
    }

    /**
     * @dev Invest in the platform, optionally providing a referrer.
     * @param referrer Address of the referrer (optional).
     */
    function invest(address referrer) external payable isValidInvestment(msg.value) {
        require(msg.value > 0, "Investment must be greater than zero");

        // Update investor data
        Investor storage investor = investors[msg.sender];
        investor.totalInvested += msg.value;

        // Handle referrals
        if (referrer != address(0) && referrer != msg.sender) {
            referrals[msg.sender] = referrer;
            uint256 bonus = (msg.value * REFERRAL_BONUS) / 100;

            // Pay referral bonus to referrer
            Investor storage referrerData = investors[referrer];
            referrerData.totalReferralBonus += bonus;

            // Transfer bonus from contract balance
            payable(referrer).transfer(bonus);

            emit ReferralBonusPaid(referrer, msg.sender, bonus);
        }

        emit InvestmentMade(msg.sender, msg.value, referrer);
    }

    /**
     * @dev Withdraw contract balance (only owner can perform this action).
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Get investor data.
     * @param investor Address of the investor.
     * @return totalInvested Total invested amount.
     * @return totalReferralBonus Total referral bonuses earned.
     */
    function getInvestorData(address investor)
        external
        view
        returns (uint256 totalInvested, uint256 totalReferralBonus)
    {
        Investor memory data = investors[investor];
        return (data.totalInvested, data.totalReferralBonus);
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to handle ether sent to the contract.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
