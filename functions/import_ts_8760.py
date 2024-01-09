import pandas as pd
import glob
import os

# import data from folder above into dataframes labelled by year going backwards from 2022
# store data for bootstrapping

#  scrape data from here: time_series_8760_data
def import_8760s():
    """
    Importing the 8760s as dataframes from the csv files, this should be transferrable into the IEEE folder after it's completed

    :return:
    Dataset of imported data ready for processing
    """
    path = os.getcwd()
    datasets = ["SolarAnywhere", "SolarGIS", "Vaisala"]
    imported_datasets = {}
    # get all the sub directories in the time_series_8760_data folder
    directories = os.listdir(os.path.join(path, "time_series_8760_data"))

    # iterate through those for each dataset import call
    for directory in directories:

        subdir = os.path.join(path, "time_series_8760_data", directory)
        # read each dataset in
        temp_dict = {}
        for set in datasets:
            imported_dataset = pd.read_csv(os.path.join(subdir, f"8760_exports_{set}.csv"))
            try:
                imported_dataset["Unnamed: 0"] = pd.to_datetime(imported_dataset["Unnamed: 0"])
            except:
                print("Error")
            imported_dataset = imported_dataset.set_index("Unnamed: 0")
            # add each of those import or read calls to a single dataset storage
            temp_dict[set] = {
                "Data" : imported_dataset,
                "Monthly Dataframe": None,
                "Bootstrap Data": None,
            }

            imported_datasets[directory] = temp_dict

    # (optional) store this in memory? Add this to another storage to get running again easily?

    return imported_datasets