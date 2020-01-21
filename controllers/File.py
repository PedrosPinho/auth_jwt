from flask import jsonify
import os

class File():
    def read_file(self):
        if os.path.isfile("storage/file.txt"):
            file = open("storage/file.txt", 'r')
            data = file.read()
            file.close()
            return data
        else:
            file = open("storage/file.txt", 'w+')
            data = file.read()
            file.close()
            return data

    def remove_line(self, index): 
        file = open("storage/file.txt", 'r+')
        file_data = file.readlines()
        if len(file_data) >= (int(index)+1):
            file.close()
            file = open("storage/file.txt", 'w+')
            del file_data[int(index)]
            file.seek(0)
            file.writelines(file_data)
            # for line_index, line in enumerate(file.read()):
            #     if line_index == index:
            #         line.strip("\n")
            #         file.write(line)
            file.close()
            return jsonify({"msg":"Linha {} removida".format(str(int(index)+1))})
        return jsonify({"msg":"Linha {} nao existe".format(str(int(index)+1))})

    def remove_file(self):
        if os.path.isfile("storage/file.txt"):
            os.remove("storage/file.txt")
        else:
            print("Error: File not found")
        return

    def append_data(self, content): 
        file = open("storage/file.txt", "a")
        file.write(content + "\n")
        file.close()
        return


    def edit_line(self, content, index):

        file = open("storage/file.txt", 'r+')
        file_data = file.readlines()
        if len(file_data) >= (int(index)+1):
            file.close()
            file = open("storage/file.txt", 'w+')
            file_data[int(index)] = content+'\n'
            file.seek(0)
            file.writelines(file_data)
            file.close()
            return jsonify({"msg":"Linha {} alterada".format(str(int(index)+1))})
        return jsonify({"msg":"Linha {} nao existe".format(str(int(index)+1))})