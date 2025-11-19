"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-io.web.app
Prompt: Generate a smart contract in Solidity for a BEP20 token with a total supply of 100,000,000 tokens, 70% for presale, 15% for treasury, development and marketing, 10% for liquidity, and 5% for the team, similar to $GIGA.
Generated: DETERMINISTIC_c68806daf95e7889
Batch ID: 20250622_210008
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

contract GIGAToken is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18;
    uint256 public constant PRESALE_ALLOCATION = 70_000_000 * 10**18; // 70%
    uint256 public constant TREASURY_ALLOCATION = 15_000_000 * 10**18; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 10_000_000 * 10**18; // 10%
    uint256 public constant TEAM_ALLOCATION = 5_000_000 * 10**18; // 5%

    address public presaleAddress;
    address public treasuryAddress;
    address public liquidityAddress;
    address public teamAddress;

    constructor(
        address _presaleAddress,
        address _treasuryAddress,
        address _liquidityAddress,
        address _teamAddress
    ) ERC20("GIGA Token", "GIGA") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_treasuryAddress != address(0), "Treasury address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");

        presaleAddress = _presaleAddress;
        treasuryAddress = _treasuryAddress;
        liquidityAddress = _liquidityAddress;
        teamAddress = _teamAddress;

        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(treasuryAddress, TREASURY_ALLOCATION);
        _mint(liquidityAddress, LIQUIDITY_ALLOCATION);
        _mint(teamAddress, TEAM_ALLOCATION);
    }

    function updatePresaleAddress(address _newPresaleAddress) external onlyOwner {
        require(_newPresaleAddress != address(0), "New presale address cannot be zero");
        presaleAddress = _newPresaleAddress;
    }

    function updateTreasuryAddress(address _newTreasuryAddress) external onlyOwner {
        require(_newTreasuryAddress != address(0), "New treasury address cannot be zero");
        treasuryAddress = _newTreasuryAddress;
    }

    function updateLiquidityAddress(address _newLiquidityAddress) external onlyOwner {
        require(_newLiquidityAddress != address(0), "New liquidity address cannot be zero");
        liquidityAddress = _newLiquidityAddress;
    }

    function updateTeamAddress(address _newTeamAddress) external onlyOwner {
        require(_newTeamAddress != address(0), "New team address cannot be zero");
        teamAddress = _newTeamAddress;
    }
}
```
