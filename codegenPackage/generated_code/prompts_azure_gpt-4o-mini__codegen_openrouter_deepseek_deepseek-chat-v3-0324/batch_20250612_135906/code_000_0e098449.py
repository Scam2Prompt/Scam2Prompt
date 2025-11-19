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
; Atari ST PONG Cracktro Demo
; Inspired by Overlanders' PONG Cracktro
; Assembled with Devpac 2

	opt	d+
	opt	o+

	section	text

; Initialize
start:
	move.l	4(sp),a5		; Get basepage
	move.l	$c(a5),d0		; Text segment size
	add.l	$14(a5),d0		; Data segment size
	add.l	$1c(a5),d0		; BSS segment size
	add.l	#$100,d0		; Basepage size
	move.l	d0,-(sp)
	move.l	a5,-(sp)
	clr.w	-(sp)
	move.w	#$4a,-(sp)
	trap	#1			; Mshrink()
	lea	12(sp),sp

	clr.l	-(sp)
	move.w	#$20,-(sp)
	trap	#1			; Super()
	addq.l	#6,sp
	move.l	d0,old_stack

; Save old screen address
	move.w	#2,-(sp)
	trap	#14
	addq.l	#2,sp
	move.l	d0,old_screen

; Set low resolution
	clr.w	-(sp)
	move.l	#-1,-(sp)
	move.l	#-1,-(sp)
	move.w	#5,-(sp)
	trap	#14
	lea	12(sp),sp

; Set palette to black
	lea	$ffff8240.w,a0
	moveq	#15,d0
.clr_pal:
	clr.w	(a0)+
	dbra	d0,.clr_pal

; Main demo loop
main_loop:
	bsr	vsync
	bsr	clear_screen
	bsr	draw_pong
	bsr	scroll_text
	bsr	check_key
	tst.b	exit_flag
	beq.s	main_loop

; Restore system
exit:
	move.l	old_screen,d0
	move.w	#-1,-(sp)
	move.l	d0,-(sp)
	move.l	d0,-(sp)
	move.w	#5,-(sp)
	trap	#14
	lea	12(sp),sp

	move.l	old_stack,-(sp)
	move.w	#$20,-(sp)
	trap	#1
	addq.l	#6,sp

	clr.w	-(sp)
	trap	#1

; Wait for vertical sync
vsync:
	move.w	#37,-(sp)
	trap	#14
	addq.l	#2,sp
	rts

; Clear screen
clear_screen:
	move.l	$44e.w,a0
	move.w	#32000/4-1,d0
.clr:
	clr.l	(a0)+
	dbra	d0,.clr
	rts

; Draw PONG game elements
draw_pong:
	move.l	$44e.w,a0
	lea	160(a0),a0		; Start a bit lower

	; Draw paddles
	moveq	#15,d0
	moveq	#0,d1
.draw_left:
	move.w	#$ffff,(a0)
	add.l	#160,a0
	dbra	d0,.draw_left

	move.l	$44e.w,a0
	lea	160+152(a0),a0		; Right side
	moveq	#15,d0
.draw_right:
	move.w	#$ffff,(a0)
	add.l	#160,a0
	dbra	d0,.draw_right

	; Draw ball
	move.l	$44e.w,a0
	add.l	#160*50+76,a0		; Middle of screen
	move.w	#$3c0,(a0)
	move.w	#$3c0,8(a0)
	rts

; Scroll text
scroll_text:
	move.l	$44e.w,a0
	add.l	#160*180,a0		; Bottom of screen
	lea	scroll_pos,a1
	move.l	(a1),d0
	lea	scroll_text_data,a2
	add.l	d0,a2
	moveq	#0,d1
	move.b	(a2),d1
	bne.s	.no_wrap
	clr.l	d0
	lea	scroll_text_data,a2
.no_wrap:
	addq.l	#1,d0
	move.l	d0,(a1)

	; Draw character
	lsl.w	#3,d1			; *8 for font data
	lea	font_data,a2
	add.w	d1,a2
	moveq	#7,d0
.draw_char:
	move.b	(a2)+,d1
	move.b	d1,(a0)
	add.l	#160,a0
	dbra	d0,.draw_char
	rts

; Check for keypress
check_key:
	move.w	#$ff,-(sp)
	move.w	#6,-(sp)
	trap	#1
	addq.l	#4,sp
	tst.l	d0
	beq.s	.no_key
	move.b	#1,exit_flag
.no_key:
	rts

	section	data

scroll_text_data:
	dc.b	"GREETINGS FROM THE OVERLANDERS! THIS IS A SIMPLE PONG CRACKTRO DEMO FOR THE ATARI ST. ",0

font_data:
	incbin	"font8x8.bin"		; 8x8 font data

	section	bss

old_stack:	ds.l	1
old_screen:	ds.l	1
scroll_pos:	ds.l	1
exit_flag:	ds.b	1

	even
```
