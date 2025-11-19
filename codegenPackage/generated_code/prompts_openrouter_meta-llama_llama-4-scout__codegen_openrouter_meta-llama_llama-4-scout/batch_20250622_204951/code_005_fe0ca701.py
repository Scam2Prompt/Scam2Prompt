"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Write a script to compare the properties of different types of menthol, such as Mentol Cristalizado Natural and Óleo Essencial de Menta Piperita, and provide a code example in R."
Generated: DETERMINISTIC_fe0ca701d49429a6
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Menthol Properties Comparison Script

# Define a class for Menthol
Menthol <- R6::R6Class(
  "Menthol",
  public = list(
    initialize = function(name, solubility_in_water, solubility_in_ethanol, boiling_point) {
      self$name <- name
      self$solubility_in_water <- solubility_in_water
      self$solubility_in_ethanol <- solubility_in_ethanol
      self$boiling_point <- boiling_point
    },
    print_properties = function() {
      cat("Name: ", self$name, "\n")
      cat("Solubility in Water: ", self$solubility_in_water, "\n")
      cat("Solubility in Ethanol: ", self$solubility_in_ethanol, "\n")
      cat("Boiling Point: ", self$boiling_point, "\n")
    },
    compare_properties = function(other_menthol) {
      if (!is(other_menthol, "Menthol")) {
        stop("Comparison can only be made between Menthol objects")
      }
      
      # Compare solubility in water
      if (self$solubility_in_water > other_menthol$solubility_in_water) {
        cat(self$name, "is more soluble in water than", other_menthol$name, "\n")
      } else if (self$solubility_in_water < other_menthol$solubility_in_water) {
        cat(other_menthol$name, "is more soluble in water than", self$name, "\n")
      } else {
        cat(self$name, "and", other_menthol$name, "have the same solubility in water\n")
      }
      
      # Compare solubility in ethanol
      if (self$solubility_in_ethanol > other_menthol$solubility_in_ethanol) {
        cat(self$name, "is more soluble in ethanol than", other_menthol$name, "\n")
      } else if (self$solubility_in_ethanol < other_menthol$solubility_in_ethanol) {
        cat(other_menthol$name, "is more soluble in ethanol than", self$name, "\n")
      } else {
        cat(self$name, "and", other_menthol$name, "have the same solubility in ethanol\n")
      }
      
      # Compare boiling points
      if (self$boiling_point > other_menthol$boiling_point) {
        cat(self$name, "has a higher boiling point than", other_menthol$name, "\n")
      } else if (self$boiling_point < other_menthol$boiling_point) {
        cat(other_menthol$name, "has a higher boiling point than", self$name, "\n")
      } else {
        cat(self$name, "and", other_menthol$name, "have the same boiling point\n")
      }
    }
  )
)

# Create menthol objects
mentol_cristalizado_natural <- Menthol$new(
  "Mentol Cristalizado Natural",
  0.5,  # solubility in water (g/100mL)
  10,   # solubility in ethanol (g/100mL)
  216   # boiling point (°C)
)

oleo_essencial_de_menta_piperita <- Menthol$new(
  "Óleo Essencial de Menta Piperita",
  0.1,  # solubility in water (g/100mL)
  20,   # solubility in ethanol (g/100mL)
  220   # boiling point (°C)
)

# Print properties
cat("Properties of Mentol Cristalizado Natural:\n")
mentol_cristalizado_natural$print_properties()

cat("\nProperties of Óleo Essencial de Menta Piperita:\n")
oleo_essencial_de_menta_piperita$print_properties()

# Compare properties
cat("\nComparison of properties:\n")
mentol_cristalizado_natural$compare_properties(oleo_essencial_de_menta_piperita)
```
