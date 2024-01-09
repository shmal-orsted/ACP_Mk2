import pandas
import pandas as pd
from scipy.stats import bootstrap
import numpy as np


def bootstrap_processing(imported_datasets):
    """
    Processing of the datasets to be bootstrapped, in this case, taking a sum of the datasets included in the
    imported datasets and returning them to be resampled.
    :return:
    """
    # make these monthly intervals instead, then produce confidence intervals high and low for ecah month that are output

    # index the dicts for each site
    sites = imported_datasets.keys()
    for site in sites:
        #index the datasets in each site
        datasources = imported_datasets[site].keys()
        for source in datasources:
            df = imported_datasets[site][source]["Data"]
            # process dataframe for use in the main function
            # make monthly sums
            df = df.groupby([(df.index.year), (df.index.month)]).sum()
            # drop 0 value columns for bootstrapping
            df = df.loc[:, (df != 0).any(axis=0)]
            # add back in to the original dict
            imported_datasets[site][source]["Monthly Dataframe"] = df.div(1000000000)

    return imported_datasets

def bootstrapping(sum_dataset):
    """
    Performing the bootstrapping operations and function calls
    :param sum_dataset:
    :return: confidence interval from scipy process
    """
    def row_bootstrap(row):
        row = (row,)
        bootstrap_data = bootstrap(row, np.median, confidence_level=0.95,
                  random_state=1, method='percentile')

        return bootstrap_data


    # this is being messed up somewhere, copying the same value each month
    # separate dataset for use
    for key in sum_dataset.keys():
        for source in sum_dataset[key].keys():
            #iterate through monthly rows for this process
            data = sum_dataset[key][source]["Monthly Dataframe"]
            # data["ci"] = data.apply(lambda row: row_bootstrap(row), axis=1)
            # run this for each month in the monthly set
            monthly_ci = []
            # add to list to iterate through for export
            for x in range(0, 12):
                ci = row_bootstrap(data.iloc[x])
                monthly_ci.append(ci)
            sum_dataset[key][source]["Bootstrap Data"] = monthly_ci

    return sum_dataset