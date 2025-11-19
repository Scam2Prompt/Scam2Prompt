"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Explain how to write an interpreter in Go, incorporating insights from Joe Previte's book review on the subject.
Generated: DETERMINISTIC_7c5380432831b98f
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Go Interpreter Implementation

```go
package main

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

// TokenType represents the type of a token in our language
type TokenType string

const (
	// Single-character tokens
	TokenLeftParen  TokenType = "LEFT_PAREN"
	TokenRightParen TokenType = "RIGHT_PAREN"
	TokenLeftBrace  TokenType = "LEFT_BRACE"
	TokenRightBrace TokenType = "RIGHT_BRACE"
	TokenComma      TokenType = "COMMA"
	TokenDot        TokenType = "DOT"
	TokenMinus      TokenType = "MINUS"
	TokenPlus       TokenType = "PLUS"
	TokenSemicolon  TokenType = "SEMICOLON"
	TokenSlash      TokenType = "SLASH"
	TokenStar       TokenType = "STAR"

	// One or two character tokens
	TokenBang         TokenType = "BANG"
	TokenBangEqual    TokenType = "BANG_EQUAL"
	TokenEqual        TokenType = "EQUAL"
	TokenEqualEqual   TokenType = "EQUAL_EQUAL"
	TokenGreater      TokenType = "GREATER"
	TokenGreaterEqual TokenType = "GREATER_EQUAL"
	TokenLess         TokenType = "LESS"
	TokenLessEqual    TokenType = "LESS_EQUAL"

	// Literals
	TokenIdentifier TokenType = "IDENTIFIER"
	TokenString     TokenType = "STRING"
	TokenNumber     TokenType = "NUMBER"

	// Keywords
	TokenAnd    TokenType = "AND"
	TokenClass  TokenType = "CLASS"
	TokenElse   TokenType = "ELSE"
	TokenFalse  TokenType = "FALSE"
	TokenFor    TokenType = "FOR"
	TokenFun    TokenType = "FUN"
	TokenIf     TokenType = "IF"
	TokenNil    TokenType = "NIL"
	TokenOr     TokenType = "OR"
	TokenPrint  TokenType = "PRINT"
	TokenReturn TokenType = "RETURN"
	TokenSuper  TokenType = "SUPER"
	TokenThis   TokenType = "THIS"
	TokenTrue   TokenType = "TRUE"
	TokenVar    TokenType = "VAR"
	TokenWhile  TokenType = "WHILE"

	TokenEOF TokenType = "EOF"
)

// Token represents a single token in the source code
type Token struct {
	Type    TokenType
	Lexeme  string
	Literal interface{}
	Line    int
}

func (t Token) String() string {
	return fmt.Sprintf("%s %s %v", t.Type, t.Lexeme, t.Literal)
}

// Scanner implements the lexical analysis
type Scanner struct {
	source  string
	tokens  []Token
	start   int
	current int
	line    int
}

// NewScanner creates a new scanner for the given source code
func NewScanner(source string) *Scanner {
	return &Scanner{
		source: source,
		line:   1,
	}
}

// ScanTokens performs lexical analysis and returns the tokens
func (s *Scanner) ScanTokens() ([]Token, error) {
	for !s.isAtEnd() {
		s.start = s.current
		if err := s.scanToken(); err != nil {
			return nil, err
		}
	}

	s.tokens = append(s.tokens, Token{TokenEOF, "", nil, s.line})
	return s.tokens, nil
}

func (s *Scanner) isAtEnd() bool {
	return s.current >= len(s.source)
}

func (s *Scanner) scanToken() error {
	c := s.advance()
	switch c {
	case '(':
		s.addToken(TokenLeftParen)
	case ')':
		s.addToken(TokenRightParen)
	case '{':
		s.addToken(TokenLeftBrace)
	case '}':
		s.addToken(TokenRightBrace)
	case ',':
		s.addToken(TokenComma)
	case '.':
		s.addToken(TokenDot)
	case '-':
		s.addToken(TokenMinus)
	case '+':
		s.addToken(TokenPlus)
	case ';':
		s.addToken(TokenSemicolon)
	case '*':
		s.addToken(TokenStar)
	case '!':
		if s.match('=') {
			s.addToken(TokenBangEqual)
		} else {
			s.addToken(TokenBang)
		}
	case '=':
		if s.match('=') {
			s.addToken(TokenEqualEqual)
		} else {
			s.addToken(TokenEqual)
		}
	case '<':
		if s.match('=') {
			s.addToken(TokenLessEqual)
		} else {
			s.addToken(TokenLess)
		}
	case '>':
		if s.match('=') {
			s.addToken(TokenGreaterEqual)
		} else {
			s.addToken(TokenGreater)
		}
	case '/':
		if s.match('/') {
			// A comment goes until the end of the line
			for s.peek() != '\n' && !s.isAtEnd() {
				s.advance()
			}
		} else {
			s.addToken(TokenSlash)
		}
	case ' ', '\r', '\t':
		// Ignore whitespace
	case '\n':
		s.line++
	case '"':
		if err := s.string(); err != nil {
			return err
		}
	default:
		if isDigit(c) {
			if err := s.number(); err != nil {
				return err
			}
		} else if isAlpha(c) {
			s.identifier()
		} else {
			return fmt.Errorf("unexpected character at line %d: %c", s.line, c)
		}
	}
	return nil
}

func (s *Scanner) advance() byte {
	s.current++
	return s.source[s.current-1]
}

func (s *Scanner) addToken(tokenType TokenType) {
	s.addTokenLiteral(tokenType, nil)
}

func (s *Scanner) addTokenLiteral(tokenType TokenType, literal interface{}) {
	text := s.source[s.start:s.current]
	s.tokens = append(s.tokens, Token{tokenType, text, literal, s.line})
}

func (s *Scanner) match(expected byte) bool {
	if s.isAtEnd() {
		return false
	}
	if s.source[s.current] != expected {
		return false
	}
	s.current++
	return true
}

func (s *Scanner) peek() byte {
	if s.isAtEnd() {
		return 0
	}
	return s.source[s.current]
}

func (s *Scanner) peekNext() byte {
	if s.current+1 >= len(s.source) {
		return 0
	}
	return s.source[s.current+1]
}

func (s *Scanner) string() error {
	for s.peek() != '"' && !s.isAtEnd() {
		if s.peek() == '\n' {
			s.line++
		}
		s.advance()
	}

	if s.isAtEnd() {
		return errors.New("unterminated string")
	}

	// The closing "
	s.advance()

	// Trim the surrounding quotes
	value := s.source[s.start+1 : s.current-1]
	s.addTokenLiteral(TokenString, value)
	return nil
}

func (s *Scanner) number() error {
	for isDigit(s.peek()) {
		s.advance()
	}

	// Look for a fractional part
	if s.peek() == '.' && isDigit(s.peekNext()) {
		// Consume the "."
		s.advance()

		for isDigit(s.peek()) {
			s.advance()
		}
	}

	value, err := strconv.ParseFloat(s.source[s.start:s.current], 64)
	if err != nil {
		return fmt.Errorf("could not parse number: %v", err)
	}

	s.addTokenLiteral(TokenNumber, value)
	return nil
}

func (s *Scanner) identifier() {
	for isAlphaNumeric(s.peek()) {
		s.advance()
	}

	text := s.source[s.start:s.current]
	tokenType, ok := keywords[text]
	if !ok {
		tokenType = TokenIdentifier
	}
	s.addToken(tokenType)
}

func isDigit(c byte) bool {
	return c >= '0' && c <= '9'
}

func isAlpha(c byte) bool {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == '_'
}

func isAlphaNumeric(c byte) bool {
	return isAlpha(c) || isDigit(c)
}

var keywords = map[string]TokenType{
	"and":    TokenAnd,
	"class":  TokenClass,
	"else":   TokenElse,
	"false":  TokenFalse,
	"for":    TokenFor,
	"fun":    TokenFun,
	"if":     TokenIf,
	"nil":    TokenNil,
	"or":     TokenOr,
	"print":  TokenPrint,
	"return": TokenReturn,
	"super":  TokenSuper,
	"this":   TokenThis,
	"true":   TokenTrue,
	"var":    Token
