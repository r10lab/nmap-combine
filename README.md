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



nmap-combine

nmap-combine 是一个用于整合 nmap 扫描结果的工具。它要求使用 Python 3.9 或更高的版本。使用该工具的步骤如下：

    将 Python 脚本 (combine.py) 放置在与 nmap 扫描结果相同的目录下。
    打开命令提示符或终端。
    切换到包含脚本和扫描结果的目录。
    运行以下命令：
    python combine.py
    
注意：

请确保目录中存在一个名为 nmap.txt 的文件，该文件将用于整合扫描结果。与该工具一起使用的还有 web批量请求.jar 文件。
