"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-frogerc20tech.pages.dev
Prompt: Suggest blockchain security best practices for implementing a community-centric token like $FROG Meme Token. Include examples of how to secure smart contracts and prevent exploits.
Generated: DETERMINISTIC_d227c689141833f4
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FrogToken
 * @dev This contract implements a community-centric ERC20 token with security best practices.
 */
contract FrogToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mappings to track user balances and allowed spenders
    mapping(address => bool) private _whitelistedAddresses;

    // Event to log whitelist changes
    event WhitelistedAddressAdded(address indexed account);
    event WhitelistedAddressRemoved(address indexed account);

    // Constructor to initialize the token
    constructor() ERC20("Frog Token", "$FROG") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to contract owner
    }

    /**
     * @dev Function to whitelist an address.
     * @param account The address to whitelist.
     */
    function addWhitelistedAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot whitelist the zero address");
        require(!_whitelistedAddresses[account], "Address is already whitelisted");

        _whitelistedAddresses[account] = true;
        emit WhitelistedAddressAdded(account);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * @param account The address to remove from whitelist.
     */
    function removeWhitelistedAddress(address account) external onlyOwner {
        require(_whitelistedAddresses[account], "Address is not whitelisted");

        delete _whitelistedAddresses[account];
        emit WhitelistedAddressRemoved(account);
    }

    /**
     * @dev Function to transfer tokens securely.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function safeTransfer(address recipient, uint256 amount) external nonReentrant {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(amount > 0, "Transfer amount must be greater than zero");

        _transfer(msg.sender, recipient, amount);
    }

    /**
     * @dev Override transfer function to include whitelisted checks.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        require(_whitelistedAddresses[sender] || _whitelistedAddresses[recipient], "Both sender and recipient must be whitelisted");
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Function to withdraw Ether accumulated in the contract.
     */
    function withdrawEther() external onlyOwner {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Failed to transfer Ether");
    }
}
```

### Security Best Practices Implemented:
1. **Ownable Access Control**: Only the contract owner can whitelist addresses.
2. **Reentrancy Guard**: Prevents reentrancy attacks on critical functions.
3. **SafeMath Library**: Ensures safe arithmetic operations to prevent overflows.
4. **Require Statements**: Checks for zero addresses, sufficient balances, and valid amounts to avoid misuse.
5. **Fallback Function**: Prevents sending Ether directly to the contract.
6. **Event Logging**: Logs significant events like whitelisting for transparency.
