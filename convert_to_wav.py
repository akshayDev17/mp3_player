from pydub import AudioSegment
import sys

# files                                                                         
src = sys.argv[1]
dst = "./"+src.split(".mp3")[0].split("/")[-1] +".wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
