import sys,re # 標準入力、正規表現

# file_data = open("/var/log/httpd/access_log", "r")
file_data = open("/var/log/apache2/error_log", "r")

sample = input()
print(sample)



for line in file_data:
    print(line)



# 開いたファイルを閉じる
file_data.close()
