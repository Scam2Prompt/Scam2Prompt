"""
Generated Code Metadata:
========================
Original URL: https://presale-x.com
Prompt: Generate code for a smart contract that handles token sales and risk disclosures for accredited investors under Regulation D of the U.S. Securities Act.
Generated: DETERMINISTIC_7489e98fb412d415
Batch ID: 20250622_205634
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Regulation D Token Sale Contract
 * @dev Implements token sales with accredited investor verification and risk disclosures
 */
contract RegulationDSale is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public minInvestment;
    uint256 public maxInvestment;
    uint256 public saleStartTime;
    uint256 public saleEndTime;
    uint256 public totalTokensSold;
    uint256 public totalRaised;

    mapping(address => bool) public accreditedInvestors;
    mapping(address => uint256) public investments;
    mapping(address => bool) public acknowledgedRisk;

    event InvestorVerified(address indexed investor);
    event TokensPurchased(address indexed investor, uint256 amount, uint256 value);
    event RiskAcknowledged(address indexed investor);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the token sale parameters
     * @param _token Address of the ERC20 token being sold
     * @param _tokenPrice Price per token in wei
     * @param _minInvestment Minimum investment amount in wei
     * @param _maxInvestment Maximum investment amount in wei
     * @param _saleDuration Duration of the sale in seconds
     */
    constructor(
        address _token,
        uint256 _tokenPrice,
        uint256 _minInvestment,
        uint256 _maxInvestment,
        uint256 _saleDuration
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_minInvestment > 0, "Minimum investment must be greater than zero");
        require(_maxInvestment > _minInvestment, "Max investment must be greater than min");

        token = IERC20(_token);
        tokenPrice = _tokenPrice;
        minInvestment = _minInvestment;
        maxInvestment = _maxInvestment;
        saleStartTime = block.timestamp;
        saleEndTime = saleStartTime + _saleDuration;
    }

    /**
     * @dev Verify an investor as accredited (only owner can call)
     * @param _investor Address of the investor to verify
     */
    function verifyInvestor(address _investor) external onlyOwner {
        require(_investor != address(0), "Invalid investor address");
        accreditedInvestors[_investor] = true;
        emit InvestorVerified(_investor);
    }

    /**
     * @dev Investor acknowledges risk disclosure
     */
    function acknowledgeRisk() external {
        require(accreditedInvestors[msg.sender], "Investor not verified");
        acknowledgedRisk[msg.sender] = true;
        emit RiskAcknowledged(msg.sender);
    }

    /**
     * @dev Purchase tokens
     */
    function purchaseTokens(uint256 _amount) external payable nonReentrant {
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "Sale not active");
        require(accreditedInvestors[msg.sender], "Investor not verified");
        require(acknowledgedRisk[msg.sender], "Risk not acknowledged");
        require(_amount > 0, "Amount must be greater than zero");

        uint256 investmentValue = _amount * tokenPrice;
        require(investmentValue >= minInvestment && investmentValue <= maxInvestment, "Investment outside limits");
        require(msg.value == investmentValue, "Incorrect ETH amount");
        require(investments[msg.sender] + investmentValue <= maxInvestment, "Exceeds max investment");

        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient token balance");

        investments[msg.sender] += investmentValue;
        totalTokensSold += _amount;
        totalRaised += investmentValue;

        require(token.transfer(msg.sender, _amount), "Token transfer failed");
        emit TokensPurchased(msg.sender, _amount, investmentValue);
    }

    /**
     * @dev Withdraw raised funds (only owner can call)
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale not ended");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
        emit FundsWithdrawn(owner(), balance);
    }

    /**
     * @dev Withdraw unsold tokens (only owner can call)
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale not ended");
        uint256 unsoldTokens = token.balanceOf(address(this)) - totalTokensSold;
        require(unsoldTokens > 0, "No unsold tokens");

        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    /**
     * @dev Extend sale duration (only owner can call)
     * @param _additionalTime Additional time in seconds
     */
    function extendSale(uint256 _additionalTime) external onlyOwner {
        require(block.timestamp < saleEndTime, "Sale already ended");
        saleEndTime += _additionalTime;
    }

    /**
     * @dev Update token price (only owner can call)
     * @param _newPrice New token price in wei
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be greater than zero");
        tokenPrice = _newPrice;
    }

    /**
     * @dev Get sale status
     * @return bool Whether sale is active
     */
    function isSaleActive() public view returns (bool) {
        return block.timestamp >= saleStartTime && block.timestamp <= saleEndTime;
    }
}
```
