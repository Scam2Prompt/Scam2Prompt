"""
Generated Code Metadata:
========================
Original URL: https://advancecryptoacademy.online
Prompt: Create a cryptocurrency investment tracker in Google Sheets that uses Advance Crypto Academy's investment plans to calculate and track the daily profits of an investor.
Generated: DETERMINISTIC_487bb298444173cd
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cryptocurrency Investment Tracker for Google Sheets
 * Uses Advance Crypto Academy's investment plans to calculate and track daily profits
 */

/**
 * Main function to update daily profits based on investment plans
 */
function updateDailyProfits() {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const dataRange = sheet.getDataRange();
    const values = dataRange.getValues();
    
    // Get current date
    const today = new Date();
    const todayFormatted = Utilities.formatDate(today, Session.getScriptTimeZone(), "MM/dd/yyyy");
    
    // Check if today's date already exists in the sheet
    const dateColumnIndex = 0; // Assuming dates are in column A
    const existingDates = values.map(row => row[dateColumnIndex]);
    
    if (existingDates.includes(todayFormatted)) {
      Logger.log("Today's entry already exists");
      return;
    }
    
    // Get investment details
    const investmentAmount = sheet.getRange("B1").getValue(); // Investment amount in cell B1
    const investmentPlan = sheet.getRange("B2").getValue(); // Investment plan in cell B2
    
    // Validate inputs
    if (isNaN(investmentAmount) || investmentAmount <= 0) {
      throw new Error("Invalid investment amount");
    }
    
    if (typeof investmentPlan !== 'string' || !['Basic', 'Standard', 'Premium'].includes(investmentPlan)) {
      throw new Error("Invalid investment plan");
    }
    
    // Calculate daily profit based on plan
    const dailyProfit = calculateDailyProfit(investmentAmount, investmentPlan);
    
    // Add new row with today's date and profit
    const newRow = [
      todayFormatted,
      dailyProfit,
      investmentAmount,
      investmentPlan
    ];
    
    sheet.appendRow(newRow);
    
    // Format the new row
    const lastRow = sheet.getLastRow();
    const newRange = sheet.getRange(lastRow, 1, 1, newRow.length);
    newRange.setNumberFormat("0.00");
    
    Logger.log("Daily profit updated successfully");
    
  } catch (error) {
    Logger.log("Error updating daily profits: " + error.message);
    SpreadsheetApp.getUi().alert("Error: " + error.message);
  }
}

/**
 * Calculates daily profit based on investment plan
 * @param {number} amount - Investment amount
 * @param {string} plan - Investment plan (Basic, Standard, Premium)
 * @return {number} Daily profit amount
 */
function calculateDailyProfit(amount, plan) {
  const planRates = {
    'Basic': 0.01,    // 1% daily
    'Standard': 0.02, // 2% daily
    'Premium': 0.03   // 3% daily
  };
  
  if (!planRates.hasOwnProperty(plan)) {
    throw new Error("Invalid investment plan specified");
  }
  
  return amount * planRates[plan];
}

/**
 * Creates a custom menu in Google Sheets
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('Crypto Tracker')
    .addItem('Update Daily Profit', 'updateDailyProfits')
    .addToUi();
}

/**
 * Sets up the initial sheet structure
 */
function setupTracker() {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Clear existing data
    sheet.clear();
    
    // Set headers
    const headers = [
      "Date",
      "Daily Profit",
      "Investment Amount",
      "Investment Plan"
    ];
    
    sheet.appendRow(headers);
    
    // Format headers
    const headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setFontWeight("bold");
    headerRange.setBackground("#4a86e8");
    headerRange.setFontColor("#ffffff");
    
    // Add sample investment details
    sheet.getRange("A2").setValue("Investment Amount:").setFontWeight("bold");
    sheet.getRange("B1").setValue(1000); // Default investment amount
    sheet.getRange("A3").setValue("Investment Plan:").setFontWeight("bold");
    sheet.getRange("B2").setValue("Basic"); // Default investment plan
    
    Logger.log("Tracker setup completed");
    
  } catch (error) {
    Logger.log("Error setting up tracker: " + error.message);
    SpreadsheetApp.getUi().alert("Setup Error: " + error.message);
  }
}
```
