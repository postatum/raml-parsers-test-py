from . import parsers
from . import utils


PARSERS = {
    'ramlfications': parsers.ramlficationsParser,
    'pyraml': parsers.pyramlParser,
}


def main():
    args = utils.parse_args()
    parserFunc = PARSERS[args.parser]
    ex_dir = utils.clone_tck_repo()
    file_list = utils.list_ramls(ex_dir)

    for fpath in file_list:
        print('> Parsing {}:'.format(fpath), end=' ')
        success = True
        err = None
        try:
            parserFunc(fpath)
        except Exception as ex:
            success = False
            err = ex
        if utils.should_fail(fpath):
            success = not success
        if success:
            print('OK')
        else:
            err = err if args.verbose else ''
            print('FAIL {}'.format(err))
