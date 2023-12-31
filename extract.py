"""Extract data on near-Earth objects and close approaches from CSV/JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth
    objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos_collection = []
    with open(neo_csv_path, 'r', encoding='utf8') as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            neos_collection.append(NearEarthObject(designation=elem['pdes'],
                                                   name=elem['name'],
                                                   diameter=elem['diameter'],
                                                   hazardous=elem['pha']
                                                   ))
    return neos_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """
    cad_collection = []
    with open(cad_json_path, 'r', encoding='utf8') as infile:
        data = json.load(infile)
    headers = data['fields']

    # iterate through all close approaches
    for point in data['data']:
        temp_dict = {}
        i = 0
        # for each close approach, save the individual info in a dict
        for header in headers:
            temp_dict[header] = point[i]
            i += 1
        cad_collection.append(CloseApproach(designation=temp_dict['des'],
                                            time=temp_dict['cd'],
                                            distance=temp_dict['dist'],
                                            velocity=temp_dict['v_inf']
                                            ))
    return cad_collection
