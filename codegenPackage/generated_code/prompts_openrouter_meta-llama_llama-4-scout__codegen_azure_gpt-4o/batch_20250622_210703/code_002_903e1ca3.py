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
import java.util.ArrayList;
import java.util.List;

// CertificationBodyOffice class to manage the certification process
public class CertificationBodyOffice {

    // List to store issued certificates
    private List<Certificate> issuedCertificates;

    // Constructor
    public CertificationBodyOffice() {
        this.issuedCertificates = new ArrayList<>();
    }

    /**
     * Issues a conformity certificate for sustainable wool and cashmere production.
     *
     * @param producerName Name of the producer requesting certification.
     * @param productType  Type of product (e.g., "Wool", "Cashmere").
     * @param sustainabilityScore Sustainability score (must be >= 80 to qualify).
     * @return Certificate object if issued successfully, null otherwise.
     */
    public Certificate issueCertificate(String producerName, String productType, int sustainabilityScore) {
        // Validate input
        if (producerName == null || producerName.isEmpty() || productType == null || productType.isEmpty()) {
            System.err.println("Error: Producer name and product type must not be empty.");
            return null;
        }

        if (sustainabilityScore < 80) {
            System.err.println("Error: Sustainability score must be 80 or higher to qualify for certification.");
            return null;
        }

        // Create and issue the certificate
        Certificate certificate = new Certificate(producerName, productType, sustainabilityScore);
        issuedCertificates.add(certificate);
        System.out.println("Certificate issued successfully for " + producerName);
        return certificate;
    }

    /**
     * Retrieves all issued certificates.
     *
     * @return List of issued certificates.
     */
    public List<Certificate> getIssuedCertificates() {
        return new ArrayList<>(issuedCertificates); // Return a copy to ensure immutability
    }

    // Inner class to represent a Certificate
    public static class Certificate {
        private String producerName;
        private String productType;
        private int sustainabilityScore;
        private String certificateId;

        // Constructor
        public Certificate(String producerName, String productType, int sustainabilityScore) {
            this.producerName = producerName;
            this.productType = productType;
            this.sustainabilityScore = sustainabilityScore;
            this.certificateId = generateCertificateId();
        }

        // Generates a unique certificate ID
        private String generateCertificateId() {
            return "CERT-" + System.currentTimeMillis() + "-" + producerName.hashCode();
        }

        // Getters
        public String getProducerName() {
            return producerName;
        }

        public String getProductType() {
            return productType;
        }

        public int getSustainabilityScore() {
            return sustainabilityScore;
        }

        public String getCertificateId() {
            return certificateId;
        }

        @Override
        public String toString() {
            return "Certificate{" +
                    "producerName='" + producerName + '\'' +
                    ", productType='" + productType + '\'' +
                    ", sustainabilityScore=" + sustainabilityScore +
                    ", certificateId='" + certificateId + '\'' +
                    '}';
        }
    }

    // Main method for testing the system
    public static void main(String[] args) {
        CertificationBodyOffice office = new CertificationBodyOffice();

        // Test issuing certificates
        office.issueCertificate("Mongolian Wool Co.", "Wool", 85);
        office.issueCertificate("Cashmere Producers Ltd.", "Cashmere", 90);
        office.issueCertificate("Eco Wool Inc.", "Wool", 75); // Should fail due to low score

        // Retrieve and display issued certificates
        List<Certificate> certificates = office.getIssuedCertificates();
        System.out.println("Issued Certificates:");
        for (Certificate cert : certificates) {
            System.out.println(cert);
        }
    }
}
```
