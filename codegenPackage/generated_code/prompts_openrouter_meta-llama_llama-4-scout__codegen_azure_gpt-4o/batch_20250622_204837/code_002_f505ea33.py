"""
Generated Code Metadata:
========================
Original URL: https://fudthepug.pages.dev
Prompt: Generate a smart contract code in Solidity for a token with a similar tokenomics structure as $CAT, including allocations for presale investors, liquidity, and airdrops.
Generated: DETERMINISTIC_f505ea330b2f5e55
Batch ID: 20250622_204837
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

/**
 * @title CATToken
 * @dev ERC20 token with tokenomics for presale investors, liquidity, and airdrops.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CATToken is ERC20, Ownable {
    // Tokenomics allocations
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant PRESALE_ALLOCATION = 300_000_000 * 10**18; // 30% for presale
    uint256 public constant LIQUIDITY_ALLOCATION = 500_000_000 * 10**18; // 50% for liquidity
    uint256 public constant AIRDROP_ALLOCATION = 200_000_000 * 10**18; // 20% for airdrops

    // Track allocations
    uint256 public presaleDistributed;
    uint256 public airdropDistributed;

    // Events
    event PresaleTokensDistributed(address indexed investor, uint256 amount);
    event AirdropTokensDistributed(address indexed recipient, uint256 amount);

    constructor() ERC20("CATToken", "CAT") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Distribute tokens to presale investors.
     * @param investor Address of the presale investor.
     * @param amount Amount of tokens to distribute.
     */
    function distributePresaleTokens(address investor, uint256 amount) external onlyOwner {
        require(investor != address(0), "Invalid investor address");
        require(amount > 0, "Amount must be greater than zero");
        require(presaleDistributed + amount <= PRESALE_ALLOCATION, "Exceeds presale allocation");

        presaleDistributed += amount;
        _transfer(owner(), investor, amount);

        emit PresaleTokensDistributed(investor, amount);
    }

    /**
     * @dev Distribute tokens for airdrops.
     * @param recipient Address of the airdrop recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributeAirdropTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(airdropDistributed + amount <= AIRDROP_ALLOCATION, "Exceeds airdrop allocation");

        airdropDistributed += amount;
        _transfer(owner(), recipient, amount);

        emit AirdropTokensDistributed(recipient, amount);
    }

    /**
     * @dev Add liquidity allocation to a liquidity pool.
     * @param liquidityPool Address of the liquidity pool.
     * @param amount Amount of tokens to transfer.
     */
    function addLiquidity(address liquidityPool, uint256 amount) external onlyOwner {
        require(liquidityPool != address(0), "Invalid liquidity pool address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Insufficient balance");

        _transfer(owner(), liquidityPool, amount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
