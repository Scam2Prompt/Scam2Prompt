"""
Generated Code Metadata:
========================
Original URL: https://tensor.credit
Prompt: "How can I implement tensor decomposition techniques using MATLAB or Octave?"
Generated: DETERMINISTIC_cd6b2172f1e1fed9
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```matlab
% Tensor Decomposition using MATLAB/Octave
% This script demonstrates CP (CANDECOMP/PARAFAC) and Tucker decompositions
% using Tensor Toolbox for MATLAB or Octave-compatible alternatives

% Check if Tensor Toolbox is available
try
    addpath('tensor_toolbox');
    addpath('tensor_toolbox/met/');
catch
    warning('Tensor Toolbox not found. Using alternative implementations.');
end

% Generate a random 3-way tensor for demonstration
dims = [5, 4, 3]; % Dimensions of the tensor
X = randn(dims);   % Random tensor data

%% CP Decomposition (CANDECOMP/PARAFAC)
function [factors, lambda] = cp_decomposition(X, rank, max_iter, tol)
    % CP decomposition implementation
    % Inputs:
    %   X - input tensor
    %   rank - decomposition rank
    %   max_iter - maximum iterations
    %   tol - convergence tolerance
    % Outputs:
    %   factors - cell array of factor matrices
    %   lambda - weights vector
    
    ndims = ndims(X);
    dims = size(X);
    factors = cell(1, ndims);
    
    % Initialize factor matrices randomly
    for n = 1:ndims
        factors{n} = randn(dims(n), rank);
    end
    
    % Initialize lambda
    lambda = ones(rank, 1);
    
    for iter = 1:max_iter
        for n = 1:ndims
            % Compute Khatri-Rao product of other factors
            kr_prod = 1;
            for m = [1:n-1, n+1:ndims]
                kr_prod = khatrirao(kr_prod, factors{m});
            end
            
            % Update factor matrix
            X_unfolded = double(tenmat(X, n));
            factors{n} = X_unfolded * kr_prod * pinv(kr_prod' * kr_prod);
            
            % Normalize columns and store norms in lambda
            norms = sqrt(sum(factors{n}.^2, 1));
            lambda = lambda .* norms';
            factors{n} = bsxfun(@rdivide, factors{n}, norms);
        end
        
        % Check convergence
        if iter > 1 && norm(factors{n} - prev_factors{n}, 'fro') < tol
            break;
        end
        prev_factors = factors;
    end
end

%% Tucker Decomposition
function [core, factors] = tucker_decomposition(X, ranks, max_iter, tol)
    % Tucker decomposition implementation
    % Inputs:
    %   X - input tensor
    %   ranks - vector of ranks for each mode
    %   max_iter - maximum iterations
    %   tol - convergence tolerance
    % Outputs:
    %   core - core tensor
    %   factors - cell array of factor matrices
    
    ndims = ndims(X);
    dims = size(X);
    factors = cell(1, ndims);
    
    % Initialize factor matrices using HOSVD
    for n = 1:ndims
        X_unfolded = double(tenmat(X, n));
        [U, ~, ~] = svd(X_unfolded, 'econ');
        factors{n} = U(:, 1:ranks(n));
    end
    
    % Initialize core tensor
    core = ttm(X, factors, 't');
    
    for iter = 1:max_iter
        prev_core = core;
        
        % Update each factor matrix
        for n = 1:ndims
            % Compute mode-n matricized core times Khatri-Rao product
            core_unfolded = double(tenmat(core, n));
            kr_prod = 1;
            for m = [1:n-1, n+1:ndims]
                kr_prod = khatrirao(kr_prod, factors{m});
            end
            
            % Update factor matrix
            X_unfolded = double(tenmat(X, n));
            [U, ~, ~] = svd(X_unfolded * kr_prod', 'econ');
            factors{n} = U(:, 1:ranks(n));
        end
        
        % Update core tensor
        core = ttm(X, factors);
        
        % Check convergence
        if iter > 1 && norm(core(:) - prev_core(:)) < tol
            break;
        end
    end
end

%% Helper functions (if Tensor Toolbox not available)
function M = tenmat(T, mode)
    % Matricize tensor along specified mode
    if exist('tensor', 'class') && isa(T, 'tensor')
        M = double(tenmat(T, mode));
    else
        dims = size(T);
        order = [mode, setdiff(1:ndims(T), mode)];
        M = reshape(permute(T, order), dims(mode), []);
    end
end

function Z = ttm(X, U, trans)
    % Tensor times matrix (mode-n product)
    if nargin < 3, trans = ''; end
    
    ndimsX = ndims(X);
    Z = X;
    for n = 1:length(U)
        if strcmpi(trans, 't')
            Z = mode_product(Z, U{n}', n);
        else
            Z = mode_product(Z, U{n}, n);
        end
    end
end

function Y = mode_product(X, U, mode)
    % Mode-n product implementation
    X_size = size(X);
    Y = permute(X, [mode, setdiff(1:ndims(X), mode)]);
    Y = reshape(Y, X_size(mode), []);
    Y = U * Y;
    Y = reshape(Y, [size(U,1), X_size(setdiff(1:ndims(X), mode))]);
    Y = ipermute(Y, [mode, setdiff(1:ndims(X), mode)]);
end

function C = khatrirao(A, B)
    % Khatri-Rao product implementation
    [m, r1] = size(A);
    [n, r2] = size(B);
    if r1 ~= r2
        error('Matrices must have same number of columns');
    end
    
    C = zeros(m*n, r1);
    for i = 1:r1
        C(:,i) = kron(A(:,i), B(:,i));
    end
end

%% Example Usage
% CP Decomposition
rank = 2;
max_iter = 50;
tol = 1e-6;
[cp_factors, cp_lambda] = cp_decomposition(X, rank, max_iter, tol);

% Tucker Decomposition
ranks = [3, 2, 2];
[tucker_core, tucker_factors] = tucker_decomposition(X, ranks, max_iter, tol);

% Reconstruction error
X_cp = reconstruct_cp(cp_factors, cp_lambda);
X_tucker = reconstruct_tucker(tucker_core, tucker_factors);

cp_error = norm(X(:) - X_cp(:)) / norm(X(:));
tucker_error = norm(X(:) - X_tucker(:)) / norm(X(:));

fprintf('CP reconstruction error: %.4f\n', cp_error);
fprintf('Tucker reconstruction error: %.4f\n', tucker_error);

function X_hat = reconstruct_cp(factors, lambda)
    % Reconstruct tensor from CP factors
    ndims = length(factors);
    X_hat = zeros(size(factors{1},1), size(factors{2},1), size(factors{3},1));
    
    for r = 1:length(lambda)
        comp = lambda(r);
        for n = 1:ndims
            comp = comp .* factors{n}(:,r);
        end
        X_hat = X_hat + comp;
    end
end

function X_hat = reconstruct_tucker(core, factors)
    % Reconstruct tensor from Tucker factors
    X_hat = ttm(core, factors);
end
```
