# /Users/shiqiang/Downloads/ctf-2023/附件/task_flag.jpg

filename = "/Users/shiqiang/Downloads/ctf-2023/附件/task_flag.jpg"

with open(filename,"rb") as f1:
    f = f1.read()
    with open("flag.jpg","ab") as f2:
        len = len(f)
        i = 0
        while i < len:
            hex = f[i:i+4][::-1]
            # print(hex)
            f2.write(hex)
            i += 4
