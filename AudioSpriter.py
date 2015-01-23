__author__ = 'Ashar Malik'

from pydub import AudioSegment
import os

def get_sound_files():
    from os import walk

    f = []

    for (dirpath, dirnames, filenames) in walk('C:\Users\Ashar Malik\Dropbox\Coding\Python\AudioSpriter\sounds'):
        f.extend(filenames)
        break

    return f

def create_sound_sprite():
    files = get_sound_files()
    current_dir = os.getcwd()+"\\"

    for file in files:
        pass

ogg_version = AudioSegment.from_ogg("C:\Users\Ashar Malik\Dropbox\Coding\Python\AudioSpriter\sounds\Boss_apfelsaft.ogg")
