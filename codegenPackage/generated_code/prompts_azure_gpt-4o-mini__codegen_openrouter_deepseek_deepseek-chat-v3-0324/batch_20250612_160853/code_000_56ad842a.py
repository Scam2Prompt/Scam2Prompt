"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a token similar to $gummy that operates within the Solana ecosystem, including features for airdrops and liquidity management.
Generated: DETERMINISTIC_56ad842ac8fa5acb
Batch ID: 20250612_160853
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GummyToken
 * @dev ERC20 token with airdrop and liquidity management features
 */
contract GummyToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Address of the liquidity pool
    address public liquidityPool;

    // Mapping to track airdrop recipients
    mapping(address => bool) private _airdropRecipients;

    // Events
    event LiquidityPoolUpdated(address indexed newPool);
    event AirdropDistributed(address[] recipients, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) ERC20("GummyToken", "GUMMY") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Set the liquidity pool address
     * @param poolAddress The address of the liquidity pool
     */
    function setLiquidityPool(address poolAddress) external onlyOwner {
        require(poolAddress != address(0), "Invalid pool address");
        liquidityPool = poolAddress;
        emit LiquidityPoolUpdated(poolAddress);
    }

    /**
     * @dev Add liquidity to the pool
     * @param amount The amount of tokens to add
     */
    function addLiquidity(uint256 amount) external onlyOwner {
        require(liquidityPool != address(0), "Liquidity pool not set");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        _transfer(msg.sender, liquidityPool, amount);
    }

    /**
     * @dev Remove liquidity from the pool
     * @param amount The amount of tokens to remove
     */
    function removeLiquidity(uint256 amount) external onlyOwner {
        require(liquidityPool != address(0), "Liquidity pool not set");
        require(balanceOf(liquidityPool) >= amount, "Insufficient pool balance");
        
        _transfer(liquidityPool, msg.sender, amount);
    }

    /**
     * @dev Distribute tokens via airdrop
     * @param recipients Array of recipient addresses
     * @param amount The amount each recipient receives
     */
    function distributeAirdrop(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount.mul(recipients.length), "Insufficient balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(recipient != address(0), "Invalid recipient address");
            require(!_airdropRecipients[recipient], "Recipient already received airdrop");

            _transfer(msg.sender, recipient, amount);
            _airdropRecipients[recipient] = true;
        }

        emit AirdropDistributed(recipients, amount);
    }

    /**
     * @dev Check if an address has received an airdrop
     * @param account The address to check
     * @return bool Whether the address received an airdrop
     */
    function hasReceivedAirdrop(address account) external view returns (bool) {
        return _airdropRecipients[account];
    }
}
```
