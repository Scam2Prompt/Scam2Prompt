"""
Generated Code Metadata:
========================
Original URL: https://starltoken.com
Prompt: Generate code to implement a slot machine game for a cryptocurrency casino, ensuring compatibility with blockchain-based randomness for fair play, as described on the STARL Token site.
Generated: DETERMINISTIC_b33c2d5c1201cb47
Batch ID: 20250612_145455
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

contract SlotMachine is Ownable, ReentrancyGuard {
    IERC20 public starlToken;
    uint256 public houseEdge = 5; // 5% house edge
    uint256 public minBet = 1 ether; // 1 STARL (assuming 18 decimals)
    uint256 public maxBet = 100 ether; // 100 STARL
    
    // Slot symbols and their multipliers (0 = cherry, 1 = lemon, etc.)
    uint8[] public symbols = [0, 1, 2, 3, 4, 5];
    uint256[] public multipliers = [2, 3, 5, 10, 20, 50];
    
    // Chainlink VRF or similar would be used in production
    // For demo purposes, we're using a pseudo-random number
    uint256 private nonce;
    
    event SpinResult(
        address indexed player,
        uint256 betAmount,
        uint8[3] symbols,
        uint256 payout,
        bool win
    );
    
    constructor(address _starlToken) {
        starlToken = IERC20(_starlToken);
    }
    
    function setHouseEdge(uint256 _houseEdge) external onlyOwner {
        require(_houseEdge <= 10, "House edge too high");
        houseEdge = _houseEdge;
    }
    
    function setBetLimits(uint256 _minBet, uint256 _maxBet) external onlyOwner {
        require(_minBet > 0, "Min bet must be > 0");
        require(_maxBet > _minBet, "Max bet must be > min bet");
        minBet = _minBet;
        maxBet = _maxBet;
    }
    
    function spin(uint256 betAmount) external nonReentrant {
        require(betAmount >= minBet && betAmount <= maxBet, "Bet amount out of range");
        require(starlToken.balanceOf(msg.sender) >= betAmount, "Insufficient balance");
        require(starlToken.allowance(msg.sender, address(this)) >= betAmount, "Allowance too low");
        
        // Transfer bet amount from player to contract
        bool success = starlToken.transferFrom(msg.sender, address(this), betAmount);
        require(success, "Token transfer failed");
        
        // Generate random symbols
        uint8[3] memory result;
        for (uint i = 0; i < 3; i++) {
            result[i] = symbols[_random() % symbols.length];
        }
        
        // Calculate payout
        uint256 payout = 0;
        bool isWin = false;
        
        if (result[0] == result[1] && result[1] == result[2]) {
            // All three symbols match
            uint256 multiplier = multipliers[result[0]];
            payout = (betAmount * multiplier * (100 - houseEdge)) / 100;
            isWin = true;
        } else if (result[0] == result[1] || result[1] == result[2] || result[0] == result[2]) {
            // Two symbols match
            payout = (betAmount * 2 * (100 - houseEdge)) / 100;
            isWin = true;
        }
        
        // Transfer winnings if any
        if (isWin) {
            success = starlToken.transfer(msg.sender, payout);
            require(success, "Payout transfer failed");
        }
        
        emit SpinResult(msg.sender, betAmount, result, payout, isWin);
    }
    
    function withdrawTokens(uint256 amount) external onlyOwner {
        uint256 balance = starlToken.balanceOf(address(this));
        require(amount <= balance, "Insufficient contract balance");
        starlToken.transfer(owner(), amount);
    }
    
    // For demo purposes only - in production use Chainlink VRF
    function _random() private returns (uint256) {
        return uint256(keccak256(abi.encodePacked(
            block.timestamp,
            block.difficulty,
            msg.sender,
            nonce++
        )));
    }
}
```
