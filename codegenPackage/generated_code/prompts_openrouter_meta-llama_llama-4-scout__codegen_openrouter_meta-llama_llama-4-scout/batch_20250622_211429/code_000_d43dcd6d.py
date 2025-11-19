"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Write a code snippet in Go for a simple interpreter, as discussed in Joe Previte's book review on this website.
Generated: DETERMINISTIC_d43dcd6d2058baca
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
// Package main provides a simple interpreter for basic arithmetic expressions.
package main

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

// TokenType represents the type of a token.
type TokenType int

const (
	// NumberToken represents a numeric token.
	NumberToken TokenType = iota
	// PlusToken represents a plus operator token.
	PlusToken
	// MinusToken represents a minus operator token.
	MinusToken
	// EOFToken represents the end of the input.
	EOFToken
)

// Token represents a single token in the input.
type Token struct {
	Type  TokenType
	Value string
}

// Interpreter represents a simple interpreter.
type Interpreter struct {
	tokens []*Token
	pos    int
}

// NewInterpreter returns a new interpreter instance.
func NewInterpreter(input string) (*Interpreter, error) {
	tokens, err := tokenize(input)
	if err != nil {
		return nil, err
	}
	return &Interpreter{tokens: tokens}, nil
}

// tokenize splits the input into individual tokens.
func tokenize(input string) ([]*Token, error) {
	tokens := []*Token{}
	parts := strings.Fields(input)
	for _, part := range parts {
		if num, err := strconv.ParseFloat(part, 64); err == nil {
			tokens = append(tokens, &Token{Type: NumberToken, Value: part})
		} else if part == "+" {
			tokens = append(tokens, &Token{Type: PlusToken, Value: part})
		} else if part == "-" {
			tokens = append(tokens, &Token{Type: MinusToken, Value: part})
		} else {
			return nil, fmt.Errorf("unknown token: %s", part)
		}
	}
	tokens = append(tokens, &Token{Type: EOFToken, Value: ""})
	return tokens, nil
}

// NextToken returns the next token from the input.
func (i *Interpreter) NextToken() *Token {
	if i.pos < len(i.tokens) {
		token := i.tokens[i.pos]
		i.pos++
		return token
	}
	return &Token{Type: EOFToken, Value: ""}
}

// Evaluate evaluates the input expression.
func (i *Interpreter) Evaluate() (float64, error) {
	result, err := i.expr()
	if err != nil {
		return 0, err
	}
	token := i.NextToken()
	if token.Type != EOFToken {
		return 0, errors.New("unexpected token after expression")
	}
	return result, nil
}

// expr evaluates an expression.
func (i *Interpreter) expr() (float64, error) {
	result, err := i.term()
	if err != nil {
		return 0, err
	}
	for {
		token := i.NextToken()
		if token.Type == PlusToken {
			term, err := i.term()
			if err != nil {
				return 0, err
			}
			result += term
		} else if token.Type == MinusToken {
			term, err := i.term()
			if err != nil {
				return 0, err
			}
			result -= term
		} else {
			i.pos-- // put back the token
			break
		}
	}
	return result, nil
}

// term evaluates a term (a single number for now).
func (i *Interpreter) term() (float64, error) {
	token := i.NextToken()
	if token.Type != NumberToken {
		return 0, fmt.Errorf("expected number, got: %s", token.Value)
	}
	num, err := strconv.ParseFloat(token.Value, 64)
	if err != nil {
		return 0, err
	}
	return num, nil
}

func main() {
	input := "2 + 3 - 1"
	interpreter, err := NewInterpreter(input)
	if err != nil {
		fmt.Println(err)
		return
	}
	result, err := interpreter.Evaluate()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(result)
}
```
