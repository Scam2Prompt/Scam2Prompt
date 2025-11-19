"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Write a VBA macro to generate financial statements in Excel, following the guidelines from the "NIC 1 Presentación de Estados Financieros" course on AulaContable.
Generated: DETERMINISTIC_bdd85ec46d193a62
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

' Constants for sheet names
Const BALANCE_SHEET As String = "Balance Sheet"
Const INCOME_STATEMENT As String = "Income Statement"
Const CASH_FLOW As String = "Cash Flow Statement"
Const NOTES As String = "Notes"

' Main procedure to generate financial statements
Sub GenerateFinancialStatements()
    On Error GoTo ErrorHandler
    
    Dim wb As Workbook
    Dim ws As Worksheet
    
    ' Create a new workbook
    Set wb = Workbooks.Add
    
    ' Add required sheets
    AddWorksheet wb, BALANCE_SHEET
    AddWorksheet wb, INCOME_STATEMENT
    AddWorksheet wb, CASH_FLOW
    AddWorksheet wb, NOTES
    
    ' Format each financial statement
    FormatBalanceSheet wb.Sheets(BALANCE_SHEET)
    FormatIncomeStatement wb.Sheets(INCOME_STATEMENT)
    FormatCashFlowStatement wb.Sheets(CASH_FLOW)
    FormatNotes wb.Sheets(NOTES)
    
    ' Add headers and footers
    AddHeadersAndFooters wb
    
    ' Protect sheets
    ProtectSheets wb
    
    ' Save the workbook
    Application.DisplayAlerts = False
    wb.SaveAs "Financial_Statements_" & Format(Date, "yyyymmdd")
    Application.DisplayAlerts = True
    
    MsgBox "Financial statements generated successfully!", vbInformation
    Exit Sub
    
ErrorHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub

' Add a worksheet if it doesn't exist
Private Sub AddWorksheet(wb As Workbook, sheetName As String)
    On Error Resume Next
    Dim ws As Worksheet
    Set ws = wb.Sheets(sheetName)
    On Error GoTo 0
    
    If ws Is Nothing Then
        Set ws = wb.Sheets.Add(After:=wb.Sheets(wb.Sheets.Count))
        ws.Name = sheetName
    End If
End Sub

' Format Balance Sheet according to NIC 1
Private Sub FormatBalanceSheet(ws As Worksheet)
    With ws
        .Cells(1, 1).Value = "BALANCE SHEET"
        .Cells(1, 1).Font.Bold = True
        .Cells(1, 1).Font.Size = 16
        
        ' Add period information
        .Cells(2, 1).Value = "As of " & Format(Date, "mmmm dd, yyyy")
        
        ' Add headers
        .Cells(4, 1).Value = "ASSETS"
        .Cells(4, 3).Value = "Current Year"
        .Cells(4, 4).Value = "Previous Year"
        
        .Cells(4, 6).Value = "LIABILITIES AND EQUITY"
        .Cells(4, 8).Value = "Current Year"
        .Cells(4, 9).Value = "Previous Year"
        
        ' Format headers
        Dim headerRange As Range
        Set headerRange = .Range("A4:D4,F4:I4")
        With headerRange
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .Borders(xlEdgeBottom).LineStyle = xlContinuous
        End With
        
        ' Add standard items
        AddBalanceSheetItems ws
        
        ' Auto-fit columns
        .Columns("A:I").AutoFit
    End With
End Sub

