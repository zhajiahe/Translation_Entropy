# Translation_Entropy
## requirements
[fast_BPE](https://github.com/glample/fastBPE): get vocab of paralell corpus

[fast_align](https://github.com/clab/fast_align): library of unsupervised alignment
## usage
`bash main.sh corpus_a corpus_b`
- corpus_a : sentences of language a
- corpus_b : sentences of language b
### 统计文本中某字符串出现次数
`awk -v RS="@#$j" '{print gsub(/targetStr/,"&")}' filename`
