"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Create a smart contract for a personalized meme wallet that stores meme assets and OMEME tokens, ensuring compatibility with the Binance Smart Chain.
Generated: DETERMINISTIC_ff9831057772f4e6
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract OMEMEToken is IERC20 {
    string public constant name = "OMEME Token";
    string public constant symbol = "OMEME";
    uint8 public constant decimals = 18;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    uint256 private _totalSupply;

    constructor(uint256 initialSupply) {
        _mint(msg.sender, initialSupply);
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(_balances[sender] >= amount, "ERC20: transfer amount exceeds balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");

        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}

contract MemeWallet is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    OMEMEToken public omemeToken;
    mapping(uint256 => string) private _memeURIs;
    mapping(address => uint256[]) private _userMemes;

    event MemeMinted(address indexed owner, uint256 tokenId, string memeURI);
    event MemeShared(address indexed from, address indexed to, uint256 tokenId);
    event TokensDeposited(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    constructor(address omemeTokenAddress) ERC721("MemeWallet", "MEME") {
        omemeToken = OMEMEToken(omemeTokenAddress);
    }

    function mintMeme(string memory memeURI) public returns (uint256) {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        
        _mint(msg.sender, newTokenId);
        _memeURIs[newTokenId] = memeURI;
        _userMemes[msg.sender].push(newTokenId);

        emit MemeMinted(msg.sender, newTokenId, memeURI);
        return newTokenId;
    }

    function shareMeme(address to, uint256 tokenId) public {
        require(ownerOf(tokenId) == msg.sender, "You don't own this meme");
        safeTransferFrom(msg.sender, to, tokenId);
        
        // Remove from sender's list and add to recipient's list
        _removeFromUserMemes(msg.sender, tokenId);
        _userMemes[to].push(tokenId);

        emit MemeShared(msg.sender, to, tokenId);
    }

    function depositTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(omemeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit TokensDeposited(msg.sender, amount);
    }

    function withdrawTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(omemeToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(omemeToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit TokensWithdrawn(msg.sender, amount);
    }

    function getUserMemes(address user) public view returns (uint256[] memory) {
        return _userMemes[user];
    }

    function getMemeURI(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "Meme does not exist");
        return _memeURIs[tokenId];
    }

    function getTokenBalance(address user) public view returns (uint256) {
        return omemeToken.balanceOf(user);
    }

    function _removeFromUserMemes(address user, uint256 tokenId) private {
        uint256[] storage memes = _userMemes[user];
        for (uint256 i = 0; i < memes.length; i++) {
            if (memes[i] == tokenId) {
                memes[i] = memes[memes.length - 1];
                memes.pop();
                break;
            }
        }
    }

    // Emergency function to withdraw any ERC20 tokens sent to the contract
    function withdrawERC20(address tokenAddress) public onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
