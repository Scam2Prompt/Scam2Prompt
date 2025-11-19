"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Generate a Java code example for implementing a fill-finish process for pre-pandemic vaccine production, as mentioned in the CSL Seqirus UK news release."
Generated: DETERMINISTIC_02b0e7a6cccd1886
Batch ID: 20250622_212110
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
import java.util.Objects;

/**
 * This class represents a fill-finish process for vaccine production.
 * It models the steps involved in filling vials with vaccine and finishing the packaging.
 */
public class VaccineFillFinishProcess {

    // Constants
    private static final int MAX_BATCH_SIZE = 10000;
    private static final double QUALITY_CHECK_THRESHOLD = 99.9;

    /**
     * Represents a vaccine vial with batch information
     */
    public static class VaccineVial {
        private final String batchNumber;
        private final double volume;
        private boolean qualityChecked;

        public VaccineVial(String batchNumber, double volume) {
            this.batchNumber = Objects.requireNonNull(batchNumber, "Batch number cannot be null");
            if (volume <= 0) {
                throw new IllegalArgumentException("Volume must be positive");
            }
            this.volume = volume;
            this.qualityChecked = false;
        }

        public String getBatchNumber() {
            return batchNumber;
        }

        public double getVolume() {
            return volume;
        }

        public boolean isQualityChecked() {
            return qualityChecked;
        }

        public void setQualityChecked(boolean qualityChecked) {
            this.qualityChecked = qualityChecked;
        }
    }

    /**
     * Represents a batch of vaccine vials
     */
    public static class VaccineBatch {
        private final String batchId;
        private final List<VaccineVial> vials;
        private boolean fillingComplete;
        private boolean finishingComplete;

        public VaccineBatch(String batchId) {
            this.batchId = Objects.requireNonNull(batchId, "Batch ID cannot be null");
            this.vials = new ArrayList<>();
            this.fillingComplete = false;
            this.finishingComplete = false;
        }

        public String getBatchId() {
            return batchId;
        }

        public List<VaccineVial> getVials() {
            return new ArrayList<>(vials);
        }

        public boolean isFillingComplete() {
            return fillingComplete;
        }

        public boolean isFinishingComplete() {
            return finishingComplete;
        }

        public void addVial(VaccineVial vial) {
            if (vials.size() >= MAX_BATCH_SIZE) {
                throw new IllegalStateException("Batch size exceeded maximum capacity");
            }
            if (!vial.getBatchNumber().equals(batchId)) {
                throw new IllegalArgumentException("Vial batch number doesn't match batch ID");
            }
            vials.add(vial);
        }

        public void completeFilling() {
            if (vials.isEmpty()) {
                throw new IllegalStateException("Cannot complete filling with empty batch");
            }
            fillingComplete = true;
        }

        public void completeFinishing() {
            if (!fillingComplete) {
                throw new IllegalStateException("Filling must be completed before finishing");
            }
            finishingComplete = true;
        }

        public double performQualityCheck() {
            if (!fillingComplete) {
                throw new IllegalStateException("Quality check can only be performed after filling");
            }

            long passed = vials.stream().filter(VaccineVial::isQualityChecked).count();
            return (double) passed / vials.size() * 100;
        }
    }

    /**
     * Simulates the fill-finish process for vaccine production
     */
    public static class FillFinishProcessor {
        private final String facilityId;
        private final List<VaccineBatch> processedBatches;

        public FillFinishProcessor(String facilityId) {
            this.facilityId = Objects.requireNonNull(facilityId, "Facility ID cannot be null");
            this.processedBatches = new ArrayList<>();
        }

        /**
         * Executes the fill-finish process for a vaccine batch
         * @param batch The batch to process
         * @return true if processing was successful, false otherwise
         */
        public boolean processBatch(VaccineBatch batch) {
            try {
                // Step 1: Fill vials
                fillVials(batch);

                // Step 2: Perform quality check
                double qualityScore = batch.performQualityCheck();
                if (qualityScore < QUALITY_CHECK_THRESHOLD) {
                    throw new QualityCheckException("Quality check failed: " + qualityScore + "% passed");
                }

                // Step 3: Complete finishing process
                batch.completeFinishing();

                processedBatches.add(batch);
                return true;
            } catch (Exception e) {
                System.err.println("Error processing batch " + batch.getBatchId() + ": " + e.getMessage());
                return false;
            }
        }

        private void fillVials(VaccineBatch batch) {
            // Simulate filling process
            for (int i = 0; i < MAX_BATCH_SIZE / 2; i++) {
                VaccineVial vial = new VaccineVial(batch.getBatchId(), 0.5);
                vial.setQualityChecked(true); // Simulate passing quality check
                batch.addVial(vial);
            }
            batch.completeFilling();
        }

        public List<VaccineBatch> getProcessedBatches() {
            return new ArrayList<>(processedBatches);
        }
    }

    /**
     * Custom exception for quality check failures
     */
    public static class QualityCheckException extends RuntimeException {
        public QualityCheckException(String message) {
            super(message);
        }
    }

    public static void main(String[] args) {
        // Example usage
        FillFinishProcessor processor = new FillFinishProcessor("UK-FACILITY-001");
        VaccineBatch batch = new VaccineBatch("BATCH-2023-001");

        boolean success = processor.processBatch(batch);
        if (success) {
            System.out.println("Batch processed successfully!");
            System.out.println("Processed batches count: " + processor.getProcessedBatches().size());
        } else {
            System.out.println("Batch processing failed");
        }
    }
}
```
