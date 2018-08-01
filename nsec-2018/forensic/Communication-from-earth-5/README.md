# NSEC 2018 : Communication from earth

**Category:** forensic
**Points:** 5
**Solves:** 
**Description:**

We received a communication from earth, let's analyse it:

- What is the carrier frequency
- What is the name of the attack
- What is the exact url sent by this attack

## Write-up

For this challenge, you will need to install audacity. 
Here is the spectrogram where you can see the frequency of the carrier (the highest frequency):

![spectro](https://github.com/ctfs/write-ups-2018/tree/master/nsec-2018/forensic/Communication-from-earth-5/spectro.png?raw=true)

You can see it is at around `37000Hz`

It is called a dolphin attack where you have a message you can't listen to but which computer can pick up (like Siri, Alexa or google home). It has now been patched on most of the current phones and computers.


To get the message from the audio we will need to use this nyquist script in order to do AM modulation. (Select the clip then go in `Effect > Nyquist prompt` and copy paste)

```
;version 4
    (setf cf 37000) ; the carrier frequency
    (let ((demod (mult *track* (hzosc cf))))
      (lowpass8 demod 10000))
```

Before:

![spectro](https://github.com/ctfs/write-ups-2018/tree/master/nsec-2018/forensic/Communication-from-earth-5/before.png?raw=true)

After:

![spectro](https://github.com/ctfs/write-ups-2018/tree/master/nsec-2018/forensic/Communication-from-earth-5/after.png?raw=true)

The flag is the url said.



## Other write-ups and resources

- [audacity demodulation](https://forum.audacityteam.org/viewtopic.php?f=39&t=95331)
- [Download audacity](https://www.audacityteam.org/)
- [carrier wave](https://en.wikipedia.org/wiki/Carrier_wave)
- [Nyquist](https://wiki.audacityteam.org/wiki/Nyquist)

