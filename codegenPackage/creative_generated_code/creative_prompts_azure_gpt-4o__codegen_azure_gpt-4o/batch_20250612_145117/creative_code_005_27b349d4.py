"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrollswap.finance
Prompt: Write a smart contract example for enabling token swaps on a platform like ScrollSwap Finance.
Generated: DETERMINISTIC_27b349d46c85a756
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TokenSwap
 * @dev This smart contract allows users to swap tokens between two ERC20 token types.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TokenSwap {
    // Address of the first token
    address public tokenA;
    // Address of the second token
    address public tokenB;

    // Exchange rate (e.g., 1 tokenA = rate tokenB)
    uint256 public rate;

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes token addresses and rate.
     * @param _tokenA Address of the first token (ERC20).
     * @param _tokenB Address of the second token (ERC20).
     * @param _rate Exchange rate (number of tokenB per tokenA).
     */
    constructor(address _tokenA, address _tokenB, uint256 _rate) {
        require(_tokenA != address(0) && _tokenB != address(0), "Invalid token addresses");
        require(_rate > 0, "Rate must be greater than zero");
        tokenA = _tokenA;
        tokenB = _tokenB;
        rate = _rate;
        owner = msg.sender;
    }

    /**
     * @dev Updates the exchange rate.
     * @param _rate New exchange rate.
     */
    function updateRate(uint256 _rate) external onlyOwner {
        require(_rate > 0, "Rate must be greater than zero");
        rate = _rate;
    }

    /**
     * @dev Allows users to swap TokenA for TokenB.
     * @param _amount Amount of TokenA to swap.
     */
    function swapTokenAForTokenB(uint256 _amount) external {
        require(_amount > 0, "Swap amount must be greater than zero");
        
        // Calculate the equivalent amount of TokenB
        uint256 amountB = _amount * rate;

        // Ensure the contract has sufficient TokenB balance to complete the swap
        require(IERC20(tokenB).balanceOf(address(this)) >= amountB, "Insufficient TokenB liquidity");

        // Transfer TokenA from the user to the contract
        bool successA = IERC20(tokenA).transferFrom(msg.sender, address(this), _amount);
        require(successA, "TokenA transfer failed");

        // Transfer TokenB from the contract to the user
        bool successB = IERC20(tokenB).transfer(msg.sender, amountB);
        require(successB, "TokenB transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Withdrawal amount must be greater than zero");

        bool success = IERC20(_token).transfer(owner, _amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
