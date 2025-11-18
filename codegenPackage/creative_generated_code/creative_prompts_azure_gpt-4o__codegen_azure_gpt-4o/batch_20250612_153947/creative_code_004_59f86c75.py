"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://faucet.wiki
Prompt: Write a smart contract that facilitates token swaps on the testnet chains supported by Faucet Wiki, ensuring compatibility with wallets like TokenPocket and MetaMask.
Generated: DETERMINISTIC_59f86c7524ef9de5
Batch ID: 20250612_153947
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

/**
 * @title TokenSwap
 * @dev A smart contract to facilitate token swaps on Ethereum testnets.
 * Compatible with wallets like TokenPocket and MetaMask.
 */
contract TokenSwap {
    // Event emitted when a successful swap occurs
    event TokenSwapped(
        address indexed sender,
        address indexed tokenFrom,
        address indexed tokenTo,
        uint256 amount
    );

    // Mapping to store supported tokens for swapping
    mapping(address => bool) public supportedTokens;

    // Owner of the contract
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(address[] memory _supportedTokens) {
        owner = msg.sender;

        // Initialize supported tokens
        for (uint256 i = 0; i < _supportedTokens.length; i++) {
            supportedTokens[_supportedTokens[i]] = true;
        }
    }

    /**
     * @dev Allows the owner to add a new supported token.
     * @param token The address of the token to add.
     */
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
    }

    /**
     * @dev Allows the owner to remove a supported token.
     * @param token The address of the token to remove.
     */
    function removeSupportedToken(address token) external onlyOwner {
        require(supportedTokens[token], "Token is not supported");
        supportedTokens[token] = false;
    }

    /**
     * @dev Facilitates token swaps between supported tokens.
     * @param tokenFrom The address of the token being swapped from.
     * @param tokenTo The address of the token being swapped to.
     * @param amount The amount of tokenFrom being swapped.
     */
    function swapTokens(
        address tokenFrom,
        address tokenTo,
        uint256 amount
    ) external {
        require(tokenFrom != tokenTo, "Cannot swap the same token");
        require(supportedTokens[tokenFrom], "TokenFrom is not supported");
        require(supportedTokens[tokenTo], "TokenTo is not supported");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 fromToken = IERC20(tokenFrom);
        IERC20 toToken = IERC20(tokenTo);

        // Transfer the tokens from the sender to this contract
        require(
            fromToken.transferFrom(msg.sender, address(this), amount),
            "TokenFrom transfer failed"
        );

        // Dummy calculation for exchange rate: 1:1 for simplicity
        // This should be replaced with actual logic for determining exchange rate
        uint256 receivedAmount = amount;

        // Transfer swapped tokens back to the sender
        require(
            toToken.transfer(msg.sender, receivedAmount),
            "TokenTo transfer failed"
        );

        emit TokenSwapped(msg.sender, tokenFrom, tokenTo, amount);
    }

    /**
     * @dev Function to recover ERC20 tokens mistakenly sent to the contract.
     * @param token The address of the token to recover.
     * @param amount The amount of tokens to recover.
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");

        IERC20 recoveringToken = IERC20(token);
        require(
            recoveringToken.transfer(owner, amount),
            "Token recovery failed"
        );
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
