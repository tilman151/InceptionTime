import subprocess
import sys
import os
import random


if __name__ == '__main__':
    script_path = os.path.dirname(__file__)
    result_path = os.path.join(script_path, 'results')
    processes_per_gpu = 2
    gpus = 2
    num_datasets = 85
    datasets_per_gpu = num_datasets // gpus
    datasets_per_process = datasets_per_gpu // processes_per_gpu
    remainder_gpus = num_datasets % gpus
    random.seed(42)

    for replication in range(0, 5):
        processes = []
        for gpu_id in range(gpus):
            for process_id in range(processes_per_gpu):
                start_dataset = gpu_id * datasets_per_gpu + process_id * datasets_per_process
                end_dataset = gpu_id * datasets_per_gpu + (process_id + 1) * datasets_per_process
                if (process_id + 1) == processes_per_gpu:
                    if (gpu_id + 1) == gpus:
                        end_dataset = num_datasets
                    else:
                        end_dataset += remainder_gpus + 1
                processes.append(subprocess.Popen([sys.executable, './main.py', 'InceptionTime',
                                                   str(random.randint(0, 999999)), str(start_dataset),
                                                   str(end_dataset), str(gpu_id)],
                                                  stdout=subprocess.DEVNULL,
                                                  shell=False))

        exit_codes = []
        for p in processes:
            exit_codes.append(p.wait())

        print(exit_codes)
        os.rename(result_path, result_path + f'_{replication}')
