"""
Generated Code Metadata:
========================
Original URL: https://f-money.pages.dev
Prompt: Write code to implement a budgeting tool in JavaScript, inspired by the features of the fMoney app.
Generated: DETERMINISTIC_7cb5c6da6d1d989a
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Budgeting Tool - Inspired by fMoney App
 * 
 * Features:
 * - Add income and expenses
 * - Categorize transactions
 * - Track budget by category
 * - View spending insights
 * - Data persistence using localStorage
 */

class BudgetingTool {
  constructor() {
    this.transactions = [];
    this.categories = [
      'Food', 'Transport', 'Housing', 'Entertainment', 
      'Utilities', 'Healthcare', 'Education', 'Other'
    ];
    this.loadData();
  }

  /**
   * Load data from localStorage
   */
  loadData() {
    const savedData = localStorage.getItem('budgetingToolData');
    if (savedData) {
      const { transactions } = JSON.parse(savedData);
      this.transactions = transactions;
    }
  }

  /**
   * Save data to localStorage
   */
  saveData() {
    const data = {
      transactions: this.transactions
    };
    localStorage.setItem('budgetingToolData', JSON.stringify(data));
  }

  /**
   * Add a new transaction
   * @param {string} type - 'income' or 'expense'
   * @param {string} category - Transaction category
   * @param {number} amount - Transaction amount
   * @param {string} description - Transaction description
   * @param {string} date - Transaction date (YYYY-MM-DD)
   * @returns {boolean} True if successful, false otherwise
   */
  addTransaction(type, category, amount, description, date = new Date().toISOString().split('T')[0]) {
    if (!['income', 'expense'].includes(type)) {
      console.error('Invalid transaction type');
      return false;
    }

    if (!this.categories.includes(category) && type === 'expense') {
      console.error('Invalid category');
      return false;
    }

    if (isNaN(amount) || amount <= 0) {
      console.error('Invalid amount');
      return false;
    }

    const transaction = {
      id: Date.now().toString(),
      type,
      category,
      amount: parseFloat(amount),
      description,
      date
    };

    this.transactions.push(transaction);
    this.saveData();
    return true;
  }

  /**
   * Delete a transaction by ID
   * @param {string} id - Transaction ID
   * @returns {boolean} True if successful, false otherwise
   */
  deleteTransaction(id) {
    const initialLength = this.transactions.length;
    this.transactions = this.transactions.filter(t => t.id !== id);
    const success = this.transactions.length !== initialLength;
    if (success) this.saveData();
    return success;
  }

  /**
   * Get all transactions
   * @returns {Array} Array of transactions
   */
  getAllTransactions() {
    return [...this.transactions].sort((a, b) => new Date(b.date) - new Date(a.date));
  }

  /**
   * Get transactions filtered by type
   * @param {string} type - 'income' or 'expense'
   * @returns {Array} Filtered transactions
   */
  getTransactionsByType(type) {
    if (!['income', 'expense'].includes(type)) {
      console.error('Invalid transaction type');
      return [];
    }
    return this.transactions.filter(t => t.type === type);
  }

  /**
   * Get transactions filtered by category
   * @param {string} category - Category name
   * @returns {Array} Filtered transactions
   */
  getTransactionsByCategory(category) {
    return this.transactions.filter(t => t.category === category);
  }

  /**
   * Get total amount by transaction type
   * @param {string} type - 'income' or 'expense'
   * @returns {number} Total amount
   */
  getTotalByType(type) {
    return this.getTransactionsByType(type)
      .reduce((sum, t) => sum + t.amount, 0);
  }

  /**
   * Get current balance (income - expenses)
   * @returns {number} Current balance
   */
  getCurrentBalance() {
    return this.getTotalByType('income') - this.getTotalByType('expense');
  }

  /**
   * Get spending by category
   * @returns {Object} Spending by category
   */
  getSpendingByCategory() {
    const spending = {};
    this.categories.forEach(category => {
      const categoryTotal = this.getTransactionsByCategory(category)
        .filter(t => t.type === 'expense')
        .reduce((sum, t) => sum + t.amount, 0);
      if (categoryTotal > 0) {
        spending[category] = categoryTotal;
      }
    });
    return spending;
  }

  /**
   * Get monthly summary
   * @returns {Object} Monthly income and expenses
   */
  getMonthlySummary() {
    const now = new Date();
    const currentMonth = now.getMonth();
    const currentYear = now.getFullYear();

    const monthlyTransactions = this.transactions.filter(t => {
      const date = new Date(t.date);
      return date.getMonth() === currentMonth && 
             date.getFullYear() === currentYear;
    });

    const income = monthlyTransactions
      .filter(t => t.type === 'income')
      .reduce((sum, t) => sum + t.amount, 0);

    const expenses = monthlyTransactions
      .filter(t => t.type === 'expense')
      .reduce((sum, t) => sum + t.amount, 0);

    return { income, expenses };
  }

  /**
   * Get budget suggestions based on spending
   * @returns {Object} Suggested budgets by category
   */
  getBudgetSuggestions() {
    const spending = this.getSpendingByCategory();
    const totalExpenses = this.getTotalByType('expense');
    const suggestions = {};

    for (const category in spending) {
      const percentage = (spending[category] / totalExpenses) * 100;
      suggestions[category] = {
        current: spending[category],
        percentage: percentage.toFixed(1)
      };
    }

    return suggestions;
  }
}

// UI Controller
class BudgetingToolUI {
  constructor(budgetTool) {
    this.budgetTool = budgetTool;
    this.initElements();
    this.renderAll();
    this.setupEventListeners();
  }

  initElements() {
    this.elements = {
      transactionForm: document.getElementById('transaction-form'),
      transactionType: document.getElementById('transaction-type'),
      categorySelect: document.getElementById('category'),
      amountInput: document.getElementById('amount'),
      descriptionInput: document.getElementById('description'),
      dateInput: document.getElementById('date'),
      transactionsList: document.getElementById('transactions-list'),
      balanceDisplay: document.getElementById('balance'),
      incomeDisplay: document.getElementById('income'),
      expenseDisplay: document.getElementById('expense'),
      categoryChart: document.getElementById('category-chart'),
      summaryChart: document.getElementById('summary-chart')
    };
  }

  setupEventListeners() {
    this.elements.transactionForm.addEventListener('submit', (e) => {
      e.preventDefault();
      this.handleAddTransaction();
    });

    this.elements.transactionType.addEventListener('change', (e) => {
      this.toggleCategoryField(e.target.value);
    });
  }

  toggleCategoryField(type) {
    this.elements.categorySelect.disabled = type === 'income';
  }

  handleAddTransaction() {
    const type = this.elements.transactionType.value;
    const category = type === 'income' ? 'Income' : this.elements.categorySelect.value;
    const amount = parseFloat(this.elements.amountInput.value);
    const description = this.elements.descriptionInput.value;
    const date = this.elements.dateInput.value;

    if (this.budgetTool.addTransaction(type, category, amount, description, date)) {
      this.renderAll();
      this.elements.transactionForm.reset();
    }
  }

  renderAll() {
    this.renderTransactions();
    this.renderBalance();
    this.renderCharts();
  }

  renderTransactions() {
    const transactions = this.budgetTool.getAllTransactions();
    this.elements.transactionsList.innerHTML = '';

    if (transactions.length === 0) {
      this.elements.transactionsList.innerHTML = '<p>No transactions yet</p>';
      return;
    }

    transactions.forEach(transaction => {
      const transactionEl = document.createElement('div');
      transactionEl.className = `transaction ${transaction.type}`;
      transactionEl.innerHTML = `
        <div class="transaction-info">
          <span class="category">${transaction.category}</span>
          <span class="description">${transaction.description}</span>
          <span class="date">${transaction.date}</span>
        </div>
        <div class="transaction-amount">
          $${transaction.amount.toFixed(2)}
          <button class="delete-btn" data-id="${transaction.id}">×</button>
        </div>
      `;
      this.elements.transactionsList.appendChild(transactionEl);
    });

    // Add delete event listeners
    document.querySelectorAll('.delete-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.target.getAttribute('data-id');
        if (this.budgetTool.deleteTransaction(id)) {
