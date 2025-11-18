"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibawo7r32uj46hju347auzbhmfq4h6f35azlyhnfqjz4d5whkaq5q.ipfs.dweb.link
Prompt: Write a smart contract in Solidity to manage liquid restaking of ETH LSTs and mint `rsETH`, ensuring compatibility with Kelp DAO's supported tokens (`stETH` and `ETHx`).
Generated: DETERMINISTIC_1119c27acb1c22d4
Batch ID: 20250612_152249
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

/// @title Liquid Restaking Contract
/// @author Professional Developer
/// @notice This contract facilitates liquid restaking of ETH LSTs (stETH and ETHx) and mints rsETH.
/// @dev Ensure compatibility with Kelp DAO's supported tokens.

interface ILSTToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function approve(address spender, uint256 amount) external returns (bool);
}

interface IKelpDAO {
    function restake(address token, uint256 amount) external returns (uint256 rsETHMinted);
}

contract LiquidRestaking {
    // Supported LST tokens
    address public immutable stETH;
    address public immutable ETHx;

    // Kelp DAO contract
    address public immutable kelpDAO;

    // Event emitted when rsETH is minted
    event Restake(address indexed user, address indexed token, uint256 amountRestaked, uint256 rsETHMinted);

    /// @notice Constructor to initialize the supported tokens and Kelp DAO contract address
    /// @param _stETH Address of the stETH token
    /// @param _ETHx Address of the ETHx token
    /// @param _kelpDAO Address of the Kelp DAO contract
    constructor(address _stETH, address _ETHx, address _kelpDAO) {
        require(_stETH != address(0), "Invalid stETH address");
        require(_ETHx != address(0), "Invalid ETHx address");
        require(_kelpDAO != address(0), "Invalid Kelp DAO address");

        stETH = _stETH;
        ETHx = _ETHx;
        kelpDAO = _kelpDAO;
    }

    /// @notice Function to restake LST tokens and mint rsETH
    /// @param token Address of the LST token to restake (must be stETH or ETHx)
    /// @param amount Amount of LST token to restake
    function restake(address token, uint256 amount) external {
        require(token == stETH || token == ETHx, "Unsupported token");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer LST tokens from the user to the contract
        ILSTToken(token).transferFrom(msg.sender, address(this), amount);

        // Approve Kelp DAO to spend the tokens
        ILSTToken(token).approve(kelpDAO, amount);

        // Call the restake function on Kelp DAO
        uint256 rsETHMinted = IKelpDAO(kelpDAO).restake(token, amount);

        // Emit the Restake event
        emit Restake(msg.sender, token, amount, rsETHMinted);
    }

    /// @notice Fallback function to handle ETH transfers (not used in this contract)
    receive() external payable {
        revert("ETH transfers not supported");
    }

    /// @notice Withdraw accidentally sent tokens to the contract
    /// @param token Address of the token to withdraw
    /// @param amount Amount of the token to withdraw
    /// @param to Address to send the withdrawn tokens
    function rescueTokens(address token, uint256 amount, address to) external {
        require(token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");

        ILSTToken(token).transfer(to, amount);
    }
}
```
