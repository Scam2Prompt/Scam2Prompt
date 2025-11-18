"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eclipse-teth.pages.dev
Prompt: Write a smart contract in Solidity that facilitates the minting and redeeming of tETH tokens, ensuring compatibility with the wallet connection features described on the Eclipse platform.
Generated: DETERMINISTIC_79c6d6333be312d4
Batch ID: 20250612_154322
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title tETH Token
 * @dev This smart contract facilitates the minting and redeeming of tETH tokens
 */
contract tETH is ERC20, Ownable {
    using SafeMath for uint256; // Using SafeMath for safe arithmetic operations

    // Event emitted when tokens are minted
    event TokensMinted(address indexed user, uint256 amount);
    
    // Event emitted when tokens are redeemed
    event TokensRedeemed(address indexed user, uint256 amount);

    // Maximum tokens that can be minted
    uint256 public constant MAX_SUPPLY = 1e24; // 1 million tETH tokens

    /**
     * @dev Constructor to initialize the token with a name and symbol
     */
    constructor() ERC20("tETH Token", "tETH") {}

    /**
     * @dev Minting function to create new tETH tokens
     * @param amount The number of tokens to mint
     */
    function mint(uint256 amount) external onlyOwner {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Minting exceeds maximum supply");
        _mint(msg.sender, amount);
        emit TokensMinted(msg.sender, amount);
    }

    /**
     * @dev Redeeming function to burn tETH tokens
     * @param amount The number of tokens to redeem
     */
    function redeem(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to redeem");
        _burn(msg.sender, amount);
        emit TokensRedeemed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract
     * This can be used to withdraw any Ether that has been sent to this contract
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(msg.sender).transfer(balance);
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @dev Function to check the balance of Ether held by the contract
     * @return The balance of Ether in the contract
     */
    function getEtherBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
