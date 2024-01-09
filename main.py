"""
This project will include several parts:
Bootstrapping our original dataset
Rebuilding the DNV api access code for coherency and usability
interface for both of these things
data visualization
"""

from functions import import_ts_8760, bootstrapping, export_to

def main():
    # Bootstrapping
    # import datasets in time_series_8760_data
    imported_datasets = import_ts_8760.import_8760s()

    # process data to bootstrap, taking sum for now of 8760
    sum_dataset = bootstrapping.bootstrap_processing(imported_datasets)

    # bootstrapping, got a confidence interval and stuff, whatever clay needs out of the bootstrapping now I can provide
    # accessible under the bootstrap_dataset[site][source]["Confidence Interval"]
    bootstrap_dataset = bootstrapping.bootstrapping(sum_dataset)

    # print to an accesible excel format
    export_to.export_to_json(bootstrap_dataset)

    return



        # todo perform the bootstrapping (not quite there yet)

    # todo Rebuild DNV API access

    # todo Interface

    # todo Data Visualization

main()