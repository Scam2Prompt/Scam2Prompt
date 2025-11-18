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
	"strconv"
	"strings"
)

// Token types
const (
	ILLEGAL = "ILLEGAL"
	EOF     = "EOF"
	INT     = "INT"
	PLUS    = "+"
	MINUS   = "-"
)

// Token represents a lexical token.
type Token struct {
	Type    string
	Literal string
}

// Lexer performs lexical analysis.
type Lexer struct {
	input        string
	position     int
	readPosition int
	ch           byte
}

// NewLexer initializes a new lexer.
func NewLexer(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar() // Initialize by reading the first character
	return l
}

// readChar advances the position in the input and sets the current character.
func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0 // EOF
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition++
}

// nextToken analyzes and returns the next token in the input.
func (l *Lexer) nextToken() Token {
	var tok Token

	switch l.ch {
	case '+':
		tok = Token{Type: PLUS, Literal: string(l.ch)}
	case '-':
		tok = Token{Type: MINUS, Literal: string(l.ch)}
	case 0: // EOF
		tok = Token{Type: EOF, Literal: ""}
	default:
		if isDigit(l.ch) {
			tok.Literal = l.readNumber()
			tok.Type = INT
		} else {
			tok = Token{Type: ILLEGAL, Literal: string(l.ch)}
		}
	}
	l.readChar()
	return tok
}

// readNumber reads a sequence of digits as a number token.
func (l *Lexer) readNumber() string {
	position := l.position
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.input[position:l.position]
}

// isDigit checks if a character is a digit.
func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

// Parser parses tokens into an abstract syntax tree (AST).
type Parser struct {
	lexer  *Lexer
	curTok Token
	peekTok Token
}

// NewParser initializes a new parser.
func NewParser(lexer *Lexer) *Parser {
	p := &Parser{lexer: lexer}
	// Read two tokens to initialize curTok and peekTok
	p.nextToken()
	p.nextToken()
	return p
}

// nextToken advances the current and peek tokens.
func (p *Parser) nextToken() {
	p.curTok = p.peekTok
	p.peekTok = p.lexer.nextToken()
}

// Expression represents an AST node for arithmetic expressions.
type Expression interface{}

// IntegerLiteral represents an integer value in the AST.
type IntegerLiteral struct {
	Value int
}

// PrefixExpression represents a prefix expression like '-5'.
type PrefixExpression struct {
	Operator string
	Right    Expression
}

// InfixExpression represents an infix expression like '5 + 5'.
type InfixExpression struct {
	Left     Expression
	Operator string
	Right    Expression
}

// ParseExpression parses an expression based on its precedence.
func (p *Parser) ParseExpression() Expression {
	left := &IntegerLiteral{Value: p.parseInteger()}
	for p.peekTok.Type == PLUS || p.peekTok.Type == MINUS {
		p.nextToken() // Advance to the operator
		left = &InfixExpression{
			Left:     left,
			Operator: p.curTok.Literal,
			Right:    &IntegerLiteral{Value: p.parseInteger()},
		}
	}
	return left
}

// parseInteger parses an integer token into its value.
func (p *Parser) parseInteger() int {
	val, err := strconv.Atoi(p.curTok.Literal)
	if err != nil {
		panic(fmt.Sprintf("could not parse %q as integer", p.curTok.Literal))
	}
	p.nextToken()
	return val
}

// Evaluator evaluates an AST representation of an expression.
func Evaluate(node Expression) int {
	switch n := node.(type) {
	case *IntegerLiteral:
		return n.Value
	case *InfixExpression:
		left := Evaluate(n.Left)
		right := Evaluate(n.Right)
		switch n.Operator {
		case "+":
			return left + right
		case "-":
			return left - right
		default:
			panic(fmt.Sprintf("unknown operator %q", n.Operator))
		}
	default:
		panic(fmt.Sprintf("unknown node type %T", node))
	}
}

func main() {
	// Example usage
	input := "5 + 10 - 3"
	lexer := NewLexer(input)
	parser := NewParser(lexer)

	expression := parser.ParseExpression()
	result := Evaluate(expression)

	fmt.Printf("Input: %s\nResult: %d\n", input, result)
}
```
