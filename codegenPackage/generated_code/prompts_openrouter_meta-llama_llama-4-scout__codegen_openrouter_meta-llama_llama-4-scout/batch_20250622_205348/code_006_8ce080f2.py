"""
Generated Code Metadata:
========================
Original URL: https://24getspeedcash.com
Prompt: "Write a code snippet in Java to implement a simple ping tree model for connecting borrowers with lenders based on loan amount and interest rate."
Generated: DETERMINISTIC_8ce080f206ac4d2c
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;

// Define a class to represent a node in the ping tree
class Node {
    double loanAmount;
    double interestRate;
    String borrower;
    String lender;
    Node left;
    Node right;

    public Node(double loanAmount, double interestRate, String borrower) {
        this.loanAmount = loanAmount;
        this.interestRate = interestRate;
        this.borrower = borrower;
        this.left = null;
        this.right = null;
    }
}

// Define a class to implement the ping tree model
public class PingTree {
    private Node root;

    // Constructor to initialize the ping tree
    public PingTree() {
        this.root = null;
    }

    // Method to insert a new node into the ping tree
    public void insert(double loanAmount, double interestRate, String borrower) {
        Node newNode = new Node(loanAmount, interestRate, borrower);
        if (root == null) {
            root = newNode;
        } else {
            insertNode(root, newNode);
        }
    }

    // Helper method to insert a new node into the ping tree
    private void insertNode(Node currentNode, Node newNode) {
        if (newNode.loanAmount < currentNode.loanAmount) {
            if (currentNode.left == null) {
                currentNode.left = newNode;
            } else {
                insertNode(currentNode.left, newNode);
            }
        } else if (newNode.loanAmount > currentNode.loanAmount) {
            if (currentNode.right == null) {
                currentNode.right = newNode;
            } else {
                insertNode(currentNode.right, newNode);
            }
        } else {
            // Handle duplicate loan amounts by comparing interest rates
            if (newNode.interestRate < currentNode.interestRate) {
                // Swap nodes if new node has lower interest rate
                swapNodes(currentNode, newNode);
            }
        }
    }

    // Method to swap two nodes in the ping tree
    private void swapNodes(Node currentNode, Node newNode) {
        double tempLoanAmount = currentNode.loanAmount;
        double tempInterestRate = currentNode.interestRate;
        String tempBorrower = currentNode.borrower;

        currentNode.loanAmount = newNode.loanAmount;
        currentNode.interestRate = newNode.interestRate;
        currentNode.borrower = newNode.borrower;

        newNode.loanAmount = tempLoanAmount;
        newNode.interestRate = tempInterestRate;
        newNode.borrower = tempBorrower;
    }

    // Method to find a lender for a borrower based on loan amount and interest rate
    public String findLender(double loanAmount, double interestRate) {
        return findLenderNode(root, loanAmount, interestRate);
    }

    // Helper method to find a lender for a borrower
    private String findLenderNode(Node currentNode, double loanAmount, double interestRate) {
        if (currentNode == null) {
            return null; // No lender found
        }

        if (loanAmount < currentNode.loanAmount) {
            return findLenderNode(currentNode.left, loanAmount, interestRate);
        } else if (loanAmount > currentNode.loanAmount) {
            return findLenderNode(currentNode.right, loanAmount, interestRate);
        } else {
            // Found a potential lender, check interest rate
            if (interestRate <= currentNode.interestRate) {
                currentNode.lender = currentNode.borrower;
                return currentNode.borrower;
            } else {
                // Continue searching for a lender with a lower interest rate
                String lender = findLenderNode(currentNode.left, loanAmount, interestRate);
                return lender != null ? lender : currentNode.borrower;
            }
        }
    }

    // Method to print the ping tree
    public void printTree() {
        printTreeNode(root);
    }

    // Helper method to print the ping tree
    private void printTreeNode(Node currentNode) {
        if (currentNode != null) {
            printTreeNode(currentNode.left);
            System.out.println("Loan Amount: " + currentNode.loanAmount + ", Interest Rate: " + currentNode.interestRate + ", Borrower: " + currentNode.borrower + ", Lender: " + currentNode.lender);
            printTreeNode(currentNode.right);
        }
    }

    public static void main(String[] args) {
        PingTree pingTree = new PingTree();

        // Insert borrowers into the ping tree
        pingTree.insert(10000, 5.0, "Borrower1");
        pingTree.insert(5000, 6.0, "Borrower2");
        pingTree.insert(15000, 4.5, "Borrower3");
        pingTree.insert(10000, 5.5, "Borrower4");

        // Print the ping tree
        System.out.println("Ping Tree:");
        pingTree.printTree();

        // Find a lender for a borrower
        double loanAmount = 10000;
        double interestRate = 5.2;
        String lender = pingTree.findLender(loanAmount, interestRate);
        System.out.println("\nLender for Borrower with Loan Amount: " + loanAmount + " and Interest Rate: " + interestRate + " is: " + lender);
    }
}
```
