"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-en.web.app
Prompt: Develop a Solidity smart contract for $SCOTTY token distribution based on the tokenomics provided (e.g., public sale, staking, development, marketing).
Generated: DETERMINISTIC_31db0c933cb7cffd
Batch ID: 20250612_151405
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

/**
 * @title ScottyToken
 * @dev ERC20 Token with specific tokenomics for distribution
 */
contract ScottyToken is ERC20, Ownable {
    // Token distribution percentages
    uint256 public constant PUBLIC_SALE_PERCENTAGE = 40; // 40% for public sale
    uint256 public constant STAKING_PERCENTAGE = 30; // 30% for staking
    uint256 public constant DEVELOPMENT_PERCENTAGE = 20; // 20% for development
    uint256 public constant MARKETING_PERCENTAGE = 10; // 10% for marketing

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    // Addresses for distribution
    address public publicSaleAddress;
    address public stakingAddress;
    address public developmentAddress;
    address public marketingAddress;

    /**
     * @dev Constructor that initializes the token and distributes the initial supply
     * @param _publicSaleAddress Address for public sale distribution
     * @param _stakingAddress Address for staking distribution
     * @param _developmentAddress Address for development fund
     * @param _marketingAddress Address for marketing fund
     */
    constructor(
        address _publicSaleAddress,
        address _stakingAddress,
        address _developmentAddress,
        address _marketingAddress
    ) ERC20("Scotty Token", "SCOTTY") {
        require(_publicSaleAddress != address(0), "Invalid public sale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_developmentAddress != address(0), "Invalid development address");
        require(_marketingAddress != address(0), "Invalid marketing address");

        publicSaleAddress = _publicSaleAddress;
        stakingAddress = _stakingAddress;
        developmentAddress = _developmentAddress;
        marketingAddress = _marketingAddress;

        // Mint tokens according to the tokenomics
        _mint(publicSaleAddress, (TOTAL_SUPPLY * PUBLIC_SALE_PERCENTAGE) / 100);
        _mint(stakingAddress, (TOTAL_SUPPLY * STAKING_PERCENTAGE) / 100);
        _mint(developmentAddress, (TOTAL_SUPPLY * DEVELOPMENT_PERCENTAGE) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_PERCENTAGE) / 100);
    }

    /**
     * @dev Function to transfer tokens from the contract owner to a specified address
     * @param recipient The address to receive the tokens
     * @param amount The amount of tokens to transfer
     */
    function transferTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Insufficient balance");

        _transfer(owner(), recipient, amount);
    }

    /**
     * @dev Function to withdraw tokens mistakenly sent to the contract
     * @param tokenAddress The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        require(amount > 0, "Amount must be greater than zero");

        ERC20 token = ERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        token.transfer(owner(), amount);
    }
}
```
