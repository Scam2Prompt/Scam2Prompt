"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitconnect666.vercel.app
Prompt: Create a smart contract for a decentralized exchange that includes features specific to $BITCONNECT token transactions.
Generated: DETERMINISTIC_75604db8d2b65c02
Batch ID: 20250612_163305
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
 * @title Decentralized Exchange Smart Contract for $BITCONNECT Token
 * @dev This contract provides functionality for trading $BITCONNECT tokens
 *      including deposit, withdrawal, and token swaps.
 */
contract BitconnectDEX {
    // Token-specific details
    string public constant TOKEN_NAME = "$BITCONNECT";
    address public immutable bitconnectTokenAddress;

    // Owner of the contract
    address public owner;

    // Mapping to track user balances for $BITCONNECT tokens
    mapping(address => uint256) public userBalances;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    event TokenSwap(address indexed user, uint256 amountIn, uint256 amountOut, address tokenOut);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the $BITCONNECT token address.
     * @param _bitconnectTokenAddress The address of the $BITCONNECT ERC20 token.
     */
    constructor(address _bitconnectTokenAddress) {
        require(_bitconnectTokenAddress != address(0), "Token address cannot be zero");
        bitconnectTokenAddress = _bitconnectTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function for users to deposit $BITCONNECT tokens into the DEX.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer $BITCONNECT tokens from the user to this contract
        IERC20(bitconnectTokenAddress).transferFrom(msg.sender, address(this), amount);

        // Update user balance
        userBalances[msg.sender] += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Function for users to withdraw $BITCONNECT tokens from the DEX.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Transfer $BITCONNECT tokens from the contract to the user
        IERC20(bitconnectTokenAddress).transfer(msg.sender, amount);

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Function to swap $BITCONNECT tokens for another ERC20 token.
     * @param amountIn The amount of $BITCONNECT tokens to swap.
     * @param tokenOut The address of the ERC20 token to receive.
     * @param rate The exchange rate between $BITCONNECT and the tokenOut.
     */
    function swap(uint256 amountIn, address tokenOut, uint256 rate) external {
        require(amountIn > 0, "Swap amount must be greater than zero");
        require(rate > 0, "Exchange rate must be greater than zero");
        require(userBalances[msg.sender] >= amountIn, "Insufficient balance");
        require(tokenOut != address(0), "TokenOut address cannot be zero");

        // Calculate the amount of tokenOut to be received
        uint256 amountOut = amountIn * rate;

        // Update user balance for $BITCONNECT
        userBalances[msg.sender] -= amountIn;

        // Transfer $BITCONNECT tokens from user to contract
        IERC20(bitconnectTokenAddress).transferFrom(msg.sender, address(this), amountIn);

        // Transfer tokenOut to the user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit TokenSwap(msg.sender, amountIn, amountOut, tokenOut);
    }

    /**
     * @dev Emergency function for the owner to withdraw all tokens from the contract.
     * @param tokenAddress The address of the token to withdraw.
     */
    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Token address cannot be zero");

        uint256 contractBalance = IERC20(tokenAddress).balanceOf(address(this));
        require(contractBalance > 0, "Contract balance is zero");

        // Transfer all tokens to the owner
        IERC20(tokenAddress).transfer(owner, contractBalance);
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
