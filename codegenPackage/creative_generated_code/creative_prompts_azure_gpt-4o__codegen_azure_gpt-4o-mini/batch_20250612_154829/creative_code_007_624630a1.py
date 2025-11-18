"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophonnow.io
Prompt: Develop a Solidity-based smart contract that tracks and verifies $SOPH token purchases during the presale stage, including bonus allocations.
Generated: DETERMINISTIC_624630a1c4d22806
Batch ID: 20250612_154829
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

/**
 * @title SOPHPresale
 * @dev Smart contract to track and verify $SOPH token purchases during the presale stage, including bonus allocations.
 */
contract SOPHPresale is Ownable {
    // The token being sold
    IERC20 public sophtoken;

    // Presale parameters
    uint256 public constant TOKEN_PRICE = 0.01 ether; // Price per token
    uint256 public constant BONUS_RATE = 10; // Bonus 10% on purchases
    uint256 public presaleEndTime; // Timestamp for presale end

    // Mapping to track the amount of tokens purchased by each buyer
    mapping(address => uint256) public purchases;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    event PresaleEnded();

    /**
     * @dev Constructor to set the SOPH token address and presale duration.
     * @param _sophToken Address of the $SOPH token contract.
     * @param _duration Duration of the presale in seconds.
     */
    constructor(address _sophToken, uint256 _duration) {
        sophtoken = IERC20(_sophToken);
        presaleEndTime = block.timestamp + _duration;
    }

    /**
     * @dev Function to purchase $SOPH tokens.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * TOKEN_PRICE, "Incorrect ETH value sent");

        uint256 bonus = (amount * BONUS_RATE) / 100; // Calculate bonus tokens
        uint256 totalTokens = amount + bonus;

        // Update purchases mapping
        purchases[msg.sender] += totalTokens;

        // Emit event for tracking
        emit TokensPurchased(msg.sender, amount, bonus);
    }

    /**
     * @dev Function to end the presale. Callable only by the owner.
     */
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");
        emit PresaleEnded();
        // Additional logic for finalization can be added here.
    }

    /**
     * @dev Function to withdraw ETH collected from presale.
     */
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to withdraw unsold tokens after presale.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = sophtoken.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        sophtoken.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
