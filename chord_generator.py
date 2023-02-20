import random
import time
import json
import re


'''
root on e string
cmaj7
c7
cm7
cm7b5
C°7 (aka cdim7)

root on a string
emaj7
e7 - 2 voicings
em7 - 2 voicings
em7b5
e°7/edim7

root on d string
cmaj7
c7
cm7
cm7b5
C°7/cdim7
'''



# TODO class

class Chords:
    
    def __init__(self, chord_dictionary) -> None:
        self.chord_dictionary = chord_dictionary
        self.guitar_tuning = ["E", "A", "D", "G", "B", "e"]
    
    def _get_key(self,chord_name):
        pattern = r'([A-G])(#|##|b|bb)?'
        key = (re.search(pattern, chord_name)).group(0)
        if key not in self.chord_dictionary['keys']:
            raise Exception (f"unsupported key {key}")
        return key
    
    def _get_chord_type(self, chord_name):
        pattern = r'(maj7|maj|min7|min|sus2)' # TODO construct this from self.chord_dictionary.chords
        type = (re.search(pattern, chord_name)).group(0)
        if type == None:
            raise Exception (f"no match for chord type {type}")
        return type
    
    def _get_chord_object(self, type):
        for chord in self.chord_dictionary['chords']:
            if chord['type'] == type:
                return chord
        
        return False
    
    def get_chord_tab(self, chord_name):
        if not self.validate_chord_name(chord_name):
            return False

        # chord = list
        # each item has string, then "|-", then fret, then "-"

        chord = ["e|-0-","B|-2-","G|-1-","D|-2-","A|-0-","E|---"]
        print(*chord, sep='\n')
    
    def get_chord_notes(self, chord_name):
        print(f"\nchord name = {chord_name}")
        key = self._get_key(chord_name)
        type = self._get_chord_type(chord_name)
        # TODO inversions?

        chord = self._get_chord_object(type)

        print(f"intervals = ", end='')
        print(*chord['intervals'])

        keys = self.chord_dictionary['keys']
        intervals = self.chord_dictionary['intervals']
        offset = keys.index(key)

        notes = []
        for tone in chord['intervals']:
            interval = intervals[tone]
            note = keys[(keys.index(key)+(interval)) % len(keys)]
            notes.append(note)
        
        print(f"notes = ", end="")
        print(*notes)
        
    def get_random_chords(self, number, keys, chords, root_strings,inversions):
        print("\nchords:")
        for i in range (number):
            # key = keys[random.randint(0,len(keys)-1)]
            key = random.choice(keys)
            chord = random.choice(chords)
            string = random.choice(root_strings)
            inversion = random.choice(inversions)
            print(f"{key}{chord} root on {string}, {inversion} inversion")

if __name__ == "__main__":
    keys = ["A","Bb","B","C","C#","D","Eb","E","F","F#","G","G#"]
    seventh_chords = ["maj7","7","m7","m7b5","dim7"]
    root_strings = ["E","A"]
    inversions =["1st","2nd", "3rd"]

    with open('C:\projects\music-theory\chord_dictionary.json', 'r') as file:
        contents = file.read()
        chord_dictionary = json.loads(contents)
    
    chords = Chords(chord_dictionary)
    chords.get_chord_notes('Amaj7')
    chords.get_chord_notes('Dmaj7')
    chords.get_chord_notes('Emaj7')
    # chords.get_random_chords(10,keys,seventh_chords,root_strings,inversions)

    # normal_chords = ["","m"]
    # chords.get_random_chords(10,keys,normal_chords,root_strings,inversions)
