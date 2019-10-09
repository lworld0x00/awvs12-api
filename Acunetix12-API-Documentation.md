##创建组

### api

{api_base_url}/api/v1/target_groups

### method

POST

### request payload

{"name":"test","description":""}

## 将target加入组中

### api

{api_base_url}/api/v1/target_groups/3dc94f87-308e-40d9-9a5a-bd85ca9e68b3/targets



3dc94f87-308e-40d9-9a5a-bd85ca9e68b3: 猜测是group id

### method

PATCH

### request payload

{"add":["4d30f3f3-c44e-48d9-b126-fcac1c79b812"],"remove":[]}



4d30f3f3-c44e-48d9-b126-fcac1c79b812： 猜测是target id 需要进一步测试