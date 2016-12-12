# MUS158A Final Project - Physical Sequencer

To run:

 - upload serial_send to board
 - open UDPReceive.maxpat (replace with final patch here)
 - run "python sequencer_send.py" (serial data gets sent to python, which gets bundled and sent as UDP packets to MAX)
 - view the UDP packets being updated as the board sends new data to the patch
