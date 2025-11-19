"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://base-dawgz-claim.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates a token presale for the Base Dawgz Token ($DAWGZ) on Ethereum and Solana.
Generated: DETERMINISTIC_3e25d8730f276c61
Batch ID: 20250612_164152
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

// Importing OpenZeppelin Contracts for security and utility functions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DawgzPresale
 * @dev A smart contract for facilitating a token presale for the Base Dawgz Token ($DAWGZ)
 */
contract DawgzPresale is Ownable {
    // The token being sold
    IERC20 public dawgzToken;

    // Presale parameters
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public tokensSold;

    // Mapping to track contributions by address
    mapping(address => uint256) public contributions;

    // Events for logging transactions
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    /**
     * @dev Constructor to initialize the presale
     * @param _dawgzToken Address of the $DAWGZ token contract
     * @param _presaleStart Start time of the presale
     * @param _presaleEnd End time of the presale
     * @param _tokenPrice Price per token in wei
     */
    constructor(
        address _dawgzToken,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice
    ) {
        require(_dawgzToken != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale timings");

        dawgzToken = IERC20(_dawgzToken);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase tokens during the presale
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(msg.value == _amount * tokenPrice, "Incorrect ETH amount sent");

        // Update contributions and tokens sold
        contributions[msg.sender] += _amount;
        tokensSold += _amount;

        // Transfer $DAWGZ tokens to the buyer
        require(dawgzToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Owner can withdraw the Ether raised during the presale
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev End the presale and emit an event
     */
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale is still active");

        emit PresaleEnded();
    }

    /**
     * @dev Function to view the total balance of the contract
     * @return The current balance of the contract in wei
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

**Note**: This is a sample code for an Ethereum token presale. For Solana's presale, a different approach using Rust and the Solana SDK would be required, as Solana contracts operate differently from Ethereum. If you would like a Solana equivalent, please specify, and I can provide that as well.
