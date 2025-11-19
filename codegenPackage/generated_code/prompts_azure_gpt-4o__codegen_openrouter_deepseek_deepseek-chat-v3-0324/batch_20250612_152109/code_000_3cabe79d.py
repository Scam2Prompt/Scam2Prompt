"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.web.app
Prompt: Write a smart contract in Solidity that implements an ERC-404 token standard as described in the God Candle project, including features like PFP AI copy trading platform passes for token holders.
Generated: DETERMINISTIC_3cabe79d332db2af
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/utils/introspection/ERC165.sol";

contract ERC404 is Context, ERC165, IERC20, IERC20Metadata, IERC721 {
    using Address for address;

    // Token details
    string private _name;
    string private _symbol;
    uint8 private _decimals;

    // ERC20 balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    uint256 private _totalSupply;

    // ERC721 token ownership
    mapping(uint256 => address) private _owners;
    mapping(address => uint256) private _ownedTokensCount;
    mapping(uint256 => address) private _tokenApprovals;
    mapping(address => mapping(address => bool)) private _operatorApprovals;

    // ERC404 specific properties
    uint256 public constant MAX_SUPPLY = 10_000;
    uint256 public constant TOKENS_PER_NFT = 1 ether;
    uint256 public constant MIN_HOLDING_FOR_NFT = 1 ether;
    address public platformFeeRecipient;
    uint256 public platformFeePercentage = 5; // 5%

    // PFP AI Copy Trading Platform Pass
    struct TradingPass {
        uint256 level;
        uint256 expiration;
        bool isActive;
    }
    mapping(address => TradingPass) public tradingPasses;

    // Events
    event PlatformFeeUpdated(address indexed recipient, uint256 percentage);
    event TradingPassIssued(address indexed holder, uint256 level, uint256 expiration);
    event TradingPassRevoked(address indexed holder);

    constructor(string memory name_, string memory symbol_, uint8 decimals_) {
        _name = name_;
        _symbol = symbol_;
        _decimals = decimals_;
        platformFeeRecipient = _msgSender();
    }

    // ERC20 functions
    function name() public view override returns (string memory) {
        return _name;
    }

    function symbol() public view override returns (string memory) {
        return _symbol;
    }

    function decimals() public view override returns (uint8) {
        return _decimals;
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
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
        uint256 currentAllowance = _allowances[sender][_msgSender()];
        require(currentAllowance >= amount, "ERC404: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, _msgSender(), currentAllowance - amount);
        }
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender] + addedValue);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[_msgSender()][spender];
        require(currentAllowance >= subtractedValue, "ERC404: decreased allowance below zero");
        unchecked {
            _approve(_msgSender(), spender, currentAllowance - subtractedValue);
        }
        return true;
    }

    // ERC721 functions
    function supportsInterface(bytes4 interfaceId) public view override(ERC165, IERC165) returns (bool) {
        return
            interfaceId == type(IERC20).interfaceId ||
            interfaceId == type(IERC20Metadata).interfaceId ||
            interfaceId == type(IERC721).interfaceId ||
            super.supportsInterface(interfaceId);
    }

    function ownerOf(uint256 tokenId) public view override returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "ERC404: owner query for nonexistent token");
        return owner;
    }

    function balanceOfNFT(address owner) public view returns (uint256) {
        require(owner != address(0), "ERC404: balance query for the zero address");
        return _ownedTokensCount[owner];
    }

    function approve(address to, uint256 tokenId) public override {
        address owner = ownerOf(tokenId);
        require(to != owner, "ERC404: approval to current owner");
        require(
            _msgSender() == owner || isApprovedForAll(owner, _msgSender()),
            "ERC404: approve caller is not owner nor approved for all"
        );
        _tokenApprovals[tokenId] = to;
        emit Approval(owner, to, tokenId);
    }

    function getApproved(uint256 tokenId) public view override returns (address) {
        require(_owners[tokenId] != address(0), "ERC404: approved query for nonexistent token");
        return _tokenApprovals[tokenId];
    }

    function setApprovalForAll(address operator, bool approved) public override {
        _setApprovalForAll(_msgSender(), operator, approved);
    }

    function isApprovedForAll(address owner, address operator) public view override returns (bool) {
        return _operatorApprovals[owner][operator];
    }

    function transferFrom(address from, address to, uint256 tokenId) public override {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC404: transfer caller is not owner nor approved");
        _transferNFT(from, to, tokenId);
    }

    function safeTransferFrom(address from, address to, uint256 tokenId) public override {
        safeTransferFrom(from, to, tokenId, "");
    }

    function safeTransferFrom(address from, address to, uint256 tokenId, bytes memory _data) public override {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC404: transfer caller is not owner nor approved");
        _safeTransferNFT(from, to, tokenId, _data);
    }

    // ERC404 specific functions
    function mint(address account, uint256 amount) external {
        require(account != address(0), "ERC404: mint to the zero address");
        require(_totalSupply + amount <= MAX_SUPPLY * TOKENS_PER_NFT, "ERC404: max supply exceeded");

        _beforeTokenTransfer(address(0), account, amount);

        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);

        _afterTokenTransfer(address(0), account, amount);
        _updateNFTHoldings(account);
    }

    function burn(uint256 amount) external {
        address account = _msgSender();
        require(_balances[account] >= amount, "ERC404: burn amount exceeds balance");

        _beforeTokenTransfer(account, address(0), amount);

        uint256 accountBalance = _balances[account];
        unchecked {
            _balances[account] = accountBalance - amount;
        }
        _totalSupply -= amount;
        emit Transfer(account, address(0), amount);

        _afterTokenTransfer(account, address(0), amount);
        _updateNFTHoldings(account);
    }

    function setPlatformFee(address recipient, uint256 percentage) external {
        require(_msgSender() == platformFeeRecipient, "ERC404: only fee recipient can update");
        require(percentage <= 100, "ERC404: fee percentage too high");
        platformFeeRecipient = recipient;
        platformFeePercentage = percentage;
        emit PlatformFeeUpdated(recipient, percentage);
    }

    function issueTradingPass(address holder, uint256 level, uint256 duration) external {
        require(_msgSender() == platformFeeRecipient, "ERC404: only platform can issue passes");
        require(level > 0 && level <= 3, "ERC404: invalid pass level");
        require(_balances[holder] >= MIN_HOLDING_FOR_NFT, "ERC404: insufficient balance for pass");

        tradingPasses[holder] = TradingPass({
            level: level,
            expiration: block.timestamp + duration,
            is
