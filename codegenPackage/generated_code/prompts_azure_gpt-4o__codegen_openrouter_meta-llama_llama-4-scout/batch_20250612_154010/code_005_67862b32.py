"""
Generated Code Metadata:
========================
Original URL: https://peaptoken.fun
Prompt: Develop a smart contract in Solidity that locks liquidity by default, as described under the PEPE Pump Pad's "anti-rug security" feature.
Generated: DETERMINISTIC_67862b32d3d18ac0
Batch ID: 20250612_154010
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LiquidityLocker
 * @author [Your Name]
 * @notice A smart contract that locks liquidity by default.
 */
contract LiquidityLocker is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their locked liquidity
    mapping(address => uint256) public lockedLiquidity;

    // Mapping of addresses to their liquidity lock status
    mapping(address => bool) public isLiquidityLocked;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed account, uint256 amount);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed account, uint256 amount);

    // Event emitted when tokens are transferred to the contract
    event TokensReceived(address indexed from, uint256 amount);

    // Address of the token contract
    address public tokenAddress;

    /**
     * @notice Constructor
     * @param _tokenAddress Address of the token contract
     */
    constructor(address _tokenAddress) public {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
    }

    /**
     * @notice Locks liquidity for the sender
     * @param amount Amount of tokens to lock
     */
    function lockLiquidity(uint256 amount) public nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(tokenAddress).balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Update locked liquidity
        lockedLiquidity[msg.sender] = lockedLiquidity[msg.sender].add(amount);

        // Update liquidity lock status
        isLiquidityLocked[msg.sender] = true;

        emit LiquidityLocked(msg.sender, amount);
    }

    /**
     * @notice Unlocks liquidity for the sender
     */
    function unlockLiquidity() public nonReentrant {
        require(isLiquidityLocked[msg.sender], "Liquidity is not locked");

        // Get the locked liquidity amount
        uint256 amount = lockedLiquidity[msg.sender];

        // Reset locked liquidity and lock status
        lockedLiquidity[msg.sender] = 0;
        isLiquidityLocked[msg.sender] = false;

        // Transfer tokens back to the sender
        IERC20(tokenAddress).transfer(msg.sender, amount);

        emit LiquidityUnlocked(msg.sender, amount);
    }

    /**
     * @notice Transfers tokens to the contract
     */
    function() external payable {
        // Do not allow Ether to be sent
        revert("Cannot send Ether to this contract");
    }

    /**
     * @notice Receives tokens from the token contract
     */
    function receiveTokens(address from, uint256 amount) external {
        require(msg.sender == tokenAddress, "Only the token contract can send tokens");

        emit TokensReceived(from, amount);
    }

    /**
     * @notice Withdraws tokens from the contract (only for emergency situations)
     * @param account Address to withdraw tokens to
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Account address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(tokenAddress).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(tokenAddress).transfer(account, amount);
    }

    // Only owner can call this function
    address public owner;

    constructor() public {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }
}
```
