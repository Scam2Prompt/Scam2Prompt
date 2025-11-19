"""
Generated Code Metadata:
========================
Original URL: https://bafybeibawo7r32uj46hju347auzbhmfq4h6f35azlyhnfqjz4d5whkaq5q.ipfs.dweb.link
Prompt: Write a smart contract in Solidity to manage liquid restaking of ETH LSTs and mint `rsETH`, ensuring compatibility with Kelp DAO's supported tokens (`stETH` and `ETHx`).
Generated: DETERMINISTIC_1119c27acb1c22d4
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract RestakingManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Supported LST tokens
    address public constant STETH = 0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84;
    address public constant ETHX = 0xA35b1B31Ce002FBF2058D22F30f95D405200A15b;

    // rsETH token
    IERC20 public immutable rsETH;

    // Track user deposits
    mapping(address => uint256) public userDeposits;
    mapping(address => mapping(address => uint256)) public userTokenDeposits;

    // Total deposits
    uint256 public totalDeposits;
    mapping(address => uint256) public totalTokenDeposits;

    // Events
    event Deposited(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);
    event RsETHMinted(address indexed user, uint256 amount);
    event RsETHBurned(address indexed user, uint256 amount);

    constructor(address _rsETH) {
        require(_rsETH != address(0), "Invalid rsETH address");
        rsETH = IERC20(_rsETH);
    }

    /**
     * @dev Deposit supported LST tokens to mint rsETH
     * @param token Address of the LST token (stETH or ETHx)
     * @param amount Amount to deposit
     */
    function deposit(address token, uint256 amount) external nonReentrant {
        require(token == STETH || token == ETHX, "Unsupported token");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Update balances
        userDeposits[msg.sender] += amount;
        userTokenDeposits[msg.sender][token] += amount;
        totalDeposits += amount;
        totalTokenDeposits[token] += amount;

        // Mint rsETH 1:1
        rsETH.safeTransfer(msg.sender, amount);

        emit Deposited(msg.sender, token, amount);
        emit RsETHMinted(msg.sender, amount);
    }

    /**
     * @dev Withdraw deposited LST tokens by burning rsETH
     * @param token Address of the LST token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(token == STETH || token == ETHX, "Unsupported token");
        require(amount > 0, "Amount must be greater than 0");
        require(userTokenDeposits[msg.sender][token] >= amount, "Insufficient balance");

        // Burn rsETH
        rsETH.safeTransferFrom(msg.sender, address(this), amount);

        // Update balances
        userDeposits[msg.sender] -= amount;
        userTokenDeposits[msg.sender][token] -= amount;
        totalDeposits -= amount;
        totalTokenDeposits[token] -= amount;

        // Transfer LST token back to user
        IERC20(token).safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, token, amount);
        emit RsETHBurned(msg.sender, amount);
    }

    /**
     * @dev Emergency withdraw all deposited tokens (onlyOwner)
     * @param token Address of the token to withdraw
     */
    function emergencyWithdraw(address token) external onlyOwner {
        require(token == STETH || token == ETHX, "Unsupported token");
        uint256 balance = IERC20(token).balanceOf(address(this));
        IERC20(token).safeTransfer(owner(), balance);
    }

    /**
     * @dev Get user's total deposited amount across all supported tokens
     * @param user Address of the user
     * @return Total deposited amount
     */
    function getUserTotalDeposits(address user) external view returns (uint256) {
        return userDeposits[user];
    }

    /**
     * @dev Get user's deposited amount for a specific token
     * @param user Address of the user
     * @param token Address of the token
     * @return Deposited amount
     */
    function getUserTokenDeposits(address user, address token) external view returns (uint256) {
        return userTokenDeposits[user][token];
    }
}
```
