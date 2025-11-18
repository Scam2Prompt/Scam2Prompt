"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Develop a smart contract for allocating $PEPU tokens according to Pepe Unchained's tokenomics (presale, staking, marketing, liquidity, etc.).
Generated: DETERMINISTIC_44abe63a9925744b
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $PEPU token
contract PepuToken is ERC20, Ownable {
    // Define tokenomics allocation percentages
    uint256 public presaleAllocation = 40; // 40% for presale
    uint256 public stakingAllocation = 30; // 30% for staking
    uint256 public marketingAllocation = 15; // 15% for marketing
    uint256 public liquidityAllocation = 10; // 10% for liquidity
    uint256 public developmentAllocation = 5; // 5% for development

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * (10 ** 18); // 1 million tokens with 18 decimals

    // Allocated balances
    uint256 public presaleTokens;
    uint256 public stakingTokens;
    uint256 public marketingTokens;
    uint256 public liquidityTokens;
    uint256 public developmentTokens;

    // Mapping for allocated addresses
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;
    address public liquidityAddress;
    address public developmentAddress;

    // Events for logging allocations
    event TokensAllocated(address indexed recipient, uint256 amount);

    // Constructor to initialize the token and allocate the total supply
    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress,
        address _liquidityAddress,
        address _developmentAddress
    ) ERC20("Pepu Token", "PEPU") {
        // Set the addresses for allocations
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
        developmentAddress = _developmentAddress;

        // Calculate the allocated tokens based on percentages
        presaleTokens = (TOTAL_SUPPLY * presaleAllocation) / 100;
        stakingTokens = (TOTAL_SUPPLY * stakingAllocation) / 100;
        marketingTokens = (TOTAL_SUPPLY * marketingAllocation) / 100;
        liquidityTokens = (TOTAL_SUPPLY * liquidityAllocation) / 100;
        developmentTokens = (TOTAL_SUPPLY * developmentAllocation) / 100;

        // Mint the total supply and distribute according to allocations
        _mint(presaleAddress, presaleTokens);
        emit TokensAllocated(presaleAddress, presaleTokens);
        
        _mint(stakingAddress, stakingTokens);
        emit TokensAllocated(stakingAddress, stakingTokens);

        _mint(marketingAddress, marketingTokens);
        emit TokensAllocated(marketingAddress, marketingTokens);

        _mint(liquidityAddress, liquidityTokens);
        emit TokensAllocated(liquidityAddress, liquidityTokens);

        _mint(developmentAddress, developmentTokens);
        emit TokensAllocated(developmentAddress, developmentTokens);
    }

    // Function to retrieve the total allocated tokens by address
    function getAllocatedTokens(address _address) external view returns (uint256) {
        require(_address == presaleAddress || 
                _address == stakingAddress || 
                _address == marketingAddress || 
                _address == liquidityAddress || 
                _address == developmentAddress, 
                "Invalid address");

        if (_address == presaleAddress) return presaleTokens;
        else if (_address == stakingAddress) return stakingTokens;
        else if (_address == marketingAddress) return marketingTokens;
        else if (_address == liquidityAddress) return liquidityTokens;
        else if (_address == developmentAddress) return developmentTokens;
        else return 0; // Fallback
    }

    // Function to withdraw tokens in case of emergency (only by owner)
    function emergencyWithdraw(address _to, uint256 _amount) external onlyOwner {
        require(_amount <= balanceOf(address(this)), "Insufficient balance for withdrawal");
        _transfer(address(this), _to, _amount);
    }
}
```
