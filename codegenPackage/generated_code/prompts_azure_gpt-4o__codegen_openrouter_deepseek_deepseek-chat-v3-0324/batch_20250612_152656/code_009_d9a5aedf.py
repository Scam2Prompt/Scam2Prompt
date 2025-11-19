"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-d.web.app
Prompt: Create a Solidity contract for DOGE20 tokenomics that allocates 25% of the supply to presale, 25% to marketing, 25% to treasury, 15% to staking rewards, and 10% to liquidity.
Generated: DETERMINISTIC_d9a5aedf77717ae8
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DOGE20 is ERC20, Ownable {
    // Allocation percentages
    uint256 public constant PRESALE_PERCENT = 25;
    uint256 public constant MARKETING_PERCENT = 25;
    uint256 public constant TREASURY_PERCENT = 25;
    uint256 public constant STAKING_PERCENT = 15;
    uint256 public constant LIQUIDITY_PERCENT = 10;

    // Allocation addresses
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingAddress;
    address public liquidityAddress;

    // Total supply: 1 trillion tokens (18 decimals)
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000_000 * 10**18;

    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingAddress,
        address _liquidityAddress
    ) ERC20("DOGE20", "DOGE20") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");
        require(_treasuryAddress != address(0), "Treasury address cannot be zero");
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingAddress = _stakingAddress;
        liquidityAddress = _liquidityAddress;

        // Mint tokens to respective addresses based on allocation percentages
        _mint(presaleAddress, (TOTAL_SUPPLY * PRESALE_PERCENT) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_PERCENT) / 100);
        _mint(treasuryAddress, (TOTAL_SUPPLY * TREASURY_PERCENT) / 100);
        _mint(stakingAddress, (TOTAL_SUPPLY * STAKING_PERCENT) / 100);
        _mint(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_PERCENT) / 100);
    }

    // Function to update allocation addresses (only owner)
    function setPresaleAddress(address _address) external onlyOwner {
        require(_address != address(0), "Address cannot be zero");
        presaleAddress = _address;
    }

    function setMarketingAddress(address _address) external onlyOwner {
        require(_address != address(0), "Address cannot be zero");
        marketingAddress = _address;
    }

    function setTreasuryAddress(address _address) external onlyOwner {
        require(_address != address(0), "Address cannot be zero");
        treasuryAddress = _address;
    }

    function setStakingAddress(address _address) external onlyOwner {
        require(_address != address(0), "Address cannot be zero");
        stakingAddress = _address;
    }

    function setLiquidityAddress(address _address) external onlyOwner {
        require(_address != address(0), "Address cannot be zero");
        liquidityAddress = _address;
    }
}
```
