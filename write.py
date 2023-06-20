"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output
    row corresponds to the information in a single close approach from the
    `results` stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should
    be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    with open(filename, 'w', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
        for r in results:
            row = [r.time_str, r.distance, r.velocity, r.neo.designation,
                   r.neo.name, r.neo.diameter, str(r.neo.hazardous)]
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is
    a list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
    saved.
    """
    transformed_results = []
    for r in results:
        temp = dict(
            datetime_utc=r.time_str,
            distance_au=r.distance,
            velocity_km_s=r.velocity,
            neo=dict(
                designation=r.neo.designation,
                name=r.neo.name if r.neo.name is not None else '',
                diameter_km=r.neo.diameter,
                potentially_hazardous=r.neo.hazardous
            )
        )
        transformed_results.append(temp)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(transformed_results, outfile)
