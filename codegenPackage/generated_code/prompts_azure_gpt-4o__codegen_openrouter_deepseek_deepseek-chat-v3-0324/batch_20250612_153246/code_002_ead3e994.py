"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: Create an Excel macro to streamline office tasks related to energy management, as described by Jacek Kaliński.
Generated: DETERMINISTIC_ead3e99408ab2e43
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

' Energy Management Excel Macro
' Author: Jacek Kaliński
' Description: Streamlines office tasks related to energy management

Sub EnergyManagementMacro()
    On Error GoTo ErrorHandler
    
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim rng As Range
    Dim energyData As Collection
    Dim cell As Range
    Dim summarySheet As Worksheet
    Dim chartObj As ChartObject
    
    ' Check if active workbook is valid
    If ActiveWorkbook Is Nothing Then
        MsgBox "No active workbook found!", vbExclamation
        Exit Sub
    End If
    
    ' Create or activate Energy Data sheet
    On Error Resume Next
    Set ws = ActiveWorkbook.Worksheets("Energy Data")
    On Error GoTo ErrorHandler
    
    If ws Is Nothing Then
        Set ws = ActiveWorkbook.Worksheets.Add(After:=ActiveWorkbook.Worksheets(ActiveWorkbook.Worksheets.Count))
        ws.Name = "Energy Data"
        ' Set up headers
        ws.Range("A1:D1").Value = Array("Date", "Energy Consumption (kWh)", "Cost ($)", "Facility")
        ws.Range("A1:D1").Font.Bold = True
    End If
    
    ' Find last row with data
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    If lastRow = 1 And ws.Range("A1").Value = "" Then lastRow = 0
    
    ' Create summary sheet if it doesn't exist
    On Error Resume Next
    Set summarySheet = ActiveWorkbook.Worksheets("Energy Summary")
    On Error GoTo ErrorHandler
    
    If summarySheet Is Nothing Then
        Set summarySheet = ActiveWorkbook.Worksheets.Add(Before:=ActiveWorkbook.Worksheets(1))
        summarySheet.Name = "Energy Summary"
        CreateSummaryReport summarySheet, ws
    End If
    
    ' Refresh data analysis
    RefreshEnergyAnalysis ws, summarySheet
    
    ' Create chart if it doesn't exist
    On Error Resume Next
    Set chartObj = summarySheet.ChartObjects("EnergyConsumptionChart")
    On Error GoTo ErrorHandler
    
    If chartObj Is Nothing Then
        CreateEnergyChart summarySheet, ws
    Else
        UpdateEnergyChart chartObj.Chart, ws
    End If
    
    ' Apply conditional formatting to highlight high consumption
    ApplyConditionalFormatting ws
    
    ' Auto-fit columns for better readability
    ws.Columns("A:D").AutoFit
    summarySheet.Columns("A:C").AutoFit
    
    MsgBox "Energy management tasks completed successfully!", vbInformation
    
    Exit Sub
    
ErrorHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub

Sub CreateSummaryReport(summarySheet As Worksheet, dataSheet As Worksheet)
    ' Set up summary report headers
    summarySheet.Range("A1:C1").Value = Array("Facility", "Total Consumption (kWh)", "Total Cost ($)")
    summarySheet.Range("A1:C1").Font.Bold = True
    
    ' Format headers
    With summarySheet.Range("A1:C1")
        .Interior.Color = RGB(200, 200, 200)
        .Borders(xlEdgeBottom).LineStyle = xlContinuous
    End With
End Sub

