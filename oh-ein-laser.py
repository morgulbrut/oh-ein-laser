#!/usr/bin/env python3

# A coworker once told me a story:
# Once he was on auditor gig together
# with an Russian engineer, Vitali. 
# At some point, Vitali got bored, and
# saw a powerful laser. While mumbling 
# "Oh, ein Laser" Vitali walked towards
# said laser and stopped giving even the 
# slightest fuck about that boring 
# audit.

# Let's be Vitali now and then.
# Because lasers.

from string import Template

preamble = '''; oh_ein_Laser.py generated
; lasercut testfile for
; zigerlaser
G00 G17 G40 G21
G90
M3
M106'''


powers = [10, 20, 30, 40, 50, 60, 70]
speeds = [50, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 2000]



'''
draws circles 7mm diameter, 10 cm apart 
'''
def circles(x,y):
    holes = ""
    for p in powers:
        for s in speeds:
            xoffset = powers.index(p)
            yoffset = speeds.index(s)
            holes += "; {}% power, speed {}\n".format(p, s)
            holes += "G0 X{} Y{}\n".format(x+xoffset*10, y+yoffset*10)
            holes += "G2 I3.5 S{} F{}\n\n".format(p/10, s)
    return holes

with open("oh-ein-Laser.gc", 'w') as file:
    t = open('template.gc')
    src = Template(t.read())
    d = {'preamble':preamble, 'holes': circles(40,10)}
    output = src.substitute(d)
    file.write(output+"\n")