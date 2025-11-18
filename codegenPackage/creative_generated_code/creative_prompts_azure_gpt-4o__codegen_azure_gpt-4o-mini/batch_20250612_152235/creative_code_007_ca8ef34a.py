"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claimportal.pages.dev
Prompt: Write code to implement a presale claiming mechanism for DOGE20 tokens, ensuring fair distribution to presale buyers at the time of the Uniswap listing.
Generated: DETERMINISTIC_ca8ef34a1b12d1ca
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PresaleContract
 * @dev Implements a presale claiming mechanism for DOGE20 tokens.
 */
contract PresaleContract is Ownable {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public presalePrice; // Price per token during presale
    uint256 public totalTokensSold; // Total tokens sold during the presale
    uint256 public maxTokensPerBuyer; // Maximum tokens a buyer can purchase
    mapping(address => uint256) public contributions; // Track contributions by each buyer
    bool public presaleEnded; // Status of the presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(!presaleEnded, "Presale has ended");
        _;
    }

    // Constructor to initialize the presale contract
    constructor(
        address _doge20Token,
        uint256 _presalePrice,
        uint256 _maxTokensPerBuyer
    ) {
        doge20Token = IERC20(_doge20Token);
        presalePrice = _presalePrice;
        maxTokensPerBuyer = _maxTokensPerBuyer;
    }

    /**
     * @dev Allows buyers to purchase DOGE20 tokens during the presale.
     * @param amount Number of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable whenPresaleActive {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= maxTokensPerBuyer, "Exceeds max tokens per buyer");
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");

        contributions[msg.sender] += amount;
        totalTokensSold += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Ends the presale and allows claiming of purchased tokens.
     */
    function endPresale() external onlyOwner {
        presaleEnded = true;
        emit PresaleEnded();
    }

    /**
     * @dev Allows buyers to claim their DOGE20 tokens after the presale has ended.
     */
    function claimTokens() external {
        require(presaleEnded, "Presale is still active");
        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No tokens to claim");

        contributions[msg.sender] = 0; // Reset contribution before transfer to prevent re-entrancy attacks
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed"); // Transfer tokens

        // Optionally, you can also handle any additional logic, such as refunding excess Ether.
    }

    /**
     * @dev Withdraws Ether collected from the presale to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
