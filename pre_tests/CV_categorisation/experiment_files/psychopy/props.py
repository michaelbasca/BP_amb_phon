# props.py

STIM_ROOT = '/Users/lauragwilliams/Dropbox/CV_categorisation/cut_CVs/'

# need to change this.. to complex?
STIMULI: (
        {'pt': '%s_pt/%s_pt/%s_pt_%s'},
        {'tp': '%s_tp/%s_tp/%s_tp_%s'},
        {'td': '%s_td/%s_td/%s_td_%s'},
        {'dt': '%s_dt/%s_dt/%s_dt_%s'}
        )

# modify this to load all the sounds
def load_sounds(names):
    from psychopy.sound import Sound

    sounds = {}
    for name in names:
        for kind in ('long', 'short'):
            sound_name = '_'.join((name, kind))
            sounds[sound_name] = Sound('../sounds/%s.wav' % sound_name, name=sound_name, autoLog=False)
    return sounds
