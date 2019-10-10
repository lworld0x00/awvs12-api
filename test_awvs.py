from API.Target import *
from API.Scan import *
from API.Target import *
from API.Group import * 
# t = Target('https://192.168.142.3:3443/', '1986ad8c0a5b3df4d7028d5f3c06e936cb0e072d2672c4eac9f3bdaf547fb96d8')
# target_id = t.add("https://jd.com")
# print(target_id)
# s = Scan('https://10.249.203.221:3443/#/', '1986ad8c0a5b3df4d7028d5f3c06e936cb0e072d2672c4eac9f3bdaf547fb96d8')
# print(s.add(target_id, 'full_scan'))
# print(s.get_all())
#
# print(s.get(scan_id))
# print(s.get_vulns(scan_id, scan_session_id))
# print(s.get_vuln_detail(scan_id, scan_session_id, vuln_id))
# s.delete(scan_id)
# target测试完成
# t = Target('https://10.0.0.22:3443', '1986ad8c0a5b3df4d7028d5f3c06e936cb0e072d2672c4eac9f3bdaf547fb96d8')
# target_id = t.add("https://jd11.com")
# print(t.get_all())
# t.delete(target_id)
# print(t.get_all())

# 测试group api
g = Group('https://10.249.203.45:3443/', '1986ad8c0a5b3df4d7028d5f3c06e936cc1ff75bf2ee6421c940058dea8472905')
# t = Target('https://10.249.203.45:3443/', '1986ad8c0a5b3df4d7028d5f3c06e936cc1ff75bf2ee6421c940058dea8472905')
group_id = g.create_new_group("hx1")
print(group_id)
# target_id = t.add("https://jd.com")
# print(target_id)
# print(g.add_to_group(target_id,'a5c682b1-a4b3-41d2-9d15-096b64e63c53'))