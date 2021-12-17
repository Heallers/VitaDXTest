import json


def parse_annotations():
    with open('data.json') as l_file:
        l_data = json.load(l_file)
        return l_data


def parse_projects():
    with open('projects.json') as l_file:
        l_data = json.load(l_file)
        return l_data
