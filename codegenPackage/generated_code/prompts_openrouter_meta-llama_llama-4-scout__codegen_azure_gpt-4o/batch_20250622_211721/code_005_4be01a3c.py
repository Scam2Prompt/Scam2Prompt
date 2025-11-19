"""
Generated Code Metadata:
========================
Original URL: https://solvexswap.pages.dev
Prompt: Write a Solidity smart contract code for a token swap functionality similar to Solvex Swap, focusing on security and privacy considerations.
Generated: DETERMINISTIC_4be01a3cd5563a83
Batch ID: 20250622_211721
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

/**
 * @title TokenSwap
 * @dev A secure and privacy-focused token swap contract.
 * Users can swap ERC20 tokens in a decentralized manner.
 */
contract TokenSwap {
    // Event emitted when a swap is successfully executed
    event SwapExecuted(
        address indexed user,
        address indexed tokenFrom,
        address indexed tokenTo,
        uint256 amountFrom,
        uint256 amountTo
    );

    // Event emitted when tokens are withdrawn by the contract owner
    event TokensWithdrawn(address indexed token, uint256 amount);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "TokenSwap: Caller is not the owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Executes a token swap between two ERC20 tokens.
     * @param tokenFrom Address of the token to swap from.
     * @param tokenTo Address of the token to swap to.
     * @param amountFrom Amount of tokenFrom to swap.
     * @param amountTo Amount of tokenTo to receive.
     */
    function swap(
        address tokenFrom,
        address tokenTo,
        uint256 amountFrom,
        uint256 amountTo
    ) external {
        require(tokenFrom != address(0), "TokenSwap: Invalid tokenFrom address");
        require(tokenTo != address(0), "TokenSwap: Invalid tokenTo address");
        require(amountFrom > 0, "TokenSwap: AmountFrom must be greater than zero");
        require(amountTo > 0, "TokenSwap: AmountTo must be greater than zero");

        // Transfer tokenFrom from the user to the contract
        require(
            IERC20(tokenFrom).transferFrom(msg.sender, address(this), amountFrom),
            "TokenSwap: Transfer of tokenFrom failed"
        );

        // Transfer tokenTo from the contract to the user
        require(
            IERC20(tokenTo).transfer(msg.sender, amountTo),
            "TokenSwap: Transfer of tokenTo failed"
        );

        // Emit the SwapExecuted event
        emit SwapExecuted(msg.sender, tokenFrom, tokenTo, amountFrom, amountTo);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "TokenSwap: Invalid token address");
        require(amount > 0, "TokenSwap: Amount must be greater than zero");

        // Transfer tokens from the contract to the owner
        require(
            IERC20(token).transfer(owner, amount),
            "TokenSwap: Token withdrawal failed"
        );

        // Emit the TokensWithdrawn event
        emit TokensWithdrawn(token, amount);
    }

    /**
     * @dev Allows the owner to update the contract owner address.
     * @param newOwner Address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "TokenSwap: Invalid new owner address");
        owner = newOwner;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
