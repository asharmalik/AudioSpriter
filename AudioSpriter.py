__author__ = 'Ashar Malik'

from pydub import AudioSegment
import os, math

def get_sound_files():
    from os import walk

    f = []

    for (dirpath, dirnames, filenames) in walk(os.getcwd()+"\\sounds"):
        f.extend(filenames)
        break

    return f

#Concatenate all .ogg files in the sounds folder into two spritesheets: mp3 and ogg
#create_sound_sprite('ogg', True, ['ogg', 'mp3'])
def create_sound_sprite(filetype='ogg', gen_code=False, pref_output=None):
    output_name = "spritesheet"
    files = get_sound_files()
    current_dir = os.getcwd()+"\\sounds\\"

    if pref_output is None:
        pref_output = [filetype]

    output_names = []

    for type in pref_output:
        output_names.append(output_name+"."+type)


    sounds = []
    code = "var sound = new Howl({\n\turls: "+output_names.__str__()+",\n\tsprite: {\n"

    current_time = 0
    padding = AudioSegment.from_wav(os.getcwd()+'\\padding.wav')

    for file in files:
        if str(file).__contains__('.'+filetype): #filter to only the filetype requested
            file_name = file.split("\\").pop().split(".")[0]

            sounds.append(AudioSegment.from_ogg(current_dir+file))
            sounds.append(padding)
            duration_ms = math.ceil(sounds[-2].duration_seconds*1000)

            code+="\t\t"+file_name+": ["+str(math.floor(current_time)).split(".")[0]+", "+str(duration_ms).split(".")[0]+"]"
            code+= ("," if files.index(file)<files.__len__()-1 else "") + "\n"

            current_time+=duration_ms+padding.duration_seconds*1000

    code+="\t}\n});"

    if sounds.__len__() < 1:
        return


    spritesheet = sounds.pop(0)

    for sound in sounds:
        spritesheet = spritesheet + sound

    export_dir = "bin\\"

    for files in output_names:
        spritesheet.export(export_dir+files)
        print("Generated "+export_dir+files)

    if gen_code:
        file = open(export_dir+"sound.js", "w")
        file.write(code)
        file.close()
        print("Generated "+export_dir+"sound.js")
