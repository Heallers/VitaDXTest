import jsonManager
import datetime

def get_annotations():
    print("get_annotations")
    l_annotations = jsonManager.parse_annotations()
    print(l_annotations)
    return l_annotations


def get_number_annotations_by_user():
    print("get_number_annotations_by_user")
    l_annotations = jsonManager.parse_annotations()
    l_number_annotations_by_user = {}

    for l_annotation in l_annotations:
        if l_annotation['user'] not in l_number_annotations_by_user:
            l_number_annotations_by_user[l_annotation['user']] = 0
        l_number_annotations_by_user[l_annotation['user']] = l_number_annotations_by_user[l_annotation['user']]+1

    print(l_number_annotations_by_user)
    return l_number_annotations_by_user


def get_number_annotations_by_project():
    print("get_number_annotations_by_project")
    l_annotations = jsonManager.parse_annotations()
    l_number_annotations_by_project = {}

    for l_annotation in l_annotations:
        if l_annotation['project_id'] not in l_number_annotations_by_project:
            l_number_annotations_by_project[l_annotation['project_id']] = 0
        l_number_annotations_by_project[l_annotation['project_id']] = l_number_annotations_by_project[l_annotation['project_id']]+1

    print(l_number_annotations_by_project)
    return l_number_annotations_by_project


def get_assets_with_majority_different_labels(_project_id):
    print("get_assets_with_majority_different_labels for project " + _project_id)
    l_annotations = jsonManager.parse_annotations()
    l_labels_by_assets = {}

    for l_annotation in l_annotations:
        if l_annotation['project_id'] == _project_id:
            if l_annotation['asset_id'] not in l_labels_by_assets:
                l_labels_by_assets[l_annotation['asset_id']] = []
            l_labels_by_assets[l_annotation['asset_id']].append(l_annotation['label'])

    l_result = []
    for l_tuple in l_labels_by_assets.items():
        if len(l_tuple[1]) / 2 < len(set(l_tuple[1])):
            l_result.append(l_tuple[0])

    print(l_result)
    return l_result


def get_projects_with_more_than_15_assets(_user, _begin, _end):
    print("get_projects_with_more_than_15_assets for user " + _user)
    l_annotations = jsonManager.parse_annotations()
    l_assets_by_project = {}

    l_begin = datetime.datetime.strptime(_begin, '%Y-%m-%dT%H:%M:%SZ').timestamp()
    l_end = datetime.datetime.strptime(_end, '%Y-%m-%dT%H:%M:%SZ').timestamp()

    for l_annotation in l_annotations:
        if l_annotation['user'] == _user:
            l_date = datetime.datetime.strptime(l_annotation['date'], '%Y-%m-%dT%H:%M:%SZ').timestamp()
            if l_begin <= l_date <= l_end:
                if l_annotation['project_id'] not in l_assets_by_project:
                    l_assets_by_project[l_annotation['project_id']] = []
                l_assets_by_project[l_annotation['project_id']].append(l_annotation['asset_id'])

    l_result = []
    for l_tuple in l_assets_by_project.items():
        if len(l_tuple[1]) > 15:
            l_result.append(l_tuple[0])

    print(l_result)
    return l_result


def initialize():
    get_number_annotations_by_user()
    get_number_annotations_by_project()
    get_assets_with_majority_different_labels('019mr8mf4a')
    get_projects_with_more_than_15_assets('annotator_001', "2021-03-12T16:09:40Z", "2022-03-12T16:09:40Z")