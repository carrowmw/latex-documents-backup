# functions to help with caching

import os
import pickle
import glob
import plotly.io as pio


def read_pkl_data_from_cache(cache_dir):
    """
    Read latest data .pkl file from pipeline cache if it exists.

    :param cache_dir: The directory where the cache files are stored.

    :return: The data from the latest .pkl file in the cache directory and the parameters and dates from the filename.
    """
    if os.path.exists(cache_dir):

        # get all files in cache directory
        pkl_files = glob.glob(os.path.join(cache_dir, "*.pkl"))
        if len(pkl_files) == 0:
            return print(f"No cache files found in cache directory {cache_dir}")
        else:
            # get latest file
            latest_file = max(pkl_files, key=os.path.getctime)
            print(f"Loading data from: {latest_file}")
            with open(latest_file, "rb") as f:
                df = pickle.load(f)
            print("Data loaded successfully")
            parameter_dict, dates_dict = extract_parameters_from_filename(latest_file)
            return df, parameter_dict, dates_dict
    else:
        return print(f"Cache directory {cache_dir} does not exist")


def save_data_to_local_cache(data, cache_file_name):
    """
    Save data to local cache.
    """
    cache_dir = os.path.join(os.getcwd(), "cache")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    with open(os.path.join(cache_dir, cache_file_name), "wb") as f:
        pickle.dump(data, f)
    print(f"Data saved to cache directory: {cache_dir}")


def extract_parameters_from_filename(filename):
    """
    Extract parameters from filename.
    """
    filename = os.path.basename(filename)
    filename = filename.replace(".pkl", "")
    filename = filename.split("&")
    dates_split = filename[0].split("|")
    start_date = dates_split[1]
    end_date = dates_split[3]
    parameter_dict = {}
    if len(filename[1]) > 0:
        parameters = filename[1].split("-")
        print(parameters)
        for i in parameters:
            i = i.split("=")
            parameter_dict[i[0]] = i[1]
    dates_dict = {}
    dates_dict["start_date"] = start_date
    dates_dict["end_date"] = end_date
    return parameter_dict, dates_dict


def save_plotly_figure_as_image(
    fig, filename, format="png", scale=4, width=None, height=None
):
    """
    Save a Plotly figure to a file.

    :param fig: The Plotly figure object to save
    :param filename: The name of the file to save (including path if needed)
    :param format: The format to save in ('png', 'jpg', 'jpeg', 'webp', 'svg', 'pdf')
    :param scale: The scale factor to use when saving the figure
    :param width: The width of the saved figure in pixels (optional)
    :param height: The height of the saved figure in pixels (optional)
    """
    if not filename.lower().endswith(f".{format}"):
        filename += f".{format}"
    pio.write_image(
        fig, filename, format=format, scale=scale, width=width, height=height
    )
    print(f"Plotly figure saved as {filename}")
