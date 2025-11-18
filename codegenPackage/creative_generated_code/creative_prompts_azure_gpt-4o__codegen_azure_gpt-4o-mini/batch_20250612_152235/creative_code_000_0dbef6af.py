"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchaincoin-presale.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the Onchain Coin presale, including features like soft cap, hard cap, minimum and maximum buy limits, and token claim functionality.
Generated: DETERMINISTIC_0dbef6af105eb540
Batch ID: 20250612_152235
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
 * @title TokenPresale
 * @dev Smart contract for a token presale with soft cap, hard cap, buy limits, and token claim functionality.
 */
contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public softCap;
    uint256 public hardCap;
    uint256 public minBuyLimit;
    uint256 public maxBuyLimit;
    uint256 public totalRaised;
    uint256 public totalTokensClaimed;

    // Sale state
    bool public presaleActive = false;

    // User contributions
    mapping(address => uint256) public contributions;

    // Events for logging
    event PresaleStarted();
    event PresaleEnded();
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to initialize the presale parameters.
     * @param _token The address of the token being sold.
     * @param _softCap The minimum amount that must be raised.
     * @param _hardCap The maximum amount that can be raised.
     * @param _minBuyLimit The minimum purchase amount per transaction.
     * @param _maxBuyLimit The maximum purchase amount per transaction.
     */
    constructor(
        IERC20 _token,
        uint256 _softCap,
        uint256 _hardCap,
        uint256 _minBuyLimit,
        uint256 _maxBuyLimit
    ) {
        token = _token;
        softCap = _softCap;
        hardCap = _hardCap;
        minBuyLimit = _minBuyLimit;
        maxBuyLimit = _maxBuyLimit;
    }

    /**
     * @dev Starts the presale.
     */
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active");
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev Ends the presale.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable {
        require(presaleActive, "Presale is not active");
        require(amount >= minBuyLimit, "Amount below minimum limit");
        require(amount <= maxBuyLimit, "Amount exceeds maximum limit");
        require(totalRaised.add(msg.value) <= hardCap, "Hard cap exceeded");

        // Update contributions
        contributions[msg.sender] = contributions[msg.sender].add(amount);
        totalRaised = totalRaised.add(msg.value);

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their tokens after the presale ends.
     */
    function claimTokens() external {
        require(!presaleActive, "Presale is still active");
        require(contributions[msg.sender] > 0, "No tokens to claim");

        uint256 tokensToClaim = contributions[msg.sender];
        contributions[msg.sender] = 0; // Reset contributions

        // Transfer tokens to the user
        token.transfer(msg.sender, tokensToClaim);
        totalTokensClaimed = totalTokensClaimed.add(tokensToClaim);

        emit TokensClaimed(msg.sender, tokensToClaim);
    }

    /**
     * @dev Allows the owner to withdraw funds raised during the presale.
     */
    function withdrawFunds() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        require(totalRaised >= softCap, "Soft cap not met");

        // Transfer funds to the owner
        payable(owner()).transfer(totalRaised);
    }

    /**
     * @dev Allows the owner to withdraw unsold tokens after presale ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        
        uint256 unsoldTokens = token.balanceOf(address(this)).sub(totalTokensClaimed);
        token.transfer(owner(), unsoldTokens);
    }
}
```
