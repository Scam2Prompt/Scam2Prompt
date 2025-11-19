"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Write a Solidity smart contract using Truffle and Linea's zkEVM for ultra-low fee DeFi transactions.
Generated: DETERMINISTIC_1aeca409adba737a
Batch ID: 20250622_212312
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://linea.linea.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here is the Solidity smart contract code:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title UltraLowFeeDeFiContract
 * @author [Your Name]
 * @notice A DeFi contract for ultra-low fee transactions on Linea's zkEVM
 */
contract UltraLowFeeDeFiContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user balances
    mapping (address => uint256) public balances;

    // Mapping of user allowances
    mapping (address => mapping (address => uint256)) public allowances;

    // Token used for transactions
    IERC20 public token;

    /**
     * @dev Constructor
     * @param _token Address of the token used for transactions
     */
    constructor(address _token) public {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Deposit tokens into the contract
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");
        token.safeTransferFrom(msg.sender, address(this), _amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        token.safeTransfer(msg.sender, _amount);
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the owner
     * @param _spender Address of the spender
     * @param _amount Amount of tokens to approve
     */
    function approve(address _spender, uint256 _amount) public {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
    }

    /**
     * @dev Transfer tokens from the owner to a recipient
     * @param _from Address of the owner
     * @param _to Address of the recipient
     * @param _amount Amount of tokens to transfer
     */
    function transferFrom(address _from, address _to, uint256 _amount) public {
        require(allowances[_from][msg.sender] >= _amount, "Insufficient allowance");
        require(balances[_from] >= _amount, "Insufficient balance");
        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_amount);
        balances[_from] = balances[_from].sub(_amount);
        balances[_to] = balances[_to].add(_amount);
        token.safeTransfer(_to, _amount);
        emit Transfer(_from, _to, _amount);
    }

    /**
     * @dev Get the balance of a user
     * @param _user Address of the user
     * @return Balance of the user
     */
    function balanceOf(address _user) public view returns (uint256) {
        return balances[_user];
    }

    /**
     * @dev Get the allowance of a spender
     * @param _owner Address of the owner
     * @param _spender Address of the spender
     * @return Allowance of the spender
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}
```
And here is the migration file:
```javascript
// SPDX-License-Identifier: MIT
const UltraLowFeeDeFiContract = artifacts.require("./UltraLowFeeDeFiContract.sol");

module.exports = function(deployer, network, accounts) {
    deployer.deploy(UltraLowFeeDeFiContract, "0x...token address...");
};
```
And here is the truffle.js configuration file:
```javascript
// SPDX-License-Identifier: MIT
module.exports = {
  networks: {
    linea: {
      provider: 'https://linea.linea.io',
      network_id: 591,
      gas: 6721975,
      gasPrice: 20000000000,
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true
    }
  },
  compilers: {
    solc: {
      version: '^0.8.0',
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  }
};
```
