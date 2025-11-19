"""
Generated Code Metadata:
========================
Original URL: https://flokidongerapp.com
Prompt: Generate a Solidity-based token sale contract for FLOKIDONGER with parameters like presale price (0.0006 USD), launch price (0.0015 USD), and maximum entries (50 billion tokens).
Generated: DETERMINISTIC_aea77dfb4bdd0ea7
Batch ID: 20250612_145423
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract FlokiDongerToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token sale parameters
    uint256 public constant PRESALE_PRICE = 0.0006 ether; // 0.0006 USD (assuming 1 ETH = 1 USD for simplicity)
    uint256 public constant LAUNCH_PRICE = 0.0015 ether; // 0.0015 USD
    uint256 public constant MAX_TOKENS = 50_000_000_000 * 10**18; // 50 billion tokens
    uint256 public constant PRESALE_MAX_PER_WALLET = 1_000_000 * 10**18; // 1 million tokens max per wallet in presale

    // Sale phases
    enum SalePhase { INACTIVE, PRESALE, LAUNCH }
    SalePhase public currentPhase = SalePhase.INACTIVE;

    // Tracking
    uint256 public totalSold;
    mapping(address => uint256) public presalePurchases;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event SalePhaseChanged(SalePhase newPhase);

    constructor() ERC20("FlokiDonger", "FLOKIDONGER") {
        _mint(msg.sender, MAX_TOKENS.mul(20).div(100)); // 20% for team/development
    }

    // Modifiers
    modifier isActive() {
        require(currentPhase != SalePhase.INACTIVE, "Sale is not active");
        _;
    }

    // Token sale functions
    function buyTokens() external payable isActive nonReentrant {
        uint256 tokenAmount;
        uint256 cost;

        if (currentPhase == SalePhase.PRESALE) {
            (tokenAmount, cost) = _calculatePresalePurchase(msg.value);
            presalePurchases[msg.sender] = presalePurchases[msg.sender].add(tokenAmount);
        } else {
            (tokenAmount, cost) = _calculateLaunchPurchase(msg.value);
        }

        require(totalSold.add(tokenAmount) <= MAX_TOKENS, "Exceeds maximum token supply");
        require(tokenAmount > 0, "Invalid token amount");

        totalSold = totalSold.add(tokenAmount);
        _transfer(owner(), msg.sender, tokenAmount);

        // Refund excess ETH
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value.sub(cost));
        }

        emit TokensPurchased(msg.sender, tokenAmount, cost);
    }

    function _calculatePresalePurchase(uint256 ethAmount) private view returns (uint256, uint256) {
        uint256 maxPurchase = PRESALE_MAX_PER_WALLET.sub(presalePurchases[msg.sender]);
        uint256 tokenAmount = ethAmount.mul(10**18).div(PRESALE_PRICE);
        
        if (tokenAmount > maxPurchase) {
            tokenAmount = maxPurchase;
        }

        uint256 cost = tokenAmount.mul(PRESALE_PRICE).div(10**18);
        return (tokenAmount, cost);
    }

    function _calculateLaunchPurchase(uint256 ethAmount) private view returns (uint256, uint256) {
        uint256 tokenAmount = ethAmount.mul(10**18).div(LAUNCH_PRICE);
        uint256 cost = tokenAmount.mul(LAUNCH_PRICE).div(10**18);
        return (tokenAmount, cost);
    }

    // Admin functions
    function setSalePhase(SalePhase _phase) external onlyOwner {
        currentPhase = _phase;
        emit SalePhaseChanged(_phase);
    }

    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Emergency functions
    function emergencyWithdrawTokens(address _token) external onlyOwner {
        IERC20 token = IERC20(_token);
        token.transfer(owner(), token.balanceOf(address(this)));
    }
}
```
