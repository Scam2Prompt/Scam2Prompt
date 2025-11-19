"""
Generated Code Metadata:
========================
Original URL: https://mercury-dusky-pi.vercel.app
Prompt: Design a function in Solidity to interact with a perpetual trading contract on a decentralized exchange, inspired by the "Perpetual Degen and Earn" feature on this platform.
Generated: DETERMINISTIC_a0429e5a5f2a1967
Batch ID: 20250622_211011
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

interface IPerpetualTrading {
    function openPosition(
        address trader,
        address baseToken,
        address quoteToken,
        uint256 amount,
        bool isLong,
        uint256 leverage
    ) external returns (uint256 positionId);
    
    function closePosition(
        uint256 positionId,
        address trader
    ) external returns (uint256 realizedPnl);
    
    function getPosition(uint256 positionId) external view returns (
        address trader,
        address baseToken,
        address quoteToken,
        uint256 amount,
        bool isLong,
        uint256 leverage,
        uint256 entryPrice,
        uint256 currentPrice,
        uint256 margin,
        uint256 fundingRate
    );
}

contract PerpetualDegenAndEarn is Ownable, ReentrancyGuard {
    IPerpetualTrading public perpetualTrading;
    IERC20 public rewardToken;
    
    // Position ID to reward amount mapping
    mapping(uint256 => uint256) public positionRewards;
    
    // Trader address to total rewards mapping
    mapping(address => uint256) public traderRewards;
    
    event PositionOpened(
        address indexed trader,
        uint256 positionId,
        address baseToken,
        address quoteToken,
        uint256 amount,
        bool isLong,
        uint256 leverage,
        uint256 reward
    );
    
    event PositionClosed(
        address indexed trader,
        uint256 positionId,
        uint256 realizedPnl,
        uint256 reward
    );
    
    event RewardClaimed(
        address indexed trader,
        uint256 amount
    );
    
    constructor(address _perpetualTrading, address _rewardToken) {
        require(_perpetualTrading != address(0), "Invalid perpetual trading address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        perpetualTrading = IPerpetualTrading(_perpetualTrading);
        rewardToken = IERC20(_rewardToken);
    }
    
    function openPosition(
        address baseToken,
        address quoteToken,
        uint256 amount,
        bool isLong,
        uint256 leverage,
        uint256 rewardAmount
    ) external nonReentrant {
        require(baseToken != address(0), "Invalid base token");
        require(quoteToken != address(0), "Invalid quote token");
        require(amount > 0, "Amount must be greater than 0");
        require(leverage > 0, "Leverage must be greater than 0");
        
        // Transfer tokens from trader to perpetual contract
        IERC20(baseToken).transferFrom(msg.sender, address(perpetualTrading), amount);
        
        // Open position
        uint256 positionId = perpetualTrading.openPosition(
            msg.sender,
            baseToken,
            quoteToken,
            amount,
            isLong,
            leverage
        );
        
        // Calculate and store reward
        positionRewards[positionId] = rewardAmount;
        
        emit PositionOpened(
            msg.sender,
            positionId,
            baseToken,
            quoteToken,
            amount,
            isLong,
            leverage,
            rewardAmount
        );
    }
    
    function closePosition(uint256 positionId) external nonReentrant {
        require(positionId > 0, "Invalid position ID");
        
        // Get position details
        (address trader, , , , , , , , , ) = perpetualTrading.getPosition(positionId);
        require(trader == msg.sender, "Not position owner");
        
        // Close position
        uint256 realizedPnl = perpetualTrading.closePosition(positionId, msg.sender);
        
        // Distribute reward
        uint256 reward = positionRewards[positionId];
        if (reward > 0) {
            traderRewards[msg.sender] += reward;
            delete positionRewards[positionId];
        }
        
        emit PositionClosed(msg.sender, positionId, realizedPnl, reward);
    }
    
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = traderRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        
        traderRewards[msg.sender] = 0;
        
        // Transfer reward tokens
        require(
            rewardToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );
        
        emit RewardClaimed(msg.sender, rewardAmount);
    }
    
    function setRewardToken(address _rewardToken) external onlyOwner {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
    }
    
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
