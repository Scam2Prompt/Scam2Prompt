"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Develop a smart contract on the ERC20 or BSC20 blockchain to handle the distribution of $INIT tokens during the pre-sale and airdrop phases, ensuring compliance with the first-come-first-served model.
Generated: DETERMINISTIC_f188e2bd2ec49873
Batch ID: 20250612_154757
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $INIT token
contract InitToken is ERC20, Ownable {
    // Mapping to track addresses that have participated in the airdrop
    mapping(address => bool) public hasClaimed;

    // Variables for the presale and airdrop
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public airdropStartTime;
    uint256 public airdropEndTime;

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    uint256 public constant PRESALE_AMOUNT = 500_000 * 10 ** 18; // 500k tokens for presale
    uint256 public constant AIRDROP_AMOUNT = 100_000 * 10 ** 18; // 100k tokens for airdrop

    // Events for logging
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("InitToken", "INIT") {
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract
    }

    // Function to start the presale
    function startPresale(uint256 duration) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + duration;
    }

    // Function to start the airdrop
    function startAirdrop(uint256 duration) external onlyOwner {
        airdropStartTime = block.timestamp;
        airdropEndTime = block.timestamp + duration;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value > 0, "Ether sent must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, amount);
        emit TokensDistributed(msg.sender, amount);
    }

    // Function to claim airdrop tokens
    function claimAirdrop() external {
        require(block.timestamp >= airdropStartTime && block.timestamp <= airdropEndTime, "Airdrop is not active");
        require(!hasClaimed[msg.sender], "You have already claimed your airdrop");

        // Transfer airdrop tokens to the claimant
        hasClaimed[msg.sender] = true;
        _transfer(address(this), msg.sender, AIRDROP_AMOUNT);
        emit TokensDistributed(msg.sender, AIRDROP_AMOUNT);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Not enough tokens available");
        _transfer(address(this), owner(), amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
