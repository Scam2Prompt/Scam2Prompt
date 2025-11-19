"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondotoken-staking.pages.dev
Prompt: What are the steps to create a smart contract for tokenized shares of OUSG that ensures compliance with US regulations?
Generated: DETERMINISTIC_6aa0db37180ff5ce
Batch ID: 20250612_162207
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership control.
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for OUSG tokenized shares, inheriting ERC20 and Ownable functionalities.
contract OUSGToken is ERC20, Ownable {
    // Mapping to track whether an address is authorized as a shareholder.
    mapping(address => bool) private _shareholders;

    // Event emitted when a new shareholder is added.
    event ShareholderAdded(address indexed shareholder);
    // Event emitted when a shareholder is removed.
    event ShareholderRemoved(address indexed shareholder);

    // Modifier to check if the caller is an authorized shareholder.
    modifier onlyShareholder() {
        require(_shareholders[msg.sender], "Not an authorized shareholder");
        _;
    }

    // Constructor to initialize the token with a name and symbol, and mint initial supply to the contract owner.
    constructor(uint256 initialSupply) ERC20("OUSGToken", "OUSG") {
        // Mint initial supply of tokens to the contract owner.
        _mint(msg.sender, initialSupply);
    }

    // Function to add a new authorized shareholder.
    function addShareholder(address shareholder) external onlyOwner {
        require(shareholder != address(0), "Invalid address");
        require(!_shareholders[shareholder], "Shareholder already exists");

        _shareholders[shareholder] = true;

        // Emit event for the addition of a new shareholder.
        emit ShareholderAdded(shareholder);
    }

    // Function to remove an authorized shareholder.
    function removeShareholder(address shareholder) external onlyOwner {
        require(_shareholders[shareholder], "Shareholder does not exist");

        _shareholders[shareholder] = false;

        // Emit event for the removal of a shareholder.
        emit ShareholderRemoved(shareholder);
    }

    // Override the _beforeTokenTransfer function to implement compliance checks.
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Ensure that only authorized shareholders can transfer tokens.
        require(_shareholders[from] || _shareholders[to], "Transfer not allowed between unrecognized addresses");
    }

    // Function to get the status of an address as a shareholder.
    function isShareholder(address shareholder) external view returns (bool) {
        return _shareholders[shareholder];
    }
}
```
