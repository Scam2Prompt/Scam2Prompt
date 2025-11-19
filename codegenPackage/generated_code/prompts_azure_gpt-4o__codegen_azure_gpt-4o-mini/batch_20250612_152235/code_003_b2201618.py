"""
Generated Code Metadata:
========================
Original URL: https://moonmouse.pages.dev
Prompt: Write a smart contract in Solidity that aligns with Moon Mouse's roadmap and tokenomics structure for distributing $MMOUSE tokens after the presale.
Generated: DETERMINISTIC_b22016180d4b028c
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Moon Mouse token
contract MoonMouseToken is ERC20, Ownable {
    // Mapping to track the amount of tokens distributed to each address
    mapping(address => uint256) public distributedTokens;

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals
    // Presale end timestamp
    uint256 public presaleEndTime;
    // Flag to indicate if the presale has ended
    bool public presaleEnded = false;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 _presaleDuration) ERC20("Moon Mouse", "MMOUSE") {
        // Set the presale end time
        presaleEndTime = block.timestamp + _presaleDuration;
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to distribute tokens after the presale
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(presaleEnded, "Presale has not ended yet");
        require(recipient != address(0), "Cannot distribute to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Insufficient balance to distribute");

        // Transfer tokens from the owner to the recipient
        _transfer(owner(), recipient, amount);
        distributedTokens[recipient] += amount;

        emit TokensDistributed(recipient, amount);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale has already ended");
        require(block.timestamp >= presaleEndTime, "Presale duration has not yet passed");

        presaleEnded = true;
    }

    // Function to withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    // Function to withdraw Ether mistakenly sent to the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
