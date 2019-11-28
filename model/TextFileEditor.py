import os

class TextFileEditor(object):

     
     def __init__(self, filename):
          self.content = []
          with open(filename, 'r', encoding="utf-8") as file:
               for line in file.readlines():
                    self.content.append(line)

     def replace_per_line(self, oldvalue = '', newvalue = '', count = 0):
          for index, line in enumerate(self.content):
               self.content[index] = line.replace(oldvalue, newvalue) if count <= 0 else line.replace(oldvalue, newvalue, count)

     def output(self, filename):
          print(filename)
          filename = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '\\' + filename
          print(filename)
          with open(filename, 'a') as file:
               for line in self.content:
                    file.write(line)


class Test(object):

     def test(self):
          print("file :", __file__)
          print("file :", __name__)
          print("file :", os.path.dirname(os.path.dirname(__file__)))


