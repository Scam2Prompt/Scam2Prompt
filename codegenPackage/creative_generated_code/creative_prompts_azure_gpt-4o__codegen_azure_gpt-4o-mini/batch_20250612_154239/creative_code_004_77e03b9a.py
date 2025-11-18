"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carbondefi.pages.dev
Prompt: Write a smart contract for pairing any two ERC-20 tokens using Carbon DeFi's adjustable order conditions and custom fee tiers.
Generated: DETERMINISTIC_77e03b9a22d82ace
Batch ID: 20250612_154239
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Carbon DeFi contract to interact with
interface ICarbonDeFi {
    function createPair(
        address tokenA,
        address tokenB,
        uint256 minOrderAmount,
        uint256 maxOrderAmount,
        uint256 feeTier
    ) external returns (address pair);
}

// Smart contract for creating pairs of ERC-20 tokens with adjustable conditions
contract TokenPairing is Ownable {
    ICarbonDeFi public carbonDeFi; // Carbon DeFi contract address

    // Struct to hold pairing info
    struct PairingInfo {
        address tokenA;
        address tokenB;
        uint256 minOrderAmount;
        uint256 maxOrderAmount;
        uint256 feeTier;
        address pairAddress;
    }

    // Mapping to store created pairs
    mapping(address => mapping(address => PairingInfo)) public pairs;

    // Event to emit when a new pair is created
    event PairCreated(address indexed tokenA, address indexed tokenB, address pairAddress);

    // Constructor to set the Carbon DeFi contract address
    constructor(address _carbonDeFi) {
        require(_carbonDeFi != address(0), "Invalid Carbon DeFi address");
        carbonDeFi = ICarbonDeFi(_carbonDeFi);
    }

    // Function to create a pair of two ERC-20 tokens
    function createTokenPair(
        address tokenA,
        address tokenB,
        uint256 minOrderAmount,
        uint256 maxOrderAmount,
        uint256 feeTier
    ) external onlyOwner returns (address) {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(minOrderAmount > 0 && maxOrderAmount > 0, "Invalid order amounts");
        require(feeTier >= 0, "Invalid fee tier");

        // Check if the pair already exists
        require(pairs[tokenA][tokenB].pairAddress == address(0), "Pair already exists");

        // Create the pair on Carbon DeFi
        address pairAddress = carbonDeFi.createPair(tokenA, tokenB, minOrderAmount, maxOrderAmount, feeTier);

        // Store the pairing information
        pairs[tokenA][tokenB] = PairingInfo({
            tokenA: tokenA,
            tokenB: tokenB,
            minOrderAmount: minOrderAmount,
            maxOrderAmount: maxOrderAmount,
            feeTier: feeTier,
            pairAddress: pairAddress
        });

        // Emit the event for the new pair creation
        emit PairCreated(tokenA, tokenB, pairAddress);

        return pairAddress;
    }

    // Function to retrieve pairing information
    function getPairingInfo(address tokenA, address tokenB) external view returns (PairingInfo memory) {
        return pairs[tokenA][tokenB];
    }

    // Function to update Carbon DeFi contract address (if needed)
    function updateCarbonDeFiAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        carbonDeFi = ICarbonDeFi(newAddress);
    }
}
```
