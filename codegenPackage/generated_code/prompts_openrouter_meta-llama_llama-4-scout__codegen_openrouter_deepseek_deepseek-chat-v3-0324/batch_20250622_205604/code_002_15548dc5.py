"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Explain the concept of stablecoins on Ethereum and provide an example of how to use them in a DeFi application.
Generated: DETERMINISTIC_15548dc510103c41
Batch ID: 20250622_205604
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

// Import OpenZeppelin contracts for ERC20 and SafeMath
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StablecoinDeFiExample
 * @dev Demonstrates basic DeFi operations with stablecoins on Ethereum
 */
contract StablecoinDeFiExample {
    using SafeMath for uint256;
    
    // Addresses of popular stablecoins
    address public constant DAI_ADDRESS = 0x6B175474E89094C44Da98b954EedeAC495271d0F;
    address public constant USDC_ADDRESS = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    address public constant USDT_ADDRESS = 0xdAC17F958D2ee523a2206206994597C13D831ec7;
    
    // Instance of stablecoin contracts
    IERC20 public dai;
    IERC20 public usdc;
    IERC20 public usdt;
    
    // Mapping to track user balances
    mapping(address => uint256) public userBalances;
    
    event Deposit(address indexed user, address indexed stablecoin, uint256 amount);
    event Withdraw(address indexed user, address indexed stablecoin, uint256 amount);
    event Swap(address indexed user, address fromStablecoin, address toStablecoin, uint256 amountIn, uint256 amountOut);
    
    constructor() {
        dai = IERC20(DAI_ADDRESS);
        usdc = IERC20(USDC_ADDRESS);
        usdt = IERC20(USDT_ADDRESS);
    }
    
    /**
     * @dev Deposit stablecoins into the contract
     * @param _stablecoin Address of the stablecoin to deposit
     * @param _amount Amount to deposit
     */
    function deposit(address _stablecoin, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            _stablecoin == DAI_ADDRESS || 
            _stablecoin == USDC_ADDRESS || 
            _stablecoin == USDT_ADDRESS,
            "Unsupported stablecoin"
        );
        
        IERC20 stablecoin = IERC20(_stablecoin);
        
        // Transfer stablecoins from user to contract
        require(
            stablecoin.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );
        
        // Update user balance
        userBalances[msg.sender] = userBalances[msg.sender].add(_amount);
        
        emit Deposit(msg.sender, _stablecoin, _amount);
    }
    
    /**
     * @dev Withdraw stablecoins from the contract
     * @param _stablecoin Address of the stablecoin to withdraw
     * @param _amount Amount to withdraw
     */
    function withdraw(address _stablecoin, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");
        require(
            _stablecoin == DAI_ADDRESS || 
            _stablecoin == USDC_ADDRESS || 
            _stablecoin == USDT_ADDRESS,
            "Unsupported stablecoin"
        );
        
        IERC20 stablecoin = IERC20(_stablecoin);
        
        // Update user balance before transfer to prevent re-entrancy
        userBalances[msg.sender] = userBalances[msg.sender].sub(_amount);
        
        // Transfer stablecoins back to user
        require(
            stablecoin.transfer(msg.sender, _amount),
            "Transfer failed"
        );
        
        emit Withdraw(msg.sender, _stablecoin, _amount);
    }
    
    /**
     * @dev Simulate a simple stablecoin swap (1:1 ratio for demonstration)
     * @param _fromStablecoin Address of stablecoin to swap from
     * @param _toStablecoin Address of stablecoin to swap to
     * @param _amount Amount to swap
     */
    function swap(address _fromStablecoin, address _toStablecoin, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");
        require(
            (_fromStablecoin == DAI_ADDRESS || _fromStablecoin == USDC_ADDRESS || _fromStablecoin == USDT_ADDRESS) &&
            (_toStablecoin == DAI_ADDRESS || _toStablecoin == USDC_ADDRESS || _toStablecoin == USDT_ADDRESS),
            "Unsupported stablecoin pair"
        );
        require(_fromStablecoin != _toStablecoin, "Cannot swap same stablecoin");
        
        // Update balances (1:1 ratio for simplicity - real implementation would use price oracles)
        userBalances[msg.sender] = userBalances[msg.sender].sub(_amount);
        
        emit Swap(msg.sender, _fromStablecoin, _toStablecoin, _amount, _amount);
    }
    
    /**
     * @dev Get user balance in the contract
     * @return User's balance
     */
    function getBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }
    
    /**
     * @dev Get contract's balance of a specific stablecoin
     * @param _stablecoin Address of the stablecoin
     * @return Contract's balance of the stablecoin
     */
    function getContractBalance(address _stablecoin) external view returns (uint256) {
        require(
            _stablecoin == DAI_ADDRESS || 
            _stablecoin == USDC_ADDRESS || 
            _stablecoin == USDT_ADDRESS,
            "Unsupported stablecoin"
        );
        
        IERC20 stablecoin = IERC20(_stablecoin);
        return stablecoin.balanceOf(address(this));
    }
}
```
