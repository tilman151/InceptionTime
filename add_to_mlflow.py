import os

import mlflow
import pandas as pd


def add(mlflow_uri):
    results = _gather_results()
    _write_to_mlflow(results, mlflow_uri)


def _gather_results():
    script_path = os.path.dirname(__file__)
    result_dirs = [f for f in os.listdir(script_path) if os.path.isdir(f) and 'results' in f]
    result_data = []
    for result_dir in result_dirs:
        result_data.extend(_get_results_from_dir(os.path.join(script_path, result_dir)))
    result_data = pd.DataFrame.from_records(result_data)

    result_data = result_data.groupby(by=['classifier', 'dataset']).agg({'accuracy': ['mean', 'std', 'count']})

    return result_data


def _get_results_from_dir(result_dir):
    directory = os.path.basename(result_dir)
    results = []
    for dir_path, _, file_names in os.walk(result_dir):
        if 'df_metrics.csv' in file_names:
            metrics = pd.read_csv(os.path.join(dir_path, 'df_metrics.csv'))
            accuracy = metrics['accuracy'][0]
            classifier, replication, dataset = dir_path.replace(result_dir + os.sep, '').split(os.sep)
            result_record = {'result_dir': directory,
                             'classifier': classifier,
                             'replication': replication,
                             'dataset': dataset,
                             'accuracy': accuracy}
            results.append(result_record)

    return results


def _write_to_mlflow(results, mlflow_uri):
    mlflow.set_tracking_uri(mlflow_uri)
    mlflow.set_experiment('ucr_data')
    for classifier in results.index.levels[0]:
        with mlflow.start_run():
            mlflow.log_param('classifier', classifier)
            for dataset, row in results.loc[classifier].iterrows():
                mlflow.log_metrics({f'mean_accuracy_{dataset}_0': row[('accuracy', 'mean')],
                                    f'std_accuracy_{dataset}_0': row[('accuracy', 'std')]})


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Add results to mlflow')
    parser.add_argument('mlflow_uri', help='tracking URI for mlflow')
    opt = parser.parse_args()

    add(opt.mlflow_uri)
