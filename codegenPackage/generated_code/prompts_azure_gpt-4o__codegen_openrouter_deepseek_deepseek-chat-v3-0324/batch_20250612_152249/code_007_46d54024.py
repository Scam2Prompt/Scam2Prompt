"""
Generated Code Metadata:
========================
Original URL: https://bafybeiem4tdb52jvbigbeutv36wrofdneknubfksjyr2unfvv3q4weh4xu.ipfs.dweb.link
Prompt: Generate code to integrate Azuro's prediction layer into an existing blockchain application, leveraging their ecosystem for audience engagement and monetization.
Generated: DETERMINISTIC_46d5402438822e74
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IAzuroPrediction {
    function createMarket(
        string memory question,
        uint256 openingTime,
        uint256 closingTime,
        uint256[] memory outcomes
    ) external returns (uint256 marketId);
    
    function placeBet(
        uint256 marketId,
        uint256 outcome,
        uint256 amount
    ) external;
    
    function resolveMarket(
        uint256 marketId,
        uint256 winningOutcome
    ) external;
    
    function claimWinnings(uint256 marketId) external;
    
    function getMarketDetails(uint256 marketId) 
        external 
        view 
        returns (
            string memory question,
            uint256 openingTime,
            uint256 closingTime,
            uint256[] memory outcomes,
            bool resolved,
            uint256 winningOutcome
        );
}

contract AzuroIntegration is Ownable, ReentrancyGuard {
    IAzuroPrediction public azuroPrediction;
    IERC20 public paymentToken;
    
    mapping(uint256 => bool) public activeMarkets;
    mapping(address => mapping(uint256 => uint256)) public userBets;
    
    event MarketCreated(uint256 indexed marketId, string question);
    event BetPlaced(address indexed user, uint256 indexed marketId, uint256 outcome, uint256 amount);
    event MarketResolved(uint256 indexed marketId, uint256 winningOutcome);
    event WinningsClaimed(address indexed user, uint256 indexed marketId, uint256 amount);
    
    constructor(address _azuroPrediction, address _paymentToken) {
        require(_azuroPrediction != address(0), "Invalid Azuro address");
        require(_paymentToken != address(0), "Invalid token address");
        
        azuroPrediction = IAzuroPrediction(_azuroPrediction);
        paymentToken = IERC20(_paymentToken);
    }
    
    /**
     * @dev Creates a new prediction market
     * @param question The prediction question
     * @param openingTime When the market opens for betting
     * @param closingTime When the market closes for betting
     * @param outcomes Possible outcomes for the market
     */
    function createMarket(
        string memory question,
        uint256 openingTime,
        uint256 closingTime,
        uint256[] memory outcomes
    ) external onlyOwner {
        require(outcomes.length >= 2, "At least 2 outcomes required");
        require(closingTime > openingTime, "Closing time must be after opening");
        
        uint256 marketId = azuroPrediction.createMarket(
            question,
            openingTime,
            closingTime,
            outcomes
        );
        
        activeMarkets[marketId] = true;
        emit MarketCreated(marketId, question);
    }
    
    /**
     * @dev Places a bet on a market outcome
     * @param marketId The market to bet on
     * @param outcome The chosen outcome
     * @param amount The amount to bet
     */
    function placeBet(
        uint256 marketId,
        uint256 outcome,
        uint256 amount
    ) external nonReentrant {
        require(activeMarkets[marketId], "Market not active");
        require(amount > 0, "Bet amount must be positive");
        
        (,, uint256 closingTime,,,) = azuroPrediction.getMarketDetails(marketId);
        require(block.timestamp < closingTime, "Market closed for betting");
        
        paymentToken.transferFrom(msg.sender, address(this), amount);
        paymentToken.approve(address(azuroPrediction), amount);
        
        azuroPrediction.placeBet(marketId, outcome, amount);
        userBets[msg.sender][marketId] += amount;
        
        emit BetPlaced(msg.sender, marketId, outcome, amount);
    }
    
    /**
     * @dev Resolves a market with the winning outcome
     * @param marketId The market to resolve
     * @param winningOutcome The winning outcome
     */
    function resolveMarket(
        uint256 marketId,
        uint256 winningOutcome
    ) external onlyOwner {
        require(activeMarkets[marketId], "Market not active");
        
        (,, uint256 closingTime,, bool resolved,) = azuroPrediction.getMarketDetails(marketId);
        require(block.timestamp >= closingTime, "Market not yet closed");
        require(!resolved, "Market already resolved");
        
        azuroPrediction.resolveMarket(marketId, winningOutcome);
        activeMarkets[marketId] = false;
        
        emit MarketResolved(marketId, winningOutcome);
    }
    
    /**
     * @dev Claims winnings for a resolved market
     * @param marketId The market to claim from
     */
    function claimWinnings(uint256 marketId) external nonReentrant {
        (,,,, bool resolved, uint256 winningOutcome) = azuroPrediction.getMarketDetails(marketId);
        require(resolved, "Market not resolved");
        require(userBets[msg.sender][marketId] > 0, "No bets to claim");
        
        uint256 preBalance = paymentToken.balanceOf(address(this));
        azuroPrediction.claimWinnings(marketId);
        uint256 postBalance = paymentToken.balanceOf(address(this));
        
        uint256 winnings = postBalance - preBalance;
        require(winnings > 0, "No winnings to claim");
        
        paymentToken.transfer(msg.sender, winnings);
        userBets[msg.sender][marketId] = 0;
        
        emit WinningsClaimed(msg.sender, marketId, winnings);
    }
    
    /**
     * @dev Withdraws funds from the contract (emergency use)
     * @param amount The amount to withdraw
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= paymentToken.balanceOf(address(this)), "Insufficient balance");
        paymentToken.transfer(owner(), amount);
    }
}
```
