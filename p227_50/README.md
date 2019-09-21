# README

使用LJSpeech 50k的checkpoint作为原始模型，性别为女；

使用VCTK中的p227中的50句语料作为训练集，性别为男；

这次实验的目的主要是想看一下50句用于finetuning是否可行，实验结果表明：50句完全可以进行微调训练，并且实验效果还不错。

继续训练了20k步。保存的checkepoint有58k/60k/64k/68k/70k。60k的checkpoint效果很好。
