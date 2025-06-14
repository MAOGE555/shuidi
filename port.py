import socket
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# 定义一个正则表达式来检查是否是IP地址
ip_pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')



# 定义一个函数来处理单个域名或IP及其端口
def extract_ip_or_domain_and_port(item):
    item = item.strip()  # 去除前后的空格和换行符
    if ':' in item:
        domain_or_ip, port = item.split(':')
    else:
        domain_or_ip, port = item, '80'

    return domain_or_ip, port


# 从1.txt中读取资产列表
with open('1.txt', 'r') as file:
    assets = file.readlines()

# 使用多线程批量处理
results = [None] * len(assets)  # 初始化结果列表，保持原始顺序
with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_index = {executor.submit(extract_ip_or_domain_and_port, assets[i]): i for i in range(len(assets))}
    for future in as_completed(future_to_index):
        index = future_to_index[future]
        try:
            ip_or_domain, port = future.result()
            results[index] = (ip_or_domain, port)
        except Exception as exc:
            results[index] = (f"生成异常: {exc}", f"生成异常: {exc}")

# 将结果写入ips_or_domains.txt和ports.txt
with open('ips_or_domains.txt', 'w') as file_ips, open('ports.txt', 'w') as file_ports:
    for ip_or_domain, port in results:
        file_ips.write(f"{ip_or_domain}\n")
        file_ports.write(f"{port}\n")
