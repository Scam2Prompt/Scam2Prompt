"""
Generated Code Metadata:
========================
Original URL: https://milady-dfk.pages.dev
Prompt: Generate a Solidity contract for a token sale mechanism that includes stepped raises and fixed-price pools, similar to the Milady Cult presale structure.
Generated: DETERMINISTIC_a3476a2614ba538b
Batch ID: 20250612_152358
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

contract TokenSale is Ownable, ReentrancyGuard {
    // Token being sold
    IERC20 public token;

    // Sale parameters
    struct SalePhase {
        uint256 price; // Price per token in wei
        uint256 maxPerWallet; // Maximum tokens per wallet in this phase
        uint256 startTime;
        uint256 endTime;
    }

    SalePhase[] public salePhases;
    uint256 public currentPhase;
    uint256 public totalTokensForSale;
    uint256 public tokensSold;

    // Tracking
    mapping(address => mapping(uint256 => uint256)) public tokensPurchasedPerPhase;
    mapping(address => uint256) public totalTokensPurchased;

    // Events
    event TokensPurchased(address indexed buyer, uint256 phase, uint256 amount, uint256 cost);
    event PhaseAdded(uint256 phaseId, uint256 price, uint256 maxPerWallet, uint256 startTime, uint256 endTime);
    event PhaseAdvanced(uint256 newPhase);
    event TokensWithdrawn(address indexed owner, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Add a new sale phase
     */
    function addSalePhase(
        uint256 _price,
        uint256 _maxPerWallet,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_startTime < _endTime, "Invalid time range");
        require(_price > 0, "Price must be greater than 0");

        salePhases.push(
            SalePhase({
                price: _price,
                maxPerWallet: _maxPerWallet,
                startTime: _startTime,
                endTime: _endTime
            })
        );

        emit PhaseAdded(salePhases.length - 1, _price, _maxPerWallet, _startTime, _endTime);
    }

    /**
     * @dev Set total tokens available for sale
     */
    function setTotalTokensForSale(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        totalTokensForSale = _amount;
    }

    /**
     * @dev Advance to the next sale phase
     */
    function advancePhase() external onlyOwner {
        require(currentPhase < salePhases.length - 1, "No more phases");
        currentPhase++;
        emit PhaseAdvanced(currentPhase);
    }

    /**
     * @dev Purchase tokens in the current phase
     */
    function purchaseTokens(uint256 _amount) external payable nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(block.timestamp >= salePhases[currentPhase].startTime, "Sale not started");
        require(block.timestamp <= salePhases[currentPhase].endTime, "Sale ended");
        require(tokensSold + _amount <= totalTokensForSale, "Not enough tokens left");

        uint256 cost = _amount * salePhases[currentPhase].price;
        require(msg.value >= cost, "Insufficient funds");

        uint256 alreadyPurchased = tokensPurchasedPerPhase[msg.sender][currentPhase];
        require(
            alreadyPurchased + _amount <= salePhases[currentPhase].maxPerWallet,
            "Exceeds wallet limit for this phase"
        );

        tokensPurchasedPerPhase[msg.sender][currentPhase] += _amount;
        totalTokensPurchased[msg.sender] += _amount;
        tokensSold += _amount;

        // Transfer tokens to buyer
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        // Refund excess ETH
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }

        emit TokensPurchased(msg.sender, currentPhase, _amount, cost);
    }

    /**
     * @dev Withdraw unsold tokens after sale ends
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > salePhases[salePhases.length - 1].endTime, "Sale not ended");
        uint256 remaining = totalTokensForSale - tokensSold;
        require(remaining > 0, "No tokens left to withdraw");
        require(token.transfer(owner(), remaining), "Token transfer failed");
        emit TokensWithdrawn(owner(), remaining);
    }

    /**
     * @dev Withdraw collected ETH
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
        emit FundsWithdrawn(owner(), balance);
    }

    /**
     * @dev Get current phase details
     */
    function getCurrentPhase() external view returns (SalePhase memory) {
        return salePhases[currentPhase];
    }

    /**
     * @dev Get number of phases
     */
    function getPhaseCount() external view returns (uint256) {
        return salePhases.length;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     */
    function recoverERC20(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(token), "Cannot withdraw sale token");
        IERC20(_tokenAddress).transfer(owner(), _amount);
    }
}
```
