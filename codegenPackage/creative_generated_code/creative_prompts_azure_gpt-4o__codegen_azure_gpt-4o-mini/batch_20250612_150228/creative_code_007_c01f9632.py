"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Generate a smart contract audited by Trail of Bits that securely manages tokenized shares of Spiko MMFs and integrates with CACEIS Bank as the custodian.
Generated: DETERMINISTIC_c01f96326c2deb35
Batch ID: 20250612_150228
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

// Importing OpenZeppelin's ERC20 contract implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract to manage tokenized shares of Spiko MMFs
contract SpikoMMFToken is ERC20, Ownable, ReentrancyGuard {
    // Address of the CACEIS Bank custodian
    address public custodian;

    // Modifier to restrict access to the custodian
    modifier onlyCustodian() {
        require(msg.sender == custodian, "Caller is not the custodian");
        _;
    }

    // Event for logging the change of custodian
    event CustodianChanged(address indexed oldCustodian, address indexed newCustodian);

    // Constructor to initialize the token with name and symbol
    constructor(string memory name, string memory symbol, address _custodian) ERC20(name, symbol) {
        require(_custodian != address(0), "Invalid custodian address");
        custodian = _custodian;
    }

    // Function to mint new tokens, callable by the custodian only
    function mint(address to, uint256 amount) external onlyCustodian nonReentrant {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(to, amount);
    }

    // Function to burn tokens, callable by the custodian only
    function burn(address from, uint256 amount) external onlyCustodian nonReentrant {
        require(from != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(from) >= amount, "Insufficient balance to burn");

        _burn(from, amount);
    }

    // Function to change the custodian, only callable by the contract owner
    function changeCustodian(address newCustodian) external onlyOwner {
        require(newCustodian != address(0), "Invalid custodian address");
        address oldCustodian = custodian;
        custodian = newCustodian;
        emit CustodianChanged(oldCustodian, newCustodian);
    }

    // Function to retrieve the custodian address
    function getCustodian() external view returns (address) {
        return custodian;
    }
}
```
