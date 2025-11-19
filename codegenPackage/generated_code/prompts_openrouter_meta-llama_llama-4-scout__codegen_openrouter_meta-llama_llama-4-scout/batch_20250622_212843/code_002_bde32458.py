"""
Generated Code Metadata:
========================
Original URL: https://xenophon.finance
Prompt: Generate a smart contract code for a DeFi application that uses a wallet connection feature, as seen on Xenophon Finance.
Generated: DETERMINISTIC_bde32458fdab900e
Batch ID: 20250622_212843
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WalletConnectionDeFiContract
 * @author [Your Name]
 * @notice A DeFi smart contract with wallet connection feature
 */
contract WalletConnectionDeFiContract is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Mapping of wallet addresses to their respective balances
    mapping (address => uint256) public balances;

    // Mapping of wallet addresses to their respective allowances
    mapping (address => mapping (address => uint256)) public allowances;

    // ERC20 token instance
    IERC20 public token;

    // Event emitted when a wallet connects
    event WalletConnected(address indexed wallet);

    // Event emitted when a wallet disconnects
    event WalletDisconnected(address indexed wallet);

    // Event emitted when a transfer occurs
    event Transfer(address indexed from, address indexed to, uint256 amount);

    // Event emitted when an allowance is updated
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    /**
     * @notice Constructor
     * @param _tokenAddress Address of the ERC20 token
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }

    /**
     * @notice Connect a wallet to the contract
     */
    function connectWallet() public {
        require(balances[msg.sender] == 0, "Wallet already connected");
        balances[msg.sender] = 0;
        emit WalletConnected(msg.sender);
    }

    /**
     * @notice Disconnect a wallet from the contract
     */
    function disconnectWallet() public {
        require(balances[msg.sender] > 0, "Wallet not connected");
        balances[msg.sender] = 0;
        emit WalletDisconnected(msg.sender);
    }

    /**
     * @notice Deposit tokens into the contract
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        balances[msg.sender] = balances[msg.sender].add(_amount);
    }

    /**
     * @notice Withdraw tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }

    /**
     * @notice Transfer tokens to another wallet
     * @param _to Address of the recipient wallet
     * @param _amount Amount of tokens to transfer
     */
    function transfer(address _to, uint256 _amount) public {
        require(_to != address(0), "Recipient address cannot be zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        balances[_to] = balances[_to].add(_amount);
        emit Transfer(msg.sender, _to, _amount);
    }

    /**
     * @notice Approve another wallet to spend tokens on behalf of the owner
     * @param _spender Address of the spender wallet
     * @param _amount Amount of tokens to approve
     */
    function approve(address _spender, uint256 _amount) public {
        require(_spender != address(0), "Spender address cannot be zero");
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
    }

    /**
     * @notice Transfer tokens from one wallet to another on behalf of the owner
     * @param _from Address of the owner wallet
     * @param _to Address of the recipient wallet
     * @param _amount Amount of tokens to transfer
     */
    function transferFrom(address _from, address _to, uint256 _amount) public {
        require(_from != address(0), "Owner address cannot be zero");
        require(_to != address(0), "Recipient address cannot be zero");
        require(allowances[_from][msg.sender] >= _amount, "Insufficient allowance");
        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_amount);
        balances[_from] = balances[_from].sub(_amount);
        balances[_to] = balances[_to].add(_amount);
        emit Transfer(_from, _to, _amount);
    }

    /**
     * @notice Get the balance of a wallet
     * @param _wallet Address of the wallet
     * @return Balance of the wallet
     */
    function getBalance(address _wallet) public view returns (uint256) {
        return balances[_wallet];
    }

    /**
     * @notice Get the allowance of a wallet
     * @param _owner Address of the owner wallet
     * @param _spender Address of the spender wallet
     * @return Allowance of the wallet
     */
    function getAllowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
