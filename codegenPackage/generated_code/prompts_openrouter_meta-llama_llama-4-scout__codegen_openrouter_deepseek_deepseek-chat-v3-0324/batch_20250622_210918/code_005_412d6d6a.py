"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Design an ERC404 token standard implementation that allows for seamless interaction with decentralized exchanges like Uniswap, using $GOFURS as a reference.
Generated: DETERMINISTIC_412d6d6a82b710b3
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/introspection/ERC165.sol";

contract GOFURS is Context, ERC165, IERC20, IERC721, IERC721Metadata {
    using Address for address;
    using Strings for uint256;

    // Token name
    string private _name;

    // Token symbol
    string private _symbol;

    // Total supply
    uint256 private _totalSupply;

    // Decimals for ERC20
    uint8 private constant _decimals = 18;

    // Base URI for ERC721 metadata
    string private _baseURI;

    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;

    // Mapping owner address to token count
    mapping(address => uint256) private _balances;

    // Mapping from token ID to approved address
    mapping(uint256 => address) private _tokenApprovals;

    // Mapping from owner to operator approvals
    mapping(address => mapping(address => bool)) private _operatorApprovals;

    // ERC20 balances
    mapping(address => uint256) private _erc20Balances;

    // ERC20 allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Mapping from owner to owned token IDs
    mapping(address => uint256[]) private _ownedTokens;

    // Mapping from token ID to index of the owner tokens list
    mapping(uint256 => uint256) private _ownedTokensIndex;

    // Events
    event Mint(address indexed to, uint256 amount, uint256[] tokenIds);
    event Burn(address indexed from, uint256 amount, uint256[] tokenIds);

    constructor(string memory name_, string memory symbol_, string memory baseURI_) {
        _name = name_;
        _symbol = symbol_;
        _baseURI = baseURI_;
    }

    // ERC20 functions
    function name() public view override returns (string memory) {
        return _name;
    }

    function symbol() public view override returns (string memory) {
        return _symbol;
    }

    function decimals() public pure returns (uint8) {
        return _decimals;
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _erc20Balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(_msgSender(), spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), _allowances[sender][_msgSender()] - amount);
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender] + addedValue);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender] - subtractedValue);
        return true;
    }

    // ERC721 functions
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC165, IERC165) returns (bool) {
        return
            interfaceId == type(IERC20).interfaceId ||
            interfaceId == type(IERC721).interfaceId ||
            interfaceId == type(IERC721Metadata).interfaceId ||
            super.supportsInterface(interfaceId);
    }

    function balanceOf(address owner) public view override returns (uint256) {
        require(owner != address(0), "ERC721: balance query for the zero address");
        return _balances[owner];
    }

    function ownerOf(uint256 tokenId) public view override returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "ERC721: owner query for nonexistent token");
        return owner;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return string(abi.encodePacked(_baseURI, tokenId.toString()));
    }

    function approve(address to, uint256 tokenId) public override {
        address owner = ownerOf(tokenId);
        require(to != owner, "ERC721: approval to current owner");
        require(
            _msgSender() == owner || isApprovedForAll(owner, _msgSender()),
            "ERC721: approve caller is not owner nor approved for all"
        );
        _approve(to, tokenId);
    }

    function getApproved(uint256 tokenId) public view override returns (address) {
        require(_exists(tokenId), "ERC721: approved query for nonexistent token");
        return _tokenApprovals[tokenId];
    }

    function setApprovalForAll(address operator, bool approved) public override {
        _setApprovalForAll(_msgSender(), operator, approved);
    }

    function isApprovedForAll(address owner, address operator) public view override returns (bool) {
        return _operatorApprovals[owner][operator];
    }

    function transferFrom(address from, address to, uint256 tokenId) public override {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: transfer caller is not owner nor approved");
        _transfer(from, to, tokenId);
    }

    function safeTransferFrom(address from, address to, uint256 tokenId) public override {
        safeTransferFrom(from, to, tokenId, "");
    }

    function safeTransferFrom(address from, address to, uint256 tokenId, bytes memory _data) public override {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: transfer caller is not owner nor approved");
        _safeTransfer(from, to, tokenId, _data);
    }

    // ERC404 functions
    function mint(address to, uint256 amount) public {
        require(to != address(0), "ERC404: mint to the zero address");
        require(amount > 0, "ERC404: mint amount must be positive");

        _totalSupply += amount;
        _erc20Balances[to] += amount;

        uint256[] memory tokenIds = new uint256[](amount);
        for (uint256 i = 0; i < amount; i++) {
            uint256 tokenId = _totalSupply - amount + i;
            _mintNFT(to, tokenId);
            tokenIds[i] = tokenId;
        }

        emit Transfer(address(0), to, amount);
        emit Mint(to, amount, tokenIds);
    }

    function burn(address from, uint256 amount) public {
        require(from != address(0), "ERC404: burn from the zero address");
        require(amount > 0, "ERC404: burn amount must be positive");
        require(_erc20Balances[from] >= amount, "ERC404: burn amount exceeds balance");

        _erc20Balances[from] -= amount;
        _totalSupply -= amount;

        uint256[] memory tokenIds = new uint256[](amount);
        for (uint256 i = 0; i < amount; i++) {
            uint256 tokenId = _ownedTokens[from][_ownedTokens[from].length - 1];
            _burnNFT(from, tokenId);
            tokenIds[i] = tokenId;
        }

        emit Transfer(from, address(0), amount);
        emit Burn(from, amount, tokenIds);
    }

    // Internal functions
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(_erc20Balances[sender] >= amount, "ERC20: transfer amount exceeds balance");

        _erc20Balances[sender] -= amount;
        _erc20Balances[recipient] += amount;

        uint256 fractionalPart = amount % (10 ** _decimals);
        uint256 wholeTokens = amount / (10 ** _decimals);

        if (wholeTokens > 0) {
