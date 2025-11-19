"""
Generated Code Metadata:
========================
Original URL: https://www.himsdemo.bste.live
Prompt: Create a template for printing healthcare data with headers like `PrintSettings.printHeader.HospitalName` and `PrintSettings.printHeader.Address` in a Health Information Management System.
Generated: DETERMINISTIC_45946e07644a9c08
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// PrintSettings.java

/**
 * This class contains settings for printing healthcare data.
 */
public class PrintSettings {

    /**
     * Nested class for print header settings.
     */
    public static class PrintHeader {
        public static final String HospitalName = "Hospital Name";
        public static final String Address = "Address";
        public static final String PatientName = "Patient Name";
        public static final String DateOfBirth = "Date of Birth";
        public static final String MedicalRecordNumber = "Medical Record Number";
    }

    /**
     * Nested class for print footer settings.
     */
    public static class PrintFooter {
        public static final String PrintedBy = "Printed By";
        public static final String PrintedDate = "Printed Date";
    }
}

// HealthcareData.java

/**
 * This class represents healthcare data.
 */
public class HealthcareData {
    private String hospitalName;
    private String address;
    private String patientName;
    private String dateOfBirth;
    private String medicalRecordNumber;

    /**
     * Constructor for HealthcareData.
     * 
     * @param hospitalName         Hospital name.
     * @param address              Address.
     * @param patientName          Patient name.
     * @param dateOfBirth          Date of birth.
     * @param medicalRecordNumber  Medical record number.
     */
    public HealthcareData(String hospitalName, String address, String patientName, String dateOfBirth, String medicalRecordNumber) {
        this.hospitalName = hospitalName;
        this.address = address;
        this.patientName = patientName;
        this.dateOfBirth = dateOfBirth;
        this.medicalRecordNumber = medicalRecordNumber;
    }

    // Getters
    public String getHospitalName() { return hospitalName; }
    public String getAddress() { return address; }
    public String getPatientName() { return patientName; }
    public String getDateOfBirth() { return dateOfBirth; }
    public String getMedicalRecordNumber() { return medicalRecordNumber; }
}

// HealthcareDataPrinter.java

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * This class prints healthcare data.
 */
public class HealthcareDataPrinter {

    /**
     * Prints healthcare data with headers and footers.
     * 
     * @param healthcareData Healthcare data to print.
     */
    public void printHealthcareData(HealthcareData healthcareData) {
        if (healthcareData == null) {
            System.out.println("Error: Healthcare data is null.");
            return;
        }

        printHeader(healthcareData);
        printData(healthcareData);
        printFooter();
    }

    /**
     * Prints the header.
     * 
     * @param healthcareData Healthcare data.
     */
    private void printHeader(HealthcareData healthcareData) {
        System.out.println(PrintSettings.PrintHeader.HospitalName + ": " + healthcareData.getHospitalName());
        System.out.println(PrintSettings.PrintHeader.Address + ": " + healthcareData.getAddress());
        System.out.println(); // Empty line for readability
    }

    /**
     * Prints the healthcare data.
     * 
     * @param healthcareData Healthcare data.
     */
    private void printData(HealthcareData healthcareData) {
        System.out.println(PrintSettings.PrintHeader.PatientName + ": " + healthcareData.getPatientName());
        System.out.println(PrintSettings.PrintHeader.DateOfBirth + ": " + healthcareData.getDateOfBirth());
        System.out.println(PrintSettings.PrintHeader.MedicalRecordNumber + ": " + healthcareData.getMedicalRecordNumber());
        System.out.println(); // Empty line for readability
    }

    /**
     * Prints the footer.
     */
    private void printFooter() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String printedDate = LocalDateTime.now().format(formatter);
        System.out.println(PrintSettings.PrintFooter.PrintedBy + ": [Your Name]");
        System.out.println(PrintSettings.PrintFooter.PrintedDate + ": " + printedDate);
    }

    public static void main(String[] args) {
        HealthcareDataPrinter printer = new HealthcareDataPrinter();

        HealthcareData data = new HealthcareData(
            "Example Hospital",
            "123 Main St, Anytown, USA",
            "John Doe",
            "1990-01-01",
            "MRN12345"
        );

        printer.printHealthcareData(data);
    }
}
```
