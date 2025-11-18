"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buytoken-scapesmania.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the ScapesMania presale, including functionality to restrict purchases based on unsupported jurisdictions.
Generated: DETERMINISTIC_e192a0f886eeda71
Batch ID: 20250612_152511
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title TokenPresale
 * @dev A smart contract for managing a token presale with jurisdiction restrictions
 */
contract TokenPresale is Ownable {
    using Address for address;

    IERC20 public token; // The token to be sold
    uint256 public price; // Price of the token in wei
    uint256 public presaleEnd; // End time of the presale
    mapping(address => bool) public isJurisdictionRestricted; // Jurisdiction restriction mapping
    mapping(address => uint256) public contributions; // Contributions from each address

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    /**
     * @dev Constructor to initialize the presale parameters
     * @param _token Address of the token to be sold
     * @param _price Price per token in wei
     * @param _duration Duration of the presale in seconds
     */
    constructor(IERC20 _token, uint256 _price, uint256 _duration) {
        token = _token;
        price = _price;
        presaleEnd = block.timestamp + _duration;
    }

    /**
     * @dev Function to set jurisdiction restrictions for purchases
     * @param account Address to restrict or allow
     * @param restricted Boolean value to set restriction
     */
    function setJurisdictionRestriction(address account, bool restricted) external onlyOwner {
        isJurisdictionRestricted[account] = restricted;
    }

    /**
     * @dev Function to purchase tokens during the presale
     * @param amount Amount of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable {
        require(block.timestamp < presaleEnd, "Presale has ended");
        require(!isJurisdictionRestricted[msg.sender], "Purchases from your jurisdiction are restricted");
        require(msg.value == amount * price, "Incorrect Ether value sent");

        // Update contributions
        contributions[msg.sender] += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw collected funds by the owner
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale is still ongoing");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to end the presale and transfer unsold tokens back to the owner
     */
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale is still ongoing");
        emit PresaleEnded();
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Fallback function to accept Ether
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed. Use buyTokens function.");
    }

    // Modifier to check if the presale is active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEnd, "Presale has ended");
        _;
    }
}
```
