# NSEC 2018 : Life on Mars?

**Category:** forensic
**Points:** 3
**Solves:**
**Description:**

Can you decrypt the message on that picture?

![challenge](https://github.com/ctfs/write-ups-2018/blob/master/nsec-2018/forensic/Life-on-Mars%3F-3/message.png?raw=true)

## Write-up

For this challenge, you had to download the font displayed in the image and decrypt the message. Here is a table for the translation

![decrypt](https://github.com/ctfs/write-ups-2018/blob/master/nsec-2018/forensic/Life-on-Mars%3F-3/decrypt.png?raw=true)

And here is the message:

```
tivvgrmt hglk gsv urihh szou lu
gsv uozt rh gsv mfnyvi gdl
nfmwivw zmw hvevm ulooldvw yb
gsv gdvougs ovggvi lu gsv
zokszyvg. hglk mvcg rh gsv
mfnyvi 3 zmw gsvm gsv hrcgs
ovggvi lu gsv zlkszyvg ulooldvw
yb gsv mrmvgvvmgs ovggvi hglk
zoo oldvixzhv
```

You can decode it using an `atbash` [decrypter](http://crypto.interactive-maths.com/atbash-cipher.html) to get the message that lets you create the flag:

```
greeting stop the firss half of
the flag is the number two
mundred and seven followed by
the twelfth letter of the
alphabet. stop next is the
number 3 and then the sixth
letter of the aophabet followed
by the nineteenth letter stop
all lowercase
```

which gives the flag `207l3fs`

## Other write-ups and resources

- [atbash decipher](http://crypto.interactive-maths.com/atbash-cipher.html)
- [The challenge's font](http://www.1001fonts.com/bit-blocks-ttf-brk-font.html)

