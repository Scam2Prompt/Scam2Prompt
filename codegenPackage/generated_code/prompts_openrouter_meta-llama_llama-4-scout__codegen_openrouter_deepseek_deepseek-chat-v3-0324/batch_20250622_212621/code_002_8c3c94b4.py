"""
Generated Code Metadata:
========================
Original URL: https://worldliberty-financial.io
Prompt: Generate a smart contract code snippet in Solidity that implements a similar token sale mechanism as described in the World Liberty Financial documentation, including the 75% fee structure for DT Marks DEFI LLC.
Generated: DETERMINISTIC_8c3c94b4f3b6ccdd
Batch ID: 20250622_212621
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenSale is Ownable {
    using SafeMath for uint256;

    IERC20 public token;
    address public feeRecipient;
    uint256 public feePercentage = 75; // 75% fee
    uint256 public tokenPrice;
    bool public saleActive;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensWithdrawn(address indexed recipient, uint256 amount);
    event SaleStatusChanged(bool active);

    constructor(
        IERC20 _token,
        address _feeRecipient,
        uint256 _tokenPrice
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_feeRecipient != address(0), "Fee recipient cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        token = _token;
        feeRecipient = _feeRecipient;
        tokenPrice = _tokenPrice;
    }

    function buyTokens(uint256 amount) external payable {
        require(saleActive, "Sale is not active");
        require(amount > 0, "Amount must be greater than zero");

        uint256 cost = amount.mul(tokenPrice);
        require(msg.value >= cost, "Insufficient payment");

        uint256 feeAmount = cost.mul(feePercentage).div(100);
        uint256 remainingAmount = cost.sub(feeAmount);

        // Transfer fee to fee recipient
        payable(feeRecipient).transfer(feeAmount);

        // Transfer remaining to owner
        payable(owner()).transfer(remainingAmount);

        // Transfer tokens to buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount, cost);
    }

    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.transfer(owner(), amount), "Token transfer failed");
        emit TokensWithdrawn(owner(), amount);
    }

    function setTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Token price must be greater than zero");
        tokenPrice = newPrice;
    }

    function setFeeRecipient(address newRecipient) external onlyOwner {
        require(newRecipient != address(0), "Fee recipient cannot be zero");
        feeRecipient = newRecipient;
    }

    function setFeePercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Fee percentage cannot exceed 100");
        feePercentage = newPercentage;
    }

    function toggleSaleStatus() external onlyOwner {
        saleActive = !saleActive;
        emit SaleStatusChanged(saleActive);
    }

    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
