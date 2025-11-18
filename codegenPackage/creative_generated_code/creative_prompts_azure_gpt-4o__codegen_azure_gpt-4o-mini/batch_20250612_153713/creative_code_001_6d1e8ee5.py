"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-claims.pages.dev
Prompt: Generate Solidity code for creating an ERC20 token similar to RETIK, including tokenomics details such as total supply, presale allocation, and liquidity reserves.
Generated: DETERMINISTIC_6d1e8ee50d231d7d
Batch ID: 20250612_153713
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

// Importing the ERC20 interface and SafeMath library
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RETIK Token
 * @dev ERC20 Token with specific tokenomics: presale allocation, liquidity reserve, and burnable feature
 */
contract RETIK is ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Define total supply and allocations
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens
    uint256 private constant PRESALE_ALLOCATION = 200_000_000 * 10 ** decimals(); // 20% for presale
    uint256 private constant LIQUIDITY_RESERVE = 300_000_000 * 10 ** decimals(); // 30% for liquidity reserve

    // Mapping to track allocations
    mapping(address => bool) public presaleAddresses;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;

    event PresaleAllocation(address indexed account, uint256 amount);

    /**
     * @dev Constructor that sets the token name and symbol.
     */
    constructor() ERC20("RETIK Token", "RETIK") {
        // Mint total supply to the contract deployer (owner)
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Start the presale by setting the start and end time.
     * @param _startTime uint256 Start time for the presale
     * @param _endTime uint256 End time for the presale
     */
    function startPresale(uint256 _startTime, uint256 _endTime) external onlyOwner {
        require(_startTime < _endTime, "Invalid presale period");
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
    }

    /**
     * @dev Allocate tokens to presale participants.
     * @param account address The address of the presale participant
     * @param amount uint256 The amount of tokens to allocate
     */
    function allocatePresaleTokens(address account, uint256 amount) external onlyOwner {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale not active");
        require(amount <= PRESALE_ALLOCATION, "Amount exceeds presale allocation");
        require(!presaleAddresses[account], "Already allocated");

        // Mark the account as allocated and transfer tokens
        presaleAddresses[account] = true;
        _transfer(owner(), account, amount);
        emit PresaleAllocation(account, amount);
    }

    /**
     * @dev Withdraw tokens from the contract (for liquidity or operational usage).
     * @param amount uint256 The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");
        _transfer(address(this), owner(), amount);
    }

    /**
     * @dev Burn tokens from the caller's balance.
     * @param amount uint256 The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
