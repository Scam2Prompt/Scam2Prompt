"""
Generated Code Metadata:
========================
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Generate a smart contract for the $MPEPE token that includes features like transaction burning and ERC-20 compatibility.
Generated: DETERMINISTIC_4c835e1cccab55ca
Batch ID: 20250612_155242
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MPepeToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public burnRate; // Percentage of tokens to burn per transaction (0-100)
    address public burnAddress = 0x000000000000000000000000000000000000dEaD;

    event BurnRateUpdated(uint256 newBurnRate);
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply and burn rate
     * @param initialSupply Initial token supply to mint
     * @param initialBurnRate Initial burn rate percentage (0-100)
     */
    constructor(
        uint256 initialSupply,
        uint256 initialBurnRate
    ) ERC20("MPepe Token", "MPEPE") {
        require(initialSupply <= MAX_SUPPLY, "Initial supply exceeds max supply");
        require(initialBurnRate <= 100, "Burn rate cannot exceed 100%");
        
        _mint(msg.sender, initialSupply);
        burnRate = initialBurnRate;
    }

    /**
     * @dev Updates the burn rate for transactions
     * @param newBurnRate New burn rate percentage (0-100)
     */
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 100, "Burn rate cannot exceed 100%");
        burnRate = newBurnRate;
        emit BurnRateUpdated(newBurnRate);
    }

    /**
     * @dev Overrides ERC20 transfer to include burn functionality
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transferWithBurn(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Overrides ERC20 transferFrom to include burn functionality
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _spendAllowance(sender, msg.sender, amount);
        _transferWithBurn(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle transfers with burn
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function _transferWithBurn(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balanceOf(sender) >= amount, "ERC20: transfer amount exceeds balance");

        if (burnRate > 0) {
            uint256 burnAmount = (amount * burnRate) / 100;
            uint256 transferAmount = amount - burnAmount;

            if (burnAmount > 0) {
                _transfer(sender, burnAddress, burnAmount);
                emit TokensBurned(sender, burnAmount);
            }

            _transfer(sender, recipient, transferAmount);
        } else {
            _transfer(sender, recipient, amount);
        }
    }

    /**
     * @dev Allows owner to mint new tokens up to max supply
     * @param to Address to receive minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting would exceed max supply");
        _mint(to, amount);
    }
}
```
