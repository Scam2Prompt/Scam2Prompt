"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-en.pages.dev
Prompt: Generate a smart contract code in Solidity for a token burn mechanism similar to Galaxy Fox's $GFOX token.
Generated: DETERMINISTIC_08fa75af3a1d6a45
Batch ID: 20250622_204931
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GFOXToken
 * @dev Implementation of the GFOX token with burn mechanism
 */
contract GFOXToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Burn address
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    // Burn percentage (e.g., 100 = 1%)
    uint256 public burnPercentage;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that initializes the token
     * @param initialSupply The initial token supply
     * @param _burnPercentage The percentage of tokens to burn on transfers (100 = 1%)
     */
    constructor(
        uint256 initialSupply,
        uint256 _burnPercentage
    ) ERC20("Galaxy Fox", "GFOX") {
        require(_burnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        _mint(msg.sender, initialSupply);
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Overrides ERC20 transfer to include burn mechanism
     * @param recipient The address to receive tokens
     * @param amount The amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transferWithBurn(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides ERC20 transferFrom to include burn mechanism
     * @param sender The address sending tokens
     * @param recipient The address to receive tokens
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public virtual override returns (bool) {
        _spendAllowance(sender, _msgSender(), amount);
        _transferWithBurn(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle transfer with burn
     * @param sender The address sending tokens
     * @param recipient The address to receive tokens
     * @param amount The amount of tokens to transfer
     */
    function _transferWithBurn(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        uint256 burnAmount = amount.mul(burnPercentage).div(10000);
        uint256 transferAmount = amount.sub(burnAmount);

        if (burnAmount > 0) {
            _transfer(sender, BURN_ADDRESS, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }

        _transfer(sender, recipient, transferAmount);
    }

    /**
     * @dev Allows owner to update the burn percentage
     * @param newBurnPercentage The new burn percentage (100 = 1%)
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        burnPercentage = newBurnPercentage;
    }

    /**
     * @dev Allows anyone to burn their own tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        _burn(_msgSender(), amount);
        emit TokensBurned(_msgSender(), amount);
    }
}
```
