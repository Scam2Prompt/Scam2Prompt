"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Generate a smart contract in Solidity for a presale token with a total supply of 100,000,000 tokens and a presale cap of 1000 ETH.
Generated: DETERMINISTIC_e8850ba803cd1c3d
Batch ID: 20250612_145436
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
 * @title PresaleToken
 * @dev A simple ERC20 token with a presale mechanism
 */
contract PresaleToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimals

    // Presale cap in ETH
    uint256 public constant PRESALE_CAP = 1000 ether; // 1000 ETH

    // Total amount raised during the presale
    uint256 public totalRaised;

    // Boolean to track if presale is active
    bool public presaleActive;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event to emit when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token and presale
    constructor() ERC20("PresaleToken", "PST") {
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract
        presaleActive = true; // Start presale as active
    }

    /**
     * @dev Function to buy tokens during the presale
     * @param amount Amount of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Ether required");
        require(totalRaised.add(msg.value) <= PRESALE_CAP, "Presale cap reached");
        require(balanceOf(address(this)) >= amount, "Not enough tokens available");

        // Update the total raised and buyer's contributions
        totalRaised = totalRaised.add(msg.value);
        contributions[msg.sender] = contributions[msg.sender].add(amount);

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, amount);
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to end the presale and withdraw Ether
     */
    function endPresale() external onlyOwner {
        presaleActive = false; // End the presale
        payable(owner()).transfer(address(this).balance); // Transfer ETH to owner
    }

    /**
     * @dev Function to withdraw unsold tokens after presale ends
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 unsoldTokens = balanceOf(address(this));
        _transfer(address(this), owner(), unsoldTokens); // Transfer unsold tokens to owner
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers to the contract
     */
    receive() external payable {
        revert("Direct ether transfers not allowed");
    }
}
```
