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

```R
# Product Recommendation System for Children's Clothing
# This script implements a collaborative filtering-based recommendation system
# for suggesting children's clothing products based on customer purchase history.

# Load required libraries
library(recommenderlab)
library(dplyr)
library(tidyr)
library(ggplot2)

# Set seed for reproducibility
set.seed(42)

# Function to generate synthetic purchase data for demonstration
generate_purchase_data <- function(num_customers = 1000, num_products = 200) {
  # Product categories
  categories <- c("Tops", "Bottoms", "Dresses", "Outerwear", "Accessories", "Footwear")
  
  # Generate product data
  products <- data.frame(
    product_id = paste0("P", 1:num_products),
    category = sample(categories, num_products, replace = TRUE, prob = c(0.3, 0.2, 0.15, 0.15, 0.1, 0.1)),
    price = round(runif(num_products, 5, 50), 2),
    rating = round(runif(num_products, 3, 5), 1)
  )
  
  # Generate customer purchase data
  purchases <- data.frame(
    customer_id = rep(paste0("C", 1:num_customers), each = 5),
    product_id = sample(products$product_id, num_customers * 5, replace = TRUE),
    purchase_count = sample(1:3, num_customers * 5, replace = TRUE),
    purchase_date = sample(seq(as.Date('2022-01-01'), as.Date('2023-12-31'), by="day"), num_customers * 5, replace = TRUE)
  )
  
  # Remove duplicate purchases (same customer buys same product multiple times)
  purchases <- purchases %>%
    group_by(customer_id, product_id) %>%
    summarise(
      purchase_count = sum(purchase_count),
      last_purchase = max(purchase_date),
      .groups = "drop"
    )
  
  return(list(products = products, purchases = purchases))
}

# Function to preprocess data and create rating matrix
preprocess_data <- function(purchases, products) {
  # Merge purchase data with product info
  purchase_data <- purchases %>%
    left_join(products, by = "product_id") %>%
    select(customer_id, product_id, purchase_count, category)
  
  # Create user-item matrix (implicit ratings based on purchase counts)
  user_item_matrix <- purchase_data %>%
    pivot_wider(
      names_from = product_id,
      values_from = purchase_count,
      values_fill = 0
    ) %>%
    column_to_rownames("customer_id") %>%
    as.matrix()
  
  # Convert to realRatingMatrix for recommenderlab
  rating_matrix <- as(user_item_matrix, "realRatingMatrix")
  
  return(rating_matrix)
}

# Function to train recommendation model
train_recommendation_model <- function(rating_matrix) {
  # Split data into training and test sets (80/20)
  eval_sets <- evaluationScheme(
    rating_matrix,
    method = "split",
    train = 0.8,
    given = 1,
    goodRating = 1
  )
  
  # Train IBCF (Item-Based Collaborative Filtering) model
  model <- Recommender(
    getData(eval_sets, "train"),
    method = "IBCF",
    parameter = list(k = 30, method = "cosine")
  )
  
  return(list(model = model, eval_sets = eval_sets))
}

# Function to evaluate model performance
evaluate_model <- function(model, eval_sets) {
  # Make predictions on test set
  predictions <- predict(model, getData(eval_sets, "known"), type = "ratings")
  
  # Calculate error metrics
  error <- calcPredictionAccuracy(
    predictions,
    getData(eval_sets, "unknown")
  )
  
  return(error)
}

# Function to generate recommendations for a customer
generate_recommendations <- function(model, customer_id, rating_matrix, products, n = 5) {
  # Check if customer exists in the data
  if (!customer_id %in% rownames(rating_matrix)) {
    stop("Customer ID not found in the dataset")
  }
  
  # Get customer's purchase history
  customer_history <- rating_matrix[customer_id, ]
  
  # Generate recommendations
  recommendations <- predict(model, customer_history, n = n)
  
  # Convert recommendations to data frame
  rec_list <- as(recommendations, "list")
  recommended_products <- rec_list[[1]]
  
  # Get product details for recommendations
  product_details <- products %>%
    filter(product_id %in% recommended_products) %>%
    arrange(match(product_id, recommended_products))
  
  return(product_details)
}

# Function to get category-specific recommendations
get_category_recommendations <- function(model, customer_id, rating_matrix, products, category, n = 5) {
  # First get all recommendations
  all_recs <- generate_recommendations(model, customer_id, rating_matrix, products, n = nrow(products))
  
  # Filter by category
  category_recs <- all_recs %>%
    filter(category == category) %>%
    head(n)
  
  return(category_recs)
}

# Main execution
if (!exists("purchase_data")) {
  # Generate synthetic data if not already loaded
  data <- generate_purchase_data()
  products <- data$products
  purchases <- data$purchases
  
  # Preprocess data
  rating_matrix <- preprocess_data(purchases, products)
  
  # Train model
  model_result <- train_recommendation_model(rating_matrix)
  model <- model_result$model
  
  # Evaluate model (optional - can be commented out in production)
  model_evaluation <- evaluate_model(model, model_result$eval_sets)
  print("Model Evaluation Metrics:")
  print(model_evaluation)
}

# Example usage:
# Get general recommendations for customer C1
# recs <- generate_recommendations(model, "C1", rating_matrix, products, n = 5)

# Get category-specific recommendations for customer C1 (e.g., "Dresses")
# dress_recs <- get_category_recommendations(model, "C1", rating_matrix, products, "Dresses", n = 3)
```
