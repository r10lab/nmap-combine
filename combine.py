with open('nmap.txt', 'r') as file:
    lines = file.readlines()

results = []
for line in lines:
    line = line.strip()
    if line.startswith("Nmap scan report for"):
        ip = line.split(" ")[-1]
    elif "/tcp" in line and "open" in line:
        parts = line.split()
        port = parts[0].split("/")[0]
        result = f"{ip}:{port}"
        results.append(result)

# 保存结果到文件
output_filename = "合并.txt"
with open(output_filename, 'w') as output_file:
    for result in results:
        output_file.write(result + '\n')

print(f"结果已保存到文件: {output_filename}")
