"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Create a Solidity function to prevent deposits directly from cryptocurrency exchanges, ensuring only personal wallets are used, as emphasized by MinerDog.
Generated: DETERMINISTIC_515b558d1fba9d6e
Batch ID: 20250612_154111
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

contract SecureDeposit {

    // Mapping to keep track of known exchange addresses
    mapping(address => bool) private exchanges;

    // Event to log deposits
    event Deposit(address indexed user, uint256 amount);

    // Constructor to initialize known exchanges
    constructor(address[] memory knownExchanges) {
        for (uint256 i = 0; i < knownExchanges.length; i++) {
            exchanges[knownExchanges[i]] = true;
        }
    }

    // Modifier to restrict deposits to personal wallets only
    modifier onlyPersonalWallet() {
        require(!isExchange(msg.sender), "Deposits from exchanges are not allowed.");
        _;
    }

    // Function to check if an address is an exchange
    function isExchange(address account) internal view returns (bool) {
        return exchanges[account];
    }

    // Deposit function allowing only personal wallets
    function deposit() external payable onlyPersonalWallet {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        
        // Emit an event for the deposit
        emit Deposit(msg.sender, msg.value);
    }

    // Function to add a new known exchange (only owner can call this)
    function addExchange(address exchange) external onlyOwner {
        require(exchange != address(0), "Invalid address.");
        exchanges[exchange] = true;
    }

    // Function to remove a known exchange (only owner can call this)
    function removeExchange(address exchange) external onlyOwner {
        require(exchange != address(0), "Invalid address.");
        exchanges[exchange] = false;
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed. Use the deposit function.");
    }

    // Function to get the status of an address (whether it is an exchange)
    function isKnownExchange(address account) external view returns (bool) {
        return isExchange(account);
    }

    // Dummy onlyOwner modifier for demonstration (replace with actual ownership logic)
    modifier onlyOwner() {
        // Assuming msg.sender is the contract owner for example purposes
        require(msg.sender == owner, "Caller is not the owner.");
        _;
    }

    address private owner = msg.sender; // Set the contract deployer as the owner
}
```
