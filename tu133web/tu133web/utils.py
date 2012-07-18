from os.path import abspath, dirname, join


def get_project_path(subdir=''):
    return join(dirname(dirname(abspath(__file__))), subdir)