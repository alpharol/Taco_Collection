'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
import os
import glob
AUTO_DETECT_SYMBOLS=True

train_text_files = glob.glob(os.path.join("../../female_golden_v2","*.corpus"))
if train_text_files and AUTO_DETECT_SYMBOLS:
    _characters = set()
    for file in train_text_files:
        with open(file,"rb") as fin:
            for line in fin:
                line = line.decode().split("|")[1]
                _characters = _characters.union(line)
else:
    _characters = "12345abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ，。！？ #*$%"

print(_characters)

_pad = "_"
_eos = "~"

symbols = [_pad,_eos]+list(_characters)

print("all symbols is {}".format(symbols))
