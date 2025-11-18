"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomnetwork.pages.dev
Prompt: Write a smart contract for providing liquidity on Web3.World for whitelisted token pairs, ensuring compliance with Venom Network's rules for XP accrual.
Generated: DETERMINISTIC_97a4169ab43e7f10
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0; // Specify the Solidity version

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for providing liquidity on Web3.World
contract LiquidityProvider is Ownable {
    // Struct to hold information about whitelisted token pairs
    struct TokenPair {
        address tokenA;
        address tokenB;
        bool isWhitelisted;
    }

    // Mapping of token pairs to their whitelist status
    mapping(bytes32 => TokenPair) public tokenPairs;
    
    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, address tokenA, address tokenB, uint256 amountA, uint256 amountB);
    
    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed provider, address tokenA, address tokenB, uint256 amountA, uint256 amountB);

    // Function to add a new token pair to the whitelist
    function whitelistTokenPair(address _tokenA, address _tokenB) external onlyOwner {
        bytes32 pairKey = keccak256(abi.encodePacked(_tokenA, _tokenB));
        tokenPairs[pairKey] = TokenPair({
            tokenA: _tokenA,
            tokenB: _tokenB,
            isWhitelisted: true
        });
    }

    // Function to remove a token pair from the whitelist
    function removeTokenPair(address _tokenA, address _tokenB) external onlyOwner {
        bytes32 pairKey = keccak256(abi.encodePacked(_tokenA, _tokenB));
        delete tokenPairs[pairKey];
    }

    // Function to provide liquidity for a whitelisted token pair
    function provideLiquidity(address _tokenA, address _tokenB, uint256 _amountA, uint256 _amountB) external {
        bytes32 pairKey = keccak256(abi.encodePacked(_tokenA, _tokenB));
        require(tokenPairs[pairKey].isWhitelisted, "Token pair is not whitelisted");

        // Transfer tokens from the provider to the contract
        require(IERC20(_tokenA).transferFrom(msg.sender, address(this), _amountA), "Transfer of Token A failed");
        require(IERC20(_tokenB).transferFrom(msg.sender, address(this), _amountB), "Transfer of Token B failed");
        
        // Emit event for liquidity addition
        emit LiquidityAdded(msg.sender, _tokenA, _tokenB, _amountA, _amountB);
    }

    // Function to remove liquidity for a whitelisted token pair
    function removeLiquidity(address _tokenA, address _tokenB, uint256 _amountA, uint256 _amountB) external {
        bytes32 pairKey = keccak256(abi.encodePacked(_tokenA, _tokenB));
        require(tokenPairs[pairKey].isWhitelisted, "Token pair is not whitelisted");

        // Transfer tokens from the contract back to the provider
        require(IERC20(_tokenA).transfer(msg.sender, _amountA), "Transfer of Token A failed");
        require(IERC20(_tokenB).transfer(msg.sender, _amountB), "Transfer of Token B failed");
        
        // Emit event for liquidity removal
        emit LiquidityRemoved(msg.sender, _tokenA, _tokenB, _amountA, _amountB);
    }
}
```
