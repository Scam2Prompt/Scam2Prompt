"""
Generated Code Metadata:
========================
Original URL: https://popcat.meme
Prompt: Create a simple contract in a programming language (e.g., Solidity) that allows users to buy $POPCAT tokens, inspired by the "Buy now" buttons on the webpage.
Generated: DETERMINISTIC_a267256a22ab78bb
Batch ID: 20250622_210122
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

contract POPCAT is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant TOKEN_PRICE = 0.01 ether; // Price per token in ETH
    uint256 public constant MAX_SUPPLY = 1000000 * 10**18; // 1 million tokens

    constructor() ERC20("POPCAT", "POPCAT") {
        _mint(msg.sender, MAX_SUPPLY); // Mint initial supply to contract owner
    }

    /**
     * @dev Allows users to buy POPCAT tokens by sending ETH
     * @param amount The number of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= amount.mul(TOKEN_PRICE), "Insufficient ETH sent");

        _transfer(owner(), msg.sender, amount);

        // Refund any excess ETH sent
        if (msg.value > amount.mul(TOKEN_PRICE)) {
            payable(msg.sender).transfer(msg.value.sub(amount.mul(TOKEN_PRICE)));
        }
    }

    /**
     * @dev Allows owner to withdraw collected ETH
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
