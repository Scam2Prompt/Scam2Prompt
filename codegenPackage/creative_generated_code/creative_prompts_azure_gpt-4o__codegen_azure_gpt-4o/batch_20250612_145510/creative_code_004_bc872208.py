"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pantherappai.pages.dev
Prompt: Develop a Solidity smart contract for PantherAI token burning mechanism, ensuring compliance with BEP20 standards. Include functionality for tracking the total supply reduction.
Generated: DETERMINISTIC_bc872208a4092635
Batch ID: 20250612_145510
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

// Import OpenZeppelin's BEP20 (ERC20) token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PantherAIToken is ERC20, Ownable {
    // Variable to track the total tokens burned
    uint256 private _totalBurned;

    /**
     * @dev Constructor function to set initial values
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply to mint
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * Reduces the caller's token balance and the total supply.
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");

        // Burn the tokens from the caller's account
        _burn(msg.sender, amount);

        // Update the total burned tokens
        _totalBurned += amount;
    }

    /**
     * @dev Function to allow the owner to burn tokens from any account.
     * @param account The account from which tokens will be burned
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(account != address(0), "Cannot burn from the zero address");

        // Burn the tokens from the specified account
        _burn(account, amount);

        // Update the total burned tokens
        _totalBurned += amount;
    }

    /**
     * @dev Public function to retrieve the total amount of burned tokens.
     * @return The total number of burned tokens
     */
    function totalBurned() external view returns (uint256) {
        return _totalBurned;
    }
}
```

### Key Points in the Code:
- This contract uses OpenZeppelin's implementation of BEP20 (ERC20) for standard token functionality.
- Includes a `burn` function for users to burn their own tokens.
- Includes a `burnFrom` function for the owner to burn tokens on behalf of any account.
- Tracks the total burned tokens via the `_totalBurned` state variable.
- Follows the BEP20 standard and includes safeguards such as input validation and restricted access to `burnFrom`.
