"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Write a Solidity smart contract using Truffle and Linea's zkEVM for ultra-low fee DeFi transactions.
Generated: DETERMINISTIC_1aeca409adba737a
Batch ID: 20250622_212312
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LowFeeDeFi
 * @dev A DeFi contract optimized for Linea's zkEVM with ultra-low fee transactions
 */
contract LowFeeDeFi is Ownable, ReentrancyGuard {
    // Struct to store user deposit information
    struct Deposit {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of token addresses to whether they're supported
    mapping(address => bool) public supportedTokens;
    
    // Mapping of user addresses to their deposits
    mapping(address => mapping(address => Deposit)) public userDeposits;
    
    // Total deposits per token
    mapping(address => uint256) public totalDeposits;
    
    // Events
    event TokenSupported(address indexed token, bool supported);
    event Deposited(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);
    event Swapped(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Constructor to initialize the contract
     * @param _tokens Array of tokens to support initially
     */
    constructor(address[] memory _tokens) {
        for (uint256 i = 0; i < _tokens.length; i++) {
            supportedTokens[_tokens[i]] = true;
            emit TokenSupported(_tokens[i], true);
        }
    }

    /**
     * @dev Add or remove a supported token
     * @param _token Token address
     * @param _supported Whether to support or not
     */
    function setSupportedToken(address _token, bool _supported) external onlyOwner {
        supportedTokens[_token] = _supported;
        emit TokenSupported(_token, _supported);
    }

    /**
     * @dev Deposit tokens into the contract
     * @param _token Token address
     * @param _amount Amount to deposit
     */
    function deposit(address _token, uint256 _amount) external nonReentrant {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(_token);
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        userDeposits[msg.sender][_token] = Deposit({
            amount: userDeposits[msg.sender][_token].amount + _amount,
            timestamp: block.timestamp
        });

        totalDeposits[_token] += _amount;
        emit Deposited(msg.sender, _token, _amount);
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param _token Token address
     * @param _amount Amount to withdraw
     */
    function withdraw(address _token, uint256 _amount) external nonReentrant {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Amount must be greater than 0");
        
        Deposit storage depositInfo = userDeposits[msg.sender][_token];
        require(depositInfo.amount >= _amount, "Insufficient balance");

        IERC20 token = IERC20(_token);
        require(token.transfer(msg.sender, _amount), "Transfer failed");

        depositInfo.amount -= _amount;
        totalDeposits[_token] -= _amount;
        emit Withdrawn(msg.sender, _token, _amount);
    }

    /**
     * @dev Swap tokens at a 1:1 ratio (simplified for demo)
     * @param _tokenIn Token to swap from
     * @param _tokenOut Token to swap to
     * @param _amount Amount to swap
     */
    function swap(address _tokenIn, address _tokenOut, uint256 _amount) external nonReentrant {
        require(supportedTokens[_tokenIn] && supportedTokens[_tokenOut], "Token not supported");
        require(_amount > 0, "Amount must be greater than 0");
        
        Deposit storage depositIn = userDeposits[msg.sender][_tokenIn];
        require(depositIn.amount >= _amount, "Insufficient balance");

        // Simplified 1:1 swap for demonstration
        depositIn.amount -= _amount;
        totalDeposits[_tokenIn] -= _amount;

        userDeposits[msg.sender][_tokenOut].amount += _amount;
        totalDeposits[_tokenOut] += _amount;

        emit Swapped(msg.sender, _tokenIn, _tokenOut, _amount, _amount);
    }

    /**
     * @dev Get user balance for a specific token
     * @param _user User address
     * @param _token Token address
     * @return User's balance
     */
    function getUserBalance(address _user, address _token) external view returns (uint256) {
        return userDeposits[_user][_token].amount;
    }
}
```
