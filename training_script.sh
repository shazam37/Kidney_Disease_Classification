#!/bin/bash
#SBATCH -w gnode113
#SBATCH -A plafnet2 
#SBATCH -p plafnet2
#SBATCH --mem-per-cpu=2G
#SBATCH --cpus-per-task=20
#SBATCH --gres=gpu:1
#SBATCH --time=4-00:00:00
#SBATCH --output=/scratch/Shaz/scripts/kidney_output.txt


export PATH=/scratch/Shaz/miniconda3/envs/kidney/bin:$PATH
export LD_LIBRARY_PATH=/scratch/Shaz/miniconda3/envs/kidney/lib:$LD_LIBRARY_PATH

python main.py 
