import sys
import subprocess


def lint(style_guide):
    target_directory = sys.argv[1]
    command = "pep8 --config {} {}".format(style_guide, target_directory)
    subprocess.call(command, shell=True)
