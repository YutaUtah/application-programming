import markdown
import sys


class FileConverter:
    def __init__(self):
        self.cmd = sys.argv[1]
        self.input_path = sys.argv[2]
        self.output_path = sys.argv[3]
    
    def __get_html(self):
        with open(self.input_path, "r") as f:
            contents = f.read()
            return markdown.markdown(contents)

    def write_to_html(self):
        html = self.__get_html()
        with open(self.output_path, "w") as f:
            f.write(html)

if __name__ == '__main__':
    FileConverter().write_to_html()