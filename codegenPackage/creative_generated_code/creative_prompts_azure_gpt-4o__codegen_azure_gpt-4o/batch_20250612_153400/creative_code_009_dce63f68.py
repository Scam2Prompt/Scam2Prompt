"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Write a function in Solidity to implement a "DEX Dog Park" feature where $POODL tokens can interact with other tokens, as described in the tokenomics section of the Poodl Inu website.
Generated: DETERMINISTIC_dce63f68659289a9
Batch ID: 20250612_153400
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
 * @title DEX Dog Park
 * @dev A decentralized exchange feature for interacting with $POODL tokens and other tokens
 */
contract DEXDogPark {
    address public poodlTokenAddress; // Address of the $POODL token contract
    address public owner; // Owner of the contract

    event TokensSwapped(address indexed user, address indexed tokenA, address indexed tokenB, uint256 amountA, uint256 amountB);

    constructor(address _poodlTokenAddress) {
        require(_poodlTokenAddress != address(0), "Invalid token address");
        poodlTokenAddress = _poodlTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to swap $POODL tokens with another ERC20 token
     * @param tokenA Address of the first token (must be $POODL or another token)
     * @param tokenB Address of the second token to swap with
     * @param amountA Amount of tokenA to swap
     * @param amountB Amount of tokenB to receive
     */
    function swapTokens(
        address tokenA,
        address tokenB,
        uint256 amountA,
        uint256 amountB
    ) external {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(tokenA == poodlTokenAddress || tokenB == poodlTokenAddress, "One token must be $POODL");

        // Transfer `amountA` of `tokenA` from the user to this contract
        require(IERC20(tokenA).transferFrom(msg.sender, address(this), amountA), "Token transfer failed");

        // Transfer `amountB` of `tokenB` from this contract to the user
        require(IERC20(tokenB).transfer(msg.sender, amountB), "Token transfer failed");

        emit TokensSwapped(msg.sender, tokenA, tokenB, amountA, amountB);
    }

    /**
     * @dev Function for the contract owner to withdraw tokens from the contract
     * @param tokenAddress Address of the token to withdraw
     * @param recipient Address to send the withdrawn tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(
        address tokenAddress,
        address recipient,
        uint256 amount
    ) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer `amount` of `tokenAddress` to the recipient
        require(IERC20(tokenAddress).transfer(recipient, amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