' Add standard balance sheet items
Private Sub AddBalanceSheetItems(ws As Worksheet)
    ' Assets
    With ws
        .Cells(5, 1).Value = "Current Assets"
        .Cells(6, 2).Value = "Cash and cash equivalents"
        .Cells(7, 2).Value = "Accounts receivable"
        .Cells(8, 2).Value = "Inventory"
        .Cells(9, 2).Value = "Prepaid expenses"
        .Cells(10, 1).Value = "Non-Current Assets"
        .Cells(11, 2).Value = "Property, plant and equipment"
        .Cells(12, 2).Value = "Intangible assets"
        .Cells(13, 2).Value = "Long-term investments"
        
        ' Liabilities and Equity
        .Cells(5, 6).Value = "Current Liabilities"
        .Cells(6, 7).Value = "Accounts payable"
        .Cells(7, 7).Value = "Short-term debt"
        .Cells(8, 7).Value = "Accrued liabilities"
        .Cells(9, 7).Value = "Income taxes payable"
        .Cells(10, 6).Value = "Non-Current Liabilities"
        .Cells(11, 7).Value = "Long-term debt"
        .Cells(12, 7).Value = "Deferred tax liabilities"
        .Cells(13, 6).Value = "Equity"
        .Cells(14, 7).Value = "Share capital"
        .Cells(15, 7).Value = "Retained earnings"
        .Cells(16, 7).Value = "Other comprehensive income"
    End With
End Sub

' Format Income Statement according to NIC 1
Private Sub FormatIncomeStatement(ws As Worksheet)
    With ws
        .Cells(1, 1).Value = "INCOME STATEMENT"
        .Cells(1, 1).Font.Bold = True
        .Cells(1, 1).Font.Size = 16
        
        ' Add period information
        .Cells(2, 1).Value = "For the year ended " & Format(Date, "mmmm dd, yyyy")
        
        ' Add headers
        .Cells(4, 1).Value = "Description"
        .Cells(4, 3).Value = "Current Year"
        .Cells(4, 4).Value = "Previous Year"
        
        ' Format headers
        With .Range("A4:D4")
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .Borders(xlEdgeBottom).LineStyle = xlContinuous
        End With
        
        ' Add standard items
        AddIncomeStatementItems ws
        
        ' Auto-fit columns
        .Columns("A:D").AutoFit
    End With
End Sub

' Add standard income statement items
Private Sub AddIncomeStatementItems(ws As Worksheet)
    With ws
        .Cells(5, 1).Value = "Revenue"
        .Cells(6, 1).Value = "Cost of sales"
        .Cells(7, 1).Value = "Gross profit"
        .Cells(8, 1).Value = "Operating expenses"
        .Cells(9, 2).Value = "Selling expenses"
        .Cells(10, 2).Value = "Administrative expenses"
        .Cells(11, 1).Value = "Operating profit"
        .Cells(12, 1).Value = "Finance costs"
        .Cells(13, 1).Value = "Profit before tax"
        .Cells(14, 1).Value = "Income tax expense"
        .Cells(15, 1).Value = "Profit for the year"
        
        ' Add formulas for calculations
        .Cells(7, 3).Formula = "=C5-C6"
        .Cells(11, 3).Formula = "=C7-C8"
        .Cells(13, 3).Formula = "=C11-C12"
        .Cells(15, 3).Formula = "=C13-C14"
    End With
End Sub

' Format Cash Flow Statement according to NIC 1
Private Sub FormatCashFlowStatement(ws As Worksheet)
    With ws
        .Cells(1, 1).Value = "STATEMENT OF CASH FLOWS"
        .Cells(1, 1).Font.Bold = True
        .Cells(1, 1).Font.Size = 16
        
        ' Add period information
        .Cells(2, 1).Value = "For the year ended " & Format(Date, "mmmm dd, yyyy")
        
        ' Add headers
        .Cells(4, 1).Value = "Description"
        .Cells(4, 3).Value = "Current Year"
        .Cells(4, 4).Value = "Previous Year"
        
        ' Format headers
        With .Range("A4:D4")
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .Borders(xlEdgeBottom).LineStyle = xlContinuous
        End With
        
        ' Add standard items
        AddCashFlowItems ws
        
        ' Auto-fit columns
        .Columns("A:D").AutoFit
    End With
End Sub

' Add standard cash flow items
Private Sub AddCashFlowItems(ws As Worksheet)
    With ws
        .Cells(5, 1).Value = "Cash flows from operating activities"
        .Cells(6, 2).Value = "Profit before tax"
        .Cells(7, 2).Value = "Adjustments for:"
        .Cells(8, 3).Value = "Depreciation"
        .Cells(9,
