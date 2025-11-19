"""
Generated Code Metadata:
========================
Original URL: https://sophonnow.io
Prompt: Create a smart contract in Solidity that can verify and process payments for $SOPH tokens during the presale stage, ensuring compatibility with Ethereum wallets.
Generated: DETERMINISTIC_deed01be5bfc9cc6
Batch ID: 20250612_154829
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

// Importing the OpenZeppelin ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SOPHPresale
 * @dev Smart contract for handling the presale of SOPH tokens
 */
contract SOPHPresale is Ownable {
    // The token being sold
    IERC20 public sophtoken;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price in wei per SOPH token
    uint256 public tokensSold;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStarted(uint256 startTime, uint256 endTime);
    event PresaleEnded();

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract
     * @param _sophtoken Address of the SOPH token contract
     * @param _tokenPrice Price of SOPH token in wei
     */
    constructor(IERC20 _sophtoken, uint256 _tokenPrice) {
        sophtoken = _sophtoken;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Start the presale
     * @param duration Duration of the presale in seconds
     */
    function startPresale(uint256 duration) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + duration;
        emit PresaleStarted(presaleStartTime, presaleEndTime);
    }

    /**
     * @dev Buy SOPH tokens during the presale
     * @param amount Amount of SOPH tokens to purchase
     */
    function buyTokens(uint256 amount) external payable isPresaleActive {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent");

        // Transfer SOPH tokens to the buyer
        tokensSold += amount;
        sophtoken.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev End the presale
     */
    function endPresale() external onlyOwner isPresaleActive {
        presaleEndTime = block.timestamp;
        emit PresaleEnded();
    }

    /**
     * @dev Withdraw Ether from the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
