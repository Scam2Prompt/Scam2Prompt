"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layeralorg.pages.dev
Prompt: Write code to mint and redeem LayerAI Data Capsules as NFTs, ensuring compatibility with both ERC-20 and BEP-20 token standards.
Generated: DETERMINISTIC_8fcc7353d7ec6a65
Batch ID: 20250612_151141
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// LayerAI Data Capsule NFT Contract
contract LayerAIDataCapsule is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Mapping from token ID to URI
    mapping(uint256 => string) private _tokenURIs;

    // Counter for NFT token IDs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new capsule is minted
    event DataCapsuleMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);
    
    // Event emitted when a capsule is redeemed
    event DataCapsuleRedeemed(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the token name and symbol
    constructor() ERC721("LayerAI Data Capsule", "LADC") {}

    // Function to mint a new Data Capsule NFT
    function mintDataCapsule(string memory tokenURI) external onlyOwner returns (uint256) {
        require(bytes(tokenURI).length > 0, "Token URI must not be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        
        emit DataCapsuleMinted(msg.sender, tokenId, tokenURI);
        
        _tokenIdCounter.increment();
        return tokenId;
    }

    // Function to redeem a Data Capsule NFT
    function redeemDataCapsule(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");

        // Logic for redeeming the capsule
        _burn(tokenId);
        
        emit DataCapsuleRedeemed(msg.sender, tokenId);
    }

    // Internal function to set token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }
}

// Sample contract for ERC20 or BEP20 token standards
contract LayerAIToken is IERC20, Ownable {
    using SafeMath for uint256;

    string public constant name = "LayerAI Token";
    string public constant symbol = "LAI";
    uint8 public constant decimals = 18;

    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);
    
    // Constructor to initialize total supply
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = _totalSupply; // Assign total supply to the owner
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // ERC20 standard functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
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

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Mint to the zero address");
        
        _totalSupply = _totalSupply.add(amount);
        _balances[to] = _balances[to].add(amount);
        
        emit Mint(to, amount);
        emit Transfer(address(0), to, amount);
    }

    // Burn tokens
    function burn(uint256 amount) external {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");
        
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        
        emit Burn(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount);
    }
}
```

This code creates a LayerAI Data Capsule NFT contract and a LayerAI Token contract. The NFT contract includes functions for minting and redeeming data capsules, while the token contract adheres to ERC20/BEP20 standards with minting and burning functionalities.
