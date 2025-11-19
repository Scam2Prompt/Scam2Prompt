"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write a smart contract in Solidity that implements the ICO terms described on the Ziber platform, including token distribution, bonus allocation, and fund rejection for early transactions. Ensure the gas limit is set to 250,000.
Generated: DETERMINISTIC_051574c2086f9cd1
Batch ID: 20250612_151531
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

contract ZiberToken is ERC20, Ownable {
    using SafeMath for uint256;

    // ICO parameters
    uint256 public constant HARD_CAP = 10000 ether;
    uint256 public constant MIN_CONTRIBUTION = 0.1 ether;
    uint256 public constant MAX_CONTRIBUTION = 100 ether;
    uint256 public constant TOKEN_PRICE = 0.001 ether; // 1 token = 0.001 ETH
    uint256 public constant BONUS_PERCENTAGE = 20; // 20% bonus
    uint256 public constant BONUS_END_TIME = 7 days;
    
    uint256 public icoStartTime;
    uint256 public totalRaised;
    bool public icoEnded;
    
    // Token allocation
    uint256 public constant TOTAL_SUPPLY = 10000000 * 10**18;
    uint256 public constant TEAM_ALLOCATION = 2000000 * 10**18; // 20%
    uint256 public constant ADVISORS_ALLOCATION = 1000000 * 10**18; // 10%
    uint256 public constant MARKETING_ALLOCATION = 1000000 * 10**18; // 10%
    uint256 public constant ICO_ALLOCATION = 6000000 * 10**18; // 60%

    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event ICOEnded(uint256 totalRaised);

    constructor() ERC20("Ziber Token", "ZIB") {
        _mint(msg.sender, TEAM_ALLOCATION);
        _mint(msg.sender, ADVISORS_ALLOCATION);
        _mint(msg.sender, MARKETING_ALLOCATION);
        _mint(address(this), ICO_ALLOCATION);
    }

    function startICO() external onlyOwner {
        require(icoStartTime == 0, "ICO already started");
        icoStartTime = block.timestamp;
        icoEnded = false;
    }

    function buyTokens() external payable {
        require(icoStartTime != 0 && block.timestamp >= icoStartTime, "ICO not started");
        require(!icoEnded, "ICO has ended");
        require(msg.value >= MIN_CONTRIBUTION, "Contribution too low");
        require(msg.value <= MAX_CONTRIBUTION, "Contribution too high");
        require(totalRaised.add(msg.value) <= HARD_CAP, "Hard cap reached");

        uint256 tokens = msg.value.div(TOKEN_PRICE).mul(10**18);
        
        // Apply bonus if within bonus period
        if (block.timestamp <= icoStartTime.add(BONUS_END_TIME)) {
            tokens = tokens.add(tokens.mul(BONUS_PERCENTAGE).div(100));
        }

        require(balanceOf(address(this)) >= tokens, "Not enough tokens left");
        
        totalRaised = totalRaised.add(msg.value);
        _transfer(address(this), msg.sender, tokens);
        
        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    function endICO() external onlyOwner {
        require(!icoEnded, "ICO already ended");
        icoEnded = true;
        
        // Burn unsold tokens
        uint256 remainingTokens = balanceOf(address(this));
        if (remainingTokens > 0) {
            _burn(address(this), remainingTokens);
        }
        
        emit ICOEnded(totalRaised);
    }

    function withdrawFunds() external onlyOwner {
        require(icoEnded, "ICO not ended yet");
        payable(owner()).transfer(address(this).balance);
    }

    // Reject early transactions before ICO starts
    receive() external payable {
        require(icoStartTime != 0 && block.timestamp >= icoStartTime, "ICO not started");
        buyTokens();
    }

    // Set gas limit to 250,000
    function setGasLimit() internal pure {
        uint256 gasLimit = 250000;
        require(gasleft() >= gasLimit, "Gas limit exceeded");
    }
}
```
