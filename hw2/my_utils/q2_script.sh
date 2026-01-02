learning_rates=(0.001 0.005 0.01 0.05 0.1 0.5 1.0)
batch_sizes=(100 500 1000 2000 5000)
export PYTHONPATH=/Users/matthew-xh/Study/CS/16831-S25/hw2

for r in "${learning_rates[@]}"; do
    for b in "${batch_sizes[@]}"; do
        python rob831/scripts/run_hw2.py --env_name InvertedPendulum-v4 \
        --ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 -b ${b} -lr ${r} -rtg \
        --exp_name q2_b${b}_r${r}
    done
done