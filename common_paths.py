#!/bin/python3

import collections
import itertools
from queue import Queue

def Tree():
    return collections.defaultdict(Tree)

def recursive_assign(tree, keylist):
    if len(keylist) == 0:
        return
    branch = keylist[0]
    if branch not in tree:
        tree[branch] = Tree()
        tree[branch]["#count"] = 0
    tree[branch]["#count"] += 1
    recursive_assign(tree[branch], keylist[1:])

def walk_dfs(node) -> int:
    """Iterate tree depth-first"""
    for branch in node.keys():
        if type(node[branch]) == int:
            yield ('', node[branch])
            continue
        for child in walk_dfs(node[branch]):
            yield (branch + "/" + child[0], child[1])

def walk_bfs(node) -> int:
    """Iterate tree breadth-first"""
    queue = Queue()
    for child_path, child_node in node.items():
        queue.put((child_path, child_node))

    # Traverse the queue
    while not queue.empty():
        path, node = queue.get()
        if path != "#count":
            yield (path, node["#count"])
        for child_path, child_node in node.items():
            if child_path != "#count":
                queue.put((path + "/" + child_path, child_node))


def advanced():
    pathtree = Tree()

    max_i = 1000000000
    with open("filelist_root.txt") as f:
        i = 0
        for line in f:
            path = line[0:line.rfind('/')]

            dirs = path.split('/')
            recursive_assign(pathtree, dirs)
            i += 1
            if i > max_i:
                break

    #sorted_pathtree = sorted(pathtree.items(), key=lambda pair: pair[1]["#count"])

    for path, filecount in walk_bfs(pathtree):
        print(filecount, path)
        if path.count("/") > 4:
            break

    """
    POLL_NUMBER = 1000

    polled_paths = list(itertools.islice(walk_bfs(pathtree), POLL_NUMBER))
    for path, filecount in polled_paths:
        print(path, filecount)
    """

    #sorted_pathtree = sorted(list(walk_bfs(pathtree)), key=lambda p: -p[1])
    #for line in sorted_pathtree[:100]:
    #    print(line)

    #for directory in sorted_pathtree:
    #    print(directory[1]["#count"], directory[0])


def simple():
    paths = collections.defaultdict(lambda: 0)

    max_i = 10000
    with open("filelist_root.txt") as f:
        i = 0
        for line in f:
            path = line[0:line.rfind('/')]

            dirs = path.split('/')
            branch = dirs[0]
            for directory in dirs[1:]:
                branch = directory
                paths[branch]
            paths[path] += 1
            i += 1
            if i > max_i:
                break

    sorted_paths = sorted(paths.items(), key=lambda pair: -pair[1])

    for path in sorted_paths[:50]:
        print(path[1], path[0])

if __name__ == "__main__":
    advanced()
