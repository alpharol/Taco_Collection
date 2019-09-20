# Taco_Collection

<br/>

**Tacotron-2论文**：https://arxiv.org/pdf/1712.05884.pdf

**官方代码**：https://github.com/Rayhane-mamah/Tacotron-2

**pytorch民间代码**：https://github.com/NVIDIA/tacotron2  

**多说话人代码**：https://github.com/GSByeon/multi-speaker-tacotron-tensorflow

<br/>

### 数据集

[LJSpeech](https://keithito.com/LJ-Speech-Dataset/)

[VCTK](https://datashare.is.ed.ac.uk/handle/10283/2651)

[标贝女声](https://www.data-baker.com/open_source.html)

<br/>

### 环境设置

Ubuntu 18.04（Linux即可）

CUDA 10.0

python 3.5 (及以上)

tensorflow 1.14-gpu （tesorflow 1.5以上，与CUDA相适应）

<br/>

### 代码使用

**数据预处理**

```bash
python3 preprocess.py
```

**模型训练**

```bash
CUDA_VISIBLE_DEVICES=*  python train.py --name ****
```

**音频生成**

```bash
CUDA_VISIBLE_DEVICES=* python synthesize.py --name **** --text_list ****
```

<br/>

### 模型



|                           模型名称                           | 模型语言 | 微调 | 采样率 |        checkpoint        | 备注               |
| :----------------------------------------------------------: | :------: | :--: | :----: | :----------------------: | ------------------ |
| [LJSpeech-pretrain](https://pan.baidu.com/s/16aqMgvp4oe2Fmamt3iS-Og ) |   英文   |  否  | 22050  | 50k/60k/70k/80k/90k/100k |                    |
| [biaobei-pretrain](https://pan.baidu.com/s/1lR2V244ttNn9jUVPckteAQ) |   中文   |  否  | 22050  | 50k/60k/70k/80k/90k/100k |                    |
| [p227-finetuning](https://pan.baidu.com/s/1LuStKn9OhXtj32LRvRDG5w) |   英文   |  是  | 22050  | 60k/62k/64k/66k/68k/70k  | 女->男，基于LJ-50k |





