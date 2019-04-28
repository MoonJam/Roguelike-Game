from os import listdir
from re import findall, search


def dir_dict(function, file_type, directory):
    """Starting from the given root folder, this will return a dictionary
    with file-names (without extension) as keys and the appropriate results
    of the passed function as values."""
    regex = r'(?<=\{}/).+(?=\.{})'.format(directory, file_type)

    file_paths = [directory + '/' + child for child in listdir(directory)
                  if child.find(file_type) != -1]

    keys = [findall(regex, file)[0] for file in file_paths]
    values = [function(file) for file in file_paths]

    return dict(zip(keys, values))


def list_subs(directory):
    sub_directories = []

    for child in listdir(directory):
        file_extension = search(r'(?<=\.)[a-z]{2,4}$', child)
        if file_extension is None:
            sub_directories.append(directory + '/' + child)

    return sub_directories
