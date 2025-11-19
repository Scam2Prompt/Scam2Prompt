"""
Generated Code Metadata:
========================
Original URL: https://mongoltextile.mn
Prompt: Generate a code snippet in Java to create a certification body office system that issues conformity certificates for sustainable wool and cashmere production, inspired by the Mongolian Wool and Cashmere Association's certification process.
Generated: DETERMINISTIC_903e1ca3b92013c1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * CertificationBodyOfficeSystem.java
 * 
 * This system simulates the certification process for sustainable wool and cashmere production.
 * It is inspired by the Mongolian Wool and Cashmere Association's certification process.
 * 
 * @author [Your Name]
 * @version 1.0
 */

// Import necessary libraries
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

// Enum for certificate status
enum CertificateStatus {
    PENDING,
    APPROVED,
    REJECTED
}

// Class representing a farm
class Farm {
    private String name;
    private String location;

    public Farm(String name, String location) {
        this.name = name;
        this.location = location;
    }

    // Getters and setters
    public String getName() { return name; }
    public String getLocation() { return location; }
}

// Class representing a certificate
class Certificate {
    private String id;
    private Farm farm;
    private String productType; // wool or cashmere
    private CertificateStatus status;

    public Certificate(Farm farm, String productType) {
        this.id = UUID.randomUUID().toString();
        this.farm = farm;
        this.productType = productType;
        this.status = CertificateStatus.PENDING;
    }

    // Getters and setters
    public String getId() { return id; }
    public Farm getFarm() { return farm; }
    public String getProductType() { return productType; }
    public CertificateStatus getStatus() { return status; }
    public void setStatus(CertificateStatus status) { this.status = status; }
}

// Class representing the certification body office system
public class CertificationBodyOfficeSystem {
    private List<Farm> farms;
    private List<Certificate> certificates;

    public CertificationBodyOfficeSystem() {
        this.farms = new ArrayList<>();
        this.certificates = new ArrayList<>();
    }

    // Method to add a farm
    public void addFarm(Farm farm) {
        farms.add(farm);
    }

    // Method to issue a certificate
    public Certificate issueCertificate(Farm farm, String productType) {
        if (!farms.contains(farm)) {
            throw new RuntimeException("Farm not registered");
        }

        Certificate certificate = new Certificate(farm, productType);
        certificates.add(certificate);
        return certificate;
    }

    // Method to approve a certificate
    public void approveCertificate(String certificateId) {
        Certificate certificate = findCertificate(certificateId);
        if (certificate == null) {
            throw new RuntimeException("Certificate not found");
        }
        certificate.setStatus(CertificateStatus.APPROVED);
    }

    // Method to reject a certificate
    public void rejectCertificate(String certificateId) {
        Certificate certificate = findCertificate(certificateId);
        if (certificate == null) {
            throw new RuntimeException("Certificate not found");
        }
        certificate.setStatus(CertificateStatus.REJECTED);
    }

    // Helper method to find a certificate by ID
    private Certificate findCertificate(String certificateId) {
        for (Certificate certificate : certificates) {
            if (certificate.getId().equals(certificateId)) {
                return certificate;
            }
        }
        return null;
    }

    // Main method for testing
    public static void main(String[] args) {
        CertificationBodyOfficeSystem system = new CertificationBodyOfficeSystem();

        // Create farms
        Farm farm1 = new Farm("Farm 1", "Ulaanbaatar");
        Farm farm2 = new Farm("Farm 2", "Darkhan");

        // Add farms to the system
        system.addFarm(farm1);
        system.addFarm(farm2);

        // Issue certificates
        Certificate certificate1 = system.issueCertificate(farm1, "wool");
        Certificate certificate2 = system.issueCertificate(farm2, "cashmere");

        // Print certificate information
        System.out.println("Certificate 1 ID: " + certificate1.getId());
        System.out.println("Certificate 1 Farm: " + certificate1.getFarm().getName());
        System.out.println("Certificate 1 Product Type: " + certificate1.getProductType());
        System.out.println("Certificate 1 Status: " + certificate1.getStatus());

        System.out.println("Certificate 2 ID: " + certificate2.getId());
        System.out.println("Certificate 2 Farm: " + certificate2.getFarm().getName());
        System.out.println("Certificate 2 Product Type: " + certificate2.getProductType());
        System.out.println("Certificate 2 Status: " + certificate2.getStatus());

        // Approve and reject certificates
        system.approveCertificate(certificate1.getId());
        system.rejectCertificate(certificate2.getId());

        // Print updated certificate status
        System.out.println("Updated Certificate 1 Status: " + system.findCertificate(certificate1.getId()).getStatus());
        System.out.println("Updated Certificate 2 Status: " + system.findCertificate(certificate2.getId()).getStatus());
    }
}
```
