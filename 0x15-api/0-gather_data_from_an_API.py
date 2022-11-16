#!/usr/bin/python3
""" return info on employees """

if __name__ == "__main__":
    import requests
    import sys

    erequest = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))

    name = erequest.json().get('name')
    trequests = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = trequests.json()
    taskcompleted = 0
    totaltasks = 0
    tasklist = []
    for taskcheck in tasks:
        if taskcheck['userId'] == int(sys.argv[1]):
            if taskcheck.get("completed"):
                tasklist.append(taskcheck)
                taskcompleted += 1
            totaltasks += 1
    print("Employee {} is done with tasks({}/{}):".format
          (name, taskcompleted, totaltasks))
    for completedtasks in tasklist:
        print("\t {}".format(completedtasks.get("title")))
