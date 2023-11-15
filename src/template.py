#!/usr/bin/env python3

from pwn import *
import sys
context.log_level = "debug"
context.binary = {bin_name}

{bindings}

if len(sys.argv) < 2:
    debug = True
else:
    debug = False

if debug:
    p = process({proc_args})
    libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
else:
    p = remote("addr", 1337)
    libc = ELF("./libc-2.31.so")

ru = lambda x : p.recvuntil(x)
sn = lambda x : p.send(x)
rl = lambda : p.recvline()
sl = lambda x : p.sendline(x)
rv = lambda x : p.recv(x)
sa = lambda a,b : p.sendafter(a,b)
sla = lambda a,b : p.sendlineafter(a, b)

def debugf(b=0):
    if debug:
        if b:
            gdb.attach(p,"b *$rebase({b})".format(b = hex(b)))
        else:
            gdb.attach(p)
#context.terminal = ['tmux', 'splitw', '-h']

p.interactive()
