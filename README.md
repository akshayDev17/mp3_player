## Introduction to .wav

1. full form WAVeform audio file format.
2. created by Microsoft and IBM
3. stores data in segments.
   1. audio data
      1. “chunks” using the Resource Interchange File Format (RIFF).
      2. [dissect a RIFF file and extract all WAVE components into .wav files](https://gist.github.com/RavuAlHemio/2e53d3b174c69653ca29) .
   2. track numbers
   3. sample rate
   4. bit rate
4. 



## Convert to .wav

1. ```bash
   pip install pydub
   sudo apt-get install ffmpeg # for ubuntu/debian-linux
   ```




### Reason(s)

1. WAV files are **lossless**, **uncompressed**, **broadcast** CD **quality** music files.  
   1. they indeed are uncompressed(size-hogging),  the *Vince-Staples-Street-Punks.wav*  is of 32 MB in size.
2. WAV files are also the right choice for loops to be processed with Flash for web animations.



# MP3



## Introduction

1. MPEG Audio Layer-3 is the full name for this format.
   1. Moving Picture Expert Group(a video is essentially a moving picture).
2. An MP3 file includes a 
   1. header
      1. includes information about the audio such as  the version of the encoding, the bitrate, and the sample_rate.
      2. A high bitrate and sample rate produces better audio quality, but also a larger file size.
   2. metadata,
   3. compressed audio.  
3. 





## When to use MP3 instead

1. Use MP3 files for web pages, web videos, in fact for **anything on the Internet**. 
2. An MP3 file is a **compressed** music file. 
3. It **loads rapidly** and still  plays with a very good sound quality. 
4. There are several levels of  possible compression but for Internet usage we recommend 128kbps which  is what you download automatically from our server when you order music  from us.
   1. they indeed are,  the *Vince-Staples-Street-Punks.mp3*  is of 7 MB in size, thus almost 1/5th of the corresponding *.wav* size.
5. the MP3 compression algorithm leaves a silent space of 10 ms to 50 ms at the start and end of the file.



# How is the job done?

1. in python, a famous module going by the name [sounddevice](https://github.com/spatialaudio/python-sounddevice) which provides bindings with the [PortAudio](http://www.portaudio.com/) library(written in C++), which in turn relays data to the sound-card.
2. audio programming is the way to go about it.



# Audio programming

1. *coding* sound.
2.  



# Fun Modifications

1. [Delay Based Effects](https://publish.illinois.edu/augmentedlistening/tutorials/music-processing/tutorial-2-delay-based-effects/)





# Questions to Ponder

1. why are .wav files uncompressed and MP3 compressed.
2. how does this compression take place?
3. what are these different options that are available while downloading music: 128 kbps, 324 kbps ..... ?
4. lossless audio? what are lossful ones?
5. what is ASIO?
6. security concerns(when accessing sites you aren't supposed to)
   1. [WAV audio files are now being used to hide malicious code](https://www.zdnet.com/article/wav-audio-files-are-now-being-used-to-hide-malicious-code/)
   2. 
7. 



