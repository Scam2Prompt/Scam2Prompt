"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Design a Solidity contract that enforces a total token supply limit of 100,000,000 SHROOM and tracks the distribution during a presale.
Generated: DETERMINISTIC_af0cfa8c0256fd46
Batch ID: 20250612_152924
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

// Import the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SHROOM token contract with presale capabilities
contract SHROOM is ERC20, Ownable {
    // Total supply cap for SHROOM tokens
    uint256 public constant TOTAL_SUPPLY_CAP = 100_000_000 * 10**18; // 100 million tokens with 18 decimals

    // Tracking presale distribution
    mapping(address => uint256) public presaleBalances;

    // Boolean to determine if presale is active
    bool public presaleActive = false;

    // Event emitted when presale is started or stopped
    event PresaleStatusUpdated(bool isActive);

    // Event emitted when tokens are distributed during presale
    event TokensDistributed(address indexed buyer, uint256 amount);

    // Constructor to initialize the contract with the token name and symbol
    constructor() ERC20("SHROOM", "SHROOM") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY_CAP);
    }

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Function to start or stop the presale
    function togglePresale() external onlyOwner {
        presaleActive = !presaleActive;
        emit PresaleStatusUpdated(presaleActive);
    }

    // Function to distribute tokens during presale
    function buyTokens(uint256 amount) external whenPresaleActive {
        require(amount > 0, "Amount must be greater than 0");
        require(totalSupply() + amount <= TOTAL_SUPPLY_CAP, "Exceeds total supply cap");

        // Update presale balance for the buyer
        presaleBalances[msg.sender] += amount;

        // Mint new tokens to the buyer
        _mint(msg.sender, amount);
        
        emit TokensDistributed(msg.sender, amount);
    }

    // Function to withdraw tokens by the owner after presale ends
    function withdrawTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer tokens to owner
        _transfer(address(this), msg.sender, balance);
    }

    // Override the _beforeTokenTransfer function to restrict transfers during presale
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(!presaleActive || from == address(0), "Token transfers are not allowed during presale");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
