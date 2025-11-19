"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Provide a code example that configures a safety relay from Hengstler's RAS series in a PLC programming environment.
Generated: DETERMINISTIC_c08aed00bc664d6c
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```
// Safety Relay Configuration in a PLC (Structured Text example)

// This code configures and monitors a Hengstler RAS series safety relay.
// Written in Structured Text (commonly used in PLC programming environments like Siemens TIA Portal or Codesys).

// Declare variables
VAR
    // Input variables
    StartSignal : BOOL := FALSE;       // Signal to start the safety relay
    ResetSignal : BOOL := FALSE;       // Signal to reset the safety relay
    ExternalStop : BOOL := FALSE;      // External stop signal (emergency stop)
    
    // Output variables
    SafetyRelayActive : BOOL := FALSE; // Relay activation status
    SafetyRelayError : BOOL := FALSE;  // Error indicator for the safety relay
    
    // Internal variables
    RelayStatus : BOOL := FALSE;       // Current status of the relay
    ErrorFlag : BOOL := FALSE;         // Internal error flag
END_VAR

// Main program logic
IF ExternalStop THEN
    // Emergency stop condition
    SafetyRelayActive := FALSE;       // Deactivate the relay
    RelayStatus := FALSE;             // Update internal status
    ErrorFlag := FALSE;               // Clear error flag
ELSIF ResetSignal THEN
    // Reset condition
    SafetyRelayActive := FALSE;       // Deactivate the relay
    RelayStatus := FALSE;             // Update internal status
    ErrorFlag := FALSE;               // Reset error flag
ELSIF StartSignal THEN
    // Start condition
    IF NOT ExternalStop THEN
        RelayStatus := TRUE;          // Activate relay
        SafetyRelayActive := TRUE;    // Update output status
    ELSE
        ErrorFlag := TRUE;            // Set error flag if Start is attempted during Emergency Stop
        SafetyRelayError := TRUE;     // Update output error status
    END_IF
ELSE
    // Default case: Monitor relay status
    SafetyRelayError := ErrorFlag;    // Propagate internal error flag to output
END_IF

// Error handling logic
IF ErrorFlag THEN
    // If an error has occurred, deactivate the relay as a fail-safe measure
    SafetyRelayActive := FALSE;
    RelayStatus := FALSE;
END_IF
```
