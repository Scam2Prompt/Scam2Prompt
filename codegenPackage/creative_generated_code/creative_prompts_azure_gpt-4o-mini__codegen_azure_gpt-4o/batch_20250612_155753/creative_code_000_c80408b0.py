"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Generate a Solidity smart contract for a cryptocurrency investment platform similar to MinerDog, incorporating features like daily profit calculations, referral commissions, and withdrawal functions.
Generated: DETERMINISTIC_c80408b0721671e8
Batch ID: 20250612_155753
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
 * @title Cryptocurrency Investment Platform
 * @notice This smart contract allows users to invest funds, earn daily profits, receive referral commissions, and withdraw earnings.
 */
contract CryptoInvestmentPlatform {
    // --- State Variables ---
    address public owner; // Contract owner
    uint256 public dailyProfitRate; // Daily profit rate (percentage, scaled by 100)
    uint256 public referralCommissionRate; // Referral commission rate (percentage, scaled by 100)
    uint256 public minimumInvestment; // Minimum investment amount in wei

    struct Investor {
        uint256 investedAmount; // Total invested amount
        uint256 lastClaimedTimestamp; // Last time profits were claimed
        uint256 referralEarnings; // Referral earnings
    }

    mapping(address => Investor) public investors; // Mapping of investor addresses to their data
    mapping(address => address) public referrals; // Mapping of user addresses to their referrer

    // --- Events ---
    event Investment(address indexed investor, uint256 amount, address indexed referrer);
    event ProfitClaimed(address indexed investor, uint256 amount);
    event ReferralEarningsPaid(address indexed referrer, uint256 amount);
    event Withdrawal(address indexed investor, uint256 amount);

    // --- Modifiers ---
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier isInvested() {
        require(investors[msg.sender].investedAmount > 0, "No active investment found");
        _;
    }

    // --- Constructor ---
    /**
     * @dev Initializes the contract with the owner and configurable settings.
     * @param _dailyProfitRate Daily profit rate (percentage scaled by 100)
     * @param _referralCommissionRate Referral commission rate (percentage scaled by 100)
     * @param _minimumInvestment Minimum investment amount in wei
     */
    constructor(uint256 _dailyProfitRate, uint256 _referralCommissionRate, uint256 _minimumInvestment) {
        require(_dailyProfitRate > 0 && _dailyProfitRate <= 10000, "Invalid daily profit rate");
        require(_referralCommissionRate > 0 && _referralCommissionRate <= 10000, "Invalid referral commission rate");
        require(_minimumInvestment > 0, "Minimum investment must be greater than zero");

        owner = msg.sender;
        dailyProfitRate = _dailyProfitRate;
        referralCommissionRate = _referralCommissionRate;
        minimumInvestment = _minimumInvestment;
    }

    // --- Functions ---
    /**
     * @dev Allows users to invest in the platform and optionally specify a referrer.
     * @param referrer Address of the referrer (optional, can be zero address)
     */
    function invest(address referrer) external payable {
        require(msg.value >= minimumInvestment, "Investment amount is below the minimum");
        
        if (investors[msg.sender].investedAmount == 0) {
            // New investor
            investors[msg.sender].lastClaimedTimestamp = block.timestamp;
        }

        investors[msg.sender].investedAmount += msg.value;

        // Handle referral
        if (referrer != address(0) && referrer != msg.sender && referrals[msg.sender] == address(0)) {
            referrals[msg.sender] = referrer;
            uint256 commission = (msg.value * referralCommissionRate) / 10000;
            investors[referrer].referralEarnings += commission;
            emit ReferralEarningsPaid(referrer, commission);
        }

        emit Investment(msg.sender, msg.value, referrer);
    }

    /**
     * @dev Calculates the daily profit for an investor since their last claim.
     * @return The calculated profit amount in wei
     */
    function calculateProfit(address investor) public view returns (uint256) {
        Investor memory user = investors[investor];
        uint256 elapsedDays = (block.timestamp - user.lastClaimedTimestamp) / 1 days;
        return (user.investedAmount * dailyProfitRate * elapsedDays) / 10000;
    }

    /**
     * @dev Allows investors to claim their profits.
     */
    function claimProfit() external isInvested {
        uint256 profit = calculateProfit(msg.sender);
        require(profit > 0, "No profit available to claim");
        investors[msg.sender].lastClaimedTimestamp = block.timestamp;

        // Transfer the profit
        (bool success, ) = msg.sender.call{value: profit}("");
        require(success, "Profit transfer failed");
        emit ProfitClaimed(msg.sender, profit);
    }

    /**
     * @dev Allows investors to withdraw their investment along with unclaimed profits.
     */
    function withdraw() external isInvested {
        uint256 profit = calculateProfit(msg.sender);
        uint256 totalAmount = investors[msg.sender].investedAmount + profit;

        investors[msg.sender].investedAmount = 0;
        investors[msg.sender].lastClaimedTimestamp = block.timestamp;

        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Withdrawal transfer failed");
        emit Withdrawal(msg.sender, totalAmount);
    }

    /**
     * @dev Allows the owner to adjust platform settings.
     * @param _dailyProfitRate New daily profit rate (percentage scaled by 100)
     * @param _referralCommissionRate New referral commission rate (percentage scaled by 100)
     * @param _minimumInvestment New minimum investment amount in wei
     */
    function updateSettings(uint256 _dailyProfitRate, uint256 _referralCommissionRate, uint256 _minimumInvestment) external onlyOwner {
        require(_dailyProfitRate > 0 && _dailyProfitRate <= 10000, "Invalid daily profit rate");
        require(_referralCommissionRate > 0 && _referralCommissionRate <= 10000, "Invalid referral commission rate");
        require(_minimumInvestment > 0, "Minimum investment must be greater than zero");

        dailyProfitRate = _dailyProfitRate;
        referralCommissionRate = _referralCommissionRate;
        minimumInvestment = _minimumInvestment;
    }

    /**
     * @dev Allows the owner to withdraw contract balance.
     */
    function ownerWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "Contract balance is zero");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Owner withdrawal transfer failed");
    }

    // --- Fallback & Receive ---
    receive() external payable {}
}
```
