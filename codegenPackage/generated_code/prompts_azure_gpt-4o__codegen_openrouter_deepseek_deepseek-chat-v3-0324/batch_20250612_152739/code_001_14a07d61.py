"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Create a smart contract in Solidity that implements a presale mechanism for a cryptocurrency token, ensuring the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_14a07d61a5789210
Batch ID: 20250612_152739
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

contract PresaleToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimals
    uint256 public constant PRESALE_RATE = 1000; // 1 ETH = 1000 tokens
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalPresaleTokensSold;
    bool public presaleFinalized = false;

    mapping(address => uint256) public presaleContributions;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleFinalized(uint256 totalTokensSold);

    constructor(
        string memory name,
        string memory symbol,
        uint256 _presaleStartTime,
        uint256 _presaleDuration
    ) ERC20(name, symbol) {
        require(_presaleStartTime >= block.timestamp, "Presale start time must be in the future");
        require(_presaleDuration > 0, "Presale duration must be greater than 0");

        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleStartTime.add(_presaleDuration);
    }

    function buyTokens() external payable {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value > 0, "ETH amount must be greater than 0");

        uint256 tokenAmount = msg.value.mul(PRESALE_RATE);
        uint256 newTotal = totalPresaleTokensSold.add(tokenAmount);

        require(newTotal <= MAX_SUPPLY, "Exceeds maximum token supply");

        totalPresaleTokensSold = newTotal;
        presaleContributions[msg.sender] = presaleContributions[msg.sender].add(tokenAmount);

        _mint(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || totalPresaleTokensSold == MAX_SUPPLY, "Presale must be ended or max supply reached");
        require(!presaleFinalized, "Presale already finalized");

        presaleFinalized = true;
        emit PresaleFinalized(totalPresaleTokensSold);
    }

    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale must be finalized before withdrawing funds");
        
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    function remainingTokens() public view returns (uint256) {
        return MAX_SUPPLY.sub(totalPresaleTokensSold);
    }

    function isPresaleActive() public view returns (bool) {
        return block.timestamp >= presaleStartTime && 
               block.timestamp <= presaleEndTime && 
               totalPresaleTokensSold < MAX_SUPPLY;
    }
}
```
