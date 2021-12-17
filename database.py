import jsonManager


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


def initialize():
    get_number_annotations_by_user()
    get_number_annotations_by_project()
    get_assets_with_majority_different_labels('019mr8mf4a')
