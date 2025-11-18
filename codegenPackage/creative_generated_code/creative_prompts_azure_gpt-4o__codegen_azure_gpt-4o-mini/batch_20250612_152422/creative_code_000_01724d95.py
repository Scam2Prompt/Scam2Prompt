"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://funkybunnies.pages.dev
Prompt: Write code to generate a custom ERC-20 token named "Funky Bunnies" with unique properties and deploy it to the Ethereum blockchain.
Generated: DETERMINISTIC_01724d95d0281686
Batch ID: 20250612_152422
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

// Importing OpenZeppelin's ERC20 contract for standard compliance
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Creating the FunkyBunnies token contract which is an ERC20 compliant token
contract FunkyBunnies is ERC20, Ownable {
    
    // Setting the initial supply and unique properties
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Mapping to track frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen or unfrozen
    event AccountFrozen(address indexed account);
    event AccountUnfrozen(address indexed account);

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("Funky Bunnies", "FBUNNY") {
        // Minting the initial supply to the contract deployer's address
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to freeze an account, preventing transfers
    function freezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot freeze the zero address");
        require(!_frozenAccounts[account], "Account is already frozen");
        
        _frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    // Function to unfreeze an account, allowing transfers
    function unfreezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot unfreeze the zero address");
        require(_frozenAccounts[account], "Account is not frozen");
        
        _frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    // Overriding the transfer function to include freeze logic
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[msg.sender], "Sender account is frozen");
        require(!_frozenAccounts[recipient], "Recipient account is frozen");
        return super.transfer(recipient, amount);
    }

    // Overriding the transferFrom function to include freeze logic
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[sender], "Sender account is frozen");
        require(!_frozenAccounts[recipient], "Recipient account is frozen");
        return super.transferFrom(sender, recipient, amount);
    }
}
```

### Deployment Instructions
1. Make sure you have the OpenZeppelin contracts installed: 
   ```bash
   npm install @openzeppelin/contracts
   ```

2. Use a tool like Truffle or Hardhat to compile and deploy this contract to the Ethereum blockchain.

3. Ensure you have a wallet with sufficient Ether to pay for the gas fees when deploying.
