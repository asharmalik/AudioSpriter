__author__ = 'Ashar Malik'

from pydub import AudioSegment
import os

def get_sound_files():
    from os import walk

    f = []

    for (dirpath, dirnames, filenames) in walk(os.getcwd()+"\\sounds"):
        f.extend(filenames)
        break

    return f

def create_sound_sprite(filetype='ogg', gen_code=False):
    files = get_sound_files()
    current_dir = os.getcwd()+"\\sounds\\"
    export_name = "spritesheet"+"."+filetype

    sounds = []
    code = "var sound = new Howl({\n\turls: ['"+export_name+"'],\n\tsprite: {\n"
    current_time = 0

    for file in files:
        if str(file).__contains__('.'+filetype): #filter to only the filetype requested
            file_name = file.split("\\").pop().split(".")[0]

            sounds.append(AudioSegment.from_ogg(current_dir+file))
            duration_ms = sounds[sounds.__len__()-1].duration_seconds*1000

            code+="\t\t"+file_name+": ["+str(current_time)+", "+str(duration_ms)+"]"
            code+= ("," if files.index(file)<files.__len__()-1 else "") + "\n"
            current_time+=duration_ms

    code+="\t}\n});"

    if sounds.__len__() < 1:
        return


    spritesheet = sounds.pop(0)

    for sound in sounds:
        spritesheet = spritesheet + sound

    spritesheet.export("spritesheet\\"+export_name)

    if gen_code:
        file = open("spritesheet\\sound.js", "w")
        file.write(code)
        file.close()
        print("Generated spritesheet\\sound.js")

    print("Generated "+"spritesheet\\"+export_name)



create_sound_sprite("ogg", True)

#ogg_version = AudioSegment.from_ogg("C:\Users\Ashar Malik\Dropbox\Coding\Python\AudioSpriter\sounds\Boss_apfelsaft.ogg")
