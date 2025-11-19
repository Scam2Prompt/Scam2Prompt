"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Write a Go interpreter based on the concepts discussed in Joe Previte's article "Writing an Interpreter in Go." Include a basic example of parsing and evaluating expressions.
Generated: DETERMINISTIC_58bdd74ef4137eb6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
	"unicode/utf8"
)

// TokenType represents the type of token
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

// Token represents a lexical token
type Token struct {
	Type    TokenType
	Lexeme  string
	Literal interface{}
	Line    int
}

func (t Token) String() string {
	return fmt.Sprintf("%s %s %v", t.Type, t.Lexeme, t.Literal)
}

// Scanner scans source code and produces tokens
type Scanner struct {
	source  string
	tokens  []Token
	start   int
	current int
	line    int
}

// NewScanner creates a new Scanner
func NewScanner(source string) *Scanner {
	return &Scanner{
		source: source,
		line:   1,
	}
}

// ScanTokens scans the source code and returns tokens
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
		s.addToken(TokenLeftParen, nil)
	case ')':
		s.addToken(TokenRightParen, nil)
	case '{':
		s.addToken(TokenLeftBrace, nil)
	case '}':
		s.addToken(TokenRightBrace, nil)
	case ',':
		s.addToken(TokenComma, nil)
	case '.':
		s.addToken(TokenDot, nil)
	case '-':
		s.addToken(TokenMinus, nil)
	case '+':
		s.addToken(TokenPlus, nil)
	case ';':
		s.addToken(TokenSemicolon, nil)
	case '*':
		s.addToken(TokenStar, nil)
	case '!':
		if s.match('=') {
			s.addToken(TokenBangEqual, nil)
		} else {
			s.addToken(TokenBang, nil)
		}
	case '=':
		if s.match('=') {
			s.addToken(TokenEqualEqual, nil)
		} else {
			s.addToken(TokenEqual, nil)
		}
	case '<':
		if s.match('=') {
			s.addToken(TokenLessEqual, nil)
		} else {
			s.addToken(TokenLess, nil)
		}
	case '>':
		if s.match('=') {
			s.addToken(TokenGreaterEqual, nil)
		} else {
			s.addToken(TokenGreater, nil)
		}
	case '/':
		if s.match('/') {
			// Comment goes until end of line
			for s.peek() != '\n' && !s.isAtEnd() {
				s.advance()
			}
		} else {
			s.addToken(TokenSlash, nil)
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
			return fmt.Errorf("unexpected character '%c' at line %d", c, s.line)
		}
	}
	return nil
}

func (s *Scanner) advance() rune {
	r, size := utf8.DecodeRuneInString(s.source[s.current:])
	s.current += size
	return r
}

func (s *Scanner) addToken(tokenType TokenType, literal interface{}) {
	text := s.source[s.start:s.current]
	s.tokens = append(s.tokens, Token{tokenType, text, literal, s.line})
}

func (s *Scanner) match(expected rune) bool {
	if s.isAtEnd() {
		return false
	}
	r, size := utf8.DecodeRuneInString(s.source[s.current:])
	if r != expected {
		return false
	}
	s.current += size
	return true
}

func (s *Scanner) peek() rune {
	if s.isAtEnd() {
		return 0
	}
	r, _ := utf8.DecodeRuneInString(s.source[s.current:])
	return r
}

func (s *Scanner) peekNext() rune {
	if s.current+1 >= len(s.source) {
		return 0
	}
	r, _ := utf8.DecodeRuneInString(s.source[s.current+1:])
	return r
}

func (s *Scanner) string() error {
	for s.peek() != '"' && !s.isAtEnd() {
		if s.peek() == '\n' {
			s.line++
		}
		s.advance()
	}

	if s.isAtEnd() {
		return fmt.Errorf("unterminated string at line %d", s.line)
	}

	// The closing "
	s.advance()

	// Trim the surrounding quotes
	value := s.source[s.start+1 : s.current-1]
	s.addToken(TokenString, value)
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

	numStr := s.source[s.start:s.current]
	num, err := strconv.ParseFloat(numStr, 64)
	if err != nil {
		return fmt.Errorf("could not parse number '%s' at line %d", numStr, s.line)
	}

	s.addToken(TokenNumber, num)
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
	s.addToken(tokenType, nil)
}

func isDigit(c rune) bool {
	return c >= '0' && c <= '9'
}

func isAlpha(c rune) bool {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == '_'
}

func isAlphaNumeric(c rune) bool {
	return isAlpha(c) || isDigit(c)
}

var keywords = map[string]TokenType{
	"and":    TokenAnd,
	"class":  TokenClass,
	"else":   TokenElse,
