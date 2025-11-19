"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: How can I use YACC to parse arithmetic expressions and handle syntax errors, similar to the implementation shown in the CD Lab?
Generated: DETERMINISTIC_7fd0c370b6080f02
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
%{
#include <stdio.h>
#include <stdlib.h>

/* Function to handle syntax errors */
void yyerror(const char *s);
int yylex(void);
%}

/* Token declarations */
%token NUMBER
%token PLUS MINUS MULT DIV LPAREN RPAREN

%%
/* Define grammar rules */
expr: expr PLUS term      { $$ = $1 + $3; }
     | expr MINUS term     { $$ = $1 - $3; }
     | term                 { $$ = $1; }
     ;

term: term MULT factor     { $$ = $1 * $3; }
     | term DIV factor      { 
           if ($3 == 0) {
               yyerror("Division by zero");
               YYABORT;
           }
           $$ = $1 / $3; 
       }
     | factor                { $$ = $1; }
     ;

factor: NUMBER             { $$ = $1; }
      | LPAREN expr RPAREN  { $$ = $2; }
      ;

%%

// Error handling function
void yyerror(const char *s) {
    fprintf(stderr, "Syntax error: %s\n", s);
}

// Main function
int main(void) {
    printf("Enter an arithmetic expression:\n");
    return yyparse();
}

// Lexer implementation
#include "lex.yy.c"
```

```lex
%{
#include "y.tab.h"
%}

%%

// Define regular expressions for tokens
[0-9]+      { yylval = atoi(yytext); return NUMBER; }
"+"        { return PLUS; }
"-"        { return MINUS; }
"*"        { return MULT; }
"/"        { return DIV; }
"("        { return LPAREN; }
")"        { return RPAREN; }
[ \t\n]    { /* skip whitespace */ }
.          { yyerror("Unexpected character"); }
%%

// Main function for the lexer
int yywrap() {
    return 1;
}
```

### Instructions to Compile
1. Save the parser code in a file named `parser.y`.
2. Save the lexer code in a file named `lexer.l`.
3. Run the following commands in the terminal:
   ```bash
   yacc -d parser.y
   lex lexer.l
   gcc y.tab.c lex.yy.c -o parser -lm
   ```
4. Execute the program with `./parser` and enter arithmetic expressions to parse.
