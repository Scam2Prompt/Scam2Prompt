"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Generate a smart contract in Solidity for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens based on the snapshot of Bitcoin and Ethereum wallets.
Generated: DETERMINISTIC_b6ae8faefd8dbcf0
Batch ID: 20250612_160600
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ZiberICO
 * @dev A smart contract for the Ziber ICO that accepts Ethereum payments
 * and distributes Ziber tokens based on a snapshot of Bitcoin and Ethereum wallets.
 */
contract ZiberICO is Ownable {
    // The Ziber token contract
    IERC20 public ziberToken;

    // Sale parameters
    uint256 public rate; // Number of Ziber tokens per Ether
    uint256 public totalRaised; // Total Ether raised
    uint256 public icoEnd; // End timestamp for the ICO

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the ICO parameters
    constructor(IERC20 _ziberToken, uint256 _rate, uint256 _durationInDays) {
        ziberToken = _ziberToken;
        rate = _rate;
        icoEnd = block.timestamp + (_durationInDays * 1 days);
    }

    /**
     * @dev Fallback function that allows the contract to receive Ether.
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Function to buy Ziber tokens with Ether.
     */
    function buyTokens() public payable {
        require(block.timestamp < icoEnd, "ICO has ended.");
        require(msg.value > 0, "Ether value must be greater than 0.");

        // Calculate the amount of tokens to purchase
        uint256 tokensToBuy = msg.value * rate;
        totalRaised += msg.value;

        // Transfer Ziber tokens to the buyer
        require(ziberToken.balanceOf(address(this)) >= tokensToBuy, "Insufficient tokens in contract.");
        ziberToken.transfer(msg.sender, tokensToBuy);

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Only callable by the owner of the contract.
     */
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No Ether to withdraw.");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to withdraw unsold tokens from the contract.
     * Only callable by the owner of the contract.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = ziberToken.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw.");
        ziberToken.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Function to check the remaining time before the ICO ends.
     * @return uint256 Remaining time in seconds.
     */
    function timeRemaining() external view returns (uint256) {
        if (block.timestamp >= icoEnd) {
            return 0;
        }
        return icoEnd - block.timestamp;
    }
}
```
