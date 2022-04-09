import csv 
import json


def read_csv(filename):
    '''
    Reads csv file and returns data.
    :param filename: Path to csv file.
    :return: Data in csv file.'''
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def write_csv(data, filename):
    '''
    Writes data to csv file
    :param data: Data to write.
    :param filename: Path to csv file.
    '''
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_json(filename):
    """
    Reads json file and returns data.
    :param filename: Path to json file.
    :return: Data in json file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(data, filename, indent=4):
    """
    Writes data to json file.
    :param data: Data to write.
    :param filename: Path to json file.
    :param indent: Indentation of json file. Default is 4.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=indent)

def read_file(filename):
    """
    Reads file and returns text content.
    :param filename: Path to file.
    """
    with open(filename, 'r') as f:
        return f.read()

