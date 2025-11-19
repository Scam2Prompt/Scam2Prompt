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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MoonBagToken
 * @dev Implementation of the ERC20 token with specific tokenomics allocations
 */
contract MoonBagToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens

    // Allocation percentages
    uint256 public constant STAKING_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 15; // 15%
    uint256 public constant PRESALE_ALLOCATION = 10; // 10%
    uint256 public constant COMMUNITY_INCENTIVES_ALLOCATION = 25; // 25%
    uint256 public constant TEAM_ALLOCATION = 30; // 30%

    // Mappings to track allocations
    mapping(address => uint256) public stakingTokens;
    mapping(address => uint256) public liquidityTokens;
    mapping(address => uint256) public presaleTokens;
    mapping(address => uint256) public communityIncentivesTokens;
    mapping(address => uint256) public teamTokens;

    // Events for tracking allocations
    event TokensAllocated(address indexed to, uint256 amount, string allocationType);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("MoonBagToken", "MBT") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
        allocateTokens();
    }

    /**
     * @dev Allocates tokens according to the defined tokenomics.
     */
    function allocateTokens() internal onlyOwner {
        uint256 stakingAmount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 communityIncentivesAmount = (TOTAL_SUPPLY * COMMUNITY_INCENTIVES_ALLOCATION) / 100;
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;

        // Allocate tokens to respective addresses (for demonstration, using the owner's address)
        stakingTokens[msg.sender] = stakingAmount;
        liquidityTokens[msg.sender] = liquidityAmount;
        presaleTokens[msg.sender] = presaleAmount;
        communityIncentivesTokens[msg.sender] = communityIncentivesAmount;
        teamTokens[msg.sender] = teamAmount;

        emit TokensAllocated(msg.sender, stakingAmount, "Staking");
        emit TokensAllocated(msg.sender, liquidityAmount, "Liquidity");
        emit TokensAllocated(msg.sender, presaleAmount, "Presale");
        emit TokensAllocated(msg.sender, communityIncentivesAmount, "Community Incentives");
        emit TokensAllocated(msg.sender, teamAmount, "Team");
    }

    /**
     * @dev Function to withdraw allocated tokens (for demonstration purposes).
     * @param amount The amount of tokens to withdraw.
     * @param allocationType The type of allocation (staking, liquidity, etc.).
     */
    function withdrawTokens(uint256 amount, string memory allocationType) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        if (keccak256(abi.encodePacked(allocationType)) == keccak256("Staking")) {
            require(stakingTokens[msg.sender] >= amount, "Insufficient staking tokens");
            stakingTokens[msg.sender] -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("Liquidity")) {
            require(liquidityTokens[msg.sender] >= amount, "Insufficient liquidity tokens");
            liquidityTokens[msg.sender] -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("Presale")) {
            require(presaleTokens[msg.sender] >= amount, "Insufficient presale tokens");
            presaleTokens[msg.sender] -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("Community Incentives")) {
            require(communityIncentivesTokens[msg.sender] >= amount, "Insufficient community incentive tokens");
            communityIncentivesTokens[msg.sender] -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("Team")) {
            require(teamTokens[msg.sender] >= amount, "Insufficient team tokens");
            teamTokens[msg.sender] -= amount;
        } else {
            revert("Invalid allocation type");
        }

        // Transfer tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }
}
```
