# awvs12-api
> `Acunetix Web Vulnerability Scanner`（简称`AWVS`）是一款知名的网络漏洞扫描工具，它提供了主动扫描web的功能，可以扫描出一些常见的的web漏洞，是渗透测试分析的好帮手。此`Repo`为`AWVS`的非官方接口，主要获取方式是靠抓包分析得到。注: 此`repo`使用的是`AWVS12`。

### 如何使用
> 在学习`AWVS API`之前，读者需要具有`AWVS`的基本使用经验，了解`AWVS`基本使用流程。

在`API`目录下存放的是与`AWVS`使用相关的类，包括：
1. Base.py
2. Dashboard.py
3. Group.py
4. Report.py
5. Scan.py
6. Target.py
7. TargetOption.py
8. Vuln.py

在`config`目录下存放的是与配置相关的脚本，包括但不仅限于`logger`配置。在根目录下,`test_awvs.py`用于测试`API`目录下的类和方法。

### `API`说明
#### 扫描相关操作
##### `Target`相关操作
1. 添加

2. 删除
3. 获取所有`Target`

##### `Scan`相关操作
##### `Group`相关操作
1. 创建组
    1. `API`
    ```shell
    /api/v1/target_groups
    ```
    2. `method`
    ```shell
    POST
    ```
    3. `request payload`
    ```shell
    {"name":"test","description":""}
    ```
2. 将指定`target`添加到组内
    1. `API`
    ```shell
    /api/v1/target_groups/{指定模式的group_id}/targets
    ```
    2. `method`
    ```shell
    PATCH
    ```
    3. `request payload`
    ```shell
    {"add":[target_id],"remove":[]}
    ```
3. 将指定`target`从组内删除
    1. `API`
    ```shell
    /api/v1/target_groups/{指定模式的group_id}/targets
    ```
    2. `method`
    ```shell
    PATCH
    ```
    3. `request payload`
    ```shell
    {"add":[],"remove":[target_id]}
    ```
#### 结果显示相关