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
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

/**
 * CertificationBodyOfficeSystem - Issues conformity certificates for sustainable wool and cashmere production
 */
public class CertificationBodyOfficeSystem {

    // Certificate status enum
    public enum CertificateStatus {
        PENDING, APPROVED, REJECTED, EXPIRED, REVOKED
    }

    // Certificate class representing a conformity certificate
    public static class Certificate {
        private final String certificateId;
        private final String producerName;
        private final String productionFacility;
        private final Date issueDate;
        private final Date expiryDate;
        private CertificateStatus status;
        private final Map<String, Boolean> sustainabilityCriteria;

        public Certificate(String producerName, String productionFacility, Date expiryDate) {
            this.certificateId = "MWCA-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
            this.producerName = producerName;
            this.productionFacility = productionFacility;
            this.issueDate = new Date();
            this.expiryDate = expiryDate;
            this.status = CertificateStatus.PENDING;
            this.sustainabilityCriteria = new HashMap<>();
            initializeDefaultCriteria();
        }

        private void initializeDefaultCriteria() {
            sustainabilityCriteria.put("Animal Welfare Standards", false);
            sustainabilityCriteria.put("Land Management Practices", false);
            sustainabilityCriteria.put("Water Conservation", false);
            sustainabilityCriteria.put("Chemical Usage Compliance", false);
            sustainabilityCriteria.put("Worker Fair Treatment", false);
            sustainabilityCriteria.put("Traceability System", false);
        }

        public void updateCriterion(String criterion, boolean meetsRequirement) {
            if (sustainabilityCriteria.containsKey(criterion)) {
                sustainabilityCriteria.put(criterion, meetsRequirement);
            }
        }

        public boolean meetsAllRequirements() {
            return !sustainabilityCriteria.containsValue(false);
        }

        // Getters
        public String getCertificateId() { return certificateId; }
        public String getProducerName() { return producerName; }
        public String getProductionFacility() { return productionFacility; }
        public Date getIssueDate() { return issueDate; }
        public Date getExpiryDate() { return expiryDate; }
        public CertificateStatus getStatus() { return status; }
        public Map<String, Boolean> getSustainabilityCriteria() { return new HashMap<>(sustainabilityCriteria); }

        // Setters
        public void setStatus(CertificateStatus status) { this.status = status; }
    }

    // Certification body office class
    public static class CertificationOffice {
        public Certificate createCertificate(String producerName, String productionFacility, Date expiryDate) {
            return new Certificate(producerName, productionFacility, expiryDate);
        }

        public void evaluateCertificate(Certificate certificate) {
            if (certificate.meetsAllRequirements()) {
                certificate.setStatus(CertificateStatus.APPROVED);
            } else {
                certificate.setStatus(CertificateStatus.REJECTED);
            }
        }

        public void revokeCertificate(Certificate certificate) {
            if (certificate.getStatus() == CertificateStatus.APPROVED) {
                certificate.setStatus(CertificateStatus.REVOKED);
            }
        }

        public void checkExpiration(Certificate certificate) {
            if (new Date().after(certificate.getExpiryDate()) && 
                certificate.getStatus() == CertificateStatus.APPROVED) {
                certificate.setStatus(CertificateStatus.EXPIRED);
            }
        }
    }

    // Example usage
    public static void main(String[] args) {
        CertificationOffice office = new CertificationOffice();
        
        // Create a new certificate (expires in 1 year)
        Date expiryDate = new Date(System.currentTimeMillis() + 365L * 24 * 60 * 60 * 1000);
        Certificate cert = office.createCertificate("Gobi Pastures LLC", "Gobi Desert Facility", expiryDate);
        
        // Update criteria based on audit
        cert.updateCriterion("Animal Welfare Standards", true);
        cert.updateCriterion("Land Management Practices", true);
        cert.updateCriterion("Water Conservation", true);
        cert.updateCriterion("Chemical Usage Compliance", true);
        cert.updateCriterion("Worker Fair Treatment", true);
        cert.updateCriterion("Traceability System", true);
        
        // Evaluate the certificate
        office.evaluateCertificate(cert);
        
        System.out.println("Certificate ID: " + cert.getCertificateId());
        System.out.println("Status: " + cert.getStatus());
    }
}
```
