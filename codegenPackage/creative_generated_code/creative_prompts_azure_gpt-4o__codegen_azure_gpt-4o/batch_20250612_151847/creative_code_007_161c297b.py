"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trust-coin.org
Prompt: Write a smart contract in Solidity for managing referral commissions and profit distribution, based on Trust-coin's investment plans.
Generated: DETERMINISTIC_161c297bf5768bdd
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TrustCoinReferralAndProfitDistribution
 * @dev Smart contract to manage referral commissions and profit distribution for Trust-coin's investment plans.
 */
contract TrustCoinReferralAndProfitDistribution {
    // Owner of the contract
    address public owner;

    // Referral commission rate (e.g., 5%)
    uint256 public referralCommissionRate;

    // Mapping to store user investments
    mapping(address => uint256) public userInvestments;

    // Mapping to store profits distributed to users
    mapping(address => uint256) public userProfits;

    // Mapping to store referral earnings for users
    mapping(address => uint256) public referralEarnings;

    // Events
    event InvestmentMade(address indexed investor, uint256 amount);
    event ProfitDistributed(address indexed investor, uint256 profit);
    event ReferralCommissionPaid(address indexed referrer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner.");
        _;
    }

    /**
     * @dev Constructor to initialize contract with owner and referral commission rate.
     * @param _referralCommissionRate Referral commission rate in percentage (e.g., 5 for 5%).
     */
    constructor(uint256 _referralCommissionRate) {
        require(
            _referralCommissionRate <= 100,
            "Referral commission rate must be between 0 and 100."
        );
        owner = msg.sender;
        referralCommissionRate = _referralCommissionRate;
    }

    /**
     * @dev Function to invest in Trust-coin's investment plans.
     * @param referrer Address of the referrer (if any, else pass address(0)).
     */
    function invest(address referrer) external payable {
        require(msg.value > 0, "Investment amount must be greater than zero.");

        // Update user's investment balance
        userInvestments[msg.sender] += msg.value;
        emit InvestmentMade(msg.sender, msg.value);

        // Pay referral commission to referrer (if valid)
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 referralCommission = (msg.value * referralCommissionRate) /
                100;
            referralEarnings[referrer] += referralCommission;

            // Transfer commission to referrer
            (bool success, ) = referrer.call{value: referralCommission}("");
            require(success, "Referral commission payment failed.");

            emit ReferralCommissionPaid(referrer, referralCommission);
        }
    }

    /**
     * @dev Distribute profits to investors based on their investment proportion.
     * @param totalProfit Amount of total profit to distribute.
     */
    function distributeProfit(uint256 totalProfit) external onlyOwner {
        require(
            address(this).balance >= totalProfit,
            "Insufficient contract balance for profit distribution."
        );
        require(totalProfit > 0, "Profit amount must be greater than zero.");

        // Calculate total investments
        uint256 totalInvestments = getTotalInvestments();
        require(totalInvestments > 0, "No investments found.");

        // Distribute profits proportionally
        for (address investor : getAllInvestors()) {
            uint256 investorShare = (userInvestments[investor] *
                totalProfit) / totalInvestments;
            userProfits[investor] += investorShare;

            // Transfer profit to investor
            (bool success, ) = investor.call{value: investorShare}("");
            require(success, "Profit payment failed.");

            emit ProfitDistributed(investor, investorShare);
        }
    }

    /**
     * @dev Function to update the referral commission rate.
     * @param _newRate New referral commission rate in percentage.
     */
    function updateReferralCommissionRate(uint256 _newRate)
        external
        onlyOwner
    {
        require(
            _newRate <= 100,
            "Referral commission rate must be between 0 and 100."
        );
        referralCommissionRate = _newRate;
    }

    /**
     * @dev Retrieve the total investments made by all users.
     * @return Total investment amount.
     */
    function getTotalInvestments() public view returns (uint256) {
        uint256 total = 0;

        for (address investor : getAllInvestors()) {
            total += userInvestments[investor];
        }

        return total;
    }

    /**
     * @dev Retrieve the list of all investors (stub implementation, replace as needed).
     */
    function getAllInvestors() internal view returns (address[] memory) {
        // Replace with a mechanism to track all investors
        return new address[](0);
    }

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw contract balance (owner only).
     * @param amount Amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(
            address(this).balance >= amount,
            "Insufficient contract balance."
        );

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed.");
    }
}
```

Note: This implementation assumes the existence of `getAllInvestors()` for tracking all investors which is a stub here—this would typically require adding investor data to an array or another data structure when they invest. Consider implementing this functionality for production use.
