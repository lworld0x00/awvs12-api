from API.Target import *
from API.Scan import *
from API.Target import *

t = Target('https://10.249.203.45:3443', '1986ad8c0a5b3df4d7028d5f3c06e936c6c04a334de794e16bbab6c49d08f9e2b')
target_id = t.add("https://jd.com")
print(target_id)
# s = Scan('https://10.249.203.221:3443/#/', '1986ad8c0a5b3df4d7028d5f3c06e936c811e798f93964d399cc99c7080d51448')
# print(s.add(target_id, 'full_scan'))
# print(s.get_all())
#
# print(s.get(scan_id))
# print(s.get_vulns(scan_id, scan_session_id))
# print(s.get_vuln_detail(scan_id, scan_session_id, vuln_id))
# s.delete(scan_id)
# target测试完成
# t = Target('https://10.0.0.22:3443', '1986ad8c0a5b3df4d7028d5f3c06e936c19cc66ad38d44c9da5a4b9107fe5e6ed')
# target_id = t.add("https://jd11.com")
# print(t.get_all())
# t.delete(target_id)
# print(t.get_all())
