"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jindo-ai.web.app
Prompt: Provide an example of a smart contract that could facilitate the Jindo Token presale process on the Ethereum network.
Generated: DETERMINISTIC_8c45175ca92edc14
Batch ID: 20250612_155534
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title JindoPresale
 * @dev A smart contract to facilitate the presale of Jindo Tokens.
 */
contract JindoPresale is Ownable {
    using SafeMath for uint256;

    // The Jindo Token contract
    IERC20 public jindoToken;

    // Presale parameters
    uint256 public constant TOKEN_PRICE = 0.01 ether; // Price per token
    uint256 public constant MAX_TOKENS_PER_PURCHASE = 1000 * 10 ** 18; // Max tokens per purchase
    uint256 public tokensSold; // Total tokens sold during presale

    // Events to log purchases
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Mapping to track the amount of tokens purchased by an address
    mapping(address => uint256) public tokensPurchasedBy;

    // Modifier to check if the presale has reached its cap
    modifier presaleCapNotReached(uint256 tokenAmount) {
        require(tokensSold.add(tokenAmount) <= jindoToken.balanceOf(address(this)), "Presale cap reached");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _jindoToken Address of the Jindo token contract.
     */
    constructor(IERC20 _jindoToken) {
        jindoToken = _jindoToken;
    }

    /**
     * @dev Function to purchase Jindo Tokens during presale.
     * @param tokenAmount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 tokenAmount) external payable presaleCapNotReached(tokenAmount) {
        // Validate the payment and token amount
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(tokenAmount <= MAX_TOKENS_PER_PURCHASE, "Exceeds max tokens per purchase");
        require(msg.value == tokenAmount.mul(TOKEN_PRICE), "Incorrect Ether amount sent");

        // Update state
        tokensSold = tokensSold.add(tokenAmount);
        tokensPurchasedBy[msg.sender] = tokensPurchasedBy[msg.sender].add(tokenAmount);

        // Transfer tokens to the buyer
        jindoToken.transfer(msg.sender, tokenAmount);

        // Emit purchase event
        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    /**
     * @dev Function for the owner to withdraw Ether from the presale.
     */
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to withdraw unsold tokens after the presale.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = jindoToken.balanceOf(address(this));
        require(unsoldTokens > 0, "No tokens to withdraw");
        jindoToken.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Fallback function to prevent sending Ether directly to the contract.
     */
    receive() external payable {
        revert("Ether not accepted directly. Use purchaseTokens function.");
    }
}
```
