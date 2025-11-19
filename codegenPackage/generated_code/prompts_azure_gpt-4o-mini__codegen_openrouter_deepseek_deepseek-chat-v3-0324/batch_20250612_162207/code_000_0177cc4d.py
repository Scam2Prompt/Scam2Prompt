"""
Generated Code Metadata:
========================
Original URL: https://maradonacoinz.vercel.app
Prompt: Generate a smart contract for the Hand of Pepe ($HOPE) token on the Solana blockchain, including details like total supply, decimals, and tokenomics.
Generated: DETERMINISTIC_0177cc4de6db7737
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solana ^0.8.0;

import "@solana/spl-token/contracts/token.sol";

contract HandOfPepe is SPLToken {
    // Token details
    string public constant NAME = "Hand of Pepe";
    string public constant SYMBOL = "HOPE";
    uint8 public constant DECIMALS = 9;
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** uint256(DECIMALS)); // 1 billion tokens
    
    // Tokenomics allocations
    uint256 public constant TEAM_ALLOCATION = 100_000_000 * (10 ** uint256(DECIMALS)); // 10%
    uint256 public constant ECOSYSTEM_FUND = 150_000_000 * (10 ** uint256(DECIMALS)); // 15%
    uint256 public constant MARKETING = 50_000_000 * (10 ** uint256(DECIMALS)); // 5%
    uint256 public constant LIQUIDITY = 200_000_000 * (10 ** uint256(DECIMALS)); // 20%
    uint256 public constant PUBLIC_SALE = 500_000_000 * (10 ** uint256(DECIMALS)); // 50%

    // Addresses for allocations
    address public teamWallet;
    address public ecosystemWallet;
    address public marketingWallet;
    address public liquidityWallet;

    // Token mint authority
    address public mintAuthority;

    // Events
    event TokensMinted(address indexed to, uint256 amount);
    event AllocationTransferred(address indexed wallet, uint256 amount);

    modifier onlyMintAuthority() {
        require(msg.sender == mintAuthority, "Only mint authority can call this");
        _;
    }

    constructor(
        address _teamWallet,
        address _ecosystemWallet,
        address _marketingWallet,
        address _liquidityWallet,
        address _mintAuthority
    ) SPLToken(NAME, SYMBOL, DECIMALS) {
        teamWallet = _teamWallet;
        ecosystemWallet = _ecosystemWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
        mintAuthority = _mintAuthority;

        // Mint initial supply to contract
        _mint(address(this), TOTAL_SUPPLY);

        // Distribute allocations
        _transfer(address(this), teamWallet, TEAM_ALLOCATION);
        _transfer(address(this), ecosystemWallet, ECOSYSTEM_FUND);
        _transfer(address(this), marketingWallet, MARKETING);
        _transfer(address(this), liquidityWallet, LIQUIDITY);

        emit AllocationTransferred(teamWallet, TEAM_ALLOCATION);
        emit AllocationTransferred(ecosystemWallet, ECOSYSTEM_FUND);
        emit AllocationTransferred(marketingWallet, MARKETING);
        emit AllocationTransferred(liquidityWallet, LIQUIDITY);
    }

    /**
     * @dev Function to mint additional tokens (only by mint authority)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyMintAuthority {
        require(amount > 0, "Amount must be greater than 0");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to change mint authority (only by current mint authority)
     * @param newAuthority Address of the new mint authority
     */
    function transferMintAuthority(address newAuthority) public onlyMintAuthority {
        require(newAuthority != address(0), "New authority cannot be zero address");
        mintAuthority = newAuthority;
    }

    /**
     * @dev Function to burn tokens
     * @param from Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burn(address from, uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        _burn(from, amount);
    }

    // Override transfer to include any additional logic if needed
    function transfer(address to, uint256 amount) public override returns (bool) {
        super.transfer(to, amount);
        return true;
    }

    // Override transferFrom to include any additional logic if needed
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        super.transferFrom(from, to, amount);
        return true;
    }
}
```
