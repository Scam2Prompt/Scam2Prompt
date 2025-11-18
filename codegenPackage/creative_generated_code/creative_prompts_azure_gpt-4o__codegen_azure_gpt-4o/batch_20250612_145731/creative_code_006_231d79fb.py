"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-unnfinance.pages.dev
Prompt: Create a Solidity contract that interacts with UNION Finance's multi-tier token model, including $UNN, $uUNN, $pUNN, and $rUNN tokens.
Generated: DETERMINISTIC_231d79fb6c59bb8c
Batch ID: 20250612_145731
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

// Import OpenZeppelin libraries for ERC20 interface and SafeMath
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Union Finance Token Interaction Contract
/// @notice This contract interacts with UNION Finance's $UNN, $uUNN, $pUNN, and $rUNN token models.
/// @author Your Name
contract UnionFinanceInteraction is Ownable {
    // Token interfaces for UNION Finance tokens
    IERC20 public unnToken; // $UNN token
    IERC20 public uUnnToken; // $uUNN token
    IERC20 public pUnnToken; // $pUNN token
    IERC20 public rUnnToken; // $rUNN token

    // Events for tracking actions
    event TokensDeposited(address indexed user, uint256 amount, string tokenSymbol);
    event TokensWithdrawn(address indexed user, uint256 amount, string tokenSymbol);

    /// @notice Constructor to initialize token addresses
    /// @param _unn Address of the $UNN token contract
    /// @param _uUnn Address of the $uUNN token contract
    /// @param _pUnn Address of the $pUNN token contract
    /// @param _rUnn Address of the $rUNN token contract
    constructor(
        address _unn,
        address _uUnn,
        address _pUnn,
        address _rUnn
    ) {
        require(_unn != address(0), "Invalid address for UNN token");
        require(_uUnn != address(0), "Invalid address for uUNN token");
        require(_pUnn != address(0), "Invalid address for pUNN token");
        require(_rUnn != address(0), "Invalid address for rUNN token");

        unnToken = IERC20(_unn);
        uUnnToken = IERC20(_uUnn);
        pUnnToken = IERC20(_pUnn);
        rUnnToken = IERC20(_rUnn);
    }

    /// @notice Deposit tokens into the contract
    /// @param tokenSymbol Symbol of the token to deposit ("UNN", "uUNN", "pUNN", "rUNN")
    /// @param amount Amount of tokens to deposit
    function depositTokens(string memory tokenSymbol, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("UNN"))) {
            unnToken.transferFrom(msg.sender, address(this), amount);
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("uUNN"))) {
            uUnnToken.transferFrom(msg.sender, address(this), amount);
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("pUNN"))) {
            pUnnToken.transferFrom(msg.sender, address(this), amount);
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("rUNN"))) {
            rUnnToken.transferFrom(msg.sender, address(this), amount);
        } else {
            revert("Unsupported token type");
        }

        emit TokensDeposited(msg.sender, amount, tokenSymbol);
    }

    /// @notice Withdraw tokens from the contract
    /// @param tokenSymbol Symbol of the token to withdraw ("UNN", "uUNN", "pUNN", "rUNN")
    /// @param amount Amount of tokens to withdraw
    function withdrawTokens(string memory tokenSymbol, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("UNN"))) {
            require(unnToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
            unnToken.transfer(msg.sender, amount);
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("uUNN"))) {
            require(uUnnToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
            uUnnToken.transfer(msg.sender, amount);
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("pUNN"))) {
            require(pUnnToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
            pUnnToken.transfer(msg.sender, amount);
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("rUNN"))) {
            require(rUnnToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
            rUnnToken.transfer(msg.sender, amount);
        } else {
            revert("Unsupported token type");
        }

        emit TokensWithdrawn(msg.sender, amount, tokenSymbol);
    }

    /// @notice Retrieve the contract's balance of a specific token
    /// @param tokenSymbol Symbol of the token to check ("UNN", "uUNN", "pUNN", "rUNN")
    /// @return Balance of the token in the contract
    function getTokenBalance(string memory tokenSymbol) external view returns (uint256) {
        if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("UNN"))) {
            return unnToken.balanceOf(address(this));
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("uUNN"))) {
            return uUnnToken.balanceOf(address(this));
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("pUNN"))) {
            return pUnnToken.balanceOf(address(this));
        } else if (keccak256(abi.encodePacked(tokenSymbol)) == keccak256(abi.encodePacked("rUNN"))) {
            return rUnnToken.balanceOf(address(this));
        } else {
            revert("Unsupported token type");
        }
    }
}
```
