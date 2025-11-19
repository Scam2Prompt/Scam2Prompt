"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: How can I implement a presale mechanism for a token with a total supply of 100,000,000 JESSE using a specific cap in a blockchain environment?
Generated: DETERMINISTIC_c62e7eeacc488f92
Batch ID: 20250612_161520
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

contract JesseToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18;
    uint256 public constant PRESALE_CAP = 20_000_000 * 10**18; // 20% of total supply
    uint256 public constant PRESALE_RATE = 1000; // 1 ETH = 1000 JESSE
    uint256 public constant MIN_CONTRIBUTION = 0.1 ether;
    uint256 public constant MAX_CONTRIBUTION = 5 ether;

    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalPresaleContribution;
    uint256 public totalPresaleTokensSold;

    bool public presaleFinalized = false;

    mapping(address => uint256) public contributions;

    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event PresaleFinalized(uint256 totalContribution, uint256 totalTokensSold);

    constructor(uint256 _presaleDurationDays) ERC20("Jesse Token", "JESSE") {
        presaleStartTime = block.timestamp;
        presaleEndTime = presaleStartTime.add(_presaleDurationDays.mul(1 days));
        _mint(address(this), TOTAL_SUPPLY);
    }

    function buyTokens() external payable {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value >= MIN_CONTRIBUTION && msg.value <= MAX_CONTRIBUTION, "Contribution out of bounds");
        require(totalPresaleContribution.add(msg.value) <= PRESALE_CAP, "Presale cap reached");

        uint256 tokens = msg.value.mul(PRESALE_RATE);
        require(totalPresaleTokensSold.add(tokens) <= PRESALE_CAP, "Not enough tokens left");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalPresaleContribution = totalPresaleContribution.add(msg.value);
        totalPresaleTokensSold = totalPresaleTokensSold.add(tokens);

        _transfer(address(this), msg.sender, tokens);
        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || totalPresaleContribution == PRESALE_CAP, "Presale not ended");
        require(!presaleFinalized, "Presale already finalized");

        presaleFinalized = true;
        
        // Transfer remaining tokens to owner
        uint256 remainingTokens = PRESALE_CAP.sub(totalPresaleTokensSold);
        if (remainingTokens > 0) {
            _transfer(address(this), owner(), remainingTokens);
        }

        // Transfer ETH to owner
        payable(owner()).transfer(address(this).balance);
        emit PresaleFinalized(totalPresaleContribution, totalPresaleTokensSold);
    }

    function withdrawContribution() external {
        require(block.timestamp > presaleEndTime && !presaleFinalized, "Cannot withdraw yet");
        require(contributions[msg.sender] > 0, "No contribution to withdraw");

        uint256 amount = contributions[msg.sender];
        contributions[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }

    function extendPresale(uint256 additionalDays) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Presale already ended");
        presaleEndTime = presaleEndTime.add(additionalDays.mul(1 days));
    }
}
```
