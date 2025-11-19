"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Develop a simple smart contract in Solidity to create and manage meme coins on the Binance Smart Chain, similar to Oracle Meme's Meme Coin Generator.
Generated: DETERMINISTIC_7815043153e8e83d
Batch ID: 20250622_205836
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

contract MemeCoinFactory is Ownable {
    using SafeMath for uint256;

    struct MemeCoin {
        address tokenAddress;
        string name;
        string symbol;
        uint256 totalSupply;
        address creator;
    }

    uint256 public creationFee = 0.01 ether;
    MemeCoin[] public memeCoins;
    mapping(string => bool) private _symbolExists;

    event MemeCoinCreated(
        address indexed tokenAddress,
        string name,
        string symbol,
        uint256 totalSupply,
        address indexed creator
    );

    function setCreationFee(uint256 _fee) external onlyOwner {
        creationFee = _fee;
    }

    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function createMemeCoin(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply
    ) external payable returns (address) {
        require(msg.value >= creationFee, "Insufficient creation fee");
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");
        require(_totalSupply > 0, "Total supply must be positive");
        require(!_symbolExists[_symbol], "Symbol already exists");

        MemeCoinToken newToken = new MemeCoinToken(
            _name,
            _symbol,
            _totalSupply,
            msg.sender
        );

        MemeCoin memory newMemeCoin = MemeCoin({
            tokenAddress: address(newToken),
            name: _name,
            symbol: _symbol,
            totalSupply: _totalSupply,
            creator: msg.sender
        });

        memeCoins.push(newMemeCoin);
        _symbolExists[_symbol] = true;

        emit MemeCoinCreated(
            address(newToken),
            _name,
            _symbol,
            _totalSupply,
            msg.sender
        );

        return address(newToken);
    }

    function getMemeCoinsCount() external view returns (uint256) {
        return memeCoins.length;
    }
}

contract MemeCoinToken is ERC20, Ownable {
    using SafeMath for uint256;

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply,
        address _owner
    ) ERC20(_name, _symbol) {
        _mint(_owner, _totalSupply);
        transferOwnership(_owner);
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
