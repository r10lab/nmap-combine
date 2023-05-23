# nmap-combine
# 对nmap扫描后结果进行整合
#python要求
python>=3.9
# 需要把py文件放到nmap扫描结果同目录下
#运行
python combine.py
#会自动保存结果到合并.txt

# 需要注意：
with open('nmap.txt', 'r') as file
nmap.txt 为nmap扫描保存结果的名称，配合web批量请求.jar使用
