# Translation_Entropy
## requirements
[fast_BPE](https://github.com/glample/fastBPE): get vocab of paralell corpus

[fast_align](https://github.com/clab/fast_align): library of unsupervised alignment

## Usage
`bash main.sh corpus_a corpus_b`
- corpus_a : sentences of language a
- corpus_b : sentences of language b
## Example

`bash main.sh corpus_en corpus_ro`

(```)
the 5.698906254414691；
, 1.444006961962339；
. 0.09609516628672199；
of 3.2255480079422636；
to 3.5215574728482197；
and 1.0304466601300641；
in 1.7478318554051528；
a 2.4863726398605657；
that 2.176085465470134；
is 1.9418089845412654；
(```)
### 统计文本中某字符串出现次数
`awk -v RS="@#$j" '{print gsub(/targetStr/,"&")}' filename`
