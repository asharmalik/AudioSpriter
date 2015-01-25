# AudioSpriter
A python module to create audio/sound spritesheets. This module supports outputting sprite sheet code for howler.js.

Requires ffmpeg. [Click here to install for Windows](http://www.wikihow.com/Install-FFmpeg-on-Windows)

# Usage
Place separate sounds files into the sound directory.

```
create_sound_sprite(filetype='ogg', gen_code=False)
'''

The function will generate the finished sound file (and optional howler.js code) to the bin directory.
