import sqlite3
import datetime
import jsonManager

l_conn = sqlite3.connect(':memory:', check_same_thread=False)


def create_tables():
    l_cursor = l_conn.cursor()

    l_cursor.execute("create table users (id INTEGER PRIMARY KEY NOT NULL, user TEXT)")

    l_cursor.execute("create table projects (id INTEGER PRIMARY KEY NOT NULL, project_id TEXT)")

    l_cursor.execute("create table annotations ("
                     "id INTEGER PRIMARY KEY NOT NULL, "
                     "user VARCHAR(100), "
                     "project_id VARCHAR(100), "
                     "asset_id VARCHAR(100), "
                     "label VARCHAR(100), "
                     "is_last_checkpoint BIT, "
                     "date TIMESTAMP, "
                     "FOREIGN KEY(user) REFERENCES users(user), "
                     "FOREIGN KEY(project_id) REFERENCES projects(project_id))")

    l_cursor.close()


def insert_data():
    l_annotations = jsonManager.parse_annotations()
    l_users_set = set()
    l_projects_set = set()
    l_annotations_list = []

    for l_annotation in l_annotations:
        date_time_obj = datetime.datetime.strptime(l_annotation['date'], '%Y-%m-%dT%H:%M:%SZ')
        l_users_set.add(tuple([l_annotation['user']]))
        l_projects_set.add(tuple([l_annotation['project_id']]))
        l_annotations_list.append((
            l_annotation['user'],
            l_annotation['project_id'],
            l_annotation['asset_id'],
            l_annotation['label'],
            l_annotation['is_last_checkpoint'],
            date_time_obj
        ))

    print(l_users_set)
    print(l_projects_set)
    print(l_annotations_list)
    l_cursor = l_conn.cursor()
    l_cursor.executemany("insert into users (user) values (?)", list(l_users_set))
    l_cursor.executemany("insert into projects (project_id) values (?)", list(l_projects_set))
    l_cursor.executemany("insert into annotations (user, project_id, asset_id, label, is_last_checkpoint, "
                         "date) values (?, ?, ?, ?, ?, ?)",
                         l_annotations_list)
    l_cursor.close()


def get_annotations():
    print("get_annotations")

    l_cursor = l_conn.cursor()
    l_cursor.execute("select a.* from annotations a")
    l_annotations = l_cursor.fetchall()
    l_annotations_list = []

    for l_annotation in l_annotations:
        l_annotations_list.append({
            "id": l_annotation[0],
            "user": l_annotation[1],
            "project_id": l_annotation[2],
            "asset_id": l_annotation[3],
            "label": l_annotation[4],
            "is_last_checkpoint": l_annotation[5],
            "date": l_annotation[6]
        })

    l_cursor.close()
    print(l_annotations_list)
    return l_annotations_list


def get_number_annotations_by_user():
    print("get_number_annotations_by_user")

    l_cursor = l_conn.cursor()
    l_cursor.execute("select u.user, count(a.id) from users u, annotations a on u.user=a.user group by u.user")
    l_number_annotations_by_user = l_cursor.fetchall()
    l_number_by_user_list = []

    for l_number_by_user in l_number_annotations_by_user:
        l_number_by_user_list.append({
            "user": l_number_by_user[0],
            "number": l_number_by_user[1]
        })

    l_cursor.close()
    print(l_number_by_user_list)
    return l_number_by_user_list


def get_number_annotations_by_project():
    print("get_number_annotations_by_project")

    l_cursor = l_conn.cursor()
    l_cursor.execute("select p.project_id, count(a.id) from projects p, annotations a on p.project_id=a.project_id "
                     "group by p.project_id")
    l_number_annotations_by_project = l_cursor.fetchall()
    l_number_by_project_list = []

    for l_number_by_project in l_number_annotations_by_project:
        l_number_by_project_list.append({
            "project": l_number_by_project[0],
            "number": l_number_by_project[1]
        })

    l_cursor.close()
    print(l_number_by_project_list)
    return l_number_by_project_list


def initialize():
    create_tables()
    insert_data()
