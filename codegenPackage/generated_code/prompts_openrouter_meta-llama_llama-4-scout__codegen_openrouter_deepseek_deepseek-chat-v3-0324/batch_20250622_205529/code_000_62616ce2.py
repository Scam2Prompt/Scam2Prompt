"""
Generated Code Metadata:
========================
Original URL: https://synthesizations.netlify.app
Prompt: Write a code snippet to implement a decentralized protocol for syncing non-custodial wallets across Ethereum, Binance, and Polygon networks.
Generated: DETERMINISTIC_62616ce293989654
Batch ID: 20250622_205529
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

import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract WalletSync is Ownable, ReentrancyGuard {
    using Address for address;

    enum Network { Ethereum, Binance, Polygon }

    struct Wallet {
        address owner;
        Network network;
        uint256 lastSyncBlock;
        bool isActive;
    }

    mapping(address => Wallet) public wallets;
    mapping(address => mapping(Network => bool)) public walletExists;
    mapping(address => bytes32) public walletHashes;

    event WalletRegistered(address indexed owner, Network network);
    event WalletSynced(address indexed owner, Network network, uint256 blockNumber);
    event FundsWithdrawn(address indexed owner, address token, uint256 amount);

    modifier onlyWalletOwner(address _wallet) {
        require(wallets[_wallet].owner == msg.sender, "WalletSync: caller is not the owner");
        _;
    }

    modifier walletNotExists(address _wallet, Network _network) {
        require(!walletExists[_wallet][_network], "WalletSync: wallet already exists");
        _;
    }

    function registerWallet(address _wallet, Network _network) 
        external 
        walletNotExists(_wallet, _network)
    {
        require(_wallet != address(0), "WalletSync: invalid wallet address");
        
        wallets[_wallet] = Wallet({
            owner: msg.sender,
            network: _network,
            lastSyncBlock: block.number,
            isActive: true
        });

        walletExists[_wallet][_network] = true;
        walletHashes[_wallet] = keccak256(abi.encodePacked(_wallet, _network));

        emit WalletRegistered(_wallet, _network);
    }

    function syncWallet(address _wallet) 
        external 
        onlyWalletOwner(_wallet)
        nonReentrant
    {
        require(wallets[_wallet].isActive, "WalletSync: wallet is not active");
        
        wallets[_wallet].lastSyncBlock = block.number;
        emit WalletSynced(_wallet, wallets[_wallet].network, block.number);
    }

    function withdrawFunds(address _token, uint256 _amount) 
        external 
        onlyWalletOwner(msg.sender)
        nonReentrant
    {
        require(_amount > 0, "WalletSync: amount must be greater than 0");
        
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= _amount, "WalletSync: insufficient contract balance");

        token.transfer(msg.sender, _amount);
        emit FundsWithdrawn(msg.sender, _token, _amount);
    }

    function getWalletHash(address _wallet) external view returns (bytes32) {
        return walletHashes[_wallet];
    }

    function deactivateWallet(address _wallet) external onlyWalletOwner(_wallet) {
        wallets[_wallet].isActive = false;
    }

    function activateWallet(address _wallet) external onlyWalletOwner(_wallet) {
        wallets[_wallet].isActive = true;
    }
}
```
