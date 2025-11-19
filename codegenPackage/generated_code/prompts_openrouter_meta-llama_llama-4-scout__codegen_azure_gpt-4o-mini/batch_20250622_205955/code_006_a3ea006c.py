"""
Generated Code Metadata:
========================
Original URL: https://loli.bg
Prompt: Develop a product recommendation system in R to suggest children's clothing products based on customer purchase history and product categories on a website like loli.bg.
Generated: DETERMINISTIC_a3ea006c309afbf9
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)      # For data manipulation
library(tidyr)      # For data tidying
library(recommenderlab) # For building recommendation systems

# Function to create a product recommendation system
create_recommendation_system <- function(purchase_data, product_data) {
  
  # Check if the input data frames are valid
  if (!is.data.frame(purchase_data) || !is.data.frame(product_data)) {
    stop("Both purchase_data and product_data must be data frames.")
  }
  
  # Ensure necessary columns are present
  required_purchase_cols <- c("customer_id", "product_id")
  required_product_cols <- c("product_id", "category")
  
  if (!all(required_purchase_cols %in% colnames(purchase_data))) {
    stop("purchase_data must contain customer_id and product_id columns.")
  }
  
  if (!all(required_product_cols %in% colnames(product_data))) {
    stop("product_data must contain product_id and category columns.")
  }
  
  # Create a transaction matrix from purchase data
  transaction_matrix <- purchase_data %>%
    group_by(customer_id, product_id) %>%
    summarise(n = n(), .groups = 'drop') %>%
    spread(product_id, n, fill = 0) %>%
    column_to_rownames("customer_id") %>%
    as.matrix()
  
  # Convert to a realRatingMatrix for the recommenderlab package
  rating_matrix <- as(transaction_matrix, "realRatingMatrix")
  
  # Create a recommendation model using collaborative filtering
  recommender_model <- Recommender(rating_matrix, method = "UBCF")
  
  # Function to recommend products for a given customer
  recommend_products <- function(customer_id, n_recommendations = 5) {
    if (!customer_id %in% rownames(rating_matrix)) {
      stop("Customer ID not found in the purchase data.")
    }
    
    # Generate recommendations
    recommendations <- predict(recommender_model, rating_matrix[customer_id, ], n = n_recommendations)
    
    # Extract recommended product IDs
    recommended_items <- as(recommendations, "list")[[1]]
    
    # Get product details for recommended items
    recommended_products <- product_data %>%
      filter(product_id %in% recommended_items) %>%
      select(product_id, category)
    
    return(recommended_products)
  }
  
  # Return the recommendation function
  return(recommend_products)
}

# Example usage
# Load sample data (replace with actual data)
purchase_data <- data.frame(
  customer_id = c(1, 1, 2, 2, 3, 3, 3),
  product_id = c("A", "B", "A", "C", "B", "C", "D")
)

product_data <- data.frame(
  product_id = c("A", "B", "C", "D"),
  category = c("T-shirts", "Pants", "Dresses", "Jackets")
)

# Create the recommendation system
recommendation_system <- create_recommendation_system(purchase_data, product_data)

# Get recommendations for a specific customer
recommended_items <- recommendation_system(customer_id = 1, n_recommendations = 3)
print(recommended_items)
```
