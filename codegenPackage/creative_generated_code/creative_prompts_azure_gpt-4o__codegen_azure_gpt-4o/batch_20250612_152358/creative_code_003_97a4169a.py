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
pragma solidity ^0.8.0;

// Import required libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LiquidityProvider is Ownable, ReentrancyGuard {
    // Struct to define whitelisted token pairs
    struct TokenPair {
        address tokenA;
        address tokenB;
        bool isWhitelisted;
    }

    // Mapping to store whitelisted token pairs
    mapping(bytes32 => TokenPair) private tokenPairs;

    // Event emitted when liquidity is added
    event LiquidityAdded(
        address indexed provider,
        address indexed tokenA,
        address indexed tokenB,
        uint256 amountTokenA,
        uint256 amountTokenB
    );

    // Event emitted when a token pair is whitelisted
    event TokenPairWhitelisted(address tokenA, address tokenB);

    // Modifier to check if a token pair is whitelisted
    modifier isWhitelisted(address tokenA, address tokenB) {
        bytes32 pairHash = keccak256(abi.encodePacked(tokenA, tokenB));
        require(
            tokenPairs[pairHash].isWhitelisted,
            "LiquidityProvider: Token pair not whitelisted"
        );
        _;
    }

    // Function to whitelist a token pair (only owner can call)
    function whitelistTokenPair(address tokenA, address tokenB) external onlyOwner {
        require(tokenA != address(0) && tokenB != address(0), "LiquidityProvider: Invalid token address");
        bytes32 pairHash = keccak256(abi.encodePacked(tokenA, tokenB));
        tokenPairs[pairHash] = TokenPair(tokenA, tokenB, true);
        emit TokenPairWhitelisted(tokenA, tokenB);
    }

    // Function to add liquidity for a whitelisted token pair
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountTokenA,
        uint256 amountTokenB
    ) external nonReentrant isWhitelisted(tokenA, tokenB) {
        require(amountTokenA > 0 && amountTokenB > 0, "LiquidityProvider: Invalid token amount");

        // Transfer tokens from the sender to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountTokenA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountTokenB);

        // Emit the liquidity added event
        emit LiquidityAdded(msg.sender, tokenA, tokenB, amountTokenA, amountTokenB);

        // Note: Compliance with Venom Network rules for XP accrual would require additional integration
        // with the network's XP system. This implementation assumes compliance logic is handled off-chain.
    }

    // Function to withdraw tokens (only owner can call; for emergency use)
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "LiquidityProvider: Invalid amount");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
