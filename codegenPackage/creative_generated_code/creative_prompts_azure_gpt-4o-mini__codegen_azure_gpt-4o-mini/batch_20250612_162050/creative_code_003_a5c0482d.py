"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-babyslerf.pages.dev
Prompt: Develop a Solidity contract that mimics the Baby Slerf token distribution model, ensuring it includes features for presale, liquidity, and airdrop allocations.
Generated: DETERMINISTIC_a5c0482db60d29ff
Batch ID: 20250612_162050
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for owner management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BabySlerf is ERC20, Ownable {
    // Events for logging significant actions
    event Presale(address indexed purchaser, uint256 amount);
    event Airdrop(address indexed recipient, uint256 amount);
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Allocation constants
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    uint256 public presaleAllocation;
    uint256 public liquidityAllocation;
    uint256 public airdropAllocation;

    // Mappings for allocations
    mapping(address => uint256) public presaleBalances;
    mapping(address => uint256) public airdropBalances;

    // Constructor to initialize the token's name, symbol, and allocations
    constructor(
        uint256 _presaleAllocation,
        uint256 _liquidityAllocation,
        uint256 _airdropAllocation
    ) ERC20("Baby Slerf", "BSLERF") {
        require(_presaleAllocation + _liquidityAllocation + _airdropAllocation <= TOTAL_SUPPLY, "Total allocation exceeds supply");

        presaleAllocation = _presaleAllocation;
        liquidityAllocation = _liquidityAllocation;
        airdropAllocation = _airdropAllocation;

        // Mint total supply to contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function for presale purchase
    function buyPresale(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(presaleAllocation >= amount, "Not enough presale allocation");

        // Transfer the tokens to the buyer
        presaleBalances[msg.sender] += amount;
        presaleAllocation -= amount;
        _transfer(owner(), msg.sender, amount);
        
        emit Presale(msg.sender, amount);
    }

    // Function to conduct airdrop
    function airdrop(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(airdropAllocation >= amount * recipients.length, "Not enough airdrop allocation");

        for (uint256 i = 0; i < recipients.length; i++) {
            airdropBalances[recipients[i]] += amount;
            airdropAllocation -= amount;
            _transfer(owner(), recipients[i], amount);
            emit Airdrop(recipients[i], amount);
        }
    }

    // Function for adding liquidity (simplified placeholder)
    function addLiquidity(uint256 tokenAmount, uint256 ethAmount) external onlyOwner {
        require(tokenAmount > 0 && ethAmount > 0, "Invalid amounts");
        require(liquidityAllocation >= tokenAmount, "Not enough liquidity allocation");

        // Transfer tokens to the liquidity pool (implementation may vary)
        _transfer(owner(), address(this), tokenAmount);
        liquidityAllocation -= tokenAmount;

        emit LiquidityAdded(tokenAmount, ethAmount);
    }

    // Function to retrieve the total allocated balances for presale, liquidity, and airdrop
    function getAllocations() external view returns (uint256, uint256, uint256) {
        return (presaleAllocation, liquidityAllocation, airdropAllocation);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
