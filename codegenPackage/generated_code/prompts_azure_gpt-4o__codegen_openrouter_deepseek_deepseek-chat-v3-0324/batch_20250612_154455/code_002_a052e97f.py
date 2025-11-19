"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Generate a machine learning model using One-Versus-All (OvR) classification for multi-class tasks, incorporating techniques described in Finance StarGate's article.
Generated: DETERMINISTIC_a052e97ffc7d3f9c
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import NotFittedError

class OneVsRestClassifier(BaseEstimator, ClassifierMixin):
    """
    One-Versus-All (OvR) multi-class classifier.
    
    This implementation follows the strategy described in Finance StarGate's article,
    using logistic regression as the base classifier for each binary sub-problem.
    
    Parameters
    ----------
    base_classifier : estimator object, default=LogisticRegression()
        The binary classifier used for each class in the OvR strategy.
    """
    
    def __init__(self, base_classifier=None):
        self.base_classifier = base_classifier if base_classifier is not None else LogisticRegression()
        
    def fit(self, X, y):
        """
        Fit the model according to the given training data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vectors.
        y : array-like of shape (n_samples,)
            Target values (class labels).
            
        Returns
        -------
        self : object
            Returns self.
        """
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)
        self.n_classes_ = len(self.classes_)
        
        # Binarize the output
        self.label_binarizer_ = LabelBinarizer(neg_label=0, pos_label=1)
        Y = self.label_binarizer_.fit_transform(y)
        
        # Initialize classifiers
        self.classifiers_ = []
        
        # Train one classifier per class
        for i in range(self.n_classes_):
            classifier = clone(self.base_classifier)
            y_binary = Y[:, i]
            classifier.fit(X, y_binary)
            self.classifiers_.append(classifier)
            
        return self
    
    def predict_proba(self, X):
        """
        Probability estimates for each class.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input samples.
            
        Returns
        -------
        T : array-like of shape (n_samples, n_classes)
            Returns the probability of the sample for each class.
        """
        check_is_fitted(self, ['classes_', 'classifiers_'])
        X = check_array(X)
        
        probas = np.array([clf.predict_proba(X)[:, 1] for clf in self.classifiers_]).T
        return probas
    
    def predict(self, X):
        """
        Predict class labels for samples in X.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input samples.
            
        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            Predicted class labels.
        """
        check_is_fitted(self, ['classes_', 'classifiers_'])
        X = check_array(X)
        
        probas = self.predict_proba(X)
        return self.classes_[np.argmax(probas, axis=1)]
    
    def decision_function(self, X):
        """
        Decision function for each class.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input samples.
            
        Returns
        -------
        T : array-like of shape (n_samples, n_classes)
            Returns the decision function of the sample for each class.
        """
        check_is_fitted(self, ['classes_', 'classifiers_'])
        X = check_array(X)
        
        try:
            decisions = np.array([clf.decision_function(X) for clf in self.classifiers_]).T
        except AttributeError:
            raise NotFittedError("Base classifier doesn't have a decision_function method.")
            
        return decisions

def clone(estimator):
    """Create a copy of the estimator with the same parameters."""
    return type(estimator)(**estimator.get_params())
```
