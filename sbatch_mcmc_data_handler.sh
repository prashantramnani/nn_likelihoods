#!/bin/bash

# Default resources are 1 core with 2.8GB of memory per core.

# job name:
#SBATCH -J mcmc_data_handler

# priority
#SBATCH --account=bibs-frankmj-condo

# output file
#SBATCH --output /users/afengler/batch_job_out/data_handler

# Request runtime, memory, cores:
#SBATCH --time=36:00:00
#SBATCH --mem=32G
#SBATCH -c 12
#SBATCH -N 1
#SBATCH --array=1-1

# python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method ddm --nburnin 5000 --ndata 2048 --nsubsample 10000 --nnbatchid -1
python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method ddm --nburnin 5000 --ndata 4096 --nsubsample 10000 --nnbatchid -1
#python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method ornstein --nburnin 5000 --ndata 2048 --nsubsample 10000 --nnbatchid -1
python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method ornstein --nburnin 5000 --ndata 4096 --nsubsample 10000 --nnbatchid -1
#python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method full_ddm --nburnin 5000 --ndata 2048 --nsubsample 10000 --nnbatchid -1
python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method full_ddm --nburnin 5000 --ndata 4096 --nsubsample 10000 --nnbatchid -1
#python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method levy --nburnin 5000 --ndata 2048 --nsubsample 10000 --nnbatchid -1
python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method levy --nburnin 5000 --ndata 4096 --nsubsample 10000 --nnbatchid -1
#python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method weibull_cdf --nburnin 5000 --ndata 2048 --nsubsample 10000 --nnbatchid -1
python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method weibull_cdf --nburnin 5000 --ndata 4096 --nsubsample 10000 --nnbatchid -1
#python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method angle --nburnin 5000 --ndata 2048 --nsubsample 10000 --nnbatchid -1
python -u /users/afengler/git_repos/nn_likelihoods/mcmc_data_handler.py --machine ccv --method angle --nburnin 5000 --ndata 4096 --nsubsample 10000 --nnbatchid -1