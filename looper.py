from pydub import AudioSegment


def bpm_to_ms(bpm):
    # convert bpm to delay in milliseconds
    return 0.25 * 1000 / (float(bpm)/60)

sound = {
    "bpm": 140,
    "total_beats": 16,
    "tracks":
        [
            {"name": "kick", "gain": 1, "file": "wav/big_beat_1.wav", "beat":   [1, 1, 1, 0,  0, 0, 1, 0,  0, 0, 1, 0,  0, 0, 0, 0]},
            {"name": "snare", "gain": 0, "file": "wav/big_beat_3.wav", "beat":  [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 1, 1, 0]},
            {"name": "hi-open", "gain": -10, "file": "wav/acoustic_4_4.wav", "beat":  [1, 0, 1, 1,  0, 0, 1, 0,  1, 0, 0, 0,  0, 0, 0, 0]},
            {"name": "hi-closed", "gain": -10, "file": "wav/acoustic_4_5.wav", "beat":  [0, 0, 0, 0,  1, 0, 0, 0, 0, 0, 0, 0,  1, 0, 0, 0]}
        ]
}

delay = bpm_to_ms(sound.get("bpm"))
length = sound.get("total_beats") * delay

output = AudioSegment.silent(duration=length)

for track in sound.get("tracks", None):
    current_beat = 0
    if track:
        sample = AudioSegment.from_wav(track.get("file", None))
        for beat in track.get("beat", None):
            if beat == 1:
                # print "mix %s at current_beat:%s" % (track.get("name"), current_beat)
                sample = sample + track.get("gain", 0)
                output = output.overlay(sample, position=current_beat)
            current_beat += delay

output = output * 4

# save the result
output.export("output.wav", format="wav")
