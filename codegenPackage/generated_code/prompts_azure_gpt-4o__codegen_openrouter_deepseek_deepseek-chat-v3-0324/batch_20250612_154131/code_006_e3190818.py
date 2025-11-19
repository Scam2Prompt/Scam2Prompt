"""
Generated Code Metadata:
========================
Original URL: https://holdexofficial.com
Prompt: Write a Solidity contract to implement a new DeFi protocol with limited products and global expansion potential, as mentioned on Holdex Official.
Generated: DETERMINISTIC_e31908185f4e33a6
Batch ID: 20250612_154131
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title HoldexDeFiProtocol
 * @dev A DeFi protocol with limited products and global expansion potential
 */
contract HoldexDeFiProtocol is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a product
    struct Product {
        uint256 id;
        string name;
        uint256 apy; // Annual Percentage Yield (in basis points, e.g., 500 = 5%)
        uint256 minDeposit;
        uint256 maxDeposit;
        uint256 lockPeriod; // in seconds
        bool isActive;
    }

    // Struct to represent a user's deposit
    struct Deposit {
        uint256 productId;
        uint256 amount;
        uint256 depositTime;
        uint256 claimedRewards;
        bool isActive;
    }

    // Mapping of product ID to Product
    mapping(uint256 => Product) public products;

    // Mapping of user address to their deposits
    mapping(address => Deposit[]) public userDeposits;

    // Supported ERC20 tokens
    mapping(address => bool) public supportedTokens;

    // Total TVL (Total Value Locked)
    uint256 public totalValueLocked;

    // Events
    event ProductAdded(uint256 indexed productId, string name, uint256 apy);
    event ProductUpdated(uint256 indexed productId, bool isActive);
    event Deposited(address indexed user, uint256 productId, uint256 amount);
    event Withdrawn(address indexed user, uint256 productId, uint256 amount, uint256 rewards);
    event TokenSupported(address indexed token, bool isSupported);

    /**
     * @dev Add a new product to the protocol
     * @param _id Product ID
     * @param _name Product name
     * @param _apy Annual Percentage Yield (in basis points)
     * @param _minDeposit Minimum deposit amount
     * @param _maxDeposit Maximum deposit amount
     * @param _lockPeriod Lock period in seconds
     */
    function addProduct(
        uint256 _id,
        string memory _name,
        uint256 _apy,
        uint256 _minDeposit,
        uint256 _maxDeposit,
        uint256 _lockPeriod
    ) external onlyOwner {
        require(products[_id].id == 0, "Product already exists");
        require(_apy > 0, "APY must be greater than 0");
        require(_minDeposit > 0, "Min deposit must be greater than 0");
        require(_maxDeposit > _minDeposit, "Max deposit must be greater than min deposit");

        products[_id] = Product({
            id: _id,
            name: _name,
            apy: _apy,
            minDeposit: _minDeposit,
            maxDeposit: _maxDeposit,
            lockPeriod: _lockPeriod,
            isActive: true
        });

        emit ProductAdded(_id, _name, _apy);
    }

    /**
     * @dev Update product status
     * @param _productId Product ID
     * @param _isActive Whether the product is active
     */
    function updateProductStatus(uint256 _productId, bool _isActive) external onlyOwner {
        require(products[_productId].id != 0, "Product does not exist");
        products[_productId].isActive = _isActive;
        emit ProductUpdated(_productId, _isActive);
    }

    /**
     * @dev Add or remove supported token
     * @param _token Token address
     * @param _isSupported Whether the token is supported
     */
    function setSupportedToken(address _token, bool _isSupported) external onlyOwner {
        supportedTokens[_token] = _isSupported;
        emit TokenSupported(_token, _isSupported);
    }

    /**
     * @dev Deposit tokens into a product
     * @param _productId Product ID
     * @param _amount Amount to deposit
     * @param _token Token address
     */
    function deposit(
        uint256 _productId,
        uint256 _amount,
        address _token
    ) external nonReentrant {
        require(products[_productId].id != 0, "Product does not exist");
        require(products[_productId].isActive, "Product is not active");
        require(supportedTokens[_token], "Token not supported");
        require(_amount >= products[_productId].minDeposit, "Amount below minimum");
        require(_amount <= products[_productId].maxDeposit, "Amount exceeds maximum");

        IERC20 token = IERC20(_token);
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        userDeposits[msg.sender].push(Deposit({
            productId: _productId,
            amount: _amount,
            depositTime: block.timestamp,
            claimedRewards: 0,
            isActive: true
        }));

        totalValueLocked = totalValueLocked.add(_amount);
        emit Deposited(msg.sender, _productId, _amount);
    }

    /**
     * @dev Withdraw deposit and claim rewards
     * @param _depositIndex Index of the deposit in user's deposits array
     * @param _token Token address
     */
    function withdraw(uint256 _depositIndex, address _token) external nonReentrant {
        require(_depositIndex < userDeposits[msg.sender].length, "Invalid deposit index");
        Deposit storage userDeposit = userDeposits[msg.sender][_depositIndex];
        require(userDeposit.isActive, "Deposit already withdrawn");

        Product memory product = products[userDeposit.productId];
        require(block.timestamp >= userDeposit.depositTime.add(product.lockPeriod), "Lock period not ended");

        uint256 rewards = calculateRewards(msg.sender, _depositIndex);
        uint256 totalAmount = userDeposit.amount.add(rewards);

        IERC20 token = IERC20(_token);
        require(token.transfer(msg.sender, totalAmount), "Transfer failed");

        userDeposit.isActive = false;
        userDeposit.claimedRewards = rewards;
        totalValueLocked = totalValueLocked.sub(userDeposit.amount);

        emit Withdrawn(msg.sender, userDeposit.productId, userDeposit.amount, rewards);
    }

    /**
     * @dev Calculate rewards for a deposit
     * @param _user User address
     * @param _depositIndex Index of the deposit in user's deposits array
     * @return rewards Calculated rewards
     */
    function calculateRewards(address _user, uint256 _depositIndex) public view returns (uint256) {
        require(_depositIndex < userDeposits[_user].length, "Invalid deposit index");
        Deposit memory userDeposit = userDeposits[_user][_depositIndex];
        require(userDeposit.isActive, "Deposit already withdrawn");

        Product memory product = products[userDeposit.productId];
        uint256 timeElapsed = block.timestamp.sub(userDeposit.depositTime);
        uint256 rewards = userDeposit.amount.mul(product.apy).mul(timeElapsed).div(365 days).div(10000);

        return rewards;
    }

    /**
     * @dev Get user's active deposits count
     * @param _user User address
     * @return count Number of active deposits
     */
    function getUserActiveDepositsCount(address _user) external view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < userDeposits[_user].length; i++) {
            if (userDeposits[_user][i].isActive) {
                count++;
            }
        }
        return count;
    }

    /**
     * @dev Emergency withdraw all funds (owner only)
     * @param _token Token address
     */
    function emergencyWithdraw(address _token) external onlyOwner {
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
