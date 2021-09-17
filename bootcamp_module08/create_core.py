import shutil
from importlib import resources
from pkg_resources import resource_filename

from jinja2 import Template


def get_test_template(package, resource):
    template_lines = resources.open_text(package, resource)
    return Template(''.join(template_lines))


def create_core_file_with_tests(module):

    starter_code_path = resource_filename('bootcamp_module08.templates',
                                          'count_substring.py',
                                          )
    module_package = 'bootcamp_module08.core'
    module_relpath = module + '.py'
    module_path = resource_filename(module_package, module_relpath)
    shutil.copyfile(starter_code_path, module_path)

    template = get_test_template('bootcamp_module08.templates',
                                 'template_test_count_substring.py')

    test_contents = template.render(module=module) + '\n'
    test_package = 'bootcamp_module08.core.tests'
    test_relpath = 'test_' + module + '.py'
    test_path = resource_filename(test_package, test_relpath)
    with open(test_path, 'w') as fh:
        fh.write(test_contents)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate python files for '
                                                 'interactive demonstration.')
    parser.add_argument(
        '--prefix',
        type=str,
        help='Format each file name with prefix.',
    )
    parser.add_argument(
        '--start',
        type=int,
        help='Number to start generating files at.',
    )
    parser.add_argument(
        '--stop',
        type=int,
        help='Number to stop generating files at.',
    )
    parser.add_argument(
        '--format-places',
        default=2,
        type=int,
        help='Number of digits to format number suffix to.'
    )
    args = parser.parse_args()
    for i in range(args.start, args.stop + 1):
        create_core_file_with_tests(
            f'{args.prefix}_{i:0{args.format_places}d}'
        )
