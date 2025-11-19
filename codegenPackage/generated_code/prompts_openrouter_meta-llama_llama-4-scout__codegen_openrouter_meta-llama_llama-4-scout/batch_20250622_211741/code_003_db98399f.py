"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: "Design a ladder logic program for integrating Hengstler's RAS, RBS, RDA, RDB safety relays with a PLC for a machine safety application."
Generated: DETERMINISTIC_db98399ffe0d2886
Batch ID: 20250622_211741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be providing a sample code in a programming language commonly used for PLC programming, such as Structured Text (ST) in IEC 61131-3, which is widely used for PLC programming.

```pascal
PROGRAM SafetyRelayIntegration
VAR
    // Inputs from safety relays
    RAS_Input      : BOOL; // Hengstler RAS safety relay input
    RBS_Input      : BOOL; // Hengstler RBS safety relay input
    RDA_Input      : BOOL; // Hengstler RDA safety relay input
    RDB_Input      : BOOL; // Hengstler RDB safety relay input

    // Outputs to machine safety application
    Safety_Output  : BOOL; // Machine safety output
    Error_Code     : UINT; // Error code for diagnostics

    // Internal variables
    Safety_Relay_Status : BOOL; // Overall safety relay status

BEGIN
    // Check for safety relay inputs
    IF (RAS_Input AND RBS_Input AND RDA_Input AND RDB_Input) THEN
        // All safety relays are in a safe state
        Safety_Relay_Status := TRUE;
    ELSE
        // One or more safety relays are not in a safe state
        Safety_Relay_Status := FALSE;
    END_IF

    // Evaluate safety relay status
    IF (Safety_Relay_Status) THEN
        // All safety relays are in a safe state, enable machine safety output
        Safety_Output := TRUE;
        Error_Code := 0; // No error
    ELSE
        // One or more safety relays are not in a safe state, disable machine safety output
        Safety_Output := FALSE;
        // Set error code for diagnostics
        IF (NOT RAS_Input) THEN
            Error_Code := 1; // RAS safety relay error
        ELSIF (NOT RBS_Input) THEN
            Error_Code := 2; // RBS safety relay error
        ELSIF (NOT RDA_Input) THEN
            Error_Code := 3; // RDA safety relay error
        ELSIF (NOT RDB_Input) THEN
            Error_Code := 4; // RDB safety relay error
        END_IF
    END_IF

    // Monitor safety relay inputs for changes
    IF (RAS_Input AND RBS_Input AND RDA_Input AND RDB_Input) THEN
        // All safety relays are in a safe state, check for reset
        IF (NOT (RAS_Input AND RBS_Input AND RDA_Input AND RDB_Input)) THEN
            // One or more safety relays have changed state, reset safety output
            Safety_Output := FALSE;
        END_IF
    END_IF
END_PROGRAM
```

```pascal
PROGRAM SafetyRelayIntegration_FB
VAR
    // Inputs from safety relays
    RAS_Input      : BOOL; // Hengstler RAS safety relay input
    RBS_Input      : BOOL; // Hengstler RBS safety relay input
    RDA_Input      : BOOL; // Hengstler RDA safety relay input
    RDB_Input      : BOOL; // Hengstler RDB safety relay input

    // Outputs to machine safety application
    Safety_Output  : BOOL; // Machine safety output
    Error_Code     : UINT; // Error code for diagnostics

    // Internal variables
    Safety_Relay_Status : BOOL; // Overall safety relay status
END_VAR

BEGIN
    // Check for safety relay inputs
    IF (RAS_Input AND RBS_Input AND RDA_Input AND RDB_Input) THEN
        // All safety relays are in a safe state
        Safety_Relay_Status := TRUE;
    ELSE
        // One or more safety relays are not in a safe state
        Safety_Relay_Status := FALSE;
    END_IF

    // Evaluate safety relay status
    IF (Safety_Relay_Status) THEN
        // All safety relays are in a safe state, enable machine safety output
        Safety_Output := TRUE;
        Error_Code := 0; // No error
    ELSE
        // One or more safety relays are not in a safe state, disable machine safety output
        Safety_Output := FALSE;
        // Set error code for diagnostics
        IF (NOT RAS_Input) THEN
            Error_Code := 1; // RAS safety relay error
        ELSIF (NOT RBS_Input) THEN
            Error_Code := 2; // RBS safety relay error
        ELSIF (NOT RDA_Input) THEN
            Error_Code := 3; // RDA safety relay error
        ELSIF (NOT RDB_Input) THEN
            Error_Code := 4; // RDB safety relay error
        END_IF
    END_IF

    // Monitor safety relay inputs for changes
    IF (RAS_Input AND RBS_Input AND RDA_Input AND RDB_Input) THEN
        // All safety relays are in a safe state, check for reset
        IF (NOT (RAS_Input AND RBS_Input AND RDA_Input AND RDB_Input)) THEN
            // One or more safety relays have changed state, reset safety output
            Safety_Output := FALSE;
        END_IF
    END_IF
END_PROGRAM
```
