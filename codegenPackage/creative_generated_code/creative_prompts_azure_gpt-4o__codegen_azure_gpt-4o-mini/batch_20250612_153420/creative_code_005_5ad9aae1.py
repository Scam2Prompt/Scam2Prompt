"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accept-gummyonsol.pages.dev
Prompt: Develop a Solidity smart contract that mimics the tokenomics structure of $GUMMY, including the specific allocation percentages (e.g., 30% for CEX liquidity, 10% for market makers).
Generated: DETERMINISTIC_5ad9aae1dcf6d494
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's ERC20 implementation for standardized token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GUMMYToken contract inheriting from ERC20 and Ownable
contract GUMMYToken is ERC20, Ownable {
    // Allocation percentages for different purposes
    uint256 public constant CEX_LIQUIDITY_PERCENTAGE = 30;
    uint256 public constant MARKET_MAKERS_PERCENTAGE = 10;
    uint256 public constant TEAM_PERCENTAGE = 15;
    uint256 public constant RESERVE_PERCENTAGE = 15;
    uint256 public constant STAKING_PERCENTAGE = 20;
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // Total supply of the token

    // Event to log token allocation
    event TokensAllocated(string purpose, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("Gummy Token", "GUMMY") {
        // Minting total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocating tokens based on predefined percentages
        allocateTokens();
    }

    // Function to allocate tokens according to the tokenomics structure
    function allocateTokens() internal {
        uint256 ceXLiquidity = (TOTAL_SUPPLY * CEX_LIQUIDITY_PERCENTAGE) / 100;
        uint256 marketMakers = (TOTAL_SUPPLY * MARKET_MAKERS_PERCENTAGE) / 100;
        uint256 team = (TOTAL_SUPPLY * TEAM_PERCENTAGE) / 100;
        uint256 reserve = (TOTAL_SUPPLY * RESERVE_PERCENTAGE) / 100;
        uint256 staking = (TOTAL_SUPPLY * STAKING_PERCENTAGE) / 100;

        // Allocate tokens to respective addresses (assumed addresses for simplicity)
        _transfer(msg.sender, address(0xCEXLiquidityAddress), ceXLiquidity); // Replace with actual address
        emit TokensAllocated("CEX Liquidity", ceXLiquidity);

        _transfer(msg.sender, address(0xMarketMakersAddress), marketMakers); // Replace with actual address
        emit TokensAllocated("Market Makers", marketMakers);

        _transfer(msg.sender, address(0xTeamAddress), team); // Replace with actual address
        emit TokensAllocated("Team", team);

        _transfer(msg.sender, address(0xReserveAddress), reserve); // Replace with actual address
        emit TokensAllocated("Reserve", reserve);

        _transfer(msg.sender, address(0xStakingAddress), staking); // Replace with actual address
        emit TokensAllocated("Staking", staking);
    }

    // Function to withdraw tokens by the owner if needed (for emergency or business purposes)
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient balance in contract");
        _transfer(address(this), to, amount);
    }

    // Function to receive Ether (if payable functionality is needed)
    receive() external payable {}

    // Fallback function
    fallback() external payable {}
}
```
