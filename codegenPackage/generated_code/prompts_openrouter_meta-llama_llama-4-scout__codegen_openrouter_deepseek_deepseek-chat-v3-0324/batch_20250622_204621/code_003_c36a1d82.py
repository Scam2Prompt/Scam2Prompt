"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Generate a smart contract code (in Solidity, for example) for managing the Wealth Coin (WEL) Treasury Reserve, ensuring that it supports investments in businesses, technology, and charities according to the described economic model.
Generated: DETERMINISTIC_c36a1d824c6e1611
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WealthCoinTreasury is Ownable {
    using SafeMath for uint256;

    // WEL token interface
    IERC20 public welToken;

    // Treasury allocation percentages
    uint256 public constant BUSINESS_PERCENT = 40;
    uint256 public constant TECHNOLOGY_PERCENT = 30;
    uint256 public constant CHARITY_PERCENT = 20;
    uint256 public constant RESERVE_PERCENT = 10;

    // Treasury balances
    uint256 public businessBalance;
    uint256 public technologyBalance;
    uint256 public charityBalance;
    uint256 public reserveBalance;

    // Investment tracking
    struct Investment {
        address recipient;
        uint256 amount;
        uint256 timestamp;
        string description;
    }

    mapping(string => Investment[]) public businessInvestments;
    mapping(string => Investment[]) public technologyInvestments;
    mapping(string => Investment[]) public charityInvestments;

    // Events
    event FundsDeposited(uint256 amount);
    event BusinessInvestmentMade(address indexed recipient, uint256 amount, string description);
    event TechnologyInvestmentMade(address indexed recipient, uint256 amount, string description);
    event CharityInvestmentMade(address indexed recipient, uint256 amount, string description);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    constructor(address _welTokenAddress) {
        require(_welTokenAddress != address(0), "Invalid token address");
        welToken = IERC20(_welTokenAddress);
    }

    /**
     * @dev Deposit WEL tokens into the treasury
     * @param amount Amount of WEL tokens to deposit
     */
    function depositFunds(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(welToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Allocate funds according to percentages
        uint256 businessAllocation = amount.mul(BUSINESS_PERCENT).div(100);
        uint256 technologyAllocation = amount.mul(TECHNOLOGY_PERCENT).div(100);
        uint256 charityAllocation = amount.mul(CHARITY_PERCENT).div(100);
        uint256 reserveAllocation = amount.mul(RESERVE_PERCENT).div(100);

        businessBalance = businessBalance.add(businessAllocation);
        technologyBalance = technologyBalance.add(technologyAllocation);
        charityBalance = charityBalance.add(charityAllocation);
        reserveBalance = reserveBalance.add(reserveAllocation);

        emit FundsDeposited(amount);
    }

    /**
     * @dev Invest in a business
     * @param recipient Address of the business receiving investment
     * @param amount Amount of WEL tokens to invest
     * @param category Investment category
     * @param description Description of the investment
     */
    function investInBusiness(
        address recipient,
        uint256 amount,
        string memory category,
        string memory description
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(businessBalance >= amount, "Insufficient business funds");

        businessBalance = businessBalance.sub(amount);
        businessInvestments[category].push(Investment(recipient, amount, block.timestamp, description));

        require(welToken.transfer(recipient, amount), "Transfer failed");

        emit BusinessInvestmentMade(recipient, amount, description);
    }

    /**
     * @dev Invest in technology
     * @param recipient Address of the technology project receiving investment
     * @param amount Amount of WEL tokens to invest
     * @param category Investment category
     * @param description Description of the investment
     */
    function investInTechnology(
        address recipient,
        uint256 amount,
        string memory category,
        string memory description
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(technologyBalance >= amount, "Insufficient technology funds");

        technologyBalance = technologyBalance.sub(amount);
        technologyInvestments[category].push(Investment(recipient, amount, block.timestamp, description));

        require(welToken.transfer(recipient, amount), "Transfer failed");

        emit TechnologyInvestmentMade(recipient, amount, description);
    }

    /**
     * @dev Donate to charity
     * @param recipient Address of the charity receiving donation
     * @param amount Amount of WEL tokens to donate
     * @param category Donation category
     * @param description Description of the donation
     */
    function donateToCharity(
        address recipient,
        uint256 amount,
        string memory category,
        string memory description
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(charityBalance >= amount, "Insufficient charity funds");

        charityBalance = charityBalance.sub(amount);
        charityInvestments[category].push(Investment(recipient, amount, block.timestamp, description));

        require(welToken.transfer(recipient, amount), "Transfer failed");

        emit CharityInvestmentMade(recipient, amount, description);
    }

    /**
     * @dev Withdraw funds from reserve (emergency use only)
     * @param recipient Address to receive the funds
     * @param amount Amount of WEL tokens to withdraw
     */
    function withdrawReserveFunds(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(reserveBalance >= amount, "Insufficient reserve funds");

        reserveBalance = reserveBalance.sub(amount);
        require(welToken.transfer(recipient, amount), "Transfer failed");

        emit FundsWithdrawn(recipient, amount);
    }

    /**
     * @dev Get business investments by category
     * @param category Investment category
     * @return Array of investments
     */
    function getBusinessInvestments(string memory category) external view returns (Investment[] memory) {
        return businessInvestments[category];
    }

    /**
     * @dev Get technology investments by category
     * @param category Investment category
     * @return Array of investments
     */
    function getTechnologyInvestments(string memory category) external view returns (Investment[] memory) {
        return technologyInvestments[category];
    }

    /**
     * @dev Get charity donations by category
     * @param category Donation category
     * @return Array of donations
     */
    function getCharityInvestments(string memory category) external view returns (Investment[] memory) {
        return charityInvestments[category];
    }

    /**
     * @dev Get total treasury balance
     * @return Total balance in WEL tokens
     */
    function getTotalBalance() external view returns (uint256) {
        return businessBalance.add(technologyBalance).add(charityBalance).add(reserveBalance);
    }
}
```
