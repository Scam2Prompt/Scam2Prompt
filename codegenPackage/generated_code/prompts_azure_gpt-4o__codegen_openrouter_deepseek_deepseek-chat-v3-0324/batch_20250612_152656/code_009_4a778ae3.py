"""
Generated Code Metadata:
========================
Original URL: https://scotty-theai-def.web.app
Prompt: Generate a Solidity contract for presale token distribution, ensuring compliance with Scotty AI's tokenomics structure (e.g., 30% public sale, 70% staking, dev, exchange, marketing).
Generated: DETERMINISTIC_4a778ae3f552826e
Batch ID: 20250612_152656
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

contract ScottyAIPresale is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public presaleSupply;
    uint256 public tokensSold;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    bool public presaleFinalized;

    // Allocation percentages (multiplied by 100 for precision)
    uint256 public constant PUBLIC_SALE_PERCENT = 3000; // 30%
    uint256 public constant STAKING_PERCENT = 3000;    // 30%
    uint256 public constant DEV_PERCENT = 1500;        // 15%
    uint256 public constant EXCHANGE_PERCENT = 1500;   // 15%
    uint256 public constant MARKETING_PERCENT = 1000;  // 10%

    // Allocation addresses
    address public stakingAddress;
    address public devAddress;
    address public exchangeAddress;
    address public marketingAddress;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 value);
    event PresaleFinalized(uint256 timestamp);
    event AllocationDistributed(address indexed recipient, uint256 amount);

    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _presaleSupply,
        uint256 _startTime,
        uint256 _endTime,
        address _stakingAddress,
        address _devAddress,
        address _exchangeAddress,
        address _marketingAddress
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_presaleSupply > 0, "Presale supply must be greater than zero");
        require(_endTime > _startTime, "End time must be after start time");
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_devAddress != address(0), "Dev address cannot be zero");
        require(_exchangeAddress != address(0), "Exchange address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");

        token = IERC20(_tokenAddress);
        tokenPrice = _tokenPrice;
        presaleSupply = _presaleSupply;
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
        stakingAddress = _stakingAddress;
        devAddress = _devAddress;
        exchangeAddress = _exchangeAddress;
        marketingAddress = _marketingAddress;
    }

    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(!presaleFinalized, "Presale is finalized");
        require(msg.value > 0, "ETH amount must be greater than zero");

        uint256 tokenAmount = (msg.value * 1e18) / tokenPrice;
        require(tokensSold + tokenAmount <= presaleSupply, "Not enough tokens left");

        tokensSold += tokenAmount;
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        require(!presaleFinalized, "Presale already finalized");

        presaleFinalized = true;

        uint256 remainingTokens = presaleSupply - tokensSold;
        if (remainingTokens > 0) {
            distributeAllocations(remainingTokens);
        }

        emit PresaleFinalized(block.timestamp);
    }

    function distributeAllocations(uint256 remainingTokens) internal {
        uint256 stakingAmount = (remainingTokens * STAKING_PERCENT) / 10000;
        uint256 devAmount = (remainingTokens * DEV_PERCENT) / 10000;
        uint256 exchangeAmount = (remainingTokens * EXCHANGE_PERCENT) / 10000;
        uint256 marketingAmount = (remainingTokens * MARKETING_PERCENT) / 10000;

        require(token.transfer(stakingAddress, stakingAmount), "Staking transfer failed");
        require(token.transfer(devAddress, devAmount), "Dev transfer failed");
        require(token.transfer(exchangeAddress, exchangeAmount), "Exchange transfer failed");
        require(token.transfer(marketingAddress, marketingAmount), "Marketing transfer failed");

        emit AllocationDistributed(stakingAddress, stakingAmount);
        emit AllocationDistributed(devAddress, devAmount);
        emit AllocationDistributed(exchangeAddress, exchangeAmount);
        emit AllocationDistributed(marketingAddress, marketingAmount);
    }

    function withdrawETH() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        payable(owner()).transfer(address(this).balance);
    }

    function updatePresaleTimes(uint256 _startTime, uint256 _endTime) external onlyOwner {
        require(!presaleFinalized, "Presale already finalized");
        require(_endTime > _startTime, "End time must be after start time");
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
    }

    function updateAllocationAddresses(
        address _stakingAddress,
        address _devAddress,
        address _exchangeAddress,
        address _marketingAddress
    ) external onlyOwner {
        require(!presaleFinalized, "Presale already finalized");
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_devAddress != address(0), "Dev address cannot be zero");
        require(_exchangeAddress != address(0), "Exchange address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");

        stakingAddress = _stakingAddress;
        devAddress = _devAddress;
        exchangeAddress = _exchangeAddress;
        marketingAddress = _marketingAddress;
    }
}
```
