from mingus.midi import fluidsynth   

from midiutil import MIDIFile

#Input is string in the form C#-4, Db-4, or F-3. If your implementation doesn't use the hyphen, 
#just replace the line :
#    letter = midstr.split('-')[0].upper()
#with:
#    letter = midstr[:-1]
def MidiStringToInt(midstr):
    Notes = [["C"],["C#","Db"],["D"],["D#","Eb"],["E"],["F"],["F#","Gb"],["G"],["G#","Ab"],["A"],["A#","Bb"],["B"]]
    answer = 0
    i = 0
    #Note
    #letter = midstr.split('-')[0].upper()
    letter = midstr[:-1]
    for note in Notes:
        for form in note:
            if letter.upper() == form:
                answer = i
                break;
        i += 1
    #Octave
    answer += (int(midstr[-1]))*12 + 12
    return answer

def main():
    #fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2',"coreaudio")
    #fluidsynth.play_Note(64,0,100)
    degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
    degrees = [60,60,67,67,69,69,67]
    degrees = [48,48,60,60,67,67,69,69,67]
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1    # In beats
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    degrees = []
    chord_list = ["C4","C4","G4","G4","A4","A4","G4"] #Just need to supply a chord list
    for chord in chord_list:
        degrees.append(MidiStringToInt(chord))
    print(degrees)
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                        # automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(degrees):
        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

    with open("major-scale.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

if __name__ == "__main__":
    main()
