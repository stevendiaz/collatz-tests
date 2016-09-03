
rm RunCollatz.out
rm RunCollatz.in
touch RunCollatz.in
touch RunCollatz.out

touch overflow
python findcollatzoverflow.py
python collatztestgen.py
