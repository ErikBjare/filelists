#!/bin/python3

import collections
import itertools
from queue import Queue

# Constant
DEEPEST_PATH = 4


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


def walk_bfs(node):
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


def main():
    pathtree = Tree()

    with open("filelist_root.txt") as f:
        for line in f:
            path = line[0:line.rfind('/')]

            dirs = path.split('/')
            recursive_assign(pathtree, dirs)

    for path, filecount in walk_bfs(pathtree):
        print(filecount, path)
        if path.count("/") > DEEPEST_PATH:
            break


if __name__ == "__main__":
    main()
