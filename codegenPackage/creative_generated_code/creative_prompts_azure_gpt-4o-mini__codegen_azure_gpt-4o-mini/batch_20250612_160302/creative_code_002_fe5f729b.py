"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-blubtheblob.com
Prompt: Can you provide code examples for integrating a presale mechanism in a blockchain project?
Generated: DETERMINISTIC_fe5f729ba17acfc9
Batch ID: 20250612_160302
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract for better security and usability
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PresaleToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 private constant TOTAL_SUPPLY = 1000000 * 10**18; // 1 million tokens
    // Presale parameters
    uint256 public presalePrice; // Price per token during presale
    uint256 public presaleEndTime; // End time of the presale
    mapping(address => uint256) public contributions; // Track contributions from each address

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    // Constructor to initialize the token and presale parameters
    constructor(uint256 _presalePrice, uint256 _duration) ERC20("PresaleToken", "PST") {
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract itself
        presalePrice = _presalePrice; // Set the presale price
        presaleEndTime = block.timestamp + _duration; // Set the presale end time
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 _amount) external payable isPresaleActive {
        require(msg.value == _amount * presalePrice, "Incorrect Ether value sent");

        // Ensure enough tokens are available for sale
        require(balanceOf(address(this)) >= _amount, "Not enough tokens available for presale");

        // Update contributions
        contributions[msg.sender] += _amount;

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, _amount);

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to end the presale and withdraw funds
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still active");

        // Transfer the balance of Ether to the owner
        payable(owner()).transfer(address(this).balance);
        emit PresaleEnded();
    }

    // Function to withdraw unsold tokens after the presale
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still active");

        uint256 unsoldTokens = balanceOf(address(this));
        _transfer(address(this), owner(), unsoldTokens);
    }

    // Function to get the current balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
