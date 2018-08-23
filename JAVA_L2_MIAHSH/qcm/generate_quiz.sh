set -x

rm -rf output
mkdir output
./notebook_quiz_generator.py
for filename in output/*.ipynb; do
	jupyter nbconvert --execute  --inplace $filename
	jupyter trust $filename
done

set +x 
