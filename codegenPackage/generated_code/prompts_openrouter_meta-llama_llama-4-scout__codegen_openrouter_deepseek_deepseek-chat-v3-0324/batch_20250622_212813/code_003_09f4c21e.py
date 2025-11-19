"""
Generated Code Metadata:
========================
Original URL: https://guardian-associates.com
Prompt: "Develop a code snippet in Java to automate the process of evaluating risks and optimizing Rolling Reserve for a business, based on the strategies provided by Guardian Associates."
Generated: DETERMINISTIC_09f4c21ea6f9b46e
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;
import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * RollingReserveOptimizer - Automates risk evaluation and rolling reserve optimization
 * based on Guardian Associates strategies.
 */
public class RollingReserveOptimizer {
    
    private static final BigDecimal MIN_RESERVE_PERCENT = new BigDecimal("0.05");
    private static final BigDecimal MAX_RESERVE_PERCENT = new BigDecimal("0.30");
    private static final BigDecimal RISK_THRESHOLD = new BigDecimal("0.70");
    
    /**
     * Represents business financial metrics needed for reserve calculation
     */
    public static class BusinessMetrics {
        private BigDecimal annualRevenue;
        private BigDecimal monthlyRevenue;
        private BigDecimal riskScore; // 0.0 (low risk) to 1.0 (high risk)
        private BigDecimal chargebackRate;
        private BigDecimal refundRate;
        
        public BusinessMetrics(BigDecimal annualRevenue, BigDecimal monthlyRevenue, 
                             BigDecimal riskScore, BigDecimal chargebackRate, 
                             BigDecimal refundRate) {
            this.annualRevenue = annualRevenue;
            this.monthlyRevenue = monthlyRevenue;
            this.riskScore = riskScore;
            this.chargebackRate = chargebackRate;
            this.refundRate = refundRate;
        }
        
        // Getters
        public BigDecimal getAnnualRevenue() { return annualRevenue; }
        public BigDecimal getMonthlyRevenue() { return monthlyRevenue; }
        public BigDecimal getRiskScore() { return riskScore; }
        public BigDecimal getChargebackRate() { return chargebackRate; }
        public BigDecimal getRefundRate() { return refundRate; }
    }
    
    /**
     * Calculates optimal rolling reserve percentage based on business metrics
     * @param metrics Business financial metrics
     * @return Optimal reserve percentage (0.05 to 0.30)
     * @throws IllegalArgumentException if metrics are invalid
     */
    public static BigDecimal calculateOptimalReserve(BusinessMetrics metrics) {
        if (metrics == null) {
            throw new IllegalArgumentException("Business metrics cannot be null");
        }
        
        validateMetrics(metrics);
        
        // Base reserve calculation (Guardian Associates formula)
        BigDecimal baseReserve = MIN_RESERVE_PERCENT.add(
            metrics.getRiskScore().multiply(new BigDecimal("0.20")));
        
        // Adjust for chargeback and refund rates
        BigDecimal chargebackAdjustment = metrics.getChargebackRate()
            .multiply(new BigDecimal("0.5"));
        BigDecimal refundAdjustment = metrics.getRefundRate()
            .multiply(new BigDecimal("0.3"));
        
        BigDecimal adjustedReserve = baseReserve
            .add(chargebackAdjustment)
            .add(refundAdjustment);
        
        // Cap at maximum reserve percentage
        if (adjustedReserve.compareTo(MAX_RESERVE_PERCENT) > 0) {
            return MAX_RESERVE_PERCENT;
        }
        
        return adjustedReserve.setScale(4, RoundingMode.HALF_UP);
    }
    
    /**
     * Evaluates business risk level based on metrics
     * @param metrics Business financial metrics
     * @return Risk evaluation result
     * @throws IllegalArgumentException if metrics are invalid
     */
    public static String evaluateRisk(BusinessMetrics metrics) {
        if (metrics == null) {
            throw new IllegalArgumentException("Business metrics cannot be null");
        }
        
        validateMetrics(metrics);
        
        if (metrics.getRiskScore().compareTo(RISK_THRESHOLD) > 0) {
            return "HIGH RISK: Immediate action recommended";
        } else if (metrics.getRiskScore().compareTo(new BigDecimal("0.4")) > 0) {
            return "MODERATE RISK: Monitor closely";
        } else {
            return "LOW RISK: Standard monitoring";
        }
    }
    
    private static void validateMetrics(BusinessMetrics metrics) {
        if (metrics.getAnnualRevenue().compareTo(BigDecimal.ZERO) <= 0 ||
            metrics.getMonthlyRevenue().compareTo(BigDecimal.ZERO) <= 0 ||
            metrics.getRiskScore().compareTo(BigDecimal.ZERO) < 0 ||
            metrics.getRiskScore().compareTo(BigDecimal.ONE) > 0 ||
            metrics.getChargebackRate().compareTo(BigDecimal.ZERO) < 0 ||
            metrics.getRefundRate().compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Invalid business metrics provided");
        }
    }
    
    /**
     * Calculates the actual reserve amount based on monthly revenue
     * @param monthlyRevenue Business monthly revenue
     * @param reservePercentage Reserve percentage (0.05 to 0.30)
     * @return Reserve amount
     * @throws IllegalArgumentException if inputs are invalid
     */
    public static BigDecimal calculateReserveAmount(BigDecimal monthlyRevenue, 
                                                  BigDecimal reservePercentage) {
        if (monthlyRevenue == null || reservePercentage == null) {
            throw new IllegalArgumentException("Inputs cannot be null");
        }
        
        if (monthlyRevenue.compareTo(BigDecimal.ZERO) <= 0 ||
            reservePercentage.compareTo(MIN_RESERVE_PERCENT) < 0 ||
            reservePercentage.compareTo(MAX_RESERVE_PERCENT) > 0) {
            throw new IllegalArgumentException("Invalid monthly revenue or reserve percentage");
        }
        
        return monthlyRevenue.multiply(reservePercentage)
            .setScale(2, RoundingMode.HALF_UP);
    }
    
    /**
     * Generates a risk mitigation plan based on risk evaluation
     * @param riskEvaluation Risk evaluation result
     * @return Mitigation plan recommendations
     */
    public static List<String> generateMitigationPlan(String riskEvaluation) {
        List<String> recommendations = new ArrayList<>();
        
        if (riskEvaluation.contains("HIGH RISK")) {
            recommendations.add("1. Increase rolling reserve by 5% immediately");
            recommendations.add("2. Conduct thorough risk assessment");
            recommendations.add("3. Implement additional fraud detection measures");
            recommendations.add("4. Review all high-risk transactions");
        } else if (riskEvaluation.contains("MODERATE RISK")) {
            recommendations.add("1. Monitor rolling reserve monthly");
            recommendations.add("2. Review chargeback patterns");
            recommendations.add("3. Consider incremental reserve adjustments");
        } else {
            recommendations.add("1. Maintain current reserve level");
            recommendations.add("2. Quarterly risk review recommended");
        }
        
        return recommendations;
    }
}
```
