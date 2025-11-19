"""
Generated Code Metadata:
========================
Original URL: https://claim-jindocoin.pages.dev
Prompt: Develop a smart contract in Solidity for Jindo Coin that includes tokenomics details such as a total supply of 100 trillion tokens and allocation for presale and community.
Generated: DETERMINISTIC_2d420722c4152501
Batch ID: 20250612_152358
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

contract JindoCoin is ERC20, Ownable {
    // Tokenomics constants
    uint256 public constant TOTAL_SUPPLY = 100_000_000_000_000 * 10**18; // 100 trillion tokens
    uint256 public constant PRESALE_ALLOCATION = 30_000_000_000_000 * 10**18; // 30% for presale
    uint256 public constant COMMUNITY_ALLOCATION = 20_000_000_000_000 * 10**18; // 20% for community
    uint256 public constant TEAM_ALLOCATION = 10_000_000_000_000 * 10**18; // 10% for team
    uint256 public constant DEVELOPMENT_ALLOCATION = 10_000_000_000_000 * 10**18; // 10% for development
    uint256 public constant MARKETING_ALLOCATION = 10_000_000_000_000 * 10**18; // 10% for marketing
    uint256 public constant LIQUIDITY_ALLOCATION = 20_000_000_000_000 * 10**18; // 20% for liquidity

    // Allocation addresses
    address public presaleAddress;
    address public communityAddress;
    address public teamAddress;
    address public developmentAddress;
    address public marketingAddress;
    address public liquidityAddress;

    constructor(
        address _presaleAddress,
        address _communityAddress,
        address _teamAddress,
        address _developmentAddress,
        address _marketingAddress,
        address _liquidityAddress
    ) ERC20("Jindo Coin", "JINDO") {
        require(
            _presaleAddress != address(0) &&
            _communityAddress != address(0) &&
            _teamAddress != address(0) &&
            _developmentAddress != address(0) &&
            _marketingAddress != address(0) &&
            _liquidityAddress != address(0),
            "Allocation addresses cannot be zero"
        );

        presaleAddress = _presaleAddress;
        communityAddress = _communityAddress;
        teamAddress = _teamAddress;
        developmentAddress = _developmentAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;

        // Mint tokens to respective addresses
        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(communityAddress, COMMUNITY_ALLOCATION);
        _mint(teamAddress, TEAM_ALLOCATION);
        _mint(developmentAddress, DEVELOPMENT_ALLOCATION);
        _mint(marketingAddress, MARKETING_ALLOCATION);
        _mint(liquidityAddress, LIQUIDITY_ALLOCATION);
    }

    // Function to update allocation addresses (only owner)
    function updateAllocationAddresses(
        address _presaleAddress,
        address _communityAddress,
        address _teamAddress,
        address _developmentAddress,
        address _marketingAddress,
        address _liquidityAddress
    ) external onlyOwner {
        require(
            _presaleAddress != address(0) &&
            _communityAddress != address(0) &&
            _teamAddress != address(0) &&
            _developmentAddress != address(0) &&
            _marketingAddress != address(0) &&
            _liquidityAddress != address(0),
            "Allocation addresses cannot be zero"
        );

        presaleAddress = _presaleAddress;
        communityAddress = _communityAddress;
        teamAddress = _teamAddress;
        developmentAddress = _developmentAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
    }
}
```
