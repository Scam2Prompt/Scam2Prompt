"""
Generated Code Metadata:
========================
Original URL: https://make1518999.cc
Prompt: Generate a code example for handling USDT approval and transfer operations in a blockchain asset management application.
Generated: DETERMINISTIC_6893b86ac8caa289
Batch ID: 20250612_162629
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

// Interface for ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract USDTManager {
    address public owner;
    IERC20 public usdtToken;

    // Events for tracking operations
    event ApprovalGiven(address indexed spender, uint256 amount);
    event TransferCompleted(address indexed from, address indexed to, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the contract with USDT token address
     * @param _usdtAddress Address of the USDT token contract
     */
    constructor(address _usdtAddress) {
        require(_usdtAddress != address(0), "Invalid token address");
        owner = msg.sender;
        usdtToken = IERC20(_usdtAddress);
    }

    /**
     * @dev Approves USDT spending by another address
     * @param _spender Address to approve for spending
     * @param _amount Amount of USDT to approve
     */
    function approveUSDT(address _spender, uint256 _amount) external onlyOwner {
        require(_spender != address(0), "Invalid spender address");
        require(_amount > 0, "Amount must be greater than zero");

        bool success = usdtToken.approve(_spender, _amount);
        require(success, "Approval failed");

        emit ApprovalGiven(_spender, _amount);
    }

    /**
     * @dev Transfers USDT from the contract to a recipient
     * @param _recipient Address to receive USDT
     * @param _amount Amount of USDT to transfer
     */
    function transferUSDT(address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");
        require(usdtToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        bool success = usdtToken.transfer(_recipient, _amount);
        require(success, "Transfer failed");

        emit TransferCompleted(address(this), _recipient, _amount);
    }

    /**
     * @dev Transfers USDT from a sender to a recipient using allowance
     * @param _sender Address sending USDT
     * @param _recipient Address to receive USDT
     * @param _amount Amount of USDT to transfer
     */
    function transferFromUSDT(address _sender, address _recipient, uint256 _amount) external onlyOwner {
        require(_sender != address(0), "Invalid sender address");
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");
        require(usdtToken.allowance(_sender, address(this)) >= _amount, "Insufficient allowance");

        bool success = usdtToken.transferFrom(_sender, _recipient, _amount);
        require(success, "TransferFrom failed");

        emit TransferCompleted(_sender, _recipient, _amount);
    }

    /**
     * @dev Gets the USDT balance of this contract
     * @return Current USDT balance
     */
    function getContractUSDTBalance() external view returns (uint256) {
        return usdtToken.balanceOf(address(this));
    }

    /**
     * @dev Gets the USDT allowance for this contract from a specific owner
     * @param _owner Address of the token owner
     * @return Current allowance
     */
    function getAllowance(address _owner) external view returns (uint256) {
        return usdtToken.allowance(_owner, address(this));
    }

    /**
     * @dev Transfers contract ownership to a new address
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}
```
