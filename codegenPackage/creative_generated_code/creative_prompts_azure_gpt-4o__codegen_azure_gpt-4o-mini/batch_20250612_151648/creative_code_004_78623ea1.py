"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogclaim.pages.dev
Prompt: Write a script in Solidity to implement a fixed token supply of 111,111,111,111 $FROP tokens, with allocations for presale, staking, marketing, rewards, and liquidity as outlined in the tokenomics section of the Popo The Frog webpage.
Generated: DETERMINISTIC_78623ea128dd13bc
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the OpenZeppelin ERC20 contract for standard functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the FROP token contract
contract FROPToken is ERC20, Ownable {
    // Total supply constant
    uint256 public constant TOTAL_SUPPLY = 111111111111 * 10 ** 18; // 111,111,111,111 tokens with 18 decimals

    // Allocation percentages (assuming these are the percentages given in tokenomics)
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 30) / 100; // 30%
    uint256 public constant STAKING_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20%
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15%
    uint256 public constant REWARDS_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10%

    // Address for various allocations
    address public presaleWallet;
    address public stakingWallet;
    address public marketingWallet;
    address public rewardsWallet;
    address public liquidityWallet;

    // Events for tracking allocations
    event TokensAllocated(string allocationType, address wallet, uint256 amount);

    // Constructor to set the token name, symbol, and allocate tokens
    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _liquidityWallet
    ) ERC20("FROP Token", "FROP") {
        // Set allocation wallets
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens to specified wallets
        allocateTokens();
    }

    // Function to allocate tokens according to the tokenomics
    function allocateTokens() internal {
        require(presaleWallet != address(0), "Presale wallet address is invalid");
        require(stakingWallet != address(0), "Staking wallet address is invalid");
        require(marketingWallet != address(0), "Marketing wallet address is invalid");
        require(rewardsWallet != address(0), "Rewards wallet address is invalid");
        require(liquidityWallet != address(0), "Liquidity wallet address is invalid");

        _transfer(msg.sender, presaleWallet, PRESALE_ALLOCATION);
        emit TokensAllocated("Presale", presaleWallet, PRESALE_ALLOCATION);

        _transfer(msg.sender, stakingWallet, STAKING_ALLOCATION);
        emit TokensAllocated("Staking", stakingWallet, STAKING_ALLOCATION);

        _transfer(msg.sender, marketingWallet, MARKETING_ALLOCATION);
        emit TokensAllocated("Marketing", marketingWallet, MARKETING_ALLOCATION);

        _transfer(msg.sender, rewardsWallet, REWARDS_ALLOCATION);
        emit TokensAllocated("Rewards", rewardsWallet, REWARDS_ALLOCATION);

        _transfer(msg.sender, liquidityWallet, LIQUIDITY_ALLOCATION);
        emit TokensAllocated("Liquidity", liquidityWallet, LIQUIDITY_ALLOCATION);
    }
}
```
