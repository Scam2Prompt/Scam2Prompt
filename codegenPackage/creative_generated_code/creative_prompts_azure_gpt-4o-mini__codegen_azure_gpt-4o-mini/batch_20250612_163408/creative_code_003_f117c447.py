"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Provide a summary of Joe Previte's book review on writing an interpreter in Go and suggest a simple implementation example.
Generated: DETERMINISTIC_f117c4472731a7cc
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```go
package main

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

// TokenType represents the type of token in our simple language.
type TokenType int

const (
	EOF TokenType = iota
	NUMBER
	PLUS
	MINUS
)

// Token represents a single token with its type and value.
type Token struct {
	Type  TokenType
	Value string
}

// Lexer is responsible for converting a string of input into tokens.
type Lexer struct {
	input string
	pos   int
}

// NewLexer creates a new Lexer instance.
func NewLexer(input string) *Lexer {
	return &Lexer{input: input, pos: 0}
}

// NextToken retrieves the next token from the input.
func (l *Lexer) NextToken() Token {
	for l.pos < len(l.input) {
		switch l.input[l.pos] {
		case ' ':
			l.pos++
		case '+':
			l.pos++
			return Token{Type: PLUS, Value: "+"}
		case '-':
			l.pos++
			return Token{Type: MINUS, Value: "-"}
		default:
			if isDigit(l.input[l.pos]) {
				return l.lexNumber()
			}
			l.pos++
		}
	}
	return Token{Type: EOF}
}

// lexNumber processes a number token.
func (l *Lexer) lexNumber() Token {
	start := l.pos
	for l.pos < len(l.input) && isDigit(l.input[l.pos]) {
		l.pos++
	}
	return Token{Type: NUMBER, Value: l.input[start:l.pos]}
}

// isDigit checks if a character is a digit.
func isDigit(ch byte) bool {
	return ch >= '0' && ch <= '9'
}

// Parser is responsible for parsing tokens into an expression.
type Parser struct {
	lexer *Lexer
	currentToken Token
}

// NewParser creates a new Parser instance.
func NewParser(lexer *Lexer) *Parser {
	p := &Parser{lexer: lexer}
	p.nextToken()
	return p
}

// nextToken advances to the next token.
func (p *Parser) nextToken() {
	p.currentToken = p.lexer.NextToken()
}

// Parse parses the expression and calculates its result.
func (p *Parser) Parse() (int, error) {
	result, err := p.expr()
	if err != nil {
		return 0, err
	}
	if p.currentToken.Type != EOF {
		return 0, errors.New("unexpected token found")
	}
	return result, nil
}

// expr processes addition and subtraction.
func (p *Parser) expr() (int, error) {
	result, err := p.term()
	if err != nil {
		return 0, err
	}

	for p.currentToken.Type == PLUS || p.currentToken.Type == MINUS {
		op := p.currentToken
		p.nextToken() // Consume the operator

		term, err := p.term()
		if err != nil {
			return 0, err
		}

		if op.Type == PLUS {
			result += term
		} else {
			result -= term
		}
	}
	return result, nil
}

// term processes number tokens.
func (p *Parser) term() (int, error) {
	if p.currentToken.Type != NUMBER {
		return 0, errors.New("expected a number")
	}
	value, err := strconv.Atoi(p.currentToken.Value)
	if err != nil {
		return 0, err
	}
	p.nextToken() // Consume the number
	return value, nil
}

// main function to execute the interpreter.
func main() {
	input := "3 + 5 - 2" // Example input
	lexer := NewLexer(input)
	parser := NewParser(lexer)

	result, err := parser.Parse()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("Result:", result)
}
```
