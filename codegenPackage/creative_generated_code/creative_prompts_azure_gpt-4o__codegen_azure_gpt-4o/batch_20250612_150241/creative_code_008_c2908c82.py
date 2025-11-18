"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-en.web.app
Prompt: Write a Solidity contract to enable instant token swaps between $PEPU and other cryptocurrencies on Pepe Unchained Layer 2.
Generated: DETERMINISTIC_c2908c829d38663e
Batch ID: 20250612_150241
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
 * @title InstantTokenSwap
 * @dev This contract enables instant token swaps between $PEPU and other ERC20 tokens on Pepe Unchained Layer 2.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract InstantTokenSwap {
    address public owner;
    address public pepuToken; // Address of $PEPU token
    uint256 public swapRate; // Swap rate in terms of $PEPU tokens per other token

    event SwapExecuted(address indexed user, address indexed token, uint256 tokenAmount, uint256 pepuAmount);
    event SwapRateUpdated(uint256 oldRate, uint256 newRate);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the contract owner");
        _;
    }

    constructor(address _pepuToken, uint256 _initialRate) {
        require(_pepuToken != address(0), "Invalid $PEPU token address");
        require(_initialRate > 0, "Swap rate must be greater than zero");

        owner = msg.sender;
        pepuToken = _pepuToken;
        swapRate = _initialRate;
    }

    /**
     * @dev Update the token swap rate.
     * @param _newRate The new swap rate for $PEPU tokens per other token.
     */
    function updateSwapRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Swap rate must be greater than zero");
        uint256 oldRate = swapRate;
        swapRate = _newRate;

        emit SwapRateUpdated(oldRate, _newRate);
    }

    /**
     * @dev Execute a swap for tokens to $PEPU.
     * @param tokenAddress The address of the ERC20 token being swapped.
     * @param tokenAmount The amount of tokens being swapped.
     */
    function swap(address tokenAddress, uint256 tokenAmount) external {
        require(tokenAddress != address(0), "Token address is invalid");
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Calculate equivalent $PEPU tokens based on swap rate
        uint256 pepuAmount = tokenAmount * swapRate;

        // Ensure user has enough $PEPU tokens in the contract for the swap
        uint256 contractBalance = IERC20(pepuToken).balanceOf(address(this));
        require(pepuAmount <= contractBalance, "Insufficient $PEPU tokens in contract");

        // Transfer the ERC20 tokens from the user to the contract
        require(
            IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmount),
            "Token transfer failed"
        );

        // Transfer equivalent $PEPU tokens from the contract to the user
        require(
            IERC20(pepuToken).transfer(msg.sender, pepuAmount),
            "$PEPU token transfer failed"
        );

        emit SwapExecuted(msg.sender, tokenAddress, tokenAmount, pepuAmount);
    }

    /**
     * @dev Withdraw tokens from the contract. Only callable by the owner.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        require(
            IERC20(tokenAddress).transfer(owner, amount),
            "Token withdrawal failed"
        );
    }

    /**
     * @dev Transfer ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is invalid");
        address oldOwner = owner;
        owner = newOwner;

        emit OwnershipTransferred(oldOwner, newOwner);
    }
}
```
