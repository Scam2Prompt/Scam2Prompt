"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappyx.pages.dev
Prompt: Generate code to implement the "Buy Presale" and "Claim Presale" functionalities for tokens using the MultiChain Protocol.
Generated: DETERMINISTIC_698405245b4e95b4
Batch ID: 20250612_150715
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for Presale functionality
contract TokenPresale is Ownable {
    // State variables
    IERC20 public token;                // The token being sold
    uint256 public presalePrice;        // Price per token in wei
    uint256 public hardCap;             // Maximum amount to be raised
    uint256 public totalRaised;         // Amount raised so far
    uint256 public presaleEnd;          // End timestamp for the presale
    mapping(address => uint256) public contributions; // User contributions

    // Events to log activities
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleClaimed(address indexed claimer, uint256 amount);

    // Constructor to initialize the presale
    constructor(IERC20 _token, uint256 _presalePrice, uint256 _hardCap, uint256 _duration) {
        token = _token;
        presalePrice = _presalePrice;
        hardCap = _hardCap;
        presaleEnd = block.timestamp + _duration;
        totalRaised = 0;
    }

    // Modifier to check if the presale is active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEnd, "Presale has ended");
        require(totalRaised < hardCap, "Hard cap reached");
        _;
    }

    // Function to buy tokens in presale
    function buyTokens(uint256 _amount) external payable isPresaleActive {
        require(msg.value == _amount * presalePrice, "Incorrect ETH amount sent");
        require(totalRaised + msg.value <= hardCap, "Exceeds hard cap");

        contributions[msg.sender] += _amount;
        totalRaised += msg.value;

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to claim purchased tokens after presale ends
    function claimTokens() external {
        require(block.timestamp >= presaleEnd, "Presale not ended yet");
        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No tokens to claim");

        // Reset user's contribution to prevent multiple claims
        contributions[msg.sender] = 0;

        // Transfer tokens to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        emit PresaleClaimed(msg.sender, amount);
    }

    // Function to withdraw the raised ETH by the owner
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
