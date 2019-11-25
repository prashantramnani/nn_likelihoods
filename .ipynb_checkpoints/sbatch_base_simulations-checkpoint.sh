#!/bin/bash

# Default resources are 1 core with 2.8GB of memory per core.

# job name:
# SBATCH -J ornstein_sim

# priority
# SBATCH --account=bibs-frankmj-condo

# output file
# SBATCH --output /users/afengler/batch_job_out/ornstein_sim_%A_%a.out

# Request runtime, memory, cores:
# SBATCH --time=24:00:00
# SBATCH --mem=24G
# SBATCH -c 14
# SBATCH -N 1
# SBATCH --array=1-1

# # Run a command
declare -a dgps=("ddm" "angle" "weibull_cdf" "ornstein" "lca" "race_model")
n_samples=( 10 100 ) #( 50000 100000 200000 400000 )
n_choices=( 3 4 5 6) #4 5 6 )
n_parameter_sets=100
# outer -------------------------------------
for n in "${n_samples[@]}"
do
# inner -------------------------------------
    for dgp in "${dgps[@]}"
    do
        if [[ "$dgp" = "lca" ]] || [[ "$dgp" = "race_model" ]];
        then
            for n_c in "${n_choices[@]}"
                do
                   python -u dataset_generator.py --machine x7 --dgplist $dgp --datatype 'cnn_train' --binned 1 --nbins 256 --maxt 10 --nchoices $n_c --nsamples $n --mode cnn --nparamsets $n_parameter_sets --save 1 --fileid TEST
                   echo "$dgp"
                   echo $n_c
            done
        else
             python -u dataset_generator.py --machine x7 --dgplist $dgp --datatype 'cnn_train' --binned 1 --nbins 256 --maxt 10 --nchoices 2 --nsamples $n --mode cnn --nparamsets $n_parameter_sets --save 1 --fileid TEST
             echo "$dgp"
             echo $n_c
        fi
    done
            # normal call to function
done
# -------------------------------------------
#done
# -------------------------------------------

# python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv ornstein 2 100000 1 $SLURM_ARRAY_TASK_ID base_simulations 10000 0

# python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv lca 3 100000 1 $SLURM_ARRAY_TASK_ID base_simulations 10000 0

# python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv lca 4 100000 1 $SLURM_ARRAY_TASK_ID base_simulations 10000 0

# python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv lca 5 100000 1 $SLURM_ARRAY_TASK_ID base_simulations 10000 0

# python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv lca 6 100000 1 $SLURM_ARRAY_TASK_ID base_simulations 10000 0

#python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv race_model 3 100000 1 $SLURM_ARRAY_TASK_ID 1000 0

#python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv race_model 5 100000 1 $SLURM_ARRAY_TASK_ID

#python -u /users/afengler/git_repos/nn_likelihoods/kde_base_simulations.py ccv race_model 6 100000 1 $SLURM_ARRAY_TASK_ID