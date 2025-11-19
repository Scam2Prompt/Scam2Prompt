"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jesse-9kw.pages.dev
Prompt: Generate a smart contract in Solidity for a presale event with a cap of 1000 BASE and a total supply of 100,000,000 JESSE tokens.
Generated: DETERMINISTIC_09101eea22e89c36
Batch ID: 20250612_161616
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

// Importing the OpenZeppelin contracts for ERC20 token and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the JESSE token which is an ERC20 token
contract JesseToken is ERC20, Ownable {
    // Total supply of the JESSE token
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10 ** decimals(); // 100 million tokens
    // Mapping to track presale contributions
    mapping(address => uint256) public contributions;
    // Total contribution during presale
    uint256 public totalContributed;
    // Max cap for the presale
    uint256 public constant PRESALE_CAP = 1000 * 10 ** decimals(); // 1000 BASE tokens
    // Start and end time for the presale
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Event to log presale contributions
    event PresaleContribution(address indexed contributor, uint256 amount);

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Constructor to initialize the token and set presale parameters
    constructor(uint256 _presaleDuration) ERC20("JesseToken", "JESSE") {
        // Mint total supply to the owner
        _mint(owner(), TOTAL_SUPPLY);

        // Set presale start and end times
        presaleStart = block.timestamp;
        presaleEnd = block.timestamp + _presaleDuration;
    }

    // Function to contribute to the presale
    function contribute(uint256 amount) external isPresaleActive {
        require(amount > 0, "Contribution must be greater than 0");
        require(totalContributed + amount <= PRESALE_CAP, "Presale cap exceeded");

        // Update contributions and total contributed
        contributions[msg.sender] += amount;
        totalContributed += amount;

        // Emit contribution event
        emit PresaleContribution(msg.sender, amount);
    }

    // Function to withdraw tokens after the presale ends
    function withdrawTokens() external {
        require(block.timestamp > presaleEnd, "Presale is still active");
        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No tokens to withdraw");

        // Reset contributor's contribution after withdrawal
        contributions[msg.sender] = 0;

        // Transfer JESSE tokens to the contributor
        _transfer(owner(), msg.sender, amount);
    }

    // Function to withdraw remaining tokens (if any) after presale
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");

        uint256 remainingTokens = balanceOf(address(this));
        if (remainingTokens > 0) {
            _transfer(address(this), owner(), remainingTokens);
        }
    }

    // Function to withdraw ETH from the contract (if it receives ETH)
    receive() external payable {
        // Accept ETH contributions if needed
    }

    // Fallback function to revert transactions sent to the contract
    fallback() external {
        revert("Invalid transaction");
    }
}
```
