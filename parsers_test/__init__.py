from . import parsers
from . import utils


PARSERS = {
    'ramlfications': parsers.ramlfications_parser,
    'pyraml': parsers.pyraml_parser,
}

def main():
    args = utils.parse_args()
    parser_func = PARSERS[args.parser]
    ex_dir = utils.clone_tck_repo()
    file_list = utils.list_ramls(ex_dir)

    passed = 0
    for fpath in file_list:
        print('> Parsing {}:'.format(fpath), end=' ')
        success = True
        err = None
        try:
            parser_func(fpath)
        except Exception as ex:
            success = False
            err = ex
        if utils.should_fail(fpath):
            success = not success
        if success:
            passed += 1
            print('OK')
        else:
            err = err if args.verbose else ''
            print('FAIL {}'.format(err))
    print('\nPassed/Total: {}/{}'.format(passed, len(file_list)))
