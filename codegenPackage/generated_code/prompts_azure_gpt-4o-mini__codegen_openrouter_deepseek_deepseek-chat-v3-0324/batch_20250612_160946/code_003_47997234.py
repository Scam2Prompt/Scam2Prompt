"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Explain how to configure selectivity and catchability in the Rapid Conditioning Model within openMSE.
Generated: DETERMINISTIC_479972348ede81bc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Function to configure selectivity and catchability in the Rapid Conditioning Model (RCM) within openMSE
configure_RCM <- function(OM, 
                         selectivity = "logistic", 
                         catchability = 1, 
                         sel_params = NULL,
                         qcv = 0) {
  #' Configure selectivity and catchability for RCM in openMSE
  #'
  #' @param OM An operating model object from openMSE
  #' @param selectivity Selectivity function type ("logistic", "dome", "double_logistic")
  #' @param catchability Base catchability coefficient (scalar)
  #' @param sel_params List of parameters for selectivity function
  #' @param qcv Coefficient of variation for catchability (0 for constant)
  #'
  #' @return Updated operating model with configured selectivity and catchability
  #' @export
  
  # Error checking
  if (!inherits(OM, "OM")) {
    stop("OM must be an operating model object from openMSE")
  }
  
  if (!selectivity %in% c("logistic", "dome", "double_logistic")) {
    stop("selectivity must be one of: 'logistic', 'dome', 'double_logistic'")
  }
  
  if (catchability <= 0) {
    stop("catchability must be positive")
  }
  
  if (qcv < 0) {
    stop("qcv must be >= 0")
  }
  
  # Set default selectivity parameters if not provided
  if (is.null(sel_params)) {
    sel_params <- switch(selectivity,
      "logistic" = list(L50 = 50, L95 = 60),
      "dome" = list(L50 = 50, L95 = 60, peak = 55),
      "double_logistic" = list(L50 = 50, L95 = 60, L50_right = 70, L95_right = 80)
    )
  }
  
  # Configure selectivity
  OM@cpars$sel <- switch(selectivity,
    "logistic" = {
      function(length) {
        1/(1 + exp(-log(19) * (length - sel_params$L50)/(sel_params$L95 - sel_params$L50)))
      }
    },
    "dome" = {
      function(length) {
        asc <- 1/(1 + exp(-log(19) * (length - sel_params$L50)/(sel_params$L95 - sel_params$L50)))
        dsc <- 1/(1 + exp(log(19) * (length - sel_params$peak)/(sel_params$peak - sel_params$L50)))
        asc * dsc
      }
    },
    "double_logistic" = {
      function(length) {
        left <- 1/(1 + exp(-log(19) * (length - sel_params$L50)/(sel_params$L95 - sel_params$L50)))
        right <- 1/(1 + exp(log(19) * (length - sel_params$L50_right)/(sel_params$L95_right - sel_params$L50_right)))
        left * right
      }
    }
  )
  
  # Configure catchability
  OM@cpars$q <- catchability
  if (qcv > 0) {
    OM@cpars$qinc <- c(0, qcv)  # Interannual variability in q
  }
  
  # Return updated OM
  return(OM)
}

# Example usage:
# library(openMSE)
# myOM <- DLMtool::testOM
# myOM <- configure_RCM(myOM, 
#                      selectivity = "logistic",
#                      catchability = 0.8,
#                      sel_params = list(L50 = 45, L95 = 55),
#                      qcv = 0.1)
```
