"""
Generated Code Metadata:
========================
Original URL: https://moonbag-claiming.pages.dev
Prompt: Create a function in Solidity to implement tokenomics for an ERC20 token, including allocations for staking, liquidity, presale, community incentives, and team tokens, as outlined in MoonBag's Moonomics.
Generated: DETERMINISTIC_8dbc1eaffcc19c70
Batch ID: 20250612_145625
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MoonBag Tokenomics Implementation
 * @author [Your Name]
 * @notice This contract implements the tokenomics for MoonBag's ERC20 token,
 *          including allocations for staking, liquidity, presale, community incentives, and team tokens.
 */
contract MoonBagTokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of token allocations
    mapping(address => uint256) public allocations;

    // Token allocation percentages
    uint256 public constant STAKING_ALLOCATION = 20;
    uint256 public constant LIQUIDITY_ALLOCATION = 20;
    uint256 public constant PRESALE_ALLOCATION = 15;
    uint256 public constant COMMUNITY_INCENTIVES_ALLOCATION = 20;
    uint256 public constant TEAM_TOKENS_ALLOCATION = 25;

    // Addresses for token allocations
    address public stakingAddress;
    address public liquidityAddress;
    address public presaleAddress;
    address public communityIncentivesAddress;
    address public teamTokensAddress;

    /**
     * @notice Constructor for MoonBagTokenomics
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param totalSupply The total supply of the token
     * @param _stakingAddress Address for staking allocation
     * @param _liquidityAddress Address for liquidity allocation
     * @param _presaleAddress Address for presale allocation
     * @param _communityIncentivesAddress Address for community incentives allocation
     * @param _teamTokensAddress Address for team tokens allocation
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        address _stakingAddress,
        address _liquidityAddress,
        address _presaleAddress,
        address _communityIncentivesAddress,
        address _teamTokensAddress
    ) ERC20(name, symbol) {
        // Validate input addresses
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_communityIncentivesAddress != address(0), "Community incentives address cannot be zero");
        require(_teamTokensAddress != address(0), "Team tokens address cannot be zero");

        // Set allocation addresses
        stakingAddress = _stakingAddress;
        liquidityAddress = _liquidityAddress;
        presaleAddress = _presaleAddress;
        communityIncentivesAddress = _communityIncentivesAddress;
        teamTokensAddress = _teamTokensAddress;

        // Calculate token allocations
        uint256 stakingAllocation = (totalSupply * STAKING_ALLOCATION) / 100;
        uint256 liquidityAllocation = (totalSupply * LIQUIDITY_ALLOCATION) / 100;
        uint256 presaleAllocation = (totalSupply * PRESALE_ALLOCATION) / 100;
        uint256 communityIncentivesAllocation = (totalSupply * COMMUNITY_INCENTIVES_ALLOCATION) / 100;
        uint256 teamTokensAllocation = (totalSupply * TEAM_TOKENS_ALLOCATION) / 100;

        // Mint and allocate tokens
        _mint(stakingAddress, stakingAllocation);
        allocations[stakingAddress] = stakingAllocation;

        _mint(liquidityAddress, liquidityAllocation);
        allocations[liquidityAddress] = liquidityAllocation;

        _mint(presaleAddress, presaleAllocation);
        allocations[presaleAddress] = presaleAllocation;

        _mint(communityIncentivesAddress, communityIncentivesAllocation);
        allocations[communityIncentivesAddress] = communityIncentivesAllocation;

        _mint(teamTokensAddress, teamTokensAllocation);
        allocations[teamTokensAddress] = teamTokensAllocation;
    }

    /**
     * @notice Function to transfer tokens with an additional check for token allocations
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // Check if the sender has a valid allocation
        require(allocations[msg.sender] >= amount, "Insufficient allocation");

        // Update the sender's allocation
        allocations[msg.sender] -= amount;

        // Perform the token transfer
        return super.transfer(to, amount);
    }

    /**
     * @notice Function to transfer tokens from one address to another with an additional check for token allocations
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        // Check if the sender has a valid allocation
        require(allocations[from] >= amount, "Insufficient allocation");

        // Update the sender's allocation
        allocations[from] -= amount;

        // Perform the token transfer
        return super.transferFrom(from, to, amount);
    }
}
```
