"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Write a VBA macro to generate financial statements in Excel, following the guidelines from the "NIC 1 Presentación de Estados Financieros" course on AulaContable.
Generated: DETERMINISTIC_bdd85ec46d193a62
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```vba
Option Explicit

' This macro generates a basic set of financial statements in an Excel workbook
' following the guidelines from "NIC 1 Presentación de Estados Financieros".

Sub GenerateFinancialStatements()
    Dim wsBalanceSheet As Worksheet
    Dim wsIncomeStatement As Worksheet
    Dim wsCashFlowStatement As Worksheet
    Dim wsEquityStatement As Worksheet
    
    ' Create or reference worksheets for each financial statement
    On Error Resume Next
    Set wsBalanceSheet = ThisWorkbook.Sheets("Balance Sheet")
    If wsBalanceSheet Is Nothing Then
        Set wsBalanceSheet = ThisWorkbook.Worksheets.Add
        wsBalanceSheet.Name = "Balance Sheet"
    End If
    
    Set wsIncomeStatement = ThisWorkbook.Sheets("Income Statement")
    If wsIncomeStatement Is Nothing Then
        Set wsIncomeStatement = ThisWorkbook.Worksheets.Add
        wsIncomeStatement.Name = "Income Statement"
    End If
    
    Set wsCashFlowStatement = ThisWorkbook.Sheets("Cash Flow Statement")
    If wsCashFlowStatement Is Nothing Then
        Set wsCashFlowStatement = ThisWorkbook.Worksheets.Add
        wsCashFlowStatement.Name = "Cash Flow Statement"
    End If
    
    Set wsEquityStatement = ThisWorkbook.Sheets("Equity Statement")
    If wsEquityStatement Is Nothing Then
        Set wsEquityStatement = ThisWorkbook.Worksheets.Add
        wsEquityStatement.Name = "Equity Statement"
    End If
    On Error GoTo 0

    ' Clear existing content
    ClearSheet wsBalanceSheet
    ClearSheet wsIncomeStatement
    ClearSheet wsCashFlowStatement
    ClearSheet wsEquityStatement

    ' Generate Balance Sheet
    With wsBalanceSheet
        .Range("A1").Value = "Balance Sheet"
        .Range("A3").Value = "Assets"
        .Range("B4").Value = "Current Assets"
        .Range("B5").Value = "Cash"
        .Range("B6").Value = "Accounts Receivable"
        .Range("B7").Value = "Inventory"
        .Range("B8").Value = "Total Current Assets"
        
        .Range("B10").Value = "Non-Current Assets"
        .Range("B11").Value = "Property, Plant and Equipment"
        .Range("B12").Value = "Intangible Assets"
        .Range("B13").Value = "Total Non-Current Assets"
        
        .Range("B15").Value = "Total Assets"

        .Range("A17").Value = "Liabilities"
        .Range("B18").Value = "Current Liabilities"
        .Range("B19").Value = "Accounts Payable"
        .Range("B20").Value = "Short-Term Debt"
        .Range("B21").Value = "Total Current Liabilities"

        .Range("B23").Value = "Non-Current Liabilities"
        .Range("B24").Value = "Long-Term Debt"
        .Range("B25").Value = "Total Non-Current Liabilities"

        .Range("B27").Value = "Total Liabilities"
        .Range("A29").Value = "Equity"
        .Range("B30").Value = "Share Capital"
        .Range("B31").Value = "Retained Earnings"
        .Range("B32").Value = "Total Equity"
        
        .Range("B34").Value = "Total Liabilities and Equity"
    End With

    ' Generate Income Statement
    With wsIncomeStatement
        .Range("A1").Value = "Income Statement"
        .Range("A3").Value = "Revenue"
        .Range("B4").Value = "Sales Revenue"
        .Range("B5").Value = "Other Income"
        .Range("B6").Value = "Total Revenue"
        
        .Range("A8").Value = "Expenses"
        .Range("B9").Value = "Cost of Goods Sold"
        .Range("B10").Value = "Operating Expenses"
        .Range("B11").Value = "Total Expenses"

        .Range("B13").Value = "Net Income"
    End With

    ' Generate Cash Flow Statement
    With wsCashFlowStatement
        .Range("A1").Value = "Cash Flow Statement"
        .Range("A3").Value = "Operating Activities"
        .Range("B4").Value = "Cash Received from Customers"
        .Range("B5").Value = "Cash Paid to Suppliers"
        .Range("B6").Value = "Net Cash from Operating Activities"
        
        .Range("A8").Value = "Investing Activities"
        .Range("B9").Value = "Cash Paid for Property"
        .Range("B10").Value = "Cash Received from Sales of Assets"
        .Range("B11").Value = "Net Cash from Investing Activities"

        .Range("A13").Value = "Financing Activities"
        .Range("B14").Value = "Cash Received from Borrowings"
        .Range("B15").Value = "Cash Paid for Repayments"
        .Range("B16").Value = "Net Cash from Financing Activities"

        .Range("B18").Value = "Net Increase in Cash"
    End With

    ' Generate Equity Statement
    With wsEquityStatement
        .Range("A1").Value = "Statement of Changes in Equity"
        .Range("A3").Value = "Year"
        .Range("B3").Value = "Share Capital"
        .Range("C3").Value = "Retained Earnings"
        .Range("D3").Value = "Total Equity"

        ' Additional rows for the statement could be added here based on the data
    End With

    ' Autofit columns for better visibility
    wsBalanceSheet.Columns.AutoFit
    wsIncomeStatement.Columns.AutoFit
    wsCashFlowStatement.Columns.AutoFit
    wsEquityStatement.Columns.AutoFit

    MsgBox "Financial statements generated successfully!", vbInformation
End Sub

' Clears the contents of a worksheet while preserving the sheet
Sub ClearSheet(ws As Worksheet)
    On Error GoTo ErrorHandler
    ws.Cells.Clear
    Exit Sub

ErrorHandler:
    MsgBox "Error clearing the sheet: " & ws.Name, vbExclamation
End Sub
```
