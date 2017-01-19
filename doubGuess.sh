#PBS -N gutSim -S /bin/sh
#PBS -l nodes=1:ppn=40
~/netlogo-6.0/netlogo-headless.sh \
--model ~/gut-nlogo-model/NLCode.nlogo \
--experiment doubGuess \
--spreadsheet ~/results/doubGuess.csv \
--threads 40