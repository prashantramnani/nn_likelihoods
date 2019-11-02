#!/bin/bash

# Default resources are 1 core with 2.8GB of memory per core.

# job name:
#SBATCH -J weibull_train_test

# priority
#SBATCH --account=bibs-frankmj-condo

# output file
#SBATCH --output /users/afengler/batch_job_out/weibull_cdf_ndt_train_test_%A_%a.out

# Request runtime, memory, cores:
#SBATCH --time=24:00:00
#SBATCH --mem=24G
#SBATCH -c 1
#SBATCH -N 1
#SBATCH --array=1-100

# Run a command

python -u /users/afengler/git_repos/nn_likelihoods/kde_train_test.py $SLURM_ARRAY_TASK_ID
#python -u /users/afengler/git_repos/nn_likelihoods/navarro_fuss_train_test.py