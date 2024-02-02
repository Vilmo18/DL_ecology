import librosa
import librosa.display
import numpy as np
import soundfile as sf

def slice_audio_per_seconde(input_path, begin_sec, end_sec, output_path):
    y, sr = librosa.load(input_path, sr=None)
    beg_sample = int(begin_sec )
    end_sample = int(end_sec )
    audio_slice = y[beg_sample:end_sample]
    sf.write(output_path, audio_slice, sr)
'''
def slice_audio_per_frequency(input_path, begin_sec, end_sec, output_path):
    y, sr = librosa.load(chemin_audio, sr=None)
    debut_echantillon = librosa.time_to_samples(1 / debut_freq, sr=sr)
    fin_echantillon = librosa.time_to_samples(1 / fin_freq, sr=sr)
    audio_decoupe = y[debut_echantillon:fin_echantillon]
    librosa.output.write_wav(chemin_sortie, audio_decoupe, sr)
'''

#decouper_audio_par_secondes(chemin_audio, debut_sec, fin_sec, chemin_sortie_sec)
#decouper_audio_par_frequence(chemin_audio, debut_freq, fin_freq, chemin_sortie_freq)

def main(input_path,interval,output):
    for i,inter in enumerate(interval):
        slice_audio_per_seconde(input_path,inter[0],inter[1],output+str(i)+'.wav')
y,sr=librosa.load('sound.wav')

inter=[[0*sr, (2) * sr] for i in range(4) ]

main('sound.wav',inter,'test')