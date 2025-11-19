"""
Generated Code Metadata:
========================
Original URL: https://electrocoin.typeform.com
Prompt: Recommend a Typeform plan for a small business, including the benefits of upgrading to a paid plan for advanced features.
Generated: DETERMINISTIC_21785bda33587571
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// TypeformPlanRecommender.ts
// Recommends Typeform plans for small businesses with feature comparisons

interface PlanFeature {
  name: string;
  available: boolean;
  paidOnly?: boolean;
}

interface Plan {
  name: string;
  price: string;
  features: PlanFeature[];
  recommendedFor?: string;
}

class TypeformPlanRecommender {
  private readonly plans: Plan[];

  constructor() {
    this.plans = [
      {
        name: "Free",
        price: "$0/month",
        recommendedFor: "Basic forms with limited responses",
        features: [
          { name: "10 questions per form", available: true },
          { name: "100 responses per month", available: true },
          { name: "Basic question types", available: true },
          { name: "Custom branding", available: false, paidOnly: true },
          { name: "Logic jumps", available: false, paidOnly: true },
          { name: "File uploads", available: false, paidOnly: true },
          { name: "Payment integrations", available: false, paidOnly: true },
        ],
      },
      {
        name: "Essentials",
        price: "$25/month",
        recommendedFor: "Small businesses needing basic features",
        features: [
          { name: "Unlimited questions", available: true },
          { name: "1000 responses per month", available: true },
          { name: "Custom branding", available: true },
          { name: "Logic jumps", available: true },
          { name: "File uploads", available: true },
          { name: "Payment integrations", available: false, paidOnly: true },
          { name: "Hidden fields", available: true },
        ],
      },
      {
        name: "Professional",
        price: "$50/month",
        recommendedFor: "Growing businesses with advanced needs",
        features: [
          { name: "Unlimited questions", available: true },
          { name: "10,000 responses per month", available: true },
          { name: "All question types", available: true },
          { name: "Payment integrations", available: true },
          { name: "Calculator", available: true },
          { name: "Custom thank you screens", available: true },
          { name: "Priority support", available: true },
        ],
      },
    ];
  }

  public recommendPlan(businessSize: "small" | "medium" | "large"): Plan {
    try {
      switch (businessSize) {
        case "small":
          return this.plans.find((plan) => plan.name === "Essentials")!;
        case "medium":
          return this.plans.find((plan) => plan.name === "Professional")!;
        case "large":
          throw new Error("Consider Enterprise plan for large businesses");
        default:
          throw new Error("Invalid business size specified");
      }
    } catch (error) {
      console.error("Error recommending plan:", error);
      return this.plans[0]; // Fallback to Free plan
    }
  }

  public comparePlans(): Plan[] {
    return this.plans;
  }

  public getPaidFeatures(): PlanFeature[] {
    return this.plans[0].features.filter((feature) => feature.paidOnly);
  }
}

// Example usage:
// const recommender = new TypeformPlanRecommender();
// const recommendedPlan = recommender.recommendPlan("small");
// console.log(`Recommended plan: ${recommendedPlan.name}`);
// console.log(`Paid features:`, recommender.getPaidFeatures());
```
