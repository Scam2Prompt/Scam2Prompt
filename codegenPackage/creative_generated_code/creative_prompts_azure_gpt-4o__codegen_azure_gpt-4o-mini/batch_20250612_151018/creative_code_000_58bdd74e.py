"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Write a Go interpreter based on the concepts discussed in Joe Previte's article "Writing an Interpreter in Go." Include a basic example of parsing and evaluating expressions.
Generated: DETERMINISTIC_58bdd74ef4137eb6
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
	"errors"
	"fmt"
	"strconv"
	"strings"
)

// TokenType defines the type of tokens in our expression language.
type TokenType int

const (
	EOF TokenType = iota
	NUMBER
	PLUS
	MINUS
	ASTERISK
	SLASH
	LPAREN
	RPAREN
)

// Token represents a lexical token in our expression language.
type Token struct {
	Type  TokenType
	Value string
}

// Lexer is responsible for converting a string into tokens.
type Lexer struct {
	input        string
	position     int  // current position in input (points to current char)
	readPosition int  // current reading position in input (after current char)
	ch          byte // current character being examined
}

// NewLexer creates a new instance of Lexer.
func NewLexer(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar() // initializes the current character
	return l
}

// readChar reads the next character in input.
func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0 // indicating EOF
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition++
}

// NextToken returns the next token from the input.
func (l *Lexer) NextToken() Token {
	var tok Token

	switch l.ch {
	case '+':
		tok = Token{Type: PLUS, Value: string(l.ch)}
	case '-':
		tok = Token{Type: MINUS, Value: string(l.ch)}
	case '*':
		tok = Token{Type: ASTERISK, Value: string(l.ch)}
	case '/':
		tok = Token{Type: SLASH, Value: string(l.ch)}
	case '(':
		tok = Token{Type: LPAREN, Value: string(l.ch)}
	case ')':
		tok = Token{Type: RPAREN, Value: string(l.ch)}
	case 0:
		tok = Token{Type: EOF, Value: ""}
	default:
		if isDigit(l.ch) {
			tok.Type = NUMBER
			tok.Value = l.readNumber()
			return tok
		} else {
			return Token{Type: EOF, Value: ""}
		}
	}

	l.readChar()
	return tok
}

// readNumber reads a full number from the input.
func (l *Lexer) readNumber() string {
	position := l.position
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.input[position:l.position]
}

// isDigit checks if a character is a digit.
func isDigit(ch byte) bool {
	return ch >= '0' && ch <= '9'
}

// Parser is responsible for parsing tokens into an expression tree.
type Parser struct {
	lexer        *Lexer
	currentToken Token
}

// NewParser creates a new instance of Parser.
func NewParser(lexer *Lexer) *Parser {
	p := &Parser{lexer: lexer}
	p.nextToken() // read the first token
	return p
}

// nextToken advances the parser to the next token.
func (p *Parser) nextToken() {
	p.currentToken = p.lexer.NextToken()
}

// ParseExpression parses an expression and returns its value.
func (p *Parser) ParseExpression() (int, error) {
	result, err := p.parseTerm()
	if err != nil {
		return 0, err
	}

	for p.currentToken.Type == PLUS || p.currentToken.Type == MINUS {
		tok := p.currentToken
		p.nextToken()
		term, err := p.parseTerm()
		if err != nil {
			return 0, err
		}
		if tok.Type == PLUS {
			result += term
		} else {
			result -= term
		}
	}

	return result, nil
}

// parseTerm parses a term (number or parenthesized expression).
func (p *Parser) parseTerm() (int, error) {
	if p.currentToken.Type == NUMBER {
		value, err := strconv.Atoi(p.currentToken.Value)
		if err != nil {
			return 0, errors.New("invalid number")
		}
		p.nextToken()
		return value, nil
	} else if p.currentToken.Type == LPAREN {
		p.nextToken() // consume '('
		result, err := p.ParseExpression()
		if err != nil {
			return 0, err
		}
		if p.currentToken.Type != RPAREN {
			return 0, errors.New("missing closing parenthesis")
		}
		p.nextToken() // consume ')'
		return result, nil
	}
	return 0, errors.New("invalid expression")
}

// Eval evaluates the given expression string.
func Eval(input string) (int, error) {
	lexer := NewLexer(input)
	parser := NewParser(lexer)
	result, err := parser.ParseExpression()
	if err != nil {
		return 0, err
	}
	if parser.currentToken.Type != EOF {
		return 0, errors.New("extra characters after expression")
	}
	return result, nil
}

// Main function to demonstrate the interpreter.
func main() {
	input := "3 + (4 - 2) * 5" // Sample expression
	result, err := Eval(input)
	if err != nil {
		fmt.Printf("Error: %s\n", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
```
