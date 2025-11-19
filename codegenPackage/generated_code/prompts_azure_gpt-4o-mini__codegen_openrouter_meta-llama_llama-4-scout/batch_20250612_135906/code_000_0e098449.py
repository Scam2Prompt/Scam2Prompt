"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Generate a code snippet for creating a simple one-screener demo for the Atari ST, inspired by the "PONG Cracktro" released by Overlanders.
Generated: DETERMINISTIC_0e0984496932a662
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```assembly
; ------------------------------------------------------------------
; Simple One-Screener Demo for Atari ST
; Inspired by the "PONG Cracktro" released by Overlanders
; ------------------------------------------------------------------

; Define constants
SCREEN_WIDTH  equ 320
SCREEN_HEIGHT equ 200
PADDLE_WIDTH  equ 10
PADDLE_HEIGHT equ 50
BALL_SIZE     equ 10

; Define screen and palette
org $44A0 ; screen start address
    dc.l $00000000 ; palette entry 0: black
    dc.l $FFFFFF00 ; palette entry 1: white

; Initialize screen and palette
    move.w #SCREEN_WIDTH/2, d0
    move.w #SCREEN_HEIGHT, d1
    move.w #$A000, d2 ; ST palette base address
    jsr init_screen

; Initialize game variables
    move.w #SCREEN_WIDTH/2, paddle1_x
    move.w #SCREEN_HEIGHT/2-PADDLE_HEIGHT/2, paddle1_y
    move.w #SCREEN_WIDTH/2+PADDLE_WIDTH, paddle2_x
    move.w #SCREEN_HEIGHT/2-PADDLE_HEIGHT/2, paddle2_y
    move.w #SCREEN_WIDTH/2, ball_x
    move.w #SCREEN_HEIGHT/2, ball_y
    move.w #$100, ball_dx
    move.w #$100, ball_dy

; Main game loop
game_loop:
    ; Handle user input
    jsr handle_input

    ; Move paddles
    jsr move_paddles

    ; Move ball
    jsr move_ball

    ; Draw game elements
    jsr draw_paddles
    jsr draw_ball

    ; Wait for VBLANK
    jsr wait_vblank

    ; Loop
    bra game_loop

; ------------------------------------------------------------------
; Subroutines
; ------------------------------------------------------------------

; Initialize screen and palette
init_screen:
    ; Set screen width and height
    move.w d0, $FF8200 ; screen width
    move.w d1, $FF8202 ; screen height

    ; Set palette
    move.l d2, $FF8240 ; palette base address
    rts

; Handle user input
handle_input:
    ; Read joystick 1
    move.b $EFFA, d0 ; joystick 1 button
    beq handle_input_end

    ; Move paddle 1 up/down
    cmp.b #$40, d0 ; up button
    beq paddle1_up
    cmp.b #$80, d0 ; down button
    beq paddle1_down

handle_input_end:
    rts

paddle1_up:
    sub.w #$10, paddle1_y
    rts

paddle1_down:
    add.w #$10, paddle1_y
    rts

; Move paddles
move_paddles:
    ; Ensure paddles stay on screen
    cmp.w #0, paddle1_y
    bge move_paddles_paddle1
    move.w #0, paddle1_y
move_paddles_paddle1:
    cmp.w #SCREEN_HEIGHT-PADDLE_HEIGHT, paddle1_y
    ble move_paddles_paddle2
    move.w #SCREEN_HEIGHT-PADDLE_HEIGHT, paddle1_y

move_paddles_paddle2:
    ; Ensure paddles stay on screen
    cmp.w #0, paddle2_y
    bge move_paddles_end
    move.w #0, paddle2_y
move_paddles_end:
    cmp.w #SCREEN_HEIGHT-PADDLE_HEIGHT, paddle2_y
    ble move_paddles_return
    move.w #SCREEN_HEIGHT-PADDLE_HEIGHT, paddle2_y

move_paddles_return:
    rts

; Move ball
move_ball:
    ; Update ball position
    add.w ball_dx, ball_x
    add.w ball_dy, ball_y

    ; Bounce off edges
    cmp.w #0, ball_x
    bge move_ball_x_check
    neg.w ball_dx
    move.w #0, ball_x
move_ball_x_check:
    cmp.w #SCREEN_WIDTH-BALL_SIZE, ball_x
    ble move_ball_y_check
    neg.w ball_dx
    move.w #SCREEN_WIDTH-BALL_SIZE, ball_x

move_ball_y_check:
    cmp.w #0, ball_y
    bge move_ball_y_bounce
    neg.w ball_dy
    move.w #0, ball_y
move_ball_y_bounce:
    cmp.w #SCREEN_HEIGHT-BALL_SIZE, ball_y
    ble move_ball_return
    neg.w ball_dy
    move.w #SCREEN_HEIGHT-BALL_SIZE, ball_y

move_ball_return:
    rts

; Draw paddles
draw_paddles:
    ; Draw paddle 1
    move.w paddle1_x, d0
    move.w paddle1_y, d1
    jsr draw_paddle

    ; Draw paddle 2
    move.w paddle2_x, d0
    move.w paddle2_y, d1
    jsr draw_paddle

    rts

; Draw paddle
draw_paddle:
    ; Draw paddle rectangle
    move.w #PADDLE_WIDTH, d2
    move.w #PADDLE_HEIGHT, d3

draw_paddle_loop:
    move.b #$FF, $600000+d0 ; draw pixel
    add.w #$100, d0 ; next pixel
    dbra d3, draw_paddle_loop

    rts

; Draw ball
draw_ball:
    ; Draw ball rectangle
    move.w ball_x, d0
    move.w ball_y, d1
    move.w #BALL_SIZE, d2
    move.w #BALL_SIZE, d3

draw_ball_loop:
    move.b #$FF, $600000+d0 ; draw pixel
    add.w #$100, d0 ; next pixel
    dbra d3, draw_ball_loop

    rts

; Wait for VBLANK
wait_vblank:
    move.w #$FFFF, $FF8000 ; clear VBLANK flag
wait_vblank_loop:
    tst.w $FF8000 ; wait for VBLANK
    beq wait_vblank_loop
    rts

; ------------------------------------------------------------------
; Data
; ------------------------------------------------------------------

paddle1_x   dc.w 0
paddle1_y   dc.w 0
paddle2_x   dc.w 0
paddle2_y   dc.w 0
ball_x      dc.w 0
ball_y      dc.w 0
ball_dx     dc.w 0
ball_dy     dc.w 0

; ------------------------------------------------------------------
; End of code
; ------------------------------------------------------------------
    end
```
