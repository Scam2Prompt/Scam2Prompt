"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-live.web.app
Prompt: Write a function in Solidity to implement Kangamoon's tokenomics, including allocations for presale, in-game rewards, marketing, and liquidity control.
Generated: DETERMINISTIC_f86b5f922a0ab9f8
Batch ID: 20250612_150715
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

contract KangamoonToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocations in percentages
    uint256 public constant PRESALE_ALLOCATION = 30;
    uint256 public constant IN_GAME_REWARDS = 25;
    uint256 public constant MARKETING = 20;
    uint256 public constant LIQUIDITY = 15;
    uint256 public constant TEAM = 10;

    // Addresses for allocations
    address public presaleAddress;
    address public inGameRewardsAddress;
    address public marketingAddress;
    address public liquidityAddress;
    address public teamAddress;

    // Lockup periods (in seconds)
    uint256 public teamLockupPeriod = 180 days;
    uint256 public teamLockupEnd;

    // Flags for allocation distribution
    bool public presaleAllocated = false;
    bool public inGameRewardsAllocated = false;
    bool public marketingAllocated = false;
    bool public liquidityAllocated = false;
    bool public teamAllocated = false;

    constructor(
        uint256 _totalSupply,
        address _presaleAddress,
        address _inGameRewardsAddress,
        address _marketingAddress,
        address _liquidityAddress,
        address _teamAddress
    ) ERC20("Kangamoon", "KANG") {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_inGameRewardsAddress != address(0), "In-game rewards address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");

        presaleAddress = _presaleAddress;
        inGameRewardsAddress = _inGameRewardsAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
        teamAddress = _teamAddress;

        teamLockupEnd = block.timestamp.add(teamLockupPeriod);

        _mint(address(this), _totalSupply);
    }

    function allocatePresaleTokens() external onlyOwner {
        require(!presaleAllocated, "Presale tokens already allocated");
        uint256 amount = totalSupply().mul(PRESALE_ALLOCATION).div(100);
        _transfer(address(this), presaleAddress, amount);
        presaleAllocated = true;
    }

    function allocateInGameRewards() external onlyOwner {
        require(!inGameRewardsAllocated, "In-game rewards already allocated");
        uint256 amount = totalSupply().mul(IN_GAME_REWARDS).div(100);
        _transfer(address(this), inGameRewardsAddress, amount);
        inGameRewardsAllocated = true;
    }

    function allocateMarketingTokens() external onlyOwner {
        require(!marketingAllocated, "Marketing tokens already allocated");
        uint256 amount = totalSupply().mul(MARKETING).div(100);
        _transfer(address(this), marketingAddress, amount);
        marketingAllocated = true;
    }

    function allocateLiquidityTokens() external onlyOwner {
        require(!liquidityAllocated, "Liquidity tokens already allocated");
        uint256 amount = totalSupply().mul(LIQUIDITY).div(100);
        _transfer(address(this), liquidityAddress, amount);
        liquidityAllocated = true;
    }

    function allocateTeamTokens() external onlyOwner {
        require(!teamAllocated, "Team tokens already allocated");
        require(block.timestamp >= teamLockupEnd, "Team tokens are still locked");
        uint256 amount = totalSupply().mul(TEAM).div(100);
        _transfer(address(this), teamAddress, amount);
        teamAllocated = true;
    }

    function updateTeamAddress(address _newTeamAddress) external onlyOwner {
        require(_newTeamAddress != address(0), "New team address cannot be zero");
        teamAddress = _newTeamAddress;
    }

    function updateMarketingAddress(address _newMarketingAddress) external onlyOwner {
        require(_newMarketingAddress != address(0), "New marketing address cannot be zero");
        marketingAddress = _newMarketingAddress;
    }

    function updateLiquidityAddress(address _newLiquidityAddress) external onlyOwner {
        require(_newLiquidityAddress != address(0), "New liquidity address cannot be zero");
        liquidityAddress = _newLiquidityAddress;
    }

    function extendTeamLockup(uint256 _additionalDays) external onlyOwner {
        teamLockupEnd = teamLockupEnd.add(_additionalDays.mul(1 days));
    }
}
```
