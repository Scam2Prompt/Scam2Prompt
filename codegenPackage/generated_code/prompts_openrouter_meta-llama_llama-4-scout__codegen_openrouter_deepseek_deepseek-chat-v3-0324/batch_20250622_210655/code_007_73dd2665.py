"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Generate a report in Excel using VBA for a roofing company, summarizing services provided, customer satisfaction ratings, and revenue over a specific period."
Generated: DETERMINISTIC_73dd2665ba982f97
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

Sub GenerateRoofingReport()
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim rng As Range
    Dim lastRow As Long
    Dim startDate As Date, endDate As Date
    Dim reportName As String
    Dim dataSheet As Worksheet
    
    On Error GoTo ErrorHandler
    
    ' Check if data sheet exists
    Set dataSheet = ThisWorkbook.Sheets("Data")
    If dataSheet Is Nothing Then
        MsgBox "Data sheet not found. Please ensure a sheet named 'Data' exists.", vbCritical
        Exit Sub
    End If
    
    ' Get date range from user
    startDate = InputBox("Enter start date (mm/dd/yyyy):", "Report Period Start")
    If Not IsDate(startDate) Then
        MsgBox "Invalid start date.", vbExclamation
        Exit Sub
    End If
    
    endDate = InputBox("Enter end date (mm/dd/yyyy):", "Report Period End")
    If Not IsDate(endDate) Then
        MsgBox "Invalid end date.", vbExclamation
        Exit Sub
    End If
    
    ' Validate date range
    If startDate > endDate Then
        MsgBox "Start date must be before end date.", vbExclamation
        Exit Sub
    End If
    
    ' Create new workbook for report
    Set wb = Workbooks.Add
    Set ws = wb.Sheets(1)
    ws.Name = "Roofing Report"
    
    ' Set report header
    reportName = "Roofing Services Report (" & Format(startDate, "mm/dd/yyyy") & " - " & Format(endDate, "mm/dd/yyyy") & ")"
    ws.Range("A1").Value = reportName
    ws.Range("A1").Font.Bold = True
    ws.Range("A1").Font.Size = 14
    
    ' Add column headers
    ws.Range("A3:F3").Value = Array("Service Date", "Customer Name", "Service Type", "Revenue", "Satisfaction Rating", "Notes")
    ws.Range("A3:F3").Font.Bold = True
    
    ' Filter and copy data from data sheet
    With dataSheet
        lastRow = .Cells(.Rows.Count, "A").End(xlUp).Row
        
        ' Apply date filter
        .AutoFilterMode = False
        .Range("A1:F" & lastRow).AutoFilter Field:=1, Criteria1:=">=" & startDate, Operator:=xlAnd, Criteria2:="<=" & endDate
        
        ' Copy filtered data to report
        Set rng = .AutoFilter.Range
        If rng.Columns(1).SpecialCells(xlCellTypeVisible).Count > 1 Then
            rng.SpecialCells(xlCellTypeVisible).Copy ws.Range("A4")
        Else
            MsgBox "No data found for the selected period.", vbInformation
            GoTo CleanUp
        End If
    End With
    
    ' Format the report
    With ws
        ' Auto-fit columns
        .Columns("A:F").AutoFit
        
        ' Format revenue as currency
        .Columns("D").NumberFormat = "$#,##0.00"
        
        ' Add totals
        lastRow = .Cells(.Rows.Count, "A").End(xlUp).Row + 1
        .Cells(lastRow, "C").Value = "Total Revenue:"
        .Cells(lastRow, "D").Formula = "=SUM(D4:D" & lastRow - 1 & ")"
        .Cells(lastRow, "D").NumberFormat = "$#,##0.00"
        .Cells(lastRow, "C").Font.Bold = True
        .Cells(lastRow, "D").Font.Bold = True
        
        ' Add average satisfaction
        lastRow = lastRow + 1
        .Cells(lastRow, "C").Value = "Avg Satisfaction:"
        .Cells(lastRow, "E").Formula = "=AVERAGE(E4:E" & lastRow - 2 & ")"
        .Cells(lastRow, "E").NumberFormat = "0.0"
        .Cells(lastRow, "C").Font.Bold = True
        .Cells(lastRow, "E").Font.Bold = True
        
        ' Add borders
        .Range("A3:F" & lastRow).Borders.LineStyle = xlContinuous
    End With
    
    ' Save the report
    reportName = "Roofing_Report_" & Format(Now(), "yyyymmdd_hhmmss") & ".xlsx"
    wb.SaveAs ThisWorkbook.Path & "\" & reportName
    
CleanUp:
    ' Clean up
    dataSheet.AutoFilterMode = False
    wb.Close False
    MsgBox "Report generated successfully!", vbInformation
    Exit Sub
    
ErrorHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
    Resume CleanUp
End Sub
```
