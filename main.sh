# author = 'hazhang'
# Pipeline to obtain translation entropy

fast=~/hazhang/tools/fastBPE/fast
fast_align=~/hazhang/tools/fast_align/build/fast_align

CORPUS_A=$1
CORPUS_B=$2

echo "Computing translation entropy ~~~"
echo "$CORPUS_A and $CORPUS_B"
paste -d '`' $CORPUS_A $CORPUS_B > tmp
sed -i 's/`/ ||| /g' tmp

$fast getvocab CORPUS_A > vocab_src
$fast getvocab CORPUS_B > vocab_tgt

$fast_align -i tmp -d -o -v > forward.align
$fast_align -i tmp -d -o -v -r > reverse.align
rm tmp

python translation_entropy.py vocab_src vocab_tgt forward.align $CORPUS_A $CORPUS_B
python translation_entropy.py vocab_tgt vocab_src reverse.align $CORPUS_B $CORPUS_A

rm forward.align
rm reverse.align
rm vocab_src
rm vocab_tgt
