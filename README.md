# Table of Contents

1. [Sound drivers](#sounddrivers)
2. [`pa_front.c`](#pa_front)
3. [`patest_wire.c`](#patest_wire)



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



## Sounddevice

1. `query_devices()` is called

   1. Devices may support input, output or both input and output.

   2. arguments

      1. device = `id`, `string `

         ```python
         print(ds(sd.query_devices(device=5), indent=2)) # device with id = 5 to be print
         ```

         kind = `'output'` or `'input'`, **default** device is returned.

         ```python
         print(ds(sd.query_devices(kind='output'), indent=2)) # default device for output
         ```

   3. output

      1. either a dictionary(if argument values are specified) or a list of dictionaries, displaying information on all available input/output devices.
      2. fields of the dictionary:
         1. `name`  "HDA Intel HDMI: 0 (hw:0,3)",
         2. `hostapi`  ID of the host API, [query_hostapis()]() for more.
         3. `max_input_channels` / `max_output_channels`: 8,
         4. `default_low_input_latency` / `default_low_output_latency` default latency values for **interactive performance**.
         5. `default_high_input_latency` / `default_high_output_latency` : default latency values for **robust, non-interactive applications**, for instance playing sound files.
         6. `default_samplerate`: default sampling frequency of the device
      3. 

   4. 

2. `cffi` is used

   1. `FFI` stands for foreign function interface - mechanism by which a program written in one programming language can call routines or make use of services written in another.
      1. inter-language calls.
      2. other names 
         1. language bindings(used by Ada programming language)
         2. JNI / JNA (java native interface/access), this works both ways, i.e. functions written in other languages can be called from inside JAVA code, and code in other languages can call functions written in JAVA.
      3. wrapper libraries, glue codes, 
      4. problems with FFI
         1. complicated data structures in one language may not be possible to implement in the other.
         2. cross-language inheritance due to the object-composition models(how an object is defined in language 1 vs language 2) being different themselves.
      5. 
   2. [cffi docs](https://cffi.readthedocs.io/en/latest/goals.html)
   3. on non-Windows platforms, C libraries typically have a specified C API but not an ABI (e.g. they may document a “struct” as having at least these fields, but maybe more)
      1. ABI  is something like `ctypes` module, i.e. application binary interface.
   4. **no c++ support, only C**

3. 



## `CFFI`

1. **system-installed shared library**
   1. code pre-compiled to be used for all programs.
   2. can be linked to any program at run-time, and underlying code can be used by any number of programs at the same time.
   3. So, this way the size of programs(using shared library) and the memory  footprint can be kept low as a lot of code is kept common in form of a  shared library.
   4. in windows, they go by the name dynamically linked libraries **`.dll`** , linux - shared objects, hence the extension **`.so`**
   5. to observe what libraries a particular program depends on, use `ldd <program/absolute/path>`
      for instance, we know that `ls` is a program, hence writing `ldd /bin/ls` would give us all `.so` files it is dependent on.
   6. since these files are pre-compiled, their content is binary in nature, i.e. you won't be able to read them.
2. 



# Sound Drivers<a name="sounddrivers"></a>

1. **Jack, Pulseaudio, and Alsa** are commonly used sound drivers.
2. CHECK `patest_pink.c` in `test` folder w.r.t. `portaudio` source.
   1. or check `patest_wire.c`, as it directly passes input(sound signals?) to output(hardware?)





## `pa_front.c` <a name="pa_front"></a>

1. `Pa_GetDefaultInputDevice()`
   1. no function arguments, return value = `PaDeviceIndex`, which is type-defined as an **`int`** in `portaudio.h` .
   2. `hostApi` and `result`, 2 int variables are declared.
   3. `PA_LOGAPI_ENTER( "Pa_GetDefaultInputDevice" )` , which basically is a function(defined in `portaudio/src/common/pa_debugprint.h`) that is supposed to take a function name(not as a string, but as a pointer to this entered function itself) and 
      1. `int printf (const char* format, ...);`  is a typical example of a **variadic function** , i.e. a function that will have variable number of arguments, i.e. number of arguments is not fixed, unlike the traditional function.
         1. the typical format of a variadic function is `<return-type> <func_name> (<arguments-expected>, ...)`, where the **`...`** is known as the ellipsis.
         2. as for the `arguments-expected` field, these are the arguments that are expected to be provided whenever this particular function is called.
            in the case of `printf`, a `char *` is passed always, `(printf("%d\n", age);` , and the arguments that follow are usually variables.
         3. A variadic function is typically used when code needs to be flexible w.r.t. amount/data-type of parameters handled.
         4. the macros used in this code section are:
            1. `va_list` : a data-type used to instantiate a linked list, that contains values of all arguments in the order of provision, both fixed and variable.
            2. `va_start` : a HEAD pointer to the fixed arguments.
            3. `va_arg` : a HEAD pointer to the variable arguments.
         5. `vfprintf` : syntax = `int vfprintf(FILE *stream, const char *format, va_list arg);` , and it clearly shows that this function writes all the variable argument values to a particular stream.
            In this case, this stream is **`stderr`** .
         6. `va_end` is called in order to return from the `va_start` call, else the result is undefined, followed by flushing the buffers of `stderr` output stream.
      2. the function `PA_LOGAPI_ENTER` calls `PaUtil_DebugPrint` which is declared in the same way as this `printf` function .
      3. 
   4. 
2. 



## `patest_wire.c`<a name="patest_wire"></a>

1. `WireConfig_s` or `WireConfig_t` 
2. `USE_FLOAT_INPUT` / `USE_FLOAT_OUTPUT` 
   1. if  `USE_FLOAT_INPUT` is to be used, then `INPUT_FORMAT` is defined as `paFloat32`, which is actually an **unsigned long integer** initialized to hexadecimal 1.
      1. `INPUT_SAMPLE` is type-defined to be a float.
   2. if  `USE_FLOAT_INPUT` is **not** used, `INPUT_FORMAT` is defined as `paInt16`, an **unsigned long integer** initialized to hexadecimal 8, and  `INPUT_SAMPLE` is type-defined to be a short integer(16-bit).
   3. the exact same `if` conditions are repeated for `USE_FLOAT_OUTPUT`
3. a variable called `gInOutScaler` of datatype `double` is initialised to 1.
4. `INPUT_DEVICE` and `OUTPUT_DEVICE` are defined as outputs of the functions `Pa_GetDefaultInputDevice()` and `Pa_GetDefaultOutputDevice()`.
5. 



# Auxiliary stuff

1. `_` leading names(underscore leading names)
   1. variable or method is intended for internal use(“Hey, this isn’t really meant to be a part of the public interface of this class. Best to leave it alone.”).
   2. merely an agreed upon convention and does not impose any restrictions on accessing the value of that variable.
2. `typedef` in C means - create a new name that will point to a pre-existing datatype.
3. 



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
7. what is ABI?



