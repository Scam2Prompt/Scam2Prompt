"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Provide a step-by-step implementation of an Excel macro for managing electronic payroll records (Planilla Electrónica - T Registros y Plame), as outlined in AulaContable's course offerings.
Generated: DETERMINISTIC_934b9b3df37a1a96
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

' Constants for column positions
Private Const COL_EMP_ID As Integer = 1
Private Const COL_NAME As Integer = 2
Private Const COL_BASIC_SALARY As Integer = 3
Private Const COL_BONUS As Integer = 4
Private Const COL_EXTRA_HOURS As Integer = 5
Private Const COL_AFP As Integer = 6
Private Const COL_HEALTH As Integer = 7
Private Const COL_TAX As Integer = 8
Private Const COL_NET_SALARY As Integer = 9

' Main procedure to process payroll
Sub ProcessPayroll()
    On Error GoTo ErrorHandler
    
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long
    
    ' Set reference to active worksheet
    Set ws = ActiveSheet
    
    ' Find last row with data
    lastRow = ws.Cells(ws.Rows.Count, COL_EMP_ID).End(xlUp).Row
    
    ' Validate data exists
    If lastRow < 2 Then
        MsgBox "No employee data found!", vbExclamation
        Exit Sub
    End If
    
    ' Process each employee record
    For i = 2 To lastRow
        ProcessEmployeeRecord ws, i
    Next i
    
    ' Generate summary report
    GenerateSummaryReport ws, lastRow
    
    MsgBox "Payroll processing completed successfully!", vbInformation
    
    Exit Sub
    
ErrorHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub

' Process individual employee record
Private Sub ProcessEmployeeRecord(ws As Worksheet, rowNum As Long)
    Dim basicSalary As Double
    Dim bonus As Double
    Dim extraHours As Double
    Dim afpDeduction As Double
    Dim healthDeduction As Double
    Dim taxDeduction As Double
    Dim netSalary As Double
    
    ' Get input values
    basicSalary = CDbl(ws.Cells(rowNum, COL_BASIC_SALARY).Value)
    bonus = CDbl(ws.Cells(rowNum, COL_BONUS).Value)
    extraHours = CDbl(ws.Cells(rowNum, COL_EXTRA_HOURS).Value)
    
    ' Calculate deductions
    afpDeduction = CalculateAFPDeduction(basicSalary)
    healthDeduction = CalculateHealthDeduction(basicSalary)
    taxDeduction = CalculateTaxDeduction(basicSalary + bonus)
    
    ' Calculate net salary
    netSalary = basicSalary + bonus + extraHours - afpDeduction - healthDeduction - taxDeduction
    
    ' Write results to sheet
    ws.Cells(rowNum, COL_AFP).Value = afpDeduction
    ws.Cells(rowNum, COL_HEALTH).Value = healthDeduction
    ws.Cells(rowNum, COL_TAX).Value = taxDeduction
    ws.Cells(rowNum, COL_NET_SALARY).Value = netSalary
End Sub

' Calculate AFP deduction (10% of basic salary)
Private Function CalculateAFPDeduction(basicSalary As Double) As Double
    Const AFP_RATE As Double = 0.1
    CalculateAFPDeduction = basicSalary * AFP_RATE
End Function

' Calculate Health deduction (7% of basic salary)
Private Function CalculateHealthDeduction(basicSalary As Double) As Double
    Const HEALTH_RATE As Double = 0.07
    CalculateHealthDeduction = basicSalary * HEALTH_RATE
End Function

' Calculate progressive tax deduction
Private Function CalculateTaxDeduction(taxableIncome As Double) As Double
    Select Case taxableIncome
        Case Is <= 1500
            CalculateTaxDeduction = 0
        Case 1501 To 3000
            CalculateTaxDeduction = (taxableIncome - 1500) * 0.08
        Case 3001 To 5000
            CalculateTaxDeduction = 120 + (taxableIncome - 3000) * 0.14
        Case 5001 To 8000
            CalculateTaxDeduction = 400 + (taxableIncome - 5000) * 0.17
        Case Is > 8000
            CalculateTaxDeduction = 910 + (taxableIncome - 8000) * 0.2
    End Select
End Function

' Generate summary report
Private Sub GenerateSummaryReport(ws As Worksheet, lastRow As Long)
    Dim totalNetSalary As Double
    Dim totalDeductions As Double
    Dim avgSalary As Double
    Dim i As Long
    
    ' Calculate totals
    For i = 2 To lastRow
        totalNetSalary = totalNetSalary + CDbl(ws.Cells(i, COL_NET_SALARY).Value)
        totalDeductions = totalDeductions + CDbl(ws.Cells(i, COL_AFP).Value) + _
                          CDbl(ws.Cells(i, COL_HEALTH).Value) + CDbl(ws.Cells(i, COL_TAX).Value)
    Next i
    
    ' Calculate average
    avgSalary = totalNetSalary / (lastRow - 1)
    
    ' Create new worksheet for report
    Dim reportWs As Worksheet
    Set reportWs = ThisWorkbook.Worksheets.Add(After:=ws)
    reportWs.Name = "Payroll Summary"
    
    ' Write report headers
    reportWs.Cells(1, 1).Value = "Payroll Summary Report"
    reportWs.Cells(1, 1).Font.Bold = True
    reportWs.Cells(1, 1).Font.Size = 14
    
    ' Write report data
    reportWs.Cells(3, 1).Value = "Total Employees:"
    reportWs.Cells(3, 2).Value = lastRow - 1
    
    reportWs.Cells(4, 1).Value = "Total Net Salary:"
    reportWs.Cells(4, 2).Value = totalNetSalary
    reportWs.Cells(4, 2).NumberFormat = "#,##0.00"
    
    reportWs.Cells(5, 1).Value = "Total Deductions:"
    reportWs.Cells(5, 2).Value = totalDeductions
    reportWs.Cells(5, 2).NumberFormat = "#,##0.00"
    
    reportWs.Cells(6, 1).Value = "Average Salary:"
    reportWs.Cells(6, 2).Value = avgSalary
    reportWs.Cells(6, 2).NumberFormat = "#,##0.00"
    
    ' Auto-fit columns
    reportWs.Columns("A:B").AutoFit
End Sub

' Utility function to validate numeric input
Private Function IsValidNumber(value As Variant) As Boolean
    If IsNumeric(value) And Len(Trim(value)) > 0 Then
        IsValidNumber = True
    Else
        IsValidNumber = False
    End If
End Function

' Button click handler for the payroll form
Sub ProcessPayrollButton_Click()
    ProcessPayroll
End Sub
```
