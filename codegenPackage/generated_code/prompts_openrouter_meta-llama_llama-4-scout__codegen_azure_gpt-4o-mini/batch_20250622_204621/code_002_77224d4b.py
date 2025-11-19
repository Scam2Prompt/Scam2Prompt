"""
Generated Code Metadata:
========================
Original URL: https://kernelprotocol-com.pages.dev
Prompt: "Generate a smart contract code in Solidity that utilizes Kernel Protocol's LRTs (krETH, ksETH, kUSD) for yield-bearing DeFi activities, including lending markets and yield markets."
Generated: DETERMINISTIC_77224d4bfb496250
Batch ID: 20250622_204621
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Kernel Protocol's LRTs
interface IKernalLRT {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getBalance(address account) external view returns (uint256);
}

// Smart contract for yield-bearing DeFi activities
contract YieldDeFiManager is Ownable {
    using SafeMath for uint256;

    // Addresses for Kernel Protocol's LRTs
    address public krETH;
    address public ksETH;
    address public kUSD;

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount, string lrt);
    event Withdrawn(address indexed user, uint256 amount, string lrt);

    // Constructor to set the addresses of the LRTs
    constructor(address _krETH, address _ksETH, address _kUSD) {
        krETH = _krETH;
        ksETH = _ksETH;
        kUSD = _kUSD;
    }

    // Function to deposit krETH into the lending market
    function depositKrETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(krETH).transferFrom(msg.sender, address(this), amount);
        IKernalLRT(krETH).deposit(amount);
        emit Deposited(msg.sender, amount, "krETH");
    }

    // Function to withdraw krETH from the lending market
    function withdrawKrETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IKernalLRT(krETH).withdraw(amount);
        IERC20(krETH).transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount, "krETH");
    }

    // Function to deposit ksETH into the yield market
    function depositKsETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(ksETH).transferFrom(msg.sender, address(this), amount);
        IKernalLRT(ksETH).deposit(amount);
        emit Deposited(msg.sender, amount, "ksETH");
    }

    // Function to withdraw ksETH from the yield market
    function withdrawKsETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IKernalLRT(ksETH).withdraw(amount);
        IERC20(ksETH).transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount, "ksETH");
    }

    // Function to deposit kUSD into the lending market
    function depositKUSD(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(kUSD).transferFrom(msg.sender, address(this), amount);
        IKernalLRT(kUSD).deposit(amount);
        emit Deposited(msg.sender, amount, "kUSD");
    }

    // Function to withdraw kUSD from the lending market
    function withdrawKUSD(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IKernalLRT(kUSD).withdraw(amount);
        IERC20(kUSD).transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount, "kUSD");
    }

    // Function to get the balance of a specific LRT for the contract
    function getBalance(string memory lrt) external view returns (uint256) {
        if (keccak256(abi.encodePacked(lrt)) == keccak256(abi.encodePacked("krETH"))) {
            return IKernalLRT(krETH).getBalance(address(this));
        } else if (keccak256(abi.encodePacked(lrt)) == keccak256(abi.encodePacked("ksETH"))) {
            return IKernalLRT(ksETH).getBalance(address(this));
        } else if (keccak256(abi.encodePacked(lrt)) == keccak256(abi.encodePacked("kUSD"))) {
            return IKernalLRT(kUSD).getBalance(address(this));
        } else {
            revert("Invalid LRT specified");
        }
    }
}
```
