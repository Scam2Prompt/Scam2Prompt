"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a Solidity smart contract code for an ERC404 token that automatically mints an NFT when the token balance exceeds 1 and burns it when the balance goes below 1.
Generated: DETERMINISTIC_b7341e7a57ae671b
Batch ID: 20250622_210918
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

// Importing the ERC20 interface and ERC721 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC404 Token Contract
contract ERC404Token is IERC20, Ownable {
    string public name = "ERC404 Token";
    string public symbol = "ERC404";
    uint8 public decimals = 18;
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // NFT Contract
    contract NFT is ERC721 {
        uint256 public tokenCounter;

        constructor() ERC721("NFT Token", "NFT") {
            tokenCounter = 0;
        }

        function mintNFT(address recipient) internal {
            _safeMint(recipient, tokenCounter);
            tokenCounter++;
        }

        function burnNFT(uint256 tokenId) internal {
            _burn(tokenId);
        }
    }

    NFT private nft;

    constructor() {
        nft = new NFT();
    }

    // ERC20 Functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        // Check balance and mint/burn NFT accordingly
        _checkAndMintOrBurnNFT(msg.sender);
        _checkAndMintOrBurnNFT(recipient);

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        // Check balance and mint/burn NFT accordingly
        _checkAndMintOrBurnNFT(sender);
        _checkAndMintOrBurnNFT(recipient);

        emit Transfer(sender, recipient, amount);
        return true;
    }

    function _checkAndMintOrBurnNFT(address account) internal {
        if (_balances[account] > 1) {
            nft.mintNFT(account);
        } else if (_balances[account] < 1) {
            // Assuming the NFT tokenId is the same as the account's balance
            // This is a simplification; in a real scenario, you would need to track token IDs
            nft.burnNFT(0); // Replace with actual tokenId logic
        }
    }

    // Additional functions for minting and burning ERC20 tokens
    function mint(uint256 amount) external onlyOwner {
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        emit Transfer(address(0), msg.sender, amount);
    }

    function burn(uint256 amount) external onlyOwner {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}
```
