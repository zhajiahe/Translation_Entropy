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

trans_entropy_en:  
```
the 5.698906254414691
, 1.444006961962339
. 0.09609516628672199
of 3.2255480079422636
to 3.5215574728482197
and 1.0304466601300641
in 1.7478318554051528
a 2.4863726398605657
that 2.176085465470134
is 1.9418089845412654
```
trans_entropy_ro:  
```
, 1.8205278972537513
de 4.262196692574352
. 0.06469172070405921
in 2.4642732106252576
si 1.2596976740293533
a 3.406584225234165
sa 2.8763043245124345
ca 2.1815101868633087
la 2.7907905045268047
pentru 1.9054245549709234
```
### 统计文本中某字符串出现次数
`awk -v RS="@#$j" '{print gsub(/targetStr/,"&")}' filename`
