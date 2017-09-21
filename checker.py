import argparse

import os

import sys


class Checker(object):
    def __init__(self, input_dir):
        self.input_dir = input_dir

    def check(self):
        xml_files = self.find_filenames_by_extension(extension="xml")
        jpg_files = self.find_filenames_by_extension(extension="jpg")
        xml_diff_filenames = [item + ".xml" for item in xml_files if item not in jpg_files]
        jpg_diff_filenames = [item + ".jpg" for item in jpg_files if item not in xml_files]
        diff_filenames = xml_diff_filenames + jpg_diff_filenames

        if len(diff_filenames) > 0:
            print("Found unmatched {} file(s)".format(len(diff_filenames)))
            for filename in diff_filenames:
                file_path = "{}{}".format(self.input_dir, filename)
                print(file_path)
                os.remove(file_path)
        else:
            print("Not found unmatched files")

    def find_filenames_by_extension(self, extension):
        filenames = []
        for filename in os.listdir(self.input_dir):
            if filename.endswith("." + extension):
                filenames.append(filename.strip().split(".")[0])
        return filenames


def main():
    parser = argparse.ArgumentParser(description="Checks xml and jpeg match")
    parser.add_argument("-dir", help="Relative location of xml files directory", required=True)
    args = parser.parse_args()
    input_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.dir)

    if not os.path.exists(input_dir):
        print("Provide the correct folder.")
        sys.exit()

    checker = Checker(input_dir=input_dir)
    checker.check()


if __name__ == "__main__":
    main()
