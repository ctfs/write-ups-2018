# NSEC 2018 : babyre0-1

**Category:** Reverse Engineering
**Points:** 1
**Solves:**
**Description:**

Find a flag in the file, baby reverse engineering level 0.

## Write-up

For this one, the easiest way to find a flag in a binary is to look for text (strings) inside.

Running 

```
strings -a babyre0| grep -iA 8 flag
```

will show you the flag directly

![challenge](https://github.com/ctfs/write-ups-2018/blob/master/nsec-2018/reverse/babyre0-1/flag.png?raw=true)

## Other write-ups and resources

- [What is strings](https://en.wikipedia.org/wiki/Strings_(Unix))