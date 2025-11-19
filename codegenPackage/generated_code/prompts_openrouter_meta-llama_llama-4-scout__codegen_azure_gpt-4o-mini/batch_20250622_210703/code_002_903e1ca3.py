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
import java.util.Optional;

// Class representing a Certification Body Office
public class CertificationBodyOffice {
    private List<Producer> producers; // List of registered producers

    // Constructor to initialize the certification body office
    public CertificationBodyOffice() {
        this.producers = new ArrayList<>();
    }

    // Method to register a new producer
    public void registerProducer(Producer producer) {
        if (producer == null || producers.contains(producer)) {
            throw new IllegalArgumentException("Invalid producer or already registered.");
        }
        producers.add(producer);
    }

    // Method to issue a conformity certificate for a producer
    public Optional<Certificate> issueCertificate(String producerName) {
        for (Producer producer : producers) {
            if (producer.getName().equalsIgnoreCase(producerName)) {
                if (producer.isEligibleForCertification()) {
                    Certificate certificate = new Certificate(producer);
                    producer.setCertificate(certificate);
                    return Optional.of(certificate);
                } else {
                    throw new IllegalStateException("Producer is not eligible for certification.");
                }
            }
        }
        throw new IllegalArgumentException("Producer not found.");
    }

    // Main method for demonstration purposes
    public static void main(String[] args) {
        CertificationBodyOffice office = new CertificationBodyOffice();
        
        // Create a producer
        Producer producer = new Producer("Mongolian Wool Co.", true);
        
        // Register the producer
        office.registerProducer(producer);
        
        // Issue a certificate
        try {
            Certificate certificate = office.issueCertificate("Mongolian Wool Co.");
            System.out.println("Certificate issued: " + certificate);
        } catch (Exception e) {
            System.err.println("Error issuing certificate: " + e.getMessage());
        }
    }
}

// Class representing a Producer
class Producer {
    private String name; // Name of the producer
    private boolean eligibleForCertification; // Eligibility status
    private Certificate certificate; // Certificate issued to the producer

    // Constructor to initialize the producer
    public Producer(String name, boolean eligibleForCertification) {
        this.name = name;
        this.eligibleForCertification = eligibleForCertification;
    }

    // Getter for producer name
    public String getName() {
        return name;
    }

    // Check if the producer is eligible for certification
    public boolean isEligibleForCertification() {
        return eligibleForCertification;
    }

    // Set the issued certificate
    public void setCertificate(Certificate certificate) {
        this.certificate = certificate;
    }
}

// Class representing a Certificate
class Certificate {
    private Producer producer; // Producer associated with the certificate
    private String certificateId; // Unique identifier for the certificate

    // Constructor to initialize the certificate
    public Certificate(Producer producer) {
        this.producer = producer;
        this.certificateId = generateCertificateId();
    }

    // Generate a unique certificate ID (for demonstration purposes)
    private String generateCertificateId() {
        return "CERT-" + System.currentTimeMillis();
    }

    // Override toString for easy representation
    @Override
    public String toString() {
        return "Certificate ID: " + certificateId + ", Producer: " + producer.getName();
    }
}
```
