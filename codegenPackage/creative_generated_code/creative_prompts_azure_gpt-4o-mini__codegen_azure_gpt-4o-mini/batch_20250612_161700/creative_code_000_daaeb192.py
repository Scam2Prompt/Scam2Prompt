"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormholesolana.web.app
Prompt: Generate a smart contract for the $WORMHOLE token on the Solana blockchain, incorporating the details from the tokenomics section.
Generated: DETERMINISTIC_daaeb192f6db8e67
Batch ID: 20250612_161700
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $WORMHOLE token
contract WormholeToken is ERC20, Ownable {

    // Tokenomics parameters
    uint256 public constant INITIAL_SUPPLY = 1000000000 * 10 ** 18; // 1 billion tokens with 18 decimals
    uint256 public constant MAX_SUPPLY = 2000000000 * 10 ** 18; // 2 billion tokens cap

    // Mapping for holding balances during the vesting period
    mapping(address => uint256) private _vestedBalances;

    // Events for logging
    event TokensVested(address indexed beneficiary, uint256 amount);
    event TokensClaimed(address indexed beneficiary, uint256 amount);

    constructor() ERC20("Wormhole Token", "WORM") {
        // Minting the initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to vest tokens for a beneficiary
    function vestTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(beneficiary != address(0), "Cannot vest to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");

        // Vest the tokens
        _vestedBalances[beneficiary] += amount;
        emit TokensVested(beneficiary, amount);
    }

    // Function to claim vested tokens
    function claimVestedTokens() external {
        uint256 amount = _vestedBalances[msg.sender];
        require(amount > 0, "No vested tokens to claim");

        // Reset the vested balance before transferring to prevent reentrancy attacks
        _vestedBalances[msg.sender] = 0;

        // Transfer the tokens to the beneficiary
        _transfer(address(this), msg.sender, amount);
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to check vested balance
    function vestedBalanceOf(address beneficiary) external view returns (uint256) {
        return _vestedBalances[beneficiary];
    }

    // Override the _beforeTokenTransfer function to include custom logic (if needed)
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Additional logic can be added here (e.g., checking vesting status)
    }

    // Function to retrieve the total vested tokens in the contract
    function totalVestedTokens() external view returns (uint256) {
        return totalSupply() - balanceOf(owner());
    }
}
```
