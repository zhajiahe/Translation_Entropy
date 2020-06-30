# Translation_Entropy
<<<<<<< HEAD
## Requirements
fast_BPE: get vocab of paralell corpus
fast_align: library of unsupervised alignment
## Usage
bash main.sh corpus_a corpus_b
=======
## requirements
[fast_BPE](https://github.com/glample/fastBPE): get vocab of paralell corpus

[fast_align](https://github.com/clab/fast_align): library of unsupervised alignment
## usage
`bash main.sh corpus_a corpus_b`
>>>>>>> d2fd6b969b6af138c00dfa32818b617e08bfd24b
- corpus_a : sentences of language a
- corpus_b : sentences of language b
## Example
corpus_en:

`this will be the only way to promote paren@@ tho@@ od with shared responsibilities .
in my opinion , this debate goes in the right direction .
at a time when states , local communities , taxpayers and businesses are accepting financial sacrifices , the union cannot exempt itself from this virtu@@ ous process .
firstly , the agreement reached on a regulation on credit @-@ rating agencies will help address one of the problems that contributed to this crisis and thus will offer some prospect of restoring market confidence .
the different legislation of the individual provinces is an additional problematic aspect .`

corpus_ro:

`aceasta va fi singura modalitate de a promova o maternitate / paternitate cu responsabilitati comune .
in opinia mea , aceasta dezbatere se indreapta in directia corecta .
intr @-@ un moment in care statele , comunitatile locale , contribuabilii si intreprinderile accepta sacrificii financiare , uniunea nu poate evita implicarea sa in acest proces just .
in primul rand , acordul obtinut asupra regulamentului privind agentiile de rating al creditelor va ajuta la rezolvarea uneia dintre problemele care au contribuit la aceasta criza si va crea astfel perspective de re@@ stabilire a increderii in piata .
legislatia diferita a provinci@@ ilor individuale este un aspect problematic suplimentar .`

`bash main.sh corpus_en corpus_ro`

trans_entropy.en:

`the 5.698906254414691
, 1.444006961962339
. 0.09609516628672199
of 3.2255480079422636
to 3.5215574728482197
and 1.0304466601300641
in 1.7478318554051528
a 2.4863726398605657
that 2.176085465470134
is 1.9418089845412654`
### 统计文本中某字符串出现次数
`awk -v RS="@#$j" '{print gsub(/targetStr/,"&")}' filename`
