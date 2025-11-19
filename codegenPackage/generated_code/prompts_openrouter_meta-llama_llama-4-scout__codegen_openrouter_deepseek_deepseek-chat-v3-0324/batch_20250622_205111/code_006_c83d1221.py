"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Write a code example for building a parimutuel crypto market using Synthetix Perps and Thales, enabling users to take positions on various markets using sUSD.
Generated: DETERMINISTIC_c83d1221e3e6e567
Batch ID: 20250622_205111
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@synthetixio/perps-market/contracts/interfaces/IPerpsMarket.sol";
import "@thales-protocol/contracts/interfaces/IThalesAMM.sol";

contract ParimutuelCryptoMarket is Ownable {
    IERC20 public sUSD;
    IPerpsMarket public perpsMarket;
    IThalesAMM public thalesAMM;

    struct Market {
        bytes32 marketKey;
        uint256 totalDeposits;
        uint256 totalPositions;
        bool isActive;
    }

    mapping(bytes32 => Market) public markets;
    mapping(address => mapping(bytes32 => uint256)) public userPositions;

    event MarketCreated(bytes32 indexed marketKey);
    event PositionTaken(address indexed user, bytes32 indexed marketKey, uint256 amount);
    event MarketResolved(bytes32 indexed marketKey, uint256 totalPayout);

    constructor(
        address _sUSD,
        address _perpsMarket,
        address _thalesAMM
    ) {
        sUSD = IERC20(_sUSD);
        perpsMarket = IPerpsMarket(_perpsMarket);
        thalesAMM = IThalesAMM(_thalesAMM);
    }

    function createMarket(bytes32 marketKey) external onlyOwner {
        require(!markets[marketKey].isActive, "Market already exists");
        markets[marketKey] = Market({
            marketKey: marketKey,
            totalDeposits: 0,
            totalPositions: 0,
            isActive: true
        });
        emit MarketCreated(marketKey);
    }

    function takePosition(bytes32 marketKey, uint256 amount) external {
        Market storage market = markets[marketKey];
        require(market.isActive, "Market not active");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer sUSD from user to contract
        require(sUSD.transferFrom(msg.sender, address(this), amount), "sUSD transfer failed");

        // Update market and user positions
        market.totalDeposits += amount;
        market.totalPositions += 1;
        userPositions[msg.sender][marketKey] += amount;

        emit PositionTaken(msg.sender, marketKey, amount);
    }

    function resolveMarket(bytes32 marketKey, uint256 winningSide) external onlyOwner {
        Market storage market = markets[marketKey];
        require(market.isActive, "Market not active");
        require(market.totalDeposits > 0, "No positions in market");

        // Calculate total payout (simplified example - actual implementation would use oracle)
        uint256 totalPayout = market.totalDeposits;

        // Distribute payout to winning positions (simplified - would need proper distribution logic)
        // In a real implementation, you would track winning/losing positions separately
        market.isActive = false;

        emit MarketResolved(marketKey, totalPayout);
    }

    function setPerpsMarket(address _perpsMarket) external onlyOwner {
        perpsMarket = IPerpsMarket(_perpsMarket);
    }

    function setThalesAMM(address _thalesAMM) external onlyOwner {
        thalesAMM = IThalesAMM(_thalesAMM);
    }

    function withdrawSUSD(uint256 amount) external onlyOwner {
        require(sUSD.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
