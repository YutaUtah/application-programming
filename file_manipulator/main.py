import sys

class FileManipulator:
    def __init__(self):
        self.cmd = sys.argv[1]
        self.first_input = sys.argv[2]
        try:
            n = int(sys.argv[3])
            self.n = n
        except:
            self.second_input = sys.argv[3]
        if len(sys.argv) == 5:
            self.third_input = sys.argv[4]
        
        self.cmd_option = {
            'reverse': self.reverse,
            'copy': self.copy,
            'duplicate-contents': self.duplicate_contents,
            'replace-string': self.replace_string,
        }
        self.cmd_option[self.cmd]()
    
    def read_content(self, path_name):
        with open(path_name, 'r') as f:
            return f.read()
        
    def write_content(self, path_name, contents):
        with open(path_name, 'w') as f:
            f.write(contents)

    def reverse(self):
        '''
        入力ファイルの内容を反転させ、その結果を出力ファイルに書き出します。
        このコマンドは、操作するファイルのパスである fileinput と、変更された新しいファイルを作成するためのパスである fileoutput を受け取ります。
        '''
        input_path = self.first_input
        output_path = self.second_input
        contents = self.read_content(input_path)
        self.write_content(output_path, contents[::-1])

    def copy(self):
        '''
        inputpath にあるファイルのコピーを作成し、outputpath として保存します。
        '''
        input_path = self.first_input
        output_path = self.second_input
        contents = self.read_content(input_path)
        self.write_content(output_path, contents)

    def duplicate_contents(self):
        '''
        inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
        '''
        input_path = self.first_input
        contents = self.read_content(input_path)
        contents = contents * self.n
        self.write_content(input_path, contents)
    
    def replace_string(self):
        '''
        inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます
        '''
        old_word = self.second_input
        new_word = self.third_input
        input_path = self.first_input
        contents = self.read_content(input_path)
        contents = contents.replace(old_word, new_word)
        self.write_content(input_path, contents)

if __name__ == '__main__':
    FileManipulator()