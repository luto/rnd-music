from subprocess import call
import random

lens = [0,0,0,0,0,0,0,0,0,0];
lens[1] = 1500;
lens[2] = lens[1] / 2;
lens[4] = lens[1] / 4;
lens[8] = lens[1] / 8;

notes = {};
notes['C'] = { 'f': 262, 'n': 0 };
notes['D'] = { 'f': 294, 'n': 1 };
notes['E'] = { 'f': 330, 'n': 2 };
notes['F'] = { 'f': 349, 'n': 3 };
notes['G'] = { 'f': 392, 'n': 4 };
notes['A'] = { 'f': 440, 'n': 5 };
notes['H'] = { 'f': 494, 'n': 6 };
notes['C2'] = { 'f': 512, 'n': 7 };


def beep(l, f):
    call(['/usr/bin/beep', '-l', str(l), '-f', str(f)]);

def smartBeep(l, note):
    beep(lens[l], note['f']);

def nextNote(notes, lastNote):
    while True:
        note = notes[random.choice(notes.keys())]
        if len(notes) == 1:
            return note
        if note != lastNote:# and note['n'] > lastNote['n'] - 2 and note['n'] < lastNote['n'] + 2:
            return note


groups = [
	{
		'len': 4,
		'notes': [ 'C', 'E', 'G' ]
	},
        {
                'len': 4,
                'notes': [ 'C', 'E', 'G' ]
        },
        {
                'len': 4,
                'notes': [ 'F', 'A', 'C' ]
        },
        {
                'len': 1,
                'notes': [ 'G' ]
        },
        {
                'len': 4,
                'notes': [ 'C', 'E', 'G' ]
        },
        {
                'len': 4,
                'notes': [ 'C', 'E', 'G' ]
        },
        {
                'len': 4,
                'notes': [ 'G', 'H', 'D' ]
        },
        {
                'len': 1,
                'notes': [ 'C' ]
        }
];



for grp in groups:
    foo = {}
    for x in grp['notes']:
        foo[x] = notes[x]
    grp['notes'] = foo


lastNote = notes[notes.keys()[0]]

while 1:
    for grp in groups:
        for x in range(grp['len']):
            lastNote = nextNote(grp['notes'], lastNote)
            smartBeep(grp['len'], lastNote)
