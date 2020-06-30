# author = 'hazhang'
# Pipeline to obtain translation entropy

fast=~/hazhang/tools/fastBPE/fast
fast_align=~/hazhang/tools/fast_align/build/fast_align

CORPUS_A=$1
CORPUS_B=$2

echo "Computing translation entropy ~~~"
echo "INPUT corpus: $CORPUS_A , $CORPUS_B"

paste -d '`' $CORPUS_A $CORPUS_B > tmp_a
paste -d '`' $CORPUS_B $CORPUS_A > tmp_b

sed -i 's/`/ ||| /g' tmp_a
sed -i 's/`/ ||| /g' tmp_b

$fast getvocab $CORPUS_A > vocab_src
$fast getvocab $CORPUS_B > vocab_tgt

$fast_align -i tmp_a -d -o -v > align_a
$fast_align -i tmp_b -d -o -v > align_b

python translation_entropy.py vocab_src vocab_tgt align_a $CORPUS_A $CORPUS_B
python translation_entropy.py vocab_tgt vocab_src align_b $CORPUS_B $CORPUS_A

rm tmp_a
rm tmp_b
rm align_a
rm align_b
rm vocab_src
rm vocab_tgt
