import os
import argparse


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--projname", help="project name")
    args = parser.parse_args()
    return args


def main():
    args = parse_argument()
    dirName = args.projname
    os.makedirs(dirName)

    os.makedirs(dirName+"/app")
    with open(dirName+"/app/__init__.py", "w") as f:
        pass

    os.makedirs(dirName+"/app/routers")
    with open(dirName+"/app/routers/__init__.py", "w") as f:
        pass

    os.makedirs(dirName+"/app/internal")
    with open(dirName+"/app/internal/__init__.py", "w") as f:
        pass


if __name__ == '__main__':
    main()