Sub RefreshEnergyAnalysis(dataSheet As Worksheet, summarySheet As Worksheet)
    Dim lastRow As Long
    Dim consumptionCol As Range
    Dim costCol As Range
    Dim facilityCol As Range
    Dim dict As Object
    Dim key As Variant
    Dim i As Long
    Dim outputRow As Long
    
    ' Initialize dictionary to store facility totals
    Set dict = CreateObject("Scripting.Dictionary")
    
    ' Get data ranges
    lastRow = dataSheet.Cells(dataSheet.Rows.Count, "A").End(xlUp).Row
    If lastRow < 2 Then Exit Sub ' No data to process
    
    Set consumptionCol = dataSheet.Range("B2:B" & lastRow)
    Set costCol = dataSheet.Range("C2:C" & lastRow)
    Set facilityCol = dataSheet.Range("D2:D" & lastRow)
    
    ' Calculate totals by facility
    For i = 1 To consumptionCol.Rows.Count
        If Not IsEmpty(facilityCol.Cells(i, 1).Value) Then
            key = facilityCol.Cells(i, 1).Value
            If dict.exists(key) Then
                dict(key)(0) = dict(key)(0) + consumptionCol.Cells(i, 1).Value
                dict(key)(1) = dict(key)(1) + costCol.Cells(i, 1).Value
            Else
                dict.Add key, Array(consumptionCol.Cells(i, 1).Value, costCol.Cells(i, 1).Value)
            End If
        End If
    Next i
    
    ' Clear existing summary data
    summarySheet.Range("A2:C" & summarySheet.Rows.Count).ClearContents
    
    ' Output summary data
    outputRow = 2
    For Each key In dict.keys
        summarySheet.Cells(outputRow, 1).Value = key
        summarySheet.Cells(outputRow, 2).Value = dict(key)(0)
        summarySheet.Cells(outputRow, 3).Value = dict(key)(1)
        outputRow = outputRow + 1
    Next key
    
    ' Add grand total
    If outputRow > 2 Then
        summarySheet.Cells(outputRow, 1).Value = "Grand Total"
        summarySheet.Cells(outputRow, 2).Formula = "=SUM(B2:B" & outputRow - 1 & ")"
        summarySheet.Cells(outputRow, 3).Formula = "=SUM(C2:C" & outputRow - 1 & ")"
        summarySheet.Range("A" & outputRow & ":C" & outputRow).Font.Bold = True
    End If
    
    ' Format numbers
    summarySheet.Range("B2:C" & outputRow).NumberFormat = "#,##0.00"
End Sub

Sub CreateEnergyChart(summarySheet As Worksheet, dataSheet As Worksheet)
    Dim chartObj As ChartObject
    Dim lastRow As Long
    
    ' Create chart object
    Set chartObj = summarySheet.ChartObjects.Add(Left:=300, Width:=500, Top:=50, Height:=300)
    chartObj.Name = "EnergyConsumptionChart"
    
    ' Configure chart
    With chartObj.Chart
        .ChartType = xlColumnClustered
        .SetSourceData Source:=summarySheet.Range("A1:B" & summarySheet.Cells(summarySheet.Rows.Count, "A").End(xlUp).Row)
        .HasTitle = True
        .ChartTitle.Text = "Energy Consumption by Facility"
        .Axes(xlCategory, xlPrimary).HasTitle = True
        .Axes(xlCategory, xlPrimary).AxisTitle.Text = "Facility"
        .Axes(xlValue, xlPrimary).HasTitle = True
        .Axes(xlValue, xlPrimary).AxisTitle.Text = "Consumption (kWh)"
        .Legend.Position = xlLegendPositionBottom
    End With
End Sub

Sub UpdateEnergyChart(chart As Chart, dataSheet As Worksheet)
    Dim summarySheet As Worksheet
    Set summarySheet = chart.Parent.Parent
    
    ' Update chart data
    chart.SetSourceData Source:=summarySheet.Range("A1:B" & summarySheet.Cells(summarySheet.Rows.Count, "A").End(xlUp).Row)
End Sub

Sub ApplyConditionalFormatting(dataSheet As Worksheet)
    Dim lastRow As Long
    Dim consumptionCol As Range
    
    ' Remove existing conditional formatting
    dataSheet.Columns("B").FormatConditions.Delete
    
    ' Get consumption column range
    lastRow = dataSheet.Cells(dataSheet.Rows.Count, "A").End(xlUp).Row
    If lastRow < 2 Then Exit Sub ' No data to format
    
    Set consumptionCol = dataSheet.Range("B2:B" & lastRow)
    
    ' Add conditional formatting for high consumption
    With consumptionCol.FormatConditions.Add(Type:=xlCellValue, Operator:=xlGreater, Formula1:="=AVERAGE(B:B)*1.5")
        .Interior.Color = RGB(255, 200, 200)
        .Font.Bold = True
    End With
    
    ' Add data bars for visualization
    With consumptionCol.FormatConditions.AddDatabar
        .BarColor.Color = RGB(100, 150, 200)
        .BarFillType = xlDataBarFillSolid
        .MinPoint.Modify newtype:=xlConditionValueAutomaticMin
        .MaxPoint.Modify newtype:=xlConditionValueAutomaticMax
    End With
End Sub

Sub ImportEnergyData()
    Dim fDialog As FileDialog
    Dim selectedFile As String
    Dim wbSource As Workbook
    Dim wsSource As Worksheet
    Dim wsDest As Worksheet
    Dim lastRow As Long
    
    On Error GoTo ErrorHandler
