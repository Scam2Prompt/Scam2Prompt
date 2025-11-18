"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherealize.fi
Prompt: Generate a Solidity smart contract template for tokenizing Wall Street trading assets, ensuring compatibility with Ethereum's security and scalability features highlighted by Etherealize.
Generated: DETERMINISTIC_83be7a85872c55bc
Batch ID: 20250612_155042
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

// Import OpenZeppelin Contracts for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title WallStreetAssetToken
/// @notice A token contract for tokenizing Wall Street trading assets, ensuring security, scalability, and Ethereum compatibility.
contract WallStreetAssetToken is ERC20, Ownable, Pausable, ReentrancyGuard {
    // Variables
    uint8 private immutable _decimals; // Token decimals

    /// @dev Constructor to initialize the token
    /// @param name The name of the token
    /// @param symbol The symbol for the token
    /// @param initialSupply The initial supply of the token, minted to the deployer
    /// @param decimals_ The number of decimals the token should have
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint8 decimals_
    ) ERC20(name, symbol) {
        _decimals = decimals_;
        _mint(msg.sender, initialSupply * (10 ** decimals_));
    }

    /// @notice Returns the number of decimals for the token
    /// @return The number of decimals
    function decimals() public view override returns (uint8) {
        return _decimals;
    }

    /// @notice Mint new tokens
    /// @param account The address to receive the minted tokens
    /// @param amount The amount of tokens to mint
    function mint(address account, uint256 amount) external onlyOwner whenNotPaused nonReentrant {
        _mint(account, amount);
    }

    /// @notice Burn tokens from the caller's account
    /// @param amount The amount of tokens to burn
    function burn(uint256 amount) external whenNotPaused nonReentrant {
        _burn(msg.sender, amount);
    }

    /// @notice Pause the contract, disabling transfers and other operations
    function pause() external onlyOwner {
        _pause();
    }

    /// @notice Unpause the contract, enabling transfers and other operations
    function unpause() external onlyOwner {
        _unpause();
    }

    /// @dev Hook that is called before any token transfer. This includes minting and burning.
    /// @param from The address transferring the tokens
    /// @param to The address receiving the tokens
    /// @param amount The amount of tokens being transferred
    /// @notice This ensures transfers are paused if required
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /// @notice Withdraw any accidentally sent ETH to the contract
    function withdrawEther() external onlyOwner nonReentrant {
        payable(owner()).transfer(address(this).balance);
    }

    /// @notice Fallback function to prevent sending ETH directly
    receive() external payable {
        revert("Direct ETH deposits not allowed");
    }

    fallback() external payable {
        revert("Fallback function called");
    }
}
```
