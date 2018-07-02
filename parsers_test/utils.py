import argparse

def parse_args():
    arg_parser = argparse.ArgumentParser(
        description='Test few RAML Python parsers.')
    arg_parser.add_argument(
        '--parser', type=str, help='Parser to test',
        choices=['ramlfications', 'pyraml'],
        required=True)
    arg_parser.add_argument(
        '--verbose', help='Print errors or not',
        action='store_true')
    return arg_parser.parse_args()


def clone_tck_repo():
    # TODO
    return

def list_ramls(ex_dir):
    # TODO
    return ['a', 'b']

def should_fail(fpath):
    # TODO
    return False