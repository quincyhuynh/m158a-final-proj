# MUS158A Final Project - Physical Sequencer

We used an Arduino, a breadboard with switches and potentiometers, python and MAX to create a physical sequencer.
This library is hosted at https://github.com/quincyhuynh/m158a-final-proj


## Video Link: https://youtu.be/i6g_i1vJj48

## Important files:
- serial_send.ino in /serial_send
- physicalsynth.maxpat
- sequencer_send.py

## To run (you also need the board):
 - upload serial_send to board
 - open physicalsynth.maxpat
 - run "python sequencer_send.py" (serial data gets sent to python, which gets bundled and sent as UDP packets to MAX), python version is 2.7
 - view the UDP packets being updated as the board sends new data to the patch as table values
 - play table values as sequence just like we did in labs (map to scale, map to index for granubuf to play 808s)
 - play around with knobs and switches to get the right sounds
 - a secondary switch is used as a loop pedal to switch between storing the 808 sequence or the scale sequence

## Contributions:

Quincy: I coded the Arduino code to send serial data to Python and parsed the serial data in Python to create OSC bundles to send to Max. I thought it was pretty awesome to see something physical connect to Max and get to play around with it. Max usually tries to emulate the idea of cords, switches and tables in audio and music. For our project we wanted to create that real thing and interface it with Max. It worked out pretty well!

Primus: I developed the maxpatcher which reads arduino input data and converts it into sequenced drum sounds and notes. I also put together the physical circuit of switches and potentiometers which served as the input. When Quincy and I put our parts together it was awesome to be able to drive the digital objects we've been working with all semester with a real, physical input.