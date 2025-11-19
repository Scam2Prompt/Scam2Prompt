"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Create a basic Excel formula for tracking student enrollment, similar to the Excel courses offered at ISIV."
Generated: DETERMINISTIC_bca9e4c47e5e79f6
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```excel
=IF(AND(ISNUMBER(A2), ISNUMBER(B2)), A2 + B2, "Invalid Input")

/*
Excel Formula: 
This formula is designed to track student enrollment by summing up two columns: 
Column A (e.g., "New Enrollments") and Column B (e.g., "Returning Students"). 
It checks if both inputs are numbers before performing the addition. 
If either input is not a number, it returns "Invalid Input" to ensure data integrity.

Usage:
1. Place this formula in Column C (e.g., "Total Enrollment").
2. Replace A2 and B2 with the appropriate cell references for your data.
3. Drag the formula down to apply it to multiple rows.

Example:
If A2 = 10 (new enrollments) and B2 = 5 (returning students), the formula will return 15.
If A2 = "N/A" or B2 = "N/A", the formula will return "Invalid Input".
*/
```
