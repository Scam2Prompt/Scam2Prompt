"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jessecoinorg.pages.dev
Prompt: Generate a Solidity contract that ensures the total supply of JESSE tokens remains fixed at 100,000,000 while allowing presale transactions up to the cap.
Generated: DETERMINISTIC_b21ffec8db016ab2
Batch ID: 20250612_153400
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

/**
 * @title JESSE Token Contract
 * @dev This contract implements a fixed supply ERC20 token with a presale mechanism.
 */
contract JESSE is ERC20, Ownable {
    // Total supply of JESSE tokens
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * (10 ** 18); // 100 million tokens with 18 decimals

    // Maximum tokens available for presale
    uint256 public constant PRESALE_CAP = 30_000_000 * (10 ** 18); // 30 million tokens for presale

    // Tracks the amount of tokens sold in the presale
    uint256 public presaleSold;

    // Mapping to keep track of presale contributions
    mapping(address => uint256) public contributions;

    // Event emitted for each presale purchase
    event PresalePurchase(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor that mints the total supply to the owner.
     */
    constructor() ERC20("JESSE Token", "JESSE") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allows users to purchase JESSE tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function buyPresaleTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(presaleSold + amount <= PRESALE_CAP, "Presale cap exceeded");

        // Update presale tracking
        presaleSold += amount;
        contributions[msg.sender] += amount;

        // Transfer tokens to the buyer
        _transfer(owner(), msg.sender, amount);

        emit PresalePurchase(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract (in case of ETH sales).
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept ether.
     */
    receive() external payable {}
}
```
