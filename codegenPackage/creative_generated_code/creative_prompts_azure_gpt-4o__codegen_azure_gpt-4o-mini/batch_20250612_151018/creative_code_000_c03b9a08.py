"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Write a Go interpreter based on the concepts discussed in Joe Previte's article "Writing an Interpreter in Go." Include a simple example of parsing and evaluating expressions.
Generated: DETERMINISTIC_c03b9a0807b21079
Batch ID: 20250612_151018
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
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

// Token types
const (
	EOF          = iota
	NUMBER       // 0-9
	PLUS         // +
	MINUS        // -
	MULTIPLY     // *
	DIVIDE       // /
	LPAREN       // (
	RPAREN       // )
)

// Token represents a lexical token
type Token struct {
	Type  int
	Value string
}

// Lexer struct to tokenize input
type Lexer struct {
	input        string
	position     int
	readPosition int
	currentChar  rune
}

// NewLexer initializes a new lexer
func NewLexer(input string) *Lexer {
	lexer := &Lexer{input: input}
	lexer.readChar()
	return lexer
}

// readChar advances the lexer to the next character
func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.currentChar = 0 // EOF
	} else {
		l.currentChar = rune(l.input[l.readPosition])
	}
	l.position = l.readPosition
	l.readPosition++
}

// NextToken returns the next token from the input
func (l *Lexer) NextToken() Token {
	var token Token

	// Skip whitespace
	for unicode.IsSpace(l.currentChar) {
		l.readChar()
	}

	switch l.currentChar {
	case '+':
		token = Token{Type: PLUS, Value: string(l.currentChar)}
	case '-':
		token = Token{Type: MINUS, Value: string(l.currentChar)}
	case '*':
		token = Token{Type: MULTIPLY, Value: string(l.currentChar)}
	case '/':
		token = Token{Type: DIVIDE, Value: string(l.currentChar)}
	case '(':
		token = Token{Type: LPAREN, Value: string(l.currentChar)}
	case ')':
		token = Token{Type: RPAREN, Value: string(l.currentChar)}
	case 0:
		token = Token{Type: EOF, Value: ""}
	default:
		if unicode.IsDigit(l.currentChar) {
			token.Value = l.readNumber()
			token.Type = NUMBER
			return token
		} else {
			fmt.Printf("Unexpected character: %c\n", l.currentChar)
			os.Exit(1)
		}
	}
	l.readChar()
	return token
}

// readNumber reads a number from input
func (l *Lexer) readNumber() string {
	start := l.position
	for unicode.IsDigit(l.currentChar) {
		l.readChar()
	}
	return l.input[start:l.position]
}

// Parser struct to parse tokens
type Parser struct {
	lexer  *Lexer
	current Token
}

// NewParser initializes a new parser
func NewParser(lexer *Lexer) *Parser {
	parser := &Parser{lexer: lexer}
	parser.nextToken() // Initialize the first token
	return parser
}

// nextToken moves to the next token
func (p *Parser) nextToken() {
	p.current = p.lexer.NextToken()
}

// Parse evaluates the expression
func (p *Parser) Parse() (int, error) {
	result, err := p.expr()
	if err != nil {
		return 0, err
	}
	return result, nil
}

// expr parses an expression
func (p *Parser) expr() (int, error) {
	result, err := p.term()
	if err != nil {
		return 0, err
	}

	for p.current.Type == PLUS || p.current.Type == MINUS {
		op := p.current
		p.nextToken()
		nextTerm, err := p.term()
		if err != nil {
			return 0, err
		}
		if op.Type == PLUS {
			result += nextTerm
		} else {
			result -= nextTerm
		}
	}
	return result, nil
}

// term parses a term
func (p *Parser) term() (int, error) {
	result, err := p.factor()
	if err != nil {
		return 0, err
	}

	for p.current.Type == MULTIPLY || p.current.Type == DIVIDE {
		op := p.current
		p.nextToken()
		nextFactor, err := p.factor()
		if err != nil {
			return 0, err
		}
		if op.Type == MULTIPLY {
			result *= nextFactor
		} else {
			if nextFactor == 0 {
				return 0, fmt.Errorf("division by zero")
			}
			result /= nextFactor
		}
	}
	return result, nil
}

// factor parses a factor
func (p *Parser) factor() (int, error) {
	switch p.current.Type {
	case NUMBER:
		value, err := strconv.Atoi(p.current.Value)
		if err != nil {
			return 0, err
		}
		p.nextToken()
		return value, nil
	case LPAREN:
		p.nextToken()
		result, err := p.expr()
		if err != nil {
			return 0, err
		}
		if p.current.Type != RPAREN {
			return 0, fmt.Errorf("expected closing parenthesis")
		}
		p.nextToken()
		return result, nil
	default:
		return 0, fmt.Errorf("unexpected token: %v", p.current)
	}
}

func main() {
	input := "3 + 5 * (2 - 8)"
	lexer := NewLexer(input)
	parser := NewParser(lexer)

	result, err := parser.Parse()
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	fmt.Printf("Result: %d\n", result)
}
```
