"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocols.web.app
Prompt: Generate a Solidity contract to manage tokenomics for CRUDO, including allocations for presale, rewards, marketing, and liquidity.
Generated: DETERMINISTIC_8e2a214953bc2a9c
Batch ID: 20250612_150435
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CRUDO Token contract
contract CRUDO is ERC20, Ownable {
    // Allocation percentages (in basis points, 10000 = 100%)
    uint256 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint256 public constant REWARDS_ALLOCATION = 2000; // 20%
    uint256 public constant MARKETING_ALLOCATION = 1500; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 2500; // 25%
    uint256 public constant TEAM_ALLOCATION = 1000; // 10%

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // 1 million tokens

    // Addresses for allocations
    address public presaleAddress;
    address public rewardsAddress;
    address public marketingAddress;
    address public liquidityAddress;
    address public teamAddress;

    // Event emitted when allocations are set
    event AllocationsSet(
        address presale,
        address rewards,
        address marketing,
        address liquidity,
        address team
    );

    // Constructor to initialize the token and allocate initial supply
    constructor(
        address _presaleAddress,
        address _rewardsAddress,
        address _marketingAddress,
        address _liquidityAddress,
        address _teamAddress
    ) ERC20("CRUDO", "CRUDO") {
        // Validate addresses
        require(
            _presaleAddress != address(0) &&
            _rewardsAddress != address(0) &&
            _marketingAddress != address(0) &&
            _liquidityAddress != address(0) &&
            _teamAddress != address(0),
            "Invalid address provided"
        );

        // Set allocation addresses
        presaleAddress = _presaleAddress;
        rewardsAddress = _rewardsAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
        teamAddress = _teamAddress;

        // Mint tokens to respective addresses based on allocations
        _mint(presaleAddress, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000);
        _mint(rewardsAddress, (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 10000);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000);
        _mint(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000);
        _mint(teamAddress, (TOTAL_SUPPLY * TEAM_ALLOCATION) / 10000);

        emit AllocationsSet(
            presaleAddress,
            rewardsAddress,
            marketingAddress,
            liquidityAddress,
            teamAddress
        );
    }

    // Function to update allocation addresses (only owner can call)
    function updateAllocationAddresses(
        address _presaleAddress,
        address _rewardsAddress,
        address _marketingAddress,
        address _liquidityAddress,
        address _teamAddress
    ) external onlyOwner {
        require(
            _presaleAddress != address(0) &&
            _rewardsAddress != address(0) &&
            _marketingAddress != address(0) &&
            _liquidityAddress != address(0) &&
            _teamAddress != address(0),
            "Invalid address provided"
        );

        // Update addresses
        presaleAddress = _presaleAddress;
        rewardsAddress = _rewardsAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
        teamAddress = _teamAddress;

        emit AllocationsSet(
            presaleAddress,
            rewardsAddress,
            marketingAddress,
            liquidityAddress,
            teamAddress
        );
    }
}
```
