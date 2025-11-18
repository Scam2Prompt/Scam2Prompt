"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonxbase.pages.dev
Prompt: Develop a Solidity smart contract snippet for managing the presale of $ANON tokens, including wallet connection verification.
Generated: DETERMINISTIC_1cd011738ea361bd
Batch ID: 20250612_153401
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

// Importing the ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for managing the presale of $ANON tokens
contract Presale {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public token;  // Reference to the $ANON token contract
    uint256 public presaleEndTime; // Timestamp when presale ends
    uint256 public tokenPrice; // Price of one token in wei
    mapping(address => uint256) public contributions; // Track contributions by address

    // Events for logging purposes
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if the presale is still active
    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    // Constructor to initialize the presale contract
    constructor(
        address _tokenAddress,
        uint256 _presaleDuration,
        uint256 _tokenPrice
    ) {
        owner = msg.sender; // Set the contract deployer as owner
        token = IERC20(_tokenAddress); // Set the token contract reference
        presaleEndTime = block.timestamp + _presaleDuration; // Set end time for presale
        tokenPrice = _tokenPrice; // Set price for the token
    }

    // Function to purchase tokens during the presale
    function buyTokens(uint256 _amount) external payable presaleActive {
        // Calculate the required ether for the token purchase
        uint256 totalCost = _amount * tokenPrice;

        // Ensure that the sender has sent enough ether
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Update contributions mapping
        contributions[msg.sender] += _amount;

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to end the presale and withdraw funds
    function endPresale() external onlyOwner {
        // Ensure that the presale has ended
        require(block.timestamp >= presaleEndTime, "Presale is still active");

        // Emit event indicating presale has ended
        emit PresaleEnded();

        // Transfer balance to owner
        payable(owner).transfer(address(this).balance);
    }

    // Function to retrieve contract balance (for owner use)
    function getContractBalance() external view onlyOwner returns (uint256) {
        return address(this).balance;
    }

    // Function to retrieve contributions made by an address
    function getContribution(address _contributor) external view returns (uint256) {
        return contributions[_contributor];
    }
}
```
