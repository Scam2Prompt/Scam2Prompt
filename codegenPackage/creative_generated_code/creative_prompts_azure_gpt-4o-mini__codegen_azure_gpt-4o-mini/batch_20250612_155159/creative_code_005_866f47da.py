"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-com.pages.dev
Prompt: Describe how to set up a smart contract on Binance Smart Chain for the CRUDO token presale, ensuring token vesting and distribution.
Generated: DETERMINISTIC_866f47daa9b76212
Batch ID: 20250612_155159
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

// Importing OpenZeppelin's ERC20 token contracts and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CRUDO Token Contract
contract CRUDO is ERC20, Ownable {
    // Event to emit when tokens are vested
    event TokensVested(address indexed beneficiary, uint256 amount, uint256 releaseTime);

    // Struct to hold vesting details
    struct Vesting {
        uint256 amount;      // Amount of tokens to vest
        uint256 releaseTime; // Timestamp when tokens can be released
        bool released;       // Status of the release
    }

    // Mapping to store vesting details for each beneficiary
    mapping(address => Vesting) public vestingDetails;

    // Constructor to initialize the token
    constructor() ERC20("CRUDO Token", "CRUDO") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Minting 1 million tokens to the owner
    }

    // Function to start a token presale with vesting
    function startPresale(address beneficiary, uint256 amount, uint256 duration) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Amount must be greater than 0");
        require(vestingDetails[beneficiary].amount == 0, "Tokens already vested to this beneficiary");

        // Set the vesting details
        vestingDetails[beneficiary] = Vesting({
            amount: amount,
            releaseTime: block.timestamp + duration,
            released: false
        });

        emit TokensVested(beneficiary, amount, vestingDetails[beneficiary].releaseTime);
    }

    // Function to release vested tokens
    function releaseTokens() external {
        Vesting storage vesting = vestingDetails[msg.sender];

        require(vesting.amount > 0, "No tokens to release");
        require(block.timestamp >= vesting.releaseTime, "Tokens are still locked");
        require(!vesting.released, "Tokens already released");

        // Transfer the vested tokens to the beneficiary
        vesting.released = true; // Mark tokens as released
        _transfer(owner(), msg.sender, vesting.amount); // Transfer tokens from owner to beneficiary

        // Reset the vesting details
        vesting.amount = 0;

        emit Transfer(owner(), msg.sender, vesting.amount);
    }

    // Function to withdraw any tokens sent to the contract by mistake
    function withdrawTokens(address token) external onlyOwner {
        require(token != address(this), "Cannot withdraw CRUDO tokens");
        ERC20(token).transfer(owner(), ERC20(token).balanceOf(address(this)));
    }
}
```